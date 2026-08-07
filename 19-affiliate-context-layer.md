---
name: affiliate-context-layer
description: >
  Give an affiliate site an AI context layer by serving superlight, citation-dense MARKDOWN TWINS
  of its existing money pages at the SAME URL, via a Cloudflare Worker (content negotiation), with
  llms.txt discovery. No new competing pages, so no cannibalisation. Trigger when asked to build or
  refresh a context layer, AEO, GEO, llms.txt, or markdown twins; to make a site citable by AI; or
  when an affiliate site is named (e.g. automechanicschools.com, radiologyed.org). Runs per site
  from config in orchestrator.db.
---

# Skill 19: Affiliate Context Layer

Makes an affiliate site's existing money pages maximally citable by AI engines WITHOUT creating new
pages. For each money page it publishes a markdown TWIN at the SAME URL: same facts, the page chrome
and all affiliate/lead-gen units removed, and a dense, accurate Sources section added. A Cloudflare
Worker serves the twin only to AI crawlers (and explicit markdown requests); humans and Googlebot
always get the original HTML. Same URL means no cannibalisation, authority stays on the money page,
and an AI citation lands the human on the monetised page.

Read before running: Skills 05 (orchestrator ops), 10 (data sources), 11 (content style), 12 (agent
operations). Related: 06 and 16 (E-E-A-T / author authority), 14 and 17 (GSC / GA credentials), 13
and 15 (architecture / technical SEO).

## Why this design (read once)
The money pages are already the informational answer, so a separate /data/ or subdomain page would
cannibalise them and split authority. The markdown twin is an alternate representation of the SAME
page, not a second page, so nothing competes, authority stays consolidated on the money URL, and the
cited URL delivers the human to the page with the units. Use paths on the existing domain, not a
subdomain; domains are already Cloudflare-proxied, so no DNS change.

## Non-negotiable guardrails
- NO affiliate or lead-gen links or units in any twin.
- NOT cloaking: humans and Googlebot (ranking) ALWAYS get the unchanged HTML. Only AI-answer crawlers
  and explicit markdown requests get the twin, and the twin is a faithful lighter version of the same
  content. It must never assert anything the HTML does not.
- FAIL OPEN: any Worker error, or no twin found, serves the origin page. Never break a money page.
- No fabrication (Skill 12 hard gate): every figure sourced and dated via Skill 10 data sources (BLS,
  accreditors, state licensing boards). Unverifiable claims are deleted, not softened.
- Style (Skill 11): no em-dashes anywhere, including agent-written copy. Follow Skill 11 throughout.
- Freshness: each twin shows "Last checked [date]"; refresh on schedule.
- Value bar: twins add citations and clean structure, not thin duplicates (avoid scaled-content).
- Live-site safety: generate and preview first; deploy the Worker to production only after Adrian's
  explicit go; verify HTML is unchanged for humans/Googlebot before and after.

## Inputs (read at runtime; do not hardcode)
Site config lives in the database, not in files. Read the site's row from
~/orchestrator/orchestrator.db table affiliate_sites (READ-ONLY; per Skill 12 never SELECT * on that
table, it carries live credentials; select only the columns you need). Use ~/orchestrator/INVENTORY.md
as the canonical table/column map. Expect per site: domain, WordPress REST base and credential
reference, niche, the money-page set (or discover via sitemap / GSC), author and E-E-A-T details
(Skills 06 and 16), target queries, competitors. GSC/GA credentials via Skills 14 and 17.

## New infrastructure (needs Adrian's go)
The Cloudflare Worker and its KV namespace are new infrastructure. Per Skill 12, anything touching
DNS, credentials, or infrastructure requires Adrian's explicit go, and any new script, table, or data
file adds a line to ~/orchestrator/INVENTORY.md in the same commit. Stage and preview first; deploy to
production routes only after sign-off.

## Modes
- build: create twins for money pages that lack them.
- maintain: refresh citations and "Last checked" dates; re-verify.
- new-topic: create net-new dual-format pages (HTML plus twin) for gaps found in the baseline.

