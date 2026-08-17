#!/usr/bin/env python3
"""Run Lighthouse's agentic-browsing category and print it as a pass/fail list.

The raw Lighthouse JSON buries the useful part - which elements failed and why - and its
0-100 number is misleading for this category: Google describes it as a fraction of checks
passed, not a weighted score. This prints only what you act on.

Python 3.8+, standard library only. Lighthouse itself is fetched by npx, so Node must be
installed; Chrome must be present for Lighthouse to drive.

    python3 run_audit.py https://example.com
    python3 run_audit.py https://example.com --mobile --json-out report.json

Identical in behaviour to run_audit.mjs - use whichever runtime the machine has.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CATEGORY = "agentic-browsing"

# The audits that carry weight today. The WebMCP and llms.txt audits report "not
# applicable" on sites that have not adopted them, which is not a failure.
SCORED = {"agent-accessibility-tree", "cumulative-layout-shift"}


def npx_command():
    """Return the argv prefix that invokes npx on this machine.

    Running npm's own npx-cli.js under the current Node binary is the most portable
    route: on Windows it sidesteps Node's refusal to spawn npx.cmd without a shell, and
    everywhere it avoids depending on how npx was put on PATH.
    """
    node = shutil.which("node")
    if node:
        cli = Path(node).resolve().parent / "node_modules" / "npm" / "bin" / "npx-cli.js"
        if cli.exists():
            return [str(node), str(cli)]
        # Typical Linux layout: /usr/bin/node with npm under /usr/lib/node_modules.
        cli = Path(node).resolve().parent.parent / "lib" / "node_modules" / "npm" / "bin" / "npx-cli.js"
        if cli.exists():
            return [str(node), str(cli)]

    npx = shutil.which("npx") or shutil.which("npx.cmd")
    if npx:
        return [npx]
    return None


def chrome_flags(no_sandbox):
    """Assemble Chrome flags, defaulting to --no-sandbox where it would otherwise fail.

    Chrome's sandbox cannot initialise as uid 0, which is the normal state on a fresh
    droplet or inside a container, and the resulting crash message is opaque. Turning the
    sandbox off is acceptable for auditing pages you already trust; keep it on elsewhere.
    """
    flags = ["--headless=new"]
    running_as_root = hasattr(os, "geteuid") and os.geteuid() == 0
    if no_sandbox or running_as_root:
        if running_as_root and not no_sandbox:
            print("Running as root - adding --no-sandbox so Chrome can start.",
                  file=sys.stderr)
        flags += ["--no-sandbox", "--disable-dev-shm-usage"]
    return "--chrome-flags=" + " ".join(flags)


def run_lighthouse(url, mobile, no_sandbox, passthrough):
    """Run Lighthouse and return the parsed report."""
    out = Path(tempfile.mkdtemp(prefix="lh-agentic-")) / "report.json"

    npx = npx_command()
    if npx is None:
        sys.exit("Node/npx not found. Install Node.js, or run the audit from Chrome "
                 "DevTools instead (Inspect > Lighthouse tab).")

    args = npx + [
        "--yes", "lighthouse@latest", url,
        "--only-categories=" + CATEGORY,
        "--output=json", "--output-path=" + str(out),
        "--quiet", chrome_flags(no_sandbox),
    ]
    if not mobile:
        args.append("--preset=desktop")
    args += passthrough

    print("Running Lighthouse against {} ({})...".format(
        url, "mobile" if mobile else "desktop"), file=sys.stderr)
    proc = subprocess.run(args, capture_output=True, text=True)

    if not out.exists():
        sys.exit(
            "Lighthouse did not produce a report.\n"
            "exit code: {}\n{}\n\n"
            "Common causes: Chrome is not installed (set CHROME_PATH to its binary, or\n"
            "apt install google-chrome-stable / chromium); the category needs Chrome 150+\n"
            "(on 130-149 it is behind the experimental flag and the CLI may not expose\n"
            "it); Chrome cannot start as root (try --no-sandbox); or the URL is not\n"
            "reachable from this machine.".format(
                proc.returncode, (proc.stderr or "").strip()[-2000:])
        )
    return json.loads(out.read_text(encoding="utf-8"))


def classify(audit):
    """Map a Lighthouse audit to PASS / FAIL / N/A."""
    mode = audit.get("scoreDisplayMode")
    if mode in ("notApplicable", "manual"):
        return "N/A"
    if mode == "error":
        return "ERROR"
    if mode == "informative":
        return "INFO"
    score = audit.get("score")
    if score is None:
        return "N/A"
    return "PASS" if score >= 0.9 else "FAIL"


def clean(value, max_len=200):
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", str(value))  # markdown links -> text
    return re.sub(r"\s+", " ", text).strip()[:max_len]


def findings(details, out=None, limit=25):
    """Collect the individual findings out of an audit's details.

    The shapes vary by audit: agent-accessibility-tree nests a table inside a list of
    list-sections, with one row per violated rule plus the failing node; llms-txt returns
    a flat table of `message` strings and no nodes at all. Walking the tree rather than
    indexing a fixed path keeps this working as Lighthouse reshuffles its output.
    """
    if out is None:
        out = []
    if not details or len(out) >= limit:
        return out

    for item in details.get("items") or []:
        if len(out) >= limit:
            break
        if not isinstance(item, dict):
            continue

        value = item.get("value")
        if item.get("type") == "list-section" or (isinstance(value, dict) and value.get("items")):
            findings(value, out, limit)  # recurse into the nested table
            continue

        rule = item.get("description") or item.get("message") or item.get("source") or ""
        node = item.get("node") or {}
        where = node.get("selector") or node.get("snippet") or item.get("url") or ""
        if rule or where:
            out.append((clean(rule), clean(where, 120)))

        for sub in (item.get("subItems") or {}).get("items") or []:
            sub_node = sub.get("node") or {}
            sub_where = sub_node.get("selector") or sub_node.get("snippet")
            if sub_where:
                out.append((clean(sub.get("description") or ""), clean(sub_where, 120)))
    return out


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url")
    ap.add_argument("--mobile", action="store_true",
                    help="audit the mobile rendering (default is desktop)")
    ap.add_argument("--json-out", help="also save the full Lighthouse JSON here")
    ap.add_argument("--no-sandbox", action="store_true",
                    help="pass --no-sandbox to Chrome (implied when running as root)")
    ap.add_argument("lighthouse_args", nargs=argparse.REMAINDER,
                    help="extra flags passed straight through to Lighthouse")
    args = ap.parse_args()

    report = run_lighthouse(args.url, args.mobile, args.no_sandbox, args.lighthouse_args)

    if args.json_out:
        Path(args.json_out).write_text(json.dumps(report, indent=2), encoding="utf-8")

    category = (report.get("categories") or {}).get(CATEGORY)
    if not category:
        sys.exit("This Lighthouse build has no agentic-browsing category.\n"
                 "It needs Chrome 150+ and a recent Lighthouse. Check with:\n"
                 "  npx lighthouse@latest --list-all-audits")

    audits = report.get("audits") or {}

    print("\nAgentic browsing - {}".format(report.get("finalDisplayedUrl", args.url)))
    print("{}\n".format((report.get("environment") or {}).get("hostUserAgent", "unknown user agent")))

    rows, failures = [], []
    for ref in category.get("auditRefs") or []:
        audit = audits.get(ref["id"])
        if not audit:
            continue
        status = classify(audit)
        rows.append((status, ref["id"], audit.get("title", ""), ref["id"] in SCORED))
        if status in ("FAIL", "ERROR"):
            failures.append((ref["id"], audit))

    width = max([len(r[1]) for r in rows] + [20])
    for status, aid, title, is_scored in rows:
        print("  [{:5}] {:<{w}}  {}  ({})".format(
            status, aid, title, "scored" if is_scored else "informational", w=width))

    scored = [r for r in rows if r[3]]
    passed = len([r for r in scored if r[0] == "PASS"])
    print("\n  {}/{} scored checks passing. "
          "'N/A' means the feature is absent, not that the site failed.\n".format(
              passed, len(scored)))

    for aid, audit in failures:
        print("--- {}: {}".format(aid, audit.get("title")))
        if aid == "cumulative-layout-shift":
            print("    CLS {} (good is <= 0.1)".format(audit.get("displayValue", "n/a")))
        items = findings(audit.get("details"))
        for rule, where in items:
            print("    - {}".format(rule or "(no description)"))
            if where:
                print("        {}".format(where))
        if not items:
            desc = clean(audit.get("description", ""), 300)
            if desc:
                print("    {}".format(desc))
        print()

    if failures:
        print("Fix in this order: accessible names on interactive elements first (an agent\n"
              "cannot act on a control it cannot identify), then layout shift (a moving page\n"
              "makes it act on the wrong one).")


if __name__ == "__main__":
    main()
