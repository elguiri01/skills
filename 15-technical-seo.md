# Skill 15: Technical SEO Review

How to review an affiliate site for the technical foundations that let content
rank: indexability, crawlability, Core Web Vitals, page speed, and structured
data. Content quality (Skills 06/09/11) and off-site authority (Skill 16) do
nothing if Google can't crawl, index, or render the page fast. This skill is the
technical layer under all of that.

Written 2026-07-18. The stack is WordPress + GeneratePress + GenerateBlocks +
AIOSEO (All in One SEO), hosting per `affiliate_sites.hosting_plan`. Where a
check needs the Search Console UI or PageSpeed Insights (things the API scopes
don't cover), it is marked **[UI]** and belongs on a human's list.

## When to run this

- A site's pages get impressions but won't rank, or won't get indexed at all.
- After a migration, a redesign, or a bulk content push.
- Quarterly as a health pass on the top-revenue sites (Skill 13 revenue rank).
- When GSC shows a rising "not indexed" count (see Indexability below).

Prioritise by revenue: run the top-earning sites first. A technical fix on a
site with traffic returns faster than on a $0 site.

## 1. Indexability — the first gate

If a page isn't indexed, nothing else matters. **[UI]** In Search Console →
Indexing → Pages, read the "Not indexed" reasons. The overview screenshot for
radiologyed showed **144 not indexed vs 135 indexed** — that ratio is worth a
look on any site: more excluded than included usually means real waste.

Common causes and the fix:
- **"Crawled - currently not indexed" / "Discovered - not indexed":** Google
  judged the page low-value or is deprioritising crawl. Fix with content depth
  (Skills 09/11) and internal links from strong pages, not technical tweaks.
- **"Excluded by noindex":** a `noindex` tag is set (check AIOSEO per-page
  settings and any theme/plugin default). Remove it on pages that should rank.
- **"Duplicate, Google chose different canonical" / "Alternate page with proper
  canonical":** canonical tags pointing away. On these education sites the
  state-page and `/es/` translation structure is a common source — confirm each
  page self-canonicals unless it is genuinely a duplicate.
- **"Blocked by robots.txt":** check `https://<domain>/robots.txt`. It should
  allow crawling of content and reference the sitemap. Rank-and-rent and
  affiliate sites should not block their own money pages.
- **"Soft 404" / "Not found (404)":** thin or empty pages, or broken URLs. The
  `url_checks` table already verifies outbound links; the same idea applies to
  internal — a page returning 404 or near-empty is excluded.

**Sitemaps:** AIOSEO generates an XML sitemap (usually
`https://<domain>/sitemap.xml`). Confirm it exists, lists the money pages, and
is submitted in Search Console. A sitemap that lists noindexed or 404 URLs sends
mixed signals — keep it clean.

## 2. Crawlability and site structure

- **Internal linking:** every converting page (state pages, guides, salary
  pages — Skill 09) should be reachable within a few clicks from the homepage
  and linked from related pages. Orphan pages (no internal links in) get crawled
  rarely. The high-impression informational pages (e.g. anatomy/glossary terms)
  are good internal-link sources into converting pages — see the
  opticiancertification plan for the pattern.
- **Crawl budget:** for large sites (radiologyed has ~130+ pages, the seopirate
  imports thousands of listing rows), don't waste crawl on low-value URL
  variants, faceted params, or `/es/` duplicates that should be canonicalised.
- **HTTPS everywhere:** all internal links and canonicals use `https://`, no
  mixed content. Confirm the certificate is valid (Siteground/host-managed).

## 3. Core Web Vitals

Google uses field data (real Chrome users) for the three CWV metrics. **[UI]**
Read them in Search Console → Core Web Vitals, or per-URL in PageSpeed Insights
(pagespeed.web.dev). Thresholds ("good"):
- **LCP** (Largest Contentful Paint) < 2.5s — usually the hero image or the main
  heading block. Biggest wins: compress/serve images as WebP, set explicit
  width/height, lazy-load below-the-fold only (never the LCP element).
- **INP** (Interaction to Next Paint) < 200ms — replaced FID. Driven by heavy
  JavaScript. On a GeneratePress/GenerateBlocks site this is usually plugin
  bloat; audit active plugins and third-party scripts (ad/affiliate scripts are
  common culprits, but ad placements are sentinel-protected — do not remove
  them, defer them).
- **CLS** (Cumulative Layout Shift) < 0.1 — content jumping as it loads. Fix by
  reserving space for images, ads, and embeds (width/height or aspect-ratio).

GeneratePress is lightweight by design, so CWV problems on these sites are
almost always added weight: unoptimised images, an unused plugin, or a
render-blocking third-party script. Strip weight before adding a caching plugin
on top.

## 4. Page speed (lab)

Lab data (PageSpeed Insights score, GTmetrix) is a proxy for CWV but not the
ranking signal itself — field CWV is. Use lab tools to find *causes*:
- Image weight (the usual top offender): serve WebP, size correctly, lazy-load.
- Render-blocking CSS/JS: defer non-critical scripts.
- No caching / no CDN: Siteground has caching; confirm it is on. Cloudflare (we
  already use it for DNS on some sites) can front static assets.
- Server response time (TTFB): a slow host or an overloaded shared plan.

Do not chase a 100/100 score. Get CWV into "good" and stop; beyond that the
effort is better spent on content and links.

## 5. Structured data (schema)

Schema doesn't directly boost rankings but earns rich results (star ratings,
FAQ accordions, breadcrumbs) that lift CTR — and CTR on page-2 rankings is
exactly the lever for sites like opticiancertification. AIOSEO can output most
of this; confirm it is enabled and valid.

