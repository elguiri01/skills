---
name: link-and-domain-vetting
description: How to judge a link, a paid placement or a dead domain before money moves, now that DR and traffic are routinely faked. Use before any acquisition under the "Links we acquire" policy, before bidding on an expired or aged domain, when choosing publishers for outreach or listicle placement, and when auditing a client's existing link profile. Covers the tells of a manufactured seller, what to buy on instead of DR, the sub-query publisher map, harmonic centrality against PageRank, dead-domain scoring, redirect mechanics, what the link sellers themselves claimed and could not show, and where exact-match domains stand. Extends backlink_profile.py; does not replace the policy in CLAUDE.md.
---

# Link and domain vetting

The policy is in CLAUDE.md: acquisition is permitted, risk is priced per site
(protect, build, push), every placement is recorded, and results are measured
against a control. This skill is the buyer's checklist.

Its main source is unusual. Six people who sell links stood up and explained
how their competitors' inventory is faked. Believe the description of the
fakery. Discount the conclusion, which in every case was "so buy ours".

## Stop buying on DR

- DR against being cited by an AI engine: reported at -0.05 over 5 billion
  citations (the attribution is garbled; probably a tool vendor's study).
  Surfer, on Common Crawl PageRank: -0.01 for the page being cited, +0.05 to
  +0.06 for the brand being named. Near zero both ways.
- DR can be raised to order. One speaker quoted a Fiverr listing: DR 74 for a
  hundred dollars.
- Traffic can be bought. The recipe described on stage is a simple site,
  connected to the tools, fed cheap junk traffic on branded keywords, and the
  numbers show in the tools within weeks. Stewart Vickers says he pushed "6,000
  searches a month" for his own name into a keyword tool.
- A typical buy described as worthless: about $12,000 a year for DR 65 sites
  with no real authority.

Our strategist rule still uses "lowest DR in the top 5". Retire it as a buying
signal. For reading how contested a SERP is, use the Door Audit in
`ai-answer-measurement`.

## The tells of a manufactured seller

Check each before paying. All are observable from outside.

| check | tell |
|---|---|
| What the traffic is for | Open the top pages and keywords. One "business and crypto" site drew 80% of its traffic from celebrity terms |
| Branded share | If almost all traffic is the site's own name, treat the traffic as bought |
| Traffic against citations | A real 5,000-visit site usually has hundreds of AI citations. Lots of traffic and none is odd. Lots of citations on off-topic pages is no use to us |
| Outbound volume | How many posts a month does it sell, and how many sites does it already link to. One sold 60 posts a month at $150. Link value is shared across everything it sells |
| PageRank against harmonic centrality | A domain whose PageRank runs far ahead of its closeness to the web's core (about 15 times was the figure, from a hallway conversation) has been inflating itself with bought links |
| Link type | Forum and profile links, penalised or traffic-hit domains, manipulated metrics: drop all three |
| Indexation | Is the placement page indexed in Google and Bing. Check monthly; an unindexed placement is wasted |
| What the seller does to the post | Bulk suppliers mislabel links nofollow, remove content later and drop tables. Agree terms first |
| Is the audience ours | Are the top pages read by people who might want a trade school |

`backlink_profile.py` already measures domains per subnet, anchor
concentration, referring pages per domain and first-seen dates. It caught
vettechcolleges' network. Three columns to add: branded-traffic share,
outbound link count, and harmonic centrality rank from Common Crawl's public
ranks.

## What to buy on instead

**Traffic value and the count of top-3 keywords** (Leo), not DR.

**Topical relevance, measured from the SERP.** His process maps straight onto
our stack:

1. Pull the site's target keywords from Search Console, a few hundred.
2. Fetch the top 30 results for each through DataForSEO.
3. Rank domains by how many of those keywords they appear for.
4. Of those, find which accept placements. Choose on price per keyword
   covered, neither the cheapest nor the dearest.

**Sub-query coverage, for AI citation.** "Michael's" publisher map, the best
single procedure in the link talks:

1. Run the keyword through ChatGPT, Perplexity and Claude. Save the pages
   cited and the sub-queries each run used.
2. For each sub-query, add the Google and Bing top 10 and the AI Overview
   sources.
3. Rank **pages, not domains**, by how many sub-queries they cover.
4. DR goes in the last column.

His example: a DR 41 page covering five sub-queries against a DR 85 page
covering none. That page list is the outreach list. It is the same thing
`listicle-placement` builds in its first step, with fan-out added, and
`query_battery.py` holds the prompts.

**The placement itself.** A placement that ranks is worth more than one that
does not: choose a keyword the post can win, write real long-form content,
answer the sub-queries inside it, and ask for internal links from the
publisher's other pages. Kasra Dash now writes deep-research pieces for bought
placements on the view that 500 words of filler does not get cited. A brand
mention with the link, always.

**Budget from the gap.** Estimate what competitors spend from a link gap with a
price column and a count of how many of them bought each domain. Do not bring
$1,000 to a SERP where the incumbents spend $10,000. Prices quoted on stage
are inconsistent ($200 to $600 a link in the US by one account, $30 to $50
before late 2023 by another), so price from live quotes, not from this file.

## Dead and aged domains

Adrian's summary, "sometimes it works, sometimes it doesn't and sometimes it's
hard to tell", is the accurate one. The sellers offered no better.

- Charles Floate: success 12 to 15% for expired domains against 90%+ for aged
  ones still holding equity. "Our testing", no count, no definition of success.
- Stewart Vickers scores candidates on four inputs and ignores DR and how
  brandable the name is. This part is sound whoever is buying:
  1. Count of the domain's best individual links: followed, in content, from
     real sites with their own traffic.
  2. Whether AI engines currently cite the domain.
  3. Harmonic centrality from Common Crawl.
  4. Current keyword traffic.
- Run `backlink_profile.py` before bidding, as CLAUDE.md already requires.
  Add those four.
- **Redirect to a new slug.** Kyle Roof: when a hit domain was redirected to
  the same path on a new domain, the problem followed after about three
  months. A new slug did not carry it.
- Emilio Takas reports recovering a tanked site by re-creating every page on
  new URLs with no redirects or canonicals, picking up in two to three weeks.
  One account, and it throws away whatever the old URLs still held.
- Niches said to hold value when expired: sports, video games, board-game
  media. Unbased.
- Check for a live trademark before bidding. That is a legal question, not a
  ranking one.

Expired domains with a live Google Business Profile attached were recommended
by two speakers (about $10 each through a marketplace) for rank-and-rent.
Buying the domain is permitted. Claiming a profile for a business we do not
operate is misrepresentation and is refused, as are the verification bypasses
that were described with it.

## Networks and "citations for AI"

Four vendors sold versions of the same product: rebuilt aged domains
publishing posts that mention a brand, with or without a link, aimed at being
cited by AI. Prices heard: $40 a post, or 6,000 credits for $25,000.

What they showed: nothing measurable. One second-hand unnamed case. Four
before-and-after screenshots with no prompt counts, run counts, engines,
periods or controls, from a speaker who said he had not slept in four days.
A 250-document figure from a real research paper about backdoors in models
trained from scratch, used as if it described brand recommendations in live
assistants. One founder told the room his company had run out of cash.

Against that: single-run screenshots are uninformative when two runs of the
same prompt share 40% of brands, and Moeller's contest saw one site with 2,000
backlinks not recommended at all.

Position:

- Protect and build tier: no.
- Push tier: a small test is permitted by policy, on Adrian's go since it is
  money on a paid channel. Record every placement in the link tables. Measure
  on a frozen cohort with repeated runs against a held-back set, 90 days.
  Decide by the 5-point rule.
- A vendor who hides which domains carry the placement is selling something
  that cannot be audited or removed. We need the URLs, for the reason CLAUDE.md
  gives: if a site is hit we must know what to take down.
- White-label resale to a client, with the agency kept invisible, is a client
  trust problem before it is anything else.

## Anchors

Adrian's rule: no exact-match anchors. The testing panel still uses them
sparingly, and it is worth recording what they do without adopting it: a new
domain goes heavy on branded anchors; a page sitting around position five gets
one or two exact-match links plus internal links from the homepage. Kyle Roof
uses the full page title as the anchor, which gives a partial match with
context. That last one fits our preference for phrase-match and is worth using.
Two panellists called the "natural profile" a comfort blanket whose real use is
spotting bad actors. That is how we use it.

## Exact-match domains

The evidence is mixed and worth holding as mixed.

- For: Quaid's freeloadbalancer.com, live since 2015, which he says brought 160
  leads in its first week and about 50 a month for ten years, needing "one or
  two links". Leo's best-category-software domain: 190 AI citations in 90 days
  on a small prompt set. Both self-reported.
- Against: in the King of AEO contest, 31 exact-match domains were tracked at
  the start and 7 remained in Google after about a month.

Reading: an exact-match domain carrying a real, useful thing, openly part of
the brand, has a long life. One carrying a thin page for a contest does not.
That is the tool-sites model, and `plays.md` uses it for LoadLander.

## Local links

Joy Hawkins: "tons of links" built with almost no movement in the local pack,
measurable on organic. Dated tests. For a local client, links are an organic
lever, not a map lever. See `local-pack-2026`.

## Refused

Bought traffic to "power up" a placement. Micro-worker posts on other people's
accounts. Hacked or injected placements. Misrepresenting who we are to a
publisher. Negative SEO. And any guarantee, which is what every link vendor in
this set was selling.
