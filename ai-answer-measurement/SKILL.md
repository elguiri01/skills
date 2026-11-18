---
name: ai-answer-measurement
description: How to measure and report AI search visibility without fooling ourselves. Use before running or reading query_battery.py or aio_citations.py, before quoting any AI visibility figure to Adrian or a client, and when designing a test of a content, link or mention change. Carries the measured noise in AI answers, the sample sizes needed to see a move, the frozen-cohort rule, the Door Audit and its decision thresholds, and the list of ways a dashboard number lies. From CMSEO and LLM Mastery, November 2026.
---

# Measuring AI answers

`grow-search-visibility` already says: a fixed, versioned prompt battery, with
engine, date, locale and model recorded, repeated, compared query by query.
That was right. This skill supplies what it lacked: how noisy the thing being
measured is, and therefore how much measuring is enough.

## How noisy it is

All from Surfer's tracker unless marked: about 50 million answers, about
100,000 prompts a day since March 2025, scraped from the real interfaces of
ChatGPT, Perplexity, Gemini, AI Overviews and AI Mode. Vendor data, large base,
values read from charts.

| fact | figure |
|---|---|
| Two runs of the same prompt share | 40% of brands |
| Brands that appear in all of 20 runs | 4% |
| Brands and cited domains present in all of 5 daily runs | 16% |
| Brand overlap with the same prompt next day, 7, 30, 90 days | 40%, 36%, 31%, 28% |
| Cited-domain overlap next day, and at 90 days | 37%, 13% |
| Rewording the prompt keeps | about three quarters of brands |
| A different intent keeps | barely a third |
| An API answer's top-3 brands that reach the chat interface's top 3 | 29 to 42% (ceiling 49 to 54%) |
| A brand that was first is still first on a repeat | 56.5% (Senuto: 443 prompts, 6 platforms, 10 runs) |
| Repeated runs returning an identical brand list | under 1% (12 prompts, 60 to 100 runs; attributed to Fishkin, not read at source) |

What follows from the table:

- **One run is a draw, not a reading.** A screenshot proves a thing can happen.
- **Citations churn much faster than brand mentions.** After eleven weeks a
  page keeps 26% of its citation frequency while the brand keeps 83% of its
  mentions. Track both, separately.
- **Wording matters less than intent.** Count distinct intents, not prompts.
  Fifty rewordings of one question are one data point.
- **The API is not the product.** `aio_citations.py` reads DataForSEO. Treat
  its output as a cheap proxy and label it as one. A client checks on a phone,
  logged in, in their own city.
- **Engines move independently.** One client blog went 30 to 0 citations on
  ChatGPT while rising to 117 on AI Overviews across 2026. Never blend engines
  into one number.

## How much measuring is enough

Kiekbusch's table, arithmetic checked (margin on a share near 50% at 95%):

| answers per prompt | margin | good for |
|---|---|---|
| 100 | plus or minus 10 points | a floor; is the brand there at all |
| 400 | plus or minus 5 points | a baseline |
| 400 before and 400 after | | showing a 10-point move |

The caveat is his and it matters: this assumes independent draws, and runs of
one prompt minutes apart may not be. Spread them across days.

For our own portfolio that volume is not affordable on every query, and it does
not need to be. Practical tiers:

- **Presence check** (are we ever cited): 5 runs per prompt per engine, weekly.
  This is what Vestigio and Burgos both run. It detects "never" against
  "sometimes" and nothing finer.
- **Before and after on a specific change**: pick at most 10 intents, 100 runs
  each, both sides. Expect to see only moves of 15 points or more.
- **A claim to a client that something moved**: the 400 and 400 design, or do
  not make the claim.

## The frozen cohort

The best cautionary tale in the set (Niechciał, a roofing client). The
dashboard showed AI visibility up 190.6%. In June, ChatGPT presence was 44%
blended. Split by cohort it was 27% on the questions tracked since March and
62% on a set added in June. The rise was the new questions being easier.

Rules:

1. Build 30 to 150 buyer questions. Most do not contain the brand.
2. **Freeze the list and version it.** `query_battery.py` already versions;
   never edit a version in place.
