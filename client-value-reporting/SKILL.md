---
name: client-value-reporting
description: How to set goals with a client and report against them when organic clicks are falling for reasons nobody controls. Use when onboarding a client, writing a monthly or quarterly client report, explaining a bad month, or resetting expectations after a search change. Covers the goal reset and when to have it, the three replacement goals, what/so what/now what, the plain-language translation of each metric, report layout and cadence, the one-pipeline view, diagnosing a branded-search drop, handling a client who will not share revenue or never implements, and the line we hold against hiding bad numbers. Replaces client-reporting-agent's "smart display logic" for our own use. From an agency lead with Salesforce and Rippling as clients, CMSEO, November 2026.
---

# Client value reporting

CLAUDE.md refuses one pattern from `client-reporting-agent`: "hide what's bad,
lead with what's good". This skill is the alternative, and it comes from
someone who kept an enterprise client through a year in which she missed the
traffic target. Her rule is stricter than ours and points the same way:
**never let a client see a bad number cold.** Bring the problem before the
numbers land, with the fix attached.

## Why the old goals fail

AI Overviews, assistants and agentic checkout intercept clicks. Her Salesforce
case, as told:

- Original goal, set four months before AI Overviews launched: non-branded
  organic growth of 100% in a year.
- Mid-year the trajectory was about 150% up, then about 70% after AI Overviews
  arrived.
- She went to the client then, reset the goals (assistant traffic +100%,
  organic target cut to 70%, an AI visibility target), and finished the year
  with assistant traffic up 1,500% and organic up 67%, just under the revised
  target. The client stayed.

One account, self-reported. The lesson is in the sequence: the conversation
happened while the numbers still looked good. Her slide: "if you raise it while
numbers still look good, nobody calls it an excuse."

## The reset conversation

Three things to say, in this order:

1. Search is changing how people find you, so we are changing how we measure.
2. Organic traffic is still reported. It is no longer the goal.
3. The goals move to enquiries and sales.

And the swap, goal for goal:

| old goal | new goal |
|---|---|
| Grow organic sessions by X% | Recommended in [n] of 10 top buying prompts, against our top three competitors |
| Rank top 3 for 50 keywords | More people searching for us by name than in the same month last year |
| Organic conversions in GA4 | Total enquiries and pipeline, including the ones GA4 does not credit to organic |

Rankings stay as a monitored secondary metric.

**Our amendment to the first goal.** "Recommended in n of 10" read from one run
is a coin toss (`ai-answer-measurement`). Set it as a share over a frozen
prompt set with repeated runs, and tell the client at the start that the number
moves by ten points on nothing. She warns that clients check on their phone in
the meeting. Check it live beforehand, and explain that their phone and ours
will differ and why.

## What, so what, now what

Every number in a report gets three sentences:

- **What**: the figure.
- **So what**: what it means for the business.
- **Now what**: what we are doing about it, and by when.

A bad number adds three things: a rankings check (did we lose position, or did
clicks fall with position held), market context (Google Trends for the client
against competitors, to show a market-wide fall), and the specific fix with a
date. "Give me a month."

Run the wording past the test she uses: would a ten-year-old and a chief
executive both understand this.

## Say the outcome, not the task

| instead of | say |
|---|---|
| Share of voice | "AI recommends us in X of 10 buyer questions. Our top competitor is Y." |
| AI citation | "ChatGPT now names us as the best option for [thing]." |
| Impressions | "We're visible on Google X times more often than this time last year." |
| Organic sessions | "Visits from people who clicked through across all organic channels." |
| Branded search | "X% more people are searching for us by name." |
| Fixing technical crawl errors | "Making sure AI can read and understand our site, products and offers, so it gives accurate answers to buyers." |
| Technical work generally | Leave it out. Say what it fixed. |

Technical detail goes to the in-house marketer who asked for it and nobody
else.

Three questions a client can hold in their head:

1. **Are we on the list?** When buyers ask an assistant or Google, are we in
   the top three, yes or no.
2. **Is AI telling the truth about us?** Prices, features, details.
3. **Is the business growing?** Direct visits, brand searches and enquiries
   alongside organic clicks.

## One pipeline

