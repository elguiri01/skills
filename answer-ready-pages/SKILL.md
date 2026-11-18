---
name: answer-ready-pages
description: What makes a page get lifted into an AI answer, and what does not. Use when writing or rewriting a money page, a best-of list, a comparison page or a state page, and before listicle-agent or any content expansion job. Covers the features that separated cited from uncited pages in two large vendor datasets, the proxies that did not, the difference between getting a page cited and getting a brand named, hub lists against "X vs Y" pages, and a six-pass method (fan-out, frame, vocabulary, answer-first, chunk check, fact triples). Read information-gain first: this governs how a page that deserves to exist is built.
---

# Answer-ready pages

`information-gain` decides whether a page should exist. Skill 11 decides how a
sentence reads. This sits between them: how a page is assembled so that an
engine retrieving passages can use it.

The evidence is correlational throughout. Surfer and Senuto both compared
winners with losers inside their customers' tracked prompts and both say it is
not proof of cause. Two independent datasets agreeing is still worth more than
any one talk.

## What separated cited pages from uncited ones

| lever | evidence |
|---|---|
| The answer in the opening | 29% of cited passages come from the first 50 words of a page, about 10% more from words 50 to 100 (Surfer). Pages whose first paragraph answers the question supply 18% of the AI answer against 5% (Senuto, n=492) |
| Intent match | A page that matches the query's intent is a source 42% of the time; an off-intent blog post 13% (Surfer) |
| Fact coverage | The top 3 sources carry 39% of the facts about the entity; by rank 50 it is 26%. Covering facts mattered about eight times more than link-graph position |
| Concrete specifics | Figures and specs only you state. His example: "weighs 300 g" |
| Self-contained sections | Each paragraph names its subject and stands alone, general to specific |
| Tables on list pages | Most-cited lists have a median 30 table cells; least-cited have 0 |
| Page type by engine | In one agency's tracking, ChatGPT cited service and product pages with prices, SLAs and operating data; AI Overviews cited how-to guides and blog articles (McDowell, two clients) |

## What did not

| proxy | evidence |
|---|---|
| PageRank and DR | Correlation with being cited: -0.01 (Surfer, Common Crawl PageRank) |
| Domain age | No real difference between 2 and 10 years |
| Schema | No detectable effect (Senuto). +3.7 points with JSON-LD in Surfer's data, which he reads as a marker of maintained sites. Product markup +0.1 |
| llms.txt | Close to zero, sometimes negative |
| FAQ blocks, table of contents, expert quotes as checklist items | Bottom of 20 page features; answering early is worth four to five times more |
| Author box, headings phrased as questions, meta description | No detectable effect (Senuto) |
| Length, fresh dates, a prices section | Zero correlation with holding a top-3 Google position (Rank Up, 3,000+ pages) |
| Outbound links to trusted sites | 0.031 |
| Newness | Most citations go to pages older than six months on every engine except Gemini. Update old pages; do not replace them |

Read that second table against what we produce by default. FAQ blocks,
question headings and schema are in most of our templates. They are not
harmful. They are not the work.

## Two different games

Surfer scored 190 page features against two outcomes: the page being cited,
and the publisher's brand being named in the answer. Twenty features push the
two in opposite directions. All correlations are small (0.15 or less).

| feature | page cited | brand named |
|---|---|---|
| Many brands on the list | helps (+0.15) | hurts (-0.10) |
| "Best" in the title | helps slightly | hurts (29% of winners against 43% of losers) |
| "vs" in the title | hurts slightly | helps (+0.11) |
| The year in the title | helps slightly | hurts |
| A key-takeaways box | helps | hurts |
| Answer first | helps (96% against 80%) | slightly negative |
| Internal links to product pages | | helps (11 against 7) |
| Length | | shorter wins (2,350 against 2,660 words) |
| Calls to action | fewer wins (median 0 against 0.13 per 1,000 words) | |

So one page cannot do both jobs well. Build a set.

### Hub list: to get the page cited

For a site that earns from traffic and clicks. This is the default shape for
our affiliate sites.

- Ten or more options. Most-cited own lists compare a median 11 brands against
  8, the strongest single factor.
- A comparison table, short paragraphs, plain H2s.
- Open with who the page is for and what it covers.
- Sources, statistics and expert quotes where they are real.
- No year in the URL. Avoid "top" in the title.
- Few or no calls to action in the body. **Test this before applying it**: our
  pages earn from the listings unit, and a page that is cited more and converts
  less is a loss. The ad sentinels are untouched either way.

