#!/usr/bin/env python3
"""Triage a list of concepts against Wikidata: already there, ambiguous, or missing.

    python3 reconcile.py entities.json
    python3 reconcile.py entities.json --json out.json
    python3 reconcile.py entities.json --term "gantry hoist" --parents Q1419194

WHY THIS EXISTS. The slow half of entity work is not writing the markup, it is
deciding whether an entity already exists in the knowledge graph. Done by hand
that is a search, five tabs, and a judgement per concept. The judgement still
has to be human. Everything before it is mechanical, and this does it.

WHAT IT WILL NOT DO. It does not create, edit or propose anything on Wikidata.
It is read-only against the public API and it writes no credentials anywhere.
Creating an item is a human act with a declared account, for the reasons in
SKILL.md.

THE VERDICTS, and what each one means for the next step:

  MATCH     An item exists whose label or alias is the term, and whose P279/P31
            chain reaches one of the parents you said to expect. Use its QID as
            sameAs on the concept. No creation needed.
  REVIEW    An item exists with the right name but the wrong or unreadable
            class, or several items claim the name. A person reads these. This
            is where a wrong QID would otherwise get adopted.
  ABSENT    Nothing carries the term. Candidate for creation, if it passes the
            notability test in SKILL.md.

THE SECOND OUTPUT, which is the one that pays for the script. For every term it
reports the senses Wikidata currently returns. For an ABSENT term those are
exactly the P1889 "different from" statements a new item needs, and the input to
the "not this" sentence on the page. Both jobs want the same list and nobody
wants to assemble it twice.

PARENT CLASSES ARE REQUIRED PER TERM, deliberately. A term matching a label is
not a match: "sling" matches a Clairo album. Naming the parents you expect is
what turns a string match into an identity check, and refusing to default them
is what stops this script quietly adopting a wrong QID.

RATE AND COURTESY. Serial requests with a pause between them, one retry with
backoff, and it honours a 429. The Wikimedia User-Agent policy asks automated
clients to identify themselves and offer a contact. CONTACT below is a generic
client name on purpose: never put a personal email address in it. If a contact
is wanted, use a role address the owner has agreed to.
"""
import argparse
import json
import pathlib
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://www.wikidata.org/w/api.php"
CONTACT = "entity-reconcile/1.0 (read-only entity research script)"
PAUSE = 0.4
VERDICTS = ("MATCH", "REVIEW", "ABSENT")


def api(params, attempt=0):
    """One GET against the Wikidata API, with one backoff retry."""
    params = dict(params, format="json")
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": CONTACT})
    try:
        with urllib.request.urlopen(req, timeout=30) as fh:
            return json.load(fh)
    except urllib.error.HTTPError as exc:
        if exc.code in (429, 503) and attempt < 1:
            wait = int(exc.headers.get("Retry-After") or 5)
            time.sleep(wait)
            return api(params, attempt + 1)
        raise
    except (urllib.error.URLError, TimeoutError):
        if attempt < 1:
            time.sleep(3)
            return api(params, attempt + 1)
        raise
    finally:
        time.sleep(PAUSE)


def search(term, limit=10):
    """Candidate items for a term, searching labels and aliases."""
    out = []
    for lang in ("en", "en-gb"):
        hit = api({
            "action": "wbsearchentities", "search": term, "language": lang,
            "uselang": lang, "limit": str(limit), "type": "item",
        })
        for row in hit.get("search", []):
            if row["id"] not in {r["id"] for r in out}:
                out.append({
                    "id": row["id"],
                    "label": row.get("label", ""),
                    "description": row.get("description", ""),
                    "matched": (row.get("match") or {}).get("text", ""),
                })
    return out


def entities(qids):
    """Full labels, aliases and claims for up to 50 items per call."""
    got = {}
    qids = list(qids)
    for i in range(0, len(qids), 50):
        chunk = qids[i:i + 50]
        res = api({
            "action": "wbgetentities", "ids": "|".join(chunk),
            "props": "labels|aliases|descriptions|claims",
            "languages": "en|en-gb",
        })
        got.update(res.get("entities", {}))
    return got


def names(entity):
    """Every label and alias an item answers to, casefolded."""
    out = set()
    for block in (entity.get("labels") or {}).values():
        out.add(block.get("value", "").casefold())
    for rows in (entity.get("aliases") or {}).values():
        for row in rows:
            out.add(row.get("value", "").casefold())
    return {n for n in out if n}


def parent_qids(entity):
    """Direct P279 subclass-of and P31 instance-of targets."""
    out = set()
    for prop in ("P279", "P31"):
        for claim in (entity.get("claims") or {}).get(prop, []):
            val = (((claim.get("mainsnak") or {}).get("datavalue") or {})
                   .get("value") or {})
            if isinstance(val, dict) and val.get("id"):
                out.add(val["id"])
    return out