3. When questions are added, they become a new cohort. Report the original
   cohort on its own, forever.
4. Log with every run: engine, model version if shown, date, locale, logged-in
   or not, and what changed on the site that week.
5. Branded prompts are tracked apart from category prompts. Mixed in, they
   inflate everything.

Measured on the frozen 81 questions, that same client went from 3.0% to 21.1%
on ChatGPT in the month its pages were rewritten answer-first, and held between
20 and 32% for seven months. One client, no control, the speaker's own caveat:
coincidence in time, not proof.

## Three numbers, not one

Per engine, per cohort:

- **Presence**: named in the answer at all.
- **First pick**: recommended first. A brand and its rival can be mentioned 71%
  and 72% of the time and recommended first 20% and 44%.
- **Framing**: what is said. Rate it, or count the commonest positive and
  negative descriptions. A brand cited as "budget, overheats" is worse off than
  one that is absent.

And two that are different things and get confused:

- **Mention**: the name appears in the answer.
- **Citation**: a page appears in the sources.

## The Door Audit (Takas)

The best-evidenced method in the set, and it replaces "lowest DR in the top 5"
as our reading of how contested a SERP is. His data and workbook are free at
emiliotakas.com/chiangmai.

1. **Inclusion rate.** Take 50 queries you want. Count how many show you
   anywhere in the top 10. That share is the ceiling. Average position only
   describes pages that already got in.
2. **Gatekeepers.** Across those 50 result pages, count slots per site. List
   the ten or so that hold half the page. In his 30 markets, 10 sites held 41%
   of all slots and Reddit was on page one in 27 of 30. The aim is to be
   mentioned there, not to outrank them.
3. **One change against a control.** Split the queries into a test set and a
   held-back control set before touching anything. Fill in the test card
   first: hypothesis, metric, both sets, the one change, the window, the owner,
   and counts at day 0, 30, 60 and 90.
4. **Decide by rule.** Lift is the test set's change minus the control set's
   change, in percentage points. Five points or more: fund five more. Under
   two: stop, log it, try a different kind of change. Between: extend 60 days,
   once.

`rewrite_control.py` and `esyoh_applied_yield.py` already do the difference.
What they lack is the pre-registered threshold. Add it.

His five questions before copying anyone's case study are worth keeping by the
keyboard: what was the baseline; how many tried it and never wrote it up; when
did it work, before or after which update; how long did it last; what else
changed at the same time, and who benefits if you believe it.

## Ways the number lies

- **Unequal groups.** Pages chosen for a change were often already rising
  (Burgos's own limits slide). Match on trend, not just type.
- **Brand variants.** One tracker counted only one of HighLevel, GoHighLevel
  and GHL. Check every spelling of a client's name is counted.
- **Locale.** Answers for Poland, the US and Switzerland differed wildly on
  the same prompts. From Thailand, Pantip surfaced; from the US, Reddit. Our
  droplet is in New Jersey.
- **Account state.** Logged out, free and paid tiers get different models.
  Trackers run logged out and see the cheapest.
- **GA4.** Its AI channel undercounts: someone who sees a brand in an answer
  and types the URL is "direct". Ask leads how they found you.
- **Poisoned scrapers.** One speaker reported DataForSEO returning an
  unrelated ad for a simple query, and local agencies report its screenshots
  differ from logged-in mobile results. Unverified, and our stack depends on
  it. Spot-check a sample by hand each month.

## Reporting

Label every number with where it came from: crawl, client-reported, official
(GSC, Bing Webmaster Tools), third-party estimate, or our inference. One row
per change: URL, what was done and when, value before, value after, label.

Free first-party sources to use before any paid tracker: Bing Webmaster Tools'
AI Performance report (citations and the searches the AI ran), Search Console's
generative AI report, and Microsoft Clarity for ChatGPT and Copilot referrals.

## What this skill will not claim

That any of these figures hold for education queries. They come from software,
e-commerce and a Polish client base. The shape will transfer. Re-measure the
size on our own cohort before relying on it.