### "X vs Y" pages: to get the brand named

For a client or product that needs to be the recommendation: Lisclare,
LoadLander, the tool sites.

- Three to five brands, the client first, on a page that is plainly the
  client's own.
- Several of these, not one: "X vs Y", "X vs Y vs Z", "alternatives to Y".
- Internal links to product features and documentation. Screenshots.
- Short. No takeaways box, no "best 2026", no numbered ranking.
- First-hand detail, not a template.
- Never misstate a competitor's features or price. Legal action was the only
  backfire the speaker named, and it is also simply wrong.

### On other people's lists

A cited third-party list raises the chance a brand on it is named from 57% to
73%, and gives each rival beside you nearly as much. Slot position: named 52%
of the time at number one, 32% at five, 13% from ten down. A better slot on a
list that already cites you is worth more than a new low slot. `listicle-placement`
has the prospecting method.

## Unique material, and where to put it

Rank Up tracked 3,000+ pages across seven B2B markets for 90 days and compared
pages that held a top-3 Google position with pages that dropped out of the top
10. Vendor study, no link controls, still running. How much more often the
holders carried each kind of first-hand material:

| material | multiple |
|---|---|
| Own experience, in the introduction | 5.5x |
| Own measurement, in explainers | 4.4x |
| Customer proof, on alternatives and pricing pages | 3.6x |
| A test shown, in best-of lists | 2.4x |
| Screenshots | 2.4x |

Four or more kinds on a page held the top 3 almost twice as often as two or
fewer. Placement in the introduction beat placement elsewhere, modestly (1.8x
against 1.5x). And the limit: fully unique articles did worse. Cover the
basics, then add what only we have.

His system is a filing cabinet per client with five drawers (tests, customer
stories, photos and screenshots, own statistics, own experience) and a claims
table mapping each product claim to its proof. When a drawer is empty the agent
interviews the human and files the answer. For us the drawers are the tables:
`jrcert_programs`, `bls_oews`, IPEDS net price, `listing_edits`, our own
aggregated behaviour. The moat ladder in `information-gain` is the same idea.
What Rank Up adds is the instruction to **spread each unique fact across every
page where it is relevant**, rather than spending it on one.

## The six-pass method

Robert Niechciał gave away six agent skills, all plain method with no code.
His own materials say a plain chat knew about as much as the skill; what the
skill adds is a fixed output shape, so runs can be compared. `six-passes.md`
has each pass. In order, on one page:

1. **Fan-out**: split the main question into the sub-questions an engine would
   run.
2. **Frame**: fill fifteen roles for the topic and add the high-priority ones
   the fan-out missed.
3. **Vocabulary**: synonyms, broader and narrower terms, parts, opposites.
4. **Chunk check**: does each section open with its answer and stand alone.
5. **Answer-first rewrite** of the weak sections, using only facts on the page.
6. **Fact triples**: list every entity, attribute and value, then sort them
   into confirmed elsewhere, stated by us alone, and in conflict.

The sixth pass is the one that changes what we do next. Facts we alone state
are the outreach list: each needs one independent source to repeat it.

Limits, from the materials themselves and worth repeating to anyone who wants
to gate on these:

- The passes read pages. They never see an AI answer. They measure readiness,
  not visibility.
- Scores drift between runs: the same page scored 5 and 6 out of 10, and
  counted 1 of 9 against 7 of 12 answer-first openings. **Never use a score as
  a gate.**
- "Facts only from the page" carries the page's errors forward.
- Every `[FACT NEEDED]`, and every health, legal or money claim, goes to a
  person. For us that is the existing fact gate.

## Applying it here

1. Pick by `opportunity_rank.py`, not by traffic.
2. Run the six passes on the page as it is. Passes 1 to 4 and 6 are analysis
   and can run on the local model or Haiku.
3. The rewrite goes through DeepSeek and the humanizer behind the fact gate, as
   all prose does. The agent supplies verified facts, not sentences.
4. Stage, preview, apply through `push_expansion.py`. Skill 12 gates unchanged.
5. Measure against a matched control set at 28 and 90 days
   (`ai-answer-measurement`).

## What this skill will not claim

That an answer-first rewrite "triples the chance of being cited". The speaker
said it twice on stage; his own files forbid describing any output that way,
and the 18% against 5% is share of the answer on a correlational sample. Nor
that AI-written pages are cited more: Surfer's detector flagged 82% of the
most-cited lists against 71% of the least, and AI detectors are unreliable.