def ancestors(qid, depth, cache):
    """Parent QIDs up to `depth` hops. Depth 1 is the direct parents only.

    A level at a time, batched. The first version of this walked the tree one
    item per request and took over eight minutes on twelve concepts, which is
    slow enough that nobody would run it twice. Each level is now a single
    wbgetentities call, so the cost is `depth` calls per starting item rather
    than one per node, and the shared cache collapses the repeats (every
    device concept reaches medical device sooner or later).
    """
    out, frontier, seen = set(), {qid}, {qid}
    for _ in range(max(depth, 0)):
        need = [q for q in frontier if q not in cache]
        if need:
            cache.update(entities(need))
        nxt = set()
        for item in frontier:
            for parent in parent_qids(cache.get(item, {})):
                if parent not in seen:
                    seen.add(parent)
                    nxt.add(parent)
        out |= nxt
        frontier = nxt
        if not frontier:
            break
    return out


def classify(term, synonyms, expect, depth, cache):
    """Verdict for one concept, plus the competing senses behind it."""
    wanted = {term.casefold()} | {s.casefold() for s in synonyms}
    candidates = []
    for phrase in [term] + list(synonyms):
        for row in search(phrase):
            if row["id"] not in {c["id"] for c in candidates}:
                candidates.append(row)

    if candidates:
        cache.update(entities([c["id"] for c in candidates]))

    exact, senses = [], []
    for cand in candidates:
        full = cache.get(cand["id"], {})
        row = {
            "qid": cand["id"],
            "label": cand["label"] or (full.get("labels", {})
                                       .get("en", {}).get("value", "")),
            "description": cand["description"],
        }
        if names(full) & wanted:
            row["parents"] = sorted(ancestors(cand["id"], depth, cache))
            row["class_ok"] = bool(set(row["parents"]) & set(expect))
            exact.append(row)
        else:
            senses.append(row)

    good = [e for e in exact if e["class_ok"]]
    if good:
        verdict = "MATCH"
    elif exact:
        verdict = "REVIEW"
    else:
        verdict = "ABSENT"

    return {
        "term": term,
        "synonyms": list(synonyms),
        "verdict": verdict,
        "expected_parents": list(expect),
        "named_matches": exact,
        "use": good[0]["qid"] if good else None,
        "other_senses": senses[:6],
    }


def report(results):
    """Markdown to stdout. The tables are the deliverable, not the JSON."""
    counts = {v: sum(1 for r in results if r["verdict"] == v) for v in VERDICTS}
    print("# Wikidata reconciliation\n")
    print(f"{len(results)} concepts checked. "
          + ", ".join(f"{counts[v]} {v.lower()}" for v in VERDICTS) + ".\n")

    print("| concept | verdict | use | named matches |")
    print("|---|---|---|---|")
    for r in results:
        named = ", ".join(
            f"{m['qid']}{'' if m['class_ok'] else ' (class?)'}"
            for m in r["named_matches"]) or "none"
        print(f"| {r['term']} | {r['verdict']} | {r['use'] or '-'} | {named} |")

    for r in results:
        if r["verdict"] == "MATCH":
            continue
        print(f"\n## {r['term']} · {r['verdict']}\n")
        if r["named_matches"]:
            print("Carries the name, class not confirmed. Read these:\n")
            for m in r["named_matches"]:
                print(f"- **{m['qid']}** {m['label']}: {m['description'] or 'no description'}")
                print(f"  parents: {', '.join(m['parents']) or 'none'}")
        if r["other_senses"]:
            print("\nCompeting senses. For an absent concept these are the")
            print("P1889 `different from` candidates and the input to the")
            print("\"not this\" sentence on the page:\n")
            for s in r["other_senses"]:
                print(f"- {s['qid']} {s['label']}: {s['description'] or 'no description'}")
        if not r["named_matches"] and not r["other_senses"]:
            print("Nothing returned at all. Check the term is the one")
            print("practitioners use before concluding the gap is real.")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("input", nargs="?", help="JSON file of concepts")
    ap.add_argument("--term", help="check one term instead of a file")
    ap.add_argument("--parents", default="",
                    help="comma-separated expected parent QIDs for --term")
    ap.add_argument("--synonyms", default="",
                    help="comma-separated synonyms for --term")
    ap.add_argument("--depth", type=int, default=2,
                    help="parent hops to follow (default 2)")
    ap.add_argument("--json", help="also write the full result here")
    args = ap.parse_args()

    if args.term:
        concepts = [{
            "term": args.term,
            "synonyms": [s.strip() for s in args.synonyms.split(",") if s.strip()],
            "expected_parents": [p.strip() for p in args.parents.split(",") if p.strip()],
        }]
    elif args.input:
        concepts = json.loads(pathlib.Path(args.input).read_text())
        if isinstance(concepts, dict):
            concepts = concepts.get("concepts", [])
    else:
        ap.error("give an input file or --term")

    missing = [c["term"] for c in concepts if not c.get("expected_parents")]
    if missing:
        sys.exit("expected_parents is required, and missing for: "
                 + ", ".join(missing)
                 + "\nA label match without a class check adopts wrong QIDs.")

    cache, results = {}, []
    for con in concepts:
        print(f"... {con['term']}", file=sys.stderr)
        results.append(classify(
            con["term"], con.get("synonyms", []),
            con["expected_parents"], args.depth, cache))

    report(results)
    if args.json:
        pathlib.Path(args.json).write_text(json.dumps(results, indent=2) + "\n")
        print(f"\nFull result: {args.json}", file=sys.stderr)


if __name__ == "__main__":
    main()
