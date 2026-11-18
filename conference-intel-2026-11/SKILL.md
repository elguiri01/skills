---
name: conference-intel-2026-11
description: Index and evidence register for 39 talks from CMSEO 2026, Black Hat Day and LLM Mastery 4.0 (Chiang Mai, 9 to 15 November 2026). Read this first when a question touches AI search, link buying, local SEO, client reporting, agency pricing, outbound or new revenue lines, because it says which talk carried evidence, which was a sales pitch, which of our own beliefs it changed, and which of the ten skills written from it to open. Holds the belief ledger, the ranked revenue plays, the black-hat ledger and a searchable text copy of the source notes.
---

# Conference intel, November 2026

Adrian uploaded `CMSEO2026_AllPresentations.docx` on 2026-11-18: transcript-verified
notes on 39 sessions across three events. This directory is the map. The
operating detail lives in ten skills written from it, listed below.

`source-extract.md` is the full text of the document (537 KB). Grep it, do not
read it whole. Every talk in it has the same shape: thesis, a measured-claims
table with a confidence column, mechanisms asserted without evidence, tactics
tagged WHITE, GREY or BLACK, tools, Q&A, corrections to the auto-summary, and a
list of what could not be verified. That last list is the most valuable part of
each talk and the first thing a quick reader drops.

## How to read any claim from this set

Almost every speaker sells something: links, a tracker, a course, a community,
a brokerage. That does not make them wrong. It decides how much weight a number
carries. Four grades, used throughout these skills:

| grade | meaning | examples |
|---|---|---|
| A | A dataset with a stated base that someone other than the speaker could recompute, or did | Takas's 30-market CSV (recomputed by the note-taker), Surfer's 238.6M citations, the arXiv papers |
| B | A vendor's own data with a stated base and a stated limit | Senuto n=492, Vestigio's frozen 81-question cohort, Kiekbusch's sample-size arithmetic |
| C | One client, one site or one run, honestly labelled | Burgos's 39-page token test, Tummy Shield, Burns's Hyatt audit |
| D | A number with no base, or a screenshot, from someone selling the fix | Floate's "our testing", Stoyanov's before and after, Kalin's keynote |

Three rules that follow:

1. **A grade D claim generates a hypothesis and nothing else.** It can earn a
   place on the test backlog. It cannot go in a client document or change a
   live site.
2. **Correlation inside a vendor's customer base is not an effect.** Surfer and
   Senuto both say so about their own numbers. Repeat that caveat whenever the
   number is repeated.
3. **Nobody at these events ran a control.** The note-taker flags it on talk
   after talk. Our standing rule (the +707% that was seasonality) is still
   ahead of the industry, not behind it.

## The ten skills written from this

| skill | open it when |
|---|---|
| `ai-answer-measurement/` | Measuring or reporting anything about AI visibility. Carries the noise figures that say our battery is under-powered |
| `answer-ready-pages/` | Writing or rewriting a page so an engine can lift from it. What moved citations, what did not, and the six-pass method |
| `perception-engineering/` | A client with a recognisable brand. What the answer says about them, not whether they are named |
| `ai-crawl-access/` | Whether crawlers can reach a site at all: CDN defaults, Common Crawl, logs. Includes our own 10-of-111 finding |
| `youtube-for-ai-overviews/` | Any careerspy or client video work. The avatar belief did not survive |
| `link-and-domain-vetting/` | Before buying a link, a placement or a dead domain |
| `local-pack-2026/` | Local clients and the directory strategy |
| `outbound-replies/` | Cold email and LinkedIn for LoadLander, the freight kit and agency prospecting, plus what happens after the reply |
| `client-value-reporting/` | Writing a client report or resetting client goals |
| `agency-economics/` | Pricing client work, and retainer against profit share against equity |

Files in this directory:

- `beliefs.md`: what we believed, what the talks say, and the verdict. Read it
  before defending an existing position.
- `plays.md`: the revenue ideas, ranked, with what each costs to test.
- `black-hat-ledger.md`: what Black Hat Day demonstrated, what we refuse, and
  what a client needs defending against.
- `talks.md`: all 39 sessions with speaker, interest, grade and where it is used.

## The five findings that matter most

1. **AI answers are a distribution, not a result.** Two runs of one prompt
   share about 40% of brands (Surfer, grade A). A single check, ours included,
   says almost nothing. See `ai-answer-measurement/`.
2. **Getting a page cited and getting a brand named are different games** that
   want partly opposite page features (Surfer, 190 factors, 20 of which flip
   sign). See `answer-ready-pages/`.
3. **The proxies everyone sells barely separate cited pages from uncited
   ones:** PageRank, DR, domain age, schema, llms.txt, FAQ blocks, author
   boxes. Two independent vendor datasets agree. What does separate them is the
   answer in the first 50 words, intent match, facts and specifics.
4. **Access fails silently and first.** Common Crawl's own figure is that about
   35% of good sites block AI crawlers by accident, mostly CDN defaults. Ten of
   our 111 Cloudflare zones look closed, careerspy.org among them.
5. **The money is moving from traffic to proof and recurring revenue.** FE
   International's top lead source is now ChatGPT while its organic traffic
   fell, and its founder calls organic-only businesses with no moat the most
   overvalued thing an acquirer can buy. That describes this portfolio. See
   `plays.md`.

## What this set is weak on

Nothing here measures state or city template pages, Spanish-language sites,
lead-gen affiliate economics, or education as a vertical. The evidence is
mostly B2B software, e-commerce and iGaming. Transfer the method, re-measure
the number.
