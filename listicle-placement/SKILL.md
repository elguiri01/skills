---
name: listicle-placement
description: Getting our sites INTO other people's "best of" listicles, which is where AI engines take their recommendations from. Prospecting from live AI citations, a scorecard for which lists are worth pursuing, the entry-blurb and outreach method, and placement tracking. Read the compliance section first, it refuses half of the source. Sibling to listicle-agent (which writes OUR listicles) and 22 (answer engine optimisation).
---

# Listicle placement

Source: Matthew Woodward, "Listicle Link Building: How To Get Placed In Best-Of
Lists For AI Search", linksthatrank.com, 24 August 2026. Read 2026-09-29.

**Read this first: the source is a sales page.** Roughly half of it pitches
LinksThatRank's own $247-$397 placement service, and the method sections exist
to make the case that the work is too hard to do yourself. The prospecting and
qualification half is genuinely good and is written up below. The paid half we
refuse, and the reason is in Compliance.

`listicle-agent/` is the mirror of this skill: it writes listicles we publish.
This one is about being listed in somebody else's.

## The claim worth taking seriously

Best-of listicles are what AI engines read to decide who to recommend. Two
figures are cited:

- Ahrefs, 26,283 AI-search source URLs behind 750 top-of-funnel prompts:
  best-of listicles are **43.8%** of pages ChatGPT cited, more than any other
  page format.
- Evertune, the 6,000 most-cited URLs per platform across ChatGPT, Copilot,
  Gemini, Google AI Overviews, AI Mode and Perplexity, roughly 25,000 unique
  URLs out of 400 million citations: **63%** pointed to listicles.

Neither is ours and neither is independently checked here, so treat them as
the source's numbers rather than facts we have verified. **Our own measurement
points the same way**, which is the reason to act on it: of 98 recorded AI
Overview citations across our sampled queries, 0 are ours, and the citations go
to .edu institutions, JRCERT and YouTube. We are not in the lists the engines
read.

A placement earns three things at once, and this is the part that makes it
different from an ordinary link: a backlink, a brand mention, and a citation.

## Where this fits our portfolio, honestly

The source assumes a product with a brand, a price and a buyer. We are
affiliate and rank-and-rent sites. The fit is narrower than it first reads:

- **Good fit.** automechanicschools needs citations rather than words, which
  the skills index already says. radiologyed's JRCERT data is the kind of thing
  a "best resources for X" list credibly cites. careerspy is a brand being
  built on purpose and is the cleanest case in the portfolio.
- **Poor fit.** A state page on a template site has nothing a listicle would
  want to name. Do not pitch those.

The test: would a reader of that list raise an eyebrow at our inclusion? If
yes, we have no business pitching it.

## Step 1: build the prospect list from live AI citations

Not from a link database. From what the engines are citing **now**.

Four prompt patterns, personalised:

    best {product/service} for {use case}
    top {category} tools for {persona}
    {competitor} alternatives
    best {product/service} in {location}

Run each through ChatGPT, Perplexity, Google AI Mode and Google search, each in
a separate chat in an incognito window, instructing the models to use live web
search rather than training data. Record: prompt, platform, cited URLs, whether
our brand appears, which competitors appear.

**We already have this machinery.** `query_battery.py` holds the versioned
prompt battery, `serp_battery.py` runs it, and `aio_citations.py` records
citations. Extending those beats building a spreadsheet by hand, and it gets
the measurement discipline `grow-search-visibility` asks for free: engine,
date, locale and model recorded, repeated because outputs vary, compared
query-by-query rather than blended.

Then classify each cited URL and keep only **third-party listicles**: a
best-of, top-10, comparison or alternatives page on a site that does not sell
what it ranks. Drop vendors' own lists, brand pages, directories, forums,
video and news. Drop our own sites and our competitors' own sites. Anything
undecidable is marked NEEDS CHECKING and reviewed by hand rather than guessed.

Sort by how many prompts cited each URL. A page cited for several prompts, or
across several platforms, is the one worth the effort.

The source then widens the net with Ahrefs Content Explorer on "best
[category]", filtered by DR or organic traffic. We do not have Ahrefs.
DataForSEO gives SERP results and domain rank at roughly $0.0006 a query, which
is the same input by another route. Target is 50-80 opportunities.

## Step 2: score them

| Criterion | What to check | Points |
|---|---|---|
| Cited by an AI platform | appeared in at least one model's sources | 30 |
| Ranks in Google | top 20 for the "best [category]" term | 25 |
| Recently maintained | updated within the last 6 months | 20 |
| Genuine editorial | named author, real criteria, links out to entries | 15 |
| Competitor gap | a direct competitor listed, we are absent | 10 |