Relevant types for education lead-gen sites:
- **BreadcrumbList** — on every page; helps Google understand structure and
  shows breadcrumbs in results.
- **FAQPage** — on pages with a genuine Q&A section (the "questions" data exists
  in `sp_pages.questions_json`). Only mark up FAQs actually visible on the page.
- **Course** / **EducationalOccupationalProgram** — for program/training pages,
  where the data is real (from the listings, not invented).
- **Article** with a real `author` — ties into Skill 16 (the persona is the
  author; the author page is the `author` entity).
- **Organization** / **WebSite** with `sitelinks searchbox` on the homepage.

**Hard rule:** never mark up data that isn't visibly on the page, and never
invent ratings/reviews. Fake `AggregateRating` or `Review` schema is a
structured-data spam violation and can earn a manual action (Skill 12: no
invented facts applies to schema too). Validate with the Rich Results Test
**[UI]** before shipping.

## 6. Listing / program-page structure + Course & FAQ schema

The honest, directory-site version of the "high-ranking course page" pattern. We
present and compare real programs from real data and link to the actual provider
to enrol — we never imply we offer or deliver the course (Skill 16).

**Above the fold:**
- **H1** with the exact-match query intent, e.g. "Radiologic Technology Programs
  in Florida" or "Certified HVAC Technician Training" — a listing/topic title,
  not "Enrol in our course".
- **Key facts from real data** where we have them: typical cost, duration,
  credential/award type, accreditor — sourced from the listings
  (`sp_listings`/`sp_colleges`) and JRCERT/BLS, dated, never invented.
- **CTA to the real provider:** "View program at <school>" / "Visit official
  site" linking out (the affiliate/referral link). The conversion is the click
  to the provider, not an enrolment by us.

**Body:**
- Program modules / what's covered and prerequisites — only where we have real
  source data; omit rather than fabricate (Skill 11).
- Balanced pros/cons and the outcome data (completion/placement/salary) with
  sources (Skill 16's editorial-integrity rule).
- A "Last reviewed on <date>" label (data freshness signal).

**Course schema (JSON-LD)** — mark up a listed program only with its REAL
provider and REAL data. `provider` is the school, never us:

```json
{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "AS in Radiologic Technology",
  "description": "Associate of Science radiography program ...",
  "provider": {
    "@type": "CollegeOrUniversity",
    "name": "Keiser University",
    "sameAs": "https://www.keiser.edu"
  },
  "url": "https://radiologyed.org/schools/florida/#keiser-university",
  "educationalCredentialAwarded": "Associate's degree",
  "isAccreditedBy": {
    "@type": "Organization",
    "name": "JRCERT",
    "url": "https://www.jrcert.org"
  }
}
```
Include `hasCourseInstance` / `offers` (price, duration) **only** when the value
is real. Never emit `AggregateRating`/`Review` for a program we haven't got
genuine review data for — fabricated rating schema is a spam violation (Skill 16).

**FAQ schema** — only for FAQs actually visible on the page. Real Q&A exists in
`sp_pages.questions_json`; mark up those, answer them accurately, and don't
invent questions to farm rich results (Google demotes FAQ-schema abuse).

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How long is a radiography program in Florida?",
    "acceptedAnswer": {"@type": "Answer", "text": "Most are 21–24 months ..."}
  }]
}
```

Validate both with the Rich Results Test **[UI]** before applying (apply is
gated, Skill 12).

## Review checklist (per site)

1. **[UI]** GSC Indexing report: not-indexed count and top reasons.
2. `robots.txt` allows content + references the sitemap.
3. Sitemap exists, is clean, is submitted.
4. Money pages self-canonical; `/es/` and duplicates handled deliberately.
5. No stray `noindex` on pages that should rank.
6. **[UI]** Core Web Vitals status (LCP/INP/CLS) in GSC / PageSpeed Insights.
7. Images are WebP, sized, lazy-loaded (except the LCP element).
8. Plugin/script audit for INP; defer render-blocking and third-party JS.
9. Schema present and valid (Breadcrumb, FAQ where real, Course, Article+author);
   no fabricated ratings.
10. Internal links into every converting page; no orphans.

## What the agent can do vs what needs a human

- **Agent (autonomous):** pull GSC page/indexing signals via the connector,
  identify orphan/thin pages from `gsc_pages` and the sitemap, draft schema and
  internal-link additions, flag pages with impressions but no index. Staging
  fixes is fine; applying them to live pages is gated (Skill 12).
- **Human [UI]:** the Search Console Indexing/CWV reports, PageSpeed field data,
  Rich Results Test, robots.txt/host/CDN settings, and anything that publishes.

## Related skills

- Skill 09 — Page Optimisation (content-side ranking work)
- Skill 13 — System Architecture (`gsc_pages`, `url_checks`, `sp_pages`)
- Skill 14 — GSC Credentials (get the data flowing first)
- Skill 16 — Persona E-E-A-T (the author entity behind Article schema)
