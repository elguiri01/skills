---
name: bing-and-non-google-search
description: Bing, DuckDuckGo and Copilot as a search channel in their own right. Use when a site's traffic mix is being examined, when AEO work needs the index that ChatGPT and Copilot actually read, or when deciding where optimisation effort goes. Covers the measured Bing share of our clicks, IndexNow and URL submission (which Google has no equivalent of), and the per-day comparison rule that stops the Bing/Google ratio being quoted wrong. Read with 22 (answer engine optimisation) and 15 (technical SEO).
---

# Bing and non-Google search

Written 2026-09-29. Until then the portfolio had `bing_connector.py` running on
cron, 525,352 rows of `bing_keywords` that nothing read, and no skill
mentioning Bing as anything other than Bing Places. That gap is the reason
this file exists.

## Why it earned a skill

Bryce, who operates esyoh and is therefore the largest single source of our
revenue, said on 2026-09-29:

> "hesntoyl not even trying for google traffic anymore... its pintless"
> "bing and chatgpt, duckduckgo, copilot"
> "the days of making big sites are donzo"

He has an incentive to talk down the asset class while buying domains cheaply,
and he described his own approach as "maybe 50/50 and that's being
conservative". So the claim was tested against our own data rather than
believed.

**Measured on identical days, 2026-09-20 to 26, portfolio-wide:**

    Bing      430 clicks    26,377 impressions   CTR 1.63%
    Google  1,996 clicks   278,316 impressions   CTR 0.72%

**Bing is 18% of our search clicks from 8.7% of the impressions, at 2.3x
Google's click-through rate.** It is already the majority source on:

    electricalschool.org     bing 109   google  73    60% bing
    medassisting.org         bing  79   google  42    65% bing
    design-training.com      bing  29   google   4    88% bing
    dentalassistantedu.org   bing  45   google   3    94% bing

electricalschool.org is our best per-click domain at $1.69. Its majority
traffic source is a channel we have never once optimised for.

The honest reading: Bryce is directionally right and rhetorically wrong. Google
is still 82% of our clicks and "pointless" is not what the data says. But a
fifth of our search traffic, at double the CTR, with zero effort applied, is
the cheapest thing on the board.

## The measurement rule, because this was got wrong first

The first comparison read **34% Bing** and was wrong. It put `bing_keywords`,
which is a daily figure, against `gsc_pages`, which is a 28-day rolling
window. Same error family as the +707% that turned out to be seasonality and
the impressions that were 28x too high.

**Always compare `bing_traffic_daily` against `gsc_traffic_daily` over
identical `report_date` ranges.** Never compare a Bing daily figure to a GSC
window figure, and never quote the ratio without naming the window.

Two false readings to expect in the per-domain table:

- **ekgtechs.com** reads 100% Bing because its GSC feed died on 2026-08-16/17.
  One of item 49's six domains.
- **mentalhealthtech.org** reads 100% Bing because it has no `gsc_pages` rows
  at all. One of item 22's three sites with esyoh revenue and no GSC.

A domain showing zero Google clicks is a broken feed until proven otherwise.

## What Bing lets you do that Google does not

This is the practical half, and it is the reason the channel is cheap.

- **IndexNow.** A single POST announces a changed URL to Bing, and it is
  shared with Yandex and Seznam. Google has no equivalent and discontinued its
  own ping endpoint. For a portfolio that publishes and re-touches pages in
  batches, this turns indexing from waiting into an API call. Nothing in the
  orchestrator uses it today.
- **URL submission in Bing Webmaster Tools**, with a daily quota, which again
  has no Google counterpart since Search Console's inspect-and-request is
  manual and rate-limited.
- **Bing Webmaster Tools gives keyword data Google withholds**, including
  query-level impressions on a shorter lag than GSC's.

## Why it is also the AEO channel

**ChatGPT and Copilot both read Bing's index.** So does DuckDuckGo. That makes
Bing coverage the mechanical substrate under a large part of Skill 22, and it
reframes "optimise for Bing" from a legacy-channel chore into the delivery
route for AI citation. A page Bing has not indexed is a page those assistants
cannot cite.

That connection is the strongest argument in this file, and it is the one Bryce
was probably making when he put "bing and chatgpt" in the same breath.

## What to do, in order

1. **Build the Bing half of `opportunity_rank.py`.** Join `bing_keywords` to
   revenue and rank by the same buyer-intent filter the Google side uses. The
   data has been collecting for months and nothing reads it.
2. **Wire IndexNow into the publish path.** After `apply_edits` or
   `push_expansion` applies a page, announce it. Cheap, no quota anxiety, and
   it suits batch work.
3. **Fix the broken feeds first** (items 49 and 22), or the per-domain Bing
   share stays unreadable on six to nine domains.
4. **Check Bing Webmaster Tools is verified** on every domain, not just the
   ones in `bing_connector`'s list.
5. **Then treat the majority-Bing domains as their own cohort.**
   electricalschool, medassisting, design-training and dentalassistantedu are
   a different optimisation problem from a Google-majority site, and nobody has
   ever looked at them that way.

## What this skill will not claim

- That Google is finished. It is 82% of our clicks.
- That Bing share is a quality signal. Several of our highest Bing shares are
  broken Google measurement, not Bing strength.
- A revenue number. We have never attributed revenue by search engine, because
  `esyoh_leads` records a referral URL and not a referrer, so the honest
  position is that Bing's 18% of clicks is worth an unknown share of revenue
  until somebody measures it.