## Procedure
1. Load and select. Read the site's affiliate_sites row. List money pages (from the DB, the sitemap,
   or GSC top pages via Skill 14). Dry-run: pick the top 2 to 3 pages.
2. Baseline. For each page's target query, record what ChatGPT, Gemini, Google AI, and Perplexity
   answer and who they cite today. Record the gap.
3. Generate the twin for each page:
   - Fetch the live HTML; extract the main content (readability-style); drop nav, sidebars, footers,
     and ALL affiliate/lead-gen units.
   - Keep the exact facts and claims from the HTML; add no new claims.
   - Add a dense, accurate "## Sources" section (authoritative, linkable references that support the
     facts; use Skill 10). Add "> Last checked: [YYYY-MM-DD]".
   - Prepend front matter: title plus canonical (the HTML page URL). Follow Skill 11 style.
   - Store in Workers KV keyed "md:{host}{path}".
4. Serve via the Worker (content negotiation; fail open; noindex on the markdown). See sketch below.
5. Discovery: write /llms.txt listing the twin URLs with one-line descriptions; add
   <link rel="alternate" type="text/markdown" href="URL.md"> to each money page head; ensure robots.txt
   allows the AI crawlers you want (GPTBot, ClaudeBot, PerplexityBot, Google-Extended, etc.). See
   Skill 15.
6. Verify: request each URL as an AI user-agent (expect markdown) AND as Googlebot plus a browser
   (expect the unchanged HTML). Confirm no money page changed for humans/Googlebot.
7. Monitor: log AI-crawler hits at the Worker; track citations and rankings vs baseline (GA via 17,
   GSC via 14); report through Skill 05.
8. new-topic mode (optional): for uncovered gaps, create net-new HTML pages plus twins.

## Cloudflare Worker (starting sketch)
```js
// Serve markdown twins to AI crawlers; HTML to everyone else. Fails OPEN to origin.
const AI_UA = /GPTBot|OAI-SearchBot|ChatGPT-User|ClaudeBot|Claude-Web|anthropic-ai|PerplexityBot|Perplexity-User|Google-Extended|Applebot-Extended|Amazonbot|CCBot/i;
export default {
  async fetch(req, env) {
    try {
      const url = new URL(req.url);
      const ua = req.headers.get('user-agent') || '';
      const accept = req.headers.get('accept') || '';
      // Ranking crawlers and humans must never be altered:
      if (/Googlebot(?!-)/i.test(ua) || /bingbot(?!-ai)/i.test(ua)) return fetch(req);
      const wantsMd = url.pathname.endsWith('.md') || url.searchParams.get('format') === 'md'
                      || AI_UA.test(ua) || accept.includes('text/markdown');
      if (!wantsMd) return fetch(req); // human -> origin HTML
      const path = url.pathname.replace(/\.md$/, '');
      const md = await env.TWINS.get('md:' + url.hostname + path); // Workers KV
      if (!md) return fetch(req); // no twin -> fail open to origin
      return new Response(md, { headers: {
        'content-type': 'text/markdown; charset=utf-8',
        'x-robots-tag': 'noindex',
        'link': '<' + url.origin + path + '>; rel="canonical"',
        'cache-control': 'public, max-age=3600'
      }});
    } catch (e) { return fetch(req); } // never break the money page
  }
}
```
Generation is a separate step (step 3): the agent produces the markdown and writes it to the TWINS KV
namespace (wrangler or the CF API). The Worker only reads and serves.

## Definition of done
- Twins generated for the selected money pages, stored in KV.
- Worker deployed (after Adrian's go) on the zone route; fail-open verified.
- AI user-agent gets markdown; Googlebot plus a browser get the unchanged HTML (verified).
- No affiliate units in any twin; every fact sourced and dated.
- llms.txt, rel=alternate, and robots updated.
- Baseline captured; monitoring/refresh scheduled.
- INVENTORY.md updated for any new script/table; per-site status reported via Skill 05.

## Dry-run targets
radiologyed.org first (accreditation/salary data is highly citable and already in the system), then
automechanicschools.com. Per site: 2 to 3 top money pages; generate and preview twins, show Worker
routing, verify HTML unchanged for humans/Googlebot, and report the baseline gap.
