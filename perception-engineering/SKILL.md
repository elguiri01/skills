---
name: perception-engineering
description: AI search work for a client with a recognisable brand, where the question is what the engines say about them, not whether a page ranks. Use for Lisclare, LoadLander, any Crecera or directory-won client, and any brand asking "why does ChatGPT say that about us". Covers the objective to pick, the diagnosis (absent, mis-framed, out-ranked, wrong axis; claim, proof, perception, fit), the truth document, the trust prompt set, the evidence-then-corroboration sequence, the 12-week enterprise plan, and what is refused. From CMSEO and LLM Mastery, November 2026.
---

# Perception engineering

A known brand is usually already in the answer. The work is what the answer
says. Jonathan Kiekbusch's client Geekom was named on 51% of its prompt set at
the start of 2026 and described as budget hardware that overheats. Being cited
that way is worse than being absent.

Read `ai-answer-measurement` first. Nothing here can be judged from one run.

## 1. Pick the objective

Oliver Pechter's split, which decides everything after it:

| the brand is | the objective is | the engines check |
|---|---|---|
| A high-consideration purchase (finance, health, care equipment, education) | To be recommended without a risk flag | Licences, regulators, auditors, standards, test evidence |
| A household name | Perception: the right attributes attached | Awards, editorial coverage, reviews |
| A challenger | To appear in more answers | An unoccupied position with two or three provable pillars |

Lisclare is the first kind. LoadLander is the third.

## 2. Discover the questions

Owned data first, because nobody else has it:

- Search Console, with a regex for long question queries.
- Bing Webmaster Tools, AI Performance: it shows the searches the AI ran
  before answering. These are real fan-outs for this site.
- Support tickets, live chat, pre-sales email, call recordings. One agency
  transcribes the call centre and turns the recurring questions into pages.
- Microsoft Clarity.

Shared data for ideas only: marketplace Q&A and reviews, Reddit and forums,
People Also Ask, competitor reviews.

Sort into three buckets and track each as its own cohort:

- **Branded** ("is Lisclare a good make"). Nearly always winnable.
- **Category** ("best profiling bed for home use"). The battlefield.
- **Jobs to be done** ("can one carer use a hoist alone"). Where rivals get in.

For a trust objective add the questions a nervous buyer asks: is this company
legitimate, what are the risks of this product, what is the difference between
this and that, does it meet the standard.

## 3. Diagnose

Freeze the set, run it, and keep the whole answer: text, tables, citations and
the fan-out queries where shown. Then classify each problem. Two schemes from
two speakers that fit together:

| what the answer does | Kiekbusch | which link is broken (ex-Semrush talk) | the fix is |
|---|---|---|---|
| Never names the brand | Absent | Proof: too few third parties back it | Distribution |
| Names it with the wrong attributes | Mis-framed | Perception: the picture is stale or wrong | Evidence on site, then corroboration |
| Names it second and says why | Out-ranked | Fit: no proof for this use case | Distribution, on the rankings the engine cites |
| Compares on terms the brand did not choose | Wrong axis | Claim: positioning unclear | Design: state the attributes that matter |

Two cheap readings that tell you which:

- **Read the comparison tables and "best for" labels** in the answers. They
  show the attributes the engine compares on.
- **List what the engine says it cannot verify.** For an investment firm the
  answers flagged risk because no licence or auditor could be found. A readable
  licence document fixed it.

And one check on first pick: export the rankings and lists the engine cites for
the category. In one pair, brand and rival were mentioned equally (71% and 72%)
but the rival was recommended first more than twice as often, and 11 of the 14
cited rankings placed the rival higher. Those 14 pages are the target list.

## 4. The truth document

Before publishing anything, write down what is true and get the business to
sign it. Three speakers describe the same artefact under different names
(truth notebook, Golden Thread, source of truth).

- One defining sentence: "[Brand] is a [category] for [segment] that
  [attribute]." Ask each engine which category it files the brand under, per
  product line. One brand was named in 97% of answers about its main product
  and 0% for its second.
- Basic facts: name, founded, where, who, website.
- Each product in a line, with price.
- The verifiable facts to surface: standards met, test results, warranty,
  certifications, years, client counts, awards.
- What the engines currently get wrong, and the correction.
- The category prompts being tracked.

This is the same module pattern as `entity-markup-and-wikidata`: one definition
that reaches every page generator. Extend that module; do not start another.

Jabez Reuben suggests publishing a version of it as a plain markdown "AI
instructions" page ("Official information about [Brand]", facts, products,
differentiators, corrections, last updated). Profound and HubSpot have one.
There is no measurement behind it. It is cheap and harmless as a page of true
facts. The section that tells an assistant how to describe the brand is the
part to leave out: it reads as an instruction to a model, which is the shape
of thing engines are learning to distrust.

