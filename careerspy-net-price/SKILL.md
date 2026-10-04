---
name: careerspy-net-price
description: The careerspy.org net price calculator and the data behind it, which is the portfolio's moat content for college cost. Use when updating IPEDS data, the SAI/Pell engine, the per-college pages, merit aid (Common Data Set) or merit deadlines, state grants, or when backfilling the "Net Price Range $X to $Y per year according to CareerSpy" line onto the 60 sites. Read before quoting any college price, Pell figure or deadline.
---

# careerspy net price: the moat, how it is built, how to keep it true

Written 2026-10-03. Code lives in `~/orchestrator`; this file is the operating guide. The rule above all others: **a published number is read from a primary source this cycle, carries its year, and a gap says so**. Never fill a gap with an estimate and call it data.

## What nobody else publishes (why this is a moat)

Everyone can show IPEDS tuition. These are the data points that are hard to copy, each with its source:

| Data point | Source | Where it lives |
|---|---|---|
| Net price range by family income, with "N of 5 bands published" | IPEDS SFA | `ipeds_institution.np_json` |
| A computed Pell Grant and net price from the federal SAI formula, beside the published band | SAI Guide 2026-27 | `careerspy_calc/engine.js` |
| Cost by housing choice and residency, per year or per program | IPEDS IC_AY / IC_PY | `ipeds_institution` |
| Merit aid split (non-need-based) per college | each school's Common Data Set, section H2A | `cds_merit`, `cds_merit_llm` |
| Verified merit scholarship deadlines with date read | each school's own page | `merit_deadlines` |
| Georgia HOPE / Zell Miller rates per school | Georgia Student Finance Commission | `data/state_aid/georgia_2026_27.json` |
| A per-school statement of what we hold and do not | computed | `careerspy_coverage` |

## The honest limits (state these, never hide them)

- **Vintage differs by field.** Newest published net price/aid is IPEDS SFA 2022-23. Charges: 2023-24 (bulk file) or 2024-25 where the Navigator export has them (3,766 rows). `ipeds_refresh.py --probe` shows whether NCES has published newer.
- **`nces.ed.gov/collegenavigator/` is robots-disallowed.** Do not scrape it. The IPEDS Data Center bulk files are fine.
- **The cohort caveat goes on every page with a net price:** first-time, full-time, degree-seeking undergraduates who received Title IV aid.
- **Imputed values (flags P/K/L/N) are not published figures.** Negative net prices are not shown.
- **No dollar figure moves with a GPA box.** Merit aid by GPA is published nowhere. Show the published distribution and the student's position, never a modelled scholarship.
- **"Number in college" is not in the SAI formula.** Do not add it.
- **Program-priced schools** (IC_PY) publish a whole-program price for their largest program. The published net price is per academic year (checked: net price / whole-program cost falls as 1/f). Annualise per Handbook Vol 7 ch 3, never present the whole-program price as annual.
- **State grants are modelled for Georgia only.** Other states say "not modelled".

## Keeping it current (commands, in order)

1. `python3 ipeds_refresh.py --probe` then `--load --reconcile --coverage`. Reconcile against Navigator must stay above 98%.
2. `python3 careerspy_calc_page.py --write-coverage` (queryable state of all 5,963 active institutions).
3. Federal parameters change every award year. Re-read the SAI Guide, the Pell max/min letter (GEN-xx-01), Handbook Vol 8 loan limits and the HHS poverty guidelines (prior-prior year). Update `engine.js` PARAMS and the source comment, run `node careerspy_calc/test_engine.js` (all must pass), add the new worked examples. Tax tables: IRS Rev. Proc. for the tax year the FAFSA reads (2026-27 reads 2024).
4. Rebuild the JS bundle: `python3 careerspy_calc_page.py --deploy-js` (hash-named, one-year cache, so a changed engine is a new URL).
5. Merit aid: `cds_fetch.py --run`, `cds_parse.py --run`, `cds_llm.py --run`. A figure is shown only if it passes the IPEDS plausibility gate and the two readers agree. CDS older than 2023-24 is not shown.
6. Deadlines: schedule below. A deadline is published only if its wording appears verbatim in the fetched page, the page shows a current-cycle marker, and the source URL and date read are stored.
7. Pages: `careerspy_calc_page.py --state XX --publish-draft` writes DRAFTS only. Going live is Adrian's call.

## Deadlines schedule (Skill 12: deadline pages are only worth citing if current)

Weekly September to February (deadlines cluster), monthly March to August, full re-collection each July. A refresh re-fetches stored pages and calls the model only when the page text hash changed (`merit_deadlines.py --refresh`). A deadline that disappears from its page becomes `withdrawn`, never silently kept.

## Page build traps (each cost a real defect)

- WordPress `convert_chars` rewrites a bare `&` to `&#038;` in inline scripts. Serve the JS from the static file, keep it ampersand-free.
- `wp_insert_post` unslashes input: use `wp_slash` and verify the stored hash.
- Never write `status=draft` over a live slug (it unpublishes). Live slugs get a `-v2` draft.
- The stock sidebar parses after the article and shifts the column (CLS 0.063 at 1280 px). Pages are `no-sidebar`.
- Test the WordPress-SERVED HTML, not the source, and test in the real theme.
- Page selection for scholarship pages must require `merit` or `scholarship` in the URL or title (a "tuition refund schedule" is not one).

## Backfill: the line on every college listing

`python3 careerspy_backfill.py --write` produces `proposed/careerspy-backfill-2026-10-03.csv`: one row per (our page, college) with the exact line, target URL, whether the target is live, and whether the row should carry the link.

> **Net Price Range $3,928 to $7,356 per year according to CareerSpy** (2022-23, 4 of 5 income bands published). Calculate your own net price.

Rules: only colleges in the publishable set; the range is the published band spread, never interpolated; contextual in the listing, never a sitewide footer or sidebar; link the first 10 listings per page and keep the rest as plain text with the attribution (thirty links to one domain from one page is the owned-network footprint); link to the college's own calculator page, not the homepage; mark `nofollow` until the target page is published. Insertion goes through the existing `link_insertions` / `apply_edits.py` mechanism (`--limit` and `--max` both explicit). Never build new insertion machinery.

## Measuring it

Before attributing any revenue change to this content, split revenue by advertiser and check whether the advertisers already present moved. If they did not, the cause is inventory. Never guarantee ranking, indexing, citation, traffic or revenue; every projection reads as one.