Report non-paid channels as one number: organic, direct, assistant referral,
organic social, referral and YouTube. Exclude paid. Reasons:

- A person who sees the brand in an AI answer and types the address is
  "direct". GA4 files YouTube clicks under organic social.
- GA4 does not isolate assistant referrals well out of the box. Build a custom
  report.
- Add branded impressions and branded clicks year on year from Search Console.

Her example of a month that looks bad and is not, from one unnamed client:
organic clicks down 15%, branded searches up 24%, direct visits up 18%, sales
enquiries up 7%. (In one telling she called the 18% assistant referral. One of
the two was a slip, so do not quote it as either.)

**Label every number by source**, as `ai-answer-measurement` requires: official,
client-reported, third-party estimate, our inference. A client report is where
an estimate most easily turns into a fact.

## Diagnosing a branded-search drop

Branded search is the metric that exposes causes that have nothing to do with
us. Her list of real ones:

- Television, radio or paid search was switched off.
- Someone changed the H1 to "Black Friday Sale" and removed the brand.
- Content was deleted from a page that had been earning 300 to 400 branded
  clicks and now earned about 12.
- A site rebuild.
- AI answers stopped naming the brand.

Method: export branded query data, find which pages lost most, check whether
answers still name the brand, then ask the client what changed in that exact
date window. Investigate; do not spin.

## Layout and cadence

- **Goals at the top**, against last month and against the same month last
  year. Year on year wherever there is a season, which for us is always
  (see the lead-revenue seasonality memory).
- **Monthly data report, delivered on a call**, then sent. The call is
  mandatory even when all is well. First or second week of the month.
- If the client must have the numbers before the call, write the story into
  the covering email: what we noticed, what we are doing, we will discuss on
  the 7th.
- **Quarterly strategy session**, in person where possible, for the wider
  group.
- **An unscheduled meeting when the ground shifts.** She booked every client
  within about three weeks of AI Overviews launching.
- **For a contact who reports upward**, hand them one or two slides they can
  forward, and offer to review what they send their boss. Budget cuts usually
  come from above and have nothing to do with the work.

## Awkward clients

- **Will not share revenue.** Work up the funnel to what they will share:
  qualified leads, enquiries, units sold. Use units as the goal. Revenue
  usually follows trust.
- **Never implements the audit.** Reissue it as "what changed since last
  year". Then find the one thing within our control, prove it, and scale it.
  Her case: a university that had fixed one item in three years. She added FAQ
  sections to course pages herself and reported a large lift on the first page
  tested (about 400%, base not stated).
- **Wants "AI SEO" quoted separately.** She folds it in: SEO is now AI SEO.
  Either trade it against current tasks or add budget; her example was an
  extra $1,000 a month. Kasra Dash, on a panel, takes the opposite line and
  sells it under the name the client's budget holder is using. Both are
  defensible. The second is easier to sell and the first is easier to keep.
- **Says the leads are poor.** Move to the one-pipeline view, show prompts
  that went from never mentioned to mentioned half the time, and be honest
  that visibility earlier in the funnel converts somewhere else.

## Do not promise blog posts

Her line: do not promise four posts a month. Promise to be the obvious source
for the client's highest-value buyer questions. That is `information-gain` in a
sentence a client understands, and it protects us from being measured on
volume.

## The line we hold

- **The bad number goes in, first, with its explanation.** Framing a number is
  not hiding it.
- **A hypothetical is labelled.** Her "named in 47 of 50 prompts" was an
  illustration, and the auto-generated summary of her own talk reported it as
  a Salesforce result. That is how it happens.
- **Nothing is guaranteed.** Not a ranking, a citation, an enquiry or a date.
  Lag, honestly: about a month for one strong corroborated piece, about three
  months for incremental change.
- **Every figure carries its source.**
- **A form default is not evidence.** One speaker suggested making "I found
  you through AI" the pre-selected answer on the "how did you find us" form.
  That manufactures the number it reports. Add the option; leave the default
  blank.

## For our own reporting

The same structure serves the daily digest and the agenda: what, so what, now
what, bad first, sources labelled. It is what the +707% and the 28-times
impressions bug would have looked like if they had been reported this way the
first time.
