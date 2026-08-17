# Keyword research methodology

The agent reads this before doing any research. Customise to your agency's house style.

## Step 1 — Seed keywords
For each priority page on the client's site, identify 3-5 seed keywords that describe the page's intent.

## Step 2 — Expand
Use Ahrefs Keywords Explorer (via MCP). For each seed:
- Get matching terms.
- Filter: monthly search volume >= 100 (configurable per niche).
- Filter: lowest DR in top 5 results <= client's current DR + 10. This is your competitive bar.
- DO NOT use Keyword Difficulty (KD). It's synthetic. Use the lowest DR top-5 method.
- Sort by CPC for commercial-intent keywords. Volume without intent is vanity.

## Step 3 — Cluster
Group keywords by SERP overlap. If two keywords have the same top-10 results in Ahrefs, they share a target page. Don't write two pages targeting overlapping keywords.

## Step 4 — Map
Each keyword cluster maps to one priority page. Output:
```
{
  url: "client.com/category/widget",
  primaryKeyword: "best widgets for X",
  secondaryKeywords: ["widget reviews", "top widgets"],
  searchVolume: 1200,
  competitiveDR: 35,
  intent: "commercial",
  notes: "Tier 1 priority — high CPC, low competition relative to client DR."
}
```

## Step 5 — Anchor analysis (audit, not engineering)
For each priority page, analyze the CURRENT backlink anchor distribution from Ahrefs. The goal is to understand the natural state of the site, identify any over-optimised anchors (which can trigger Google penalties on their own), and brief any future editorial outreach so the natural mix isn't pushed further out of balance.

Healthy editorial profiles tend to have a heavy weight of branded + naked-URL anchors and only a small share of exact-match — because that's how real editorial linking works. If your audit shows >30% exact-match on a priority page, that's a signal to investigate (and possibly disavow) regardless of what you plan next.

Important: do not treat this as a recipe for engineering anchor distribution via paid placements. That's link-scheme territory and a search-engine guidelines violation. Any compensated placement should be `rel="sponsored"` or `rel="nofollow"` per Google's rules — anchor distribution on those is a non-issue because they're not passing PageRank.

## Step 6 — Output briefs
For each priority page that needs links/content, output a structured brief downstream agents can consume.

## Don'ts
- Don't research keywords without Ahrefs (synthetic-volume tools lie).
- Don't ignore SERP intent — if top 10 are all category pages and client has a blog, target the right page type.
- Don't propose >5 priority pages per quarter for a small site — too thin a focus.
- Don't engineer anchor distribution via paid placements — that's a link scheme. Compensated placements get `rel="sponsored"` / `nofollow`; earned editorial coverage is what moves rankings.