## 5. Design: put the evidence on the site

- **Publish what fixes the record.** Geekom: thermal test data for the old
  overheating fault, the hardware changes, the warranty.
- **Facts on the homepage and product pages.** One unread study reports brand
  mention probability rising from 5% to 30% with the number of verifiable
  facts on the homepage. Low confidence; the direction agrees with everything
  else.
- **Specs and features as text, not images.** Load a competitor's product page
  with JavaScript off and show the client what a crawler sees.
- **Every variant in a table** with sizes, materials and prices, identical in
  the site, the merchant feed and the schema. An agent that finds two prices
  skips the product.
- **One page listing every award**, if there are real ones. For one airline
  that page was cited far more than any other.
- **The undocumented.** Ask the product team what the product does that is
  written down nowhere. Publish it. Then show the client that the engines now
  know it.
- **Do not chase use cases the product does not fit.**

`answer-ready-pages` covers how those pages are built.

## 6. Distribute: get it confirmed

An engine trusts a specific fact when independent sources agree on it. The
on-site evidence is half the job.

The Tummy Shield sequence is the cleanest worked example in the set. A
pregnancy seatbelt product was absent from AI answers; a cheaper rival that did
not meet the Australian standard was being named. The agency:

1. Published one very strong article: what the product is, why it works, and
   crash-test evidence against the Australian standard. The client was the only
   brand that had crash-tested.
2. Put a press release, digital PR and placements in pregnancy and car-safety
   articles behind it, all pointing at that article.
3. Within about a month the answer called it the exception to the usual
   advice, citing a national insurer and the client.

One client, engine not named. The pattern is what matters: a verifiable claim
only this brand can make, then other people repeating it.

By source type (map what the engines cite for the category first; it varies by
country and by engine):

| source | action |
|---|---|
| Review platforms | Collect and answer reviews. Ask every customer, name topics not wording |
| Editors and rankings | Brief them, correct errors, supply test data. Sometimes asking to be added works |
| Forums and Reddit | Signed, expert, disclosed presence. A correction posted in the thread as the brand was picked up within days in one case |
| Marketplaces and directories | Complete listings. Test that the directory is readable by crawlers before paying for it |
| YouTube | Advise creators on metadata. Fix auto-captions that mangle the brand name. Timestamps worded as the target prompts |
| Wikipedia and Wikidata | Where the notability is real. See `entity-markup-and-wikidata` |

One version of each fact, quoted the same everywhere. For the three most
specific facts, get one independent source to state each.

## 7. Defend

Re-run on schedule. Leaders get unseated and answers drift. Monitor named
people as well as the brand (see `conference-intel-2026-11/black-hat-ledger.md`).
Tell the client the lag honestly: about a month for one strong corroborated
piece, about three months for incremental change, and a model update can undo
either.

## The 12-week plan for a larger client

Rahul Sengupta's order, which is right because the first failure is usually
plumbing: **crawl, then comprehend, then convert.**

- **Before kick-off**, from public data: a visibility snapshot, which engines
  the buyers use by market, which sources are cited in the category.
- **Weeks 1 to 4**: stakeholders (brand, legal, service); the prompt set;
  tracker setup; a baseline that is four weeks of repeated runs and not a
  screenshot. KPIs: mention rate, share of voice against three to five rivals,
  citation share, source map, sentiment, accuracy. Map each to something the
  marketing lead is already judged on.
- **Weeks 5 to 8**: the truth document signed off; truth gaps and where each
  comes from, agreed by week 8.
- **Week 12**: a plan per engine. Re-plan when a model changes.

The crawl stage is `ai-crawl-access`. Check the firewall before robots.txt, and
do not trust a 200.

## Refused

Each of these was recommended on stage by someone.

- **An owned "independent" review site**, or buying one, to review a client's
  products without saying who owns it. Kiekbusch built one for $14 with
  invented authors; ChatGPT cited it within days. His own verdict: "you could
  get yourself in trouble with the FTC". Ours: no invented people, no
  undisclosed self-review.
- **Paying a critic** to change a review without disclosure.
- **Award mills.** Sengupta's own words: "a quick black-hatty way".
- **Paid roundup placements that are not labelled.** A paid placement is
  permitted where the publisher labels it. We do not ask them not to.
- **Steering the wording of reviews**, or sending only happy customers to the
  review platform. Illegal in some places and wrong in all of them.
- **An "AI instructions" page that tells models what to say.**

## What this skill will not claim

That any of this has a measured, controlled result. Geekom moved from "budget,
overheats" to "extremely positive" across a year in which thermal data,
readable specs, paid gaming placements and paid roundups all changed, with no
control and no end number. It is the best-described process in the set and an
unproven one. Sell the diagnosis and the monitoring as certain. Sell the
outcome as a projection.