Above 55, pitch first. 35-54, secondary. Below 35, leave it.

The weights are a starting point and the source says so. Note the shape of it:
**55 points is unreachable without the AI-citation 30 plus something real**,
which is the scorecard quietly encoding the whole thesis.

## Step 3: the pitch

Find the author's business email (Hunter.io, LinkedIn). Generic `contact@` is
a last resort.

Then write an **entry blurb**: everything the author needs to add us, in a form
they can nearly paste. This is the part that does the work.

    [Brand] is a [category] built for [specific buyer].
    Best for: [one scenario, under ten words].
    [Verifiable fact one, with a number].
    [Verifiable fact two, e.g. pricing or an integration count].
    Unlike [an adjacent entry on their list], it [one concrete differentiator].
    Pricing starts at [figure]. [URL].

Personalise per target: "best for" should match their article's title, and
"unlike" should name a brand actually on their list. Put it in a Google Doc
with images and links and send the link, rather than pasting a wall of text.

Outreach email:

    Hi [Name],

    Your [exact listicle title] covers [N] options but skips [named use case
    or segment].

    [Brand] fills that gap because [one line of evidence a stranger can verify].

    If this is something you think would benefit your audience, I've created a
    short write-up plus screenshots and a test account if you want to check it
    yourself: [Google Doc link]

    What do you think?

Pace: **15-20 prospects a week including follow-ups**, per the source.

For us the "verifiable fact with a number" is the strongest card we hold and
the one we should lead with: JRCERT programme counts, BLS medians by state,
scored listings. That is proprietary synthesised data, which is the moat Skill
12 names, and it is exactly what a list author cannot get elsewhere.

## Step 4: track and reclaim

Listicles change. Ahrefs reviewed 1,100 blog listicles: **79% updated in the
last 12 months, 26% in the last two**. A placement is not permanent.

One row per secured link: URL, listicle title, our position in the list, date
live, date last checked. Re-check every 90 days. When a link is gone, find
which brand replaced us, then write to the author offering an updated section.

`publisher-crm/` and `inventory-database/` are the shelved skills this belongs
in if it ever becomes routine.

## Compliance: what we refuse, and why

The source is explicit that most site owners will ask for a placement fee,
quotes $200-$600 as normal and $1,000+ for large sites, and says of its own
paid service: **"your link will always be dofollow"**.

That is a link scheme. It is not a borderline call:

- Google's link spam policy covers links created primarily to manipulate
  rankings, and the article acknowledges this before arguing that quality
  exempts it. It does not.
- Google's spam definition now explicitly includes "attempting to manipulate
  generative AI responses in Google Search", which is precisely what buying a
  placement in an AI-cited listicle is for.
- Our own standing rule, in the skills index and the goal: **any compensated
  placement gets `rel="sponsored"` or `rel="nofollow"`**, and earned editorial
  coverage is the only kind worth chasing. The goal skill puts "bought links
  shaped to look editorial" permanently out of scope.

**So: use steps 1, 2 and 4 in full. Use step 3 to earn placements. If a
publisher asks for money, either walk away or pay and insist the link is
marked sponsored, knowing that removes most of the ranking value and leaves
the brand mention and the AI citation, which may still be worth it.** Be
honest that the second option is a different, smaller trade than the one the
article is selling.

That is not squeamishness. A bought dofollow link on a site the engines
currently trust is a bet that Google never works out which sites sell
placements, against a company that maintains an 80,000-domain blacklist of
exactly that, as this source proudly advertises.

## The quality checklist, repurposed

The source offers this to vet a site before paying. It is more useful to us as
a test of whether a placement is worth **earning**, and as a specification for
the listicles `listicle-agent/` writes on our own sites:

- Links out to every brand named, with natural branded anchors
- Visible last-updated date, within 12 months
- 500+ monthly organic visitors
- Real comparisons and data, not cookie-cutter text
- Honest pros and cons per entry
- Topically relevant to what the site normally covers, and to us
- **No "write for us" or "submit a guest post" page anywhere on the site**
- Named human author with a bio and an about page
- Bonus: a stated selection methodology

That seventh point is the sharpest. A site advertising guest posts is selling
placements, and a list on it is not editorial however it reads.

## What to do with this

1. Extend `query_battery.py` with the four buyer-prompt patterns for our four
   high-$/click verticals, and record cited URLs rather than only citation
   counts. That is the prospect list and it is free.
2. Score what comes back. Expect few 55+ results: our verticals are .edu and
   accreditation-body territory, which is a harder list to join than "best
   project management software" and also a more valuable one.
3. Pitch with the data, not with the site. The JRCERT and BLS tables are the
   reason someone would cite us.
4. Never buy a dofollow placement.
