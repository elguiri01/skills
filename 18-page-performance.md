# Skill 18 — Page Performance (Core Web Vitals)

How to measure, diagnose and fix Core Web Vitals across the portfolio, and how
the scheduled review keeps them fixed. Skill 15 §3–§4 named Core Web Vitals as a
**[UI]** job — something only a human with PageSpeed Insights could do. That is
no longer true for lab data: `perf_audit.py` measures real LCP/FCP/CLS in
headless Chromium under Lighthouse's mobile profile, on every site, on a
schedule. This skill owns that loop.

Written 2026-08-06, from fixing automechanicschools.com (LCP 3.30s → 1.74s).

## Field vs lab — know which one you are holding

Google ranks on **field** data (CrUX: real Chrome users, 28-day rolling). Our
audit is **lab** data (one synthetic load, throttled). They disagree, and that is
normal: field data mixes devices, networks and cache states we cannot simulate.

Use them for different things:
- **Lab (perf_audit.py)** — finding *causes* and proving a fix worked. It is
  reproducible, so a before/after difference is real signal.
- **Field (Search Console → Core Web Vitals, PageSpeed Insights) [UI]** — the
  number Google actually uses. Check it a few weeks after a fix ships; CrUX is a
  28-day rolling window, so it moves slowly.

Never report a lab improvement as a ranking improvement. It is a *cause* fixed;
`weekly_performance.py` tells you whether rankings followed.

## Thresholds

| Metric | Good | Poor above | Notes |
|---|---|---|---|
| LCP | < 2.5s | 4.0s | The one that usually fails here. Hero image or main heading. |
| CLS | < 0.1 | 0.25 | Reserve space for images, ads, embeds. |
| INP | < 200ms | 500ms | Not measured by our audit (needs real interaction). Plugin/JS bloat. |
| FCP | < 1.8s | 3.0s | Not a CWV metric, but it is the ceiling LCP can never beat. |

A page's verdict is the **worst** of its metrics. `perf_audit.py` scores it that
way deliberately — "good LCP, terrible CLS" is not a good page.

## Measuring

```bash
python3 perf_audit.py --url https://site.com/page/   # one page, with diagnosis
python3 perf_audit.py --domain site.com              # one site's homepage
python3 perf_audit.py --all                          # whole portfolio (~25 min)
python3 perf_audit.py --all --pages 2                # + each site's top GSC page
python3 perf_audit.py --report --compare --html      # latest vs previous run
```

Every run is stored in `perf_audits`, so the history is the evidence base.

Measurement is **serial on purpose**. The network throttle is per-browser;
auditing pages in parallel makes them share one simulated 1.6 Mbps pipe and
inflates every number. Do not "optimise" this into a thread pool — you would be
optimising away the measurement's validity.

## The diagnosis that matters: the preload-scanner blind spot

This is the single most common LCP fault on these sites, and it is invisible if
you only look at the number.

A browser's **preload scanner** reads ahead of the HTML parser and starts
downloading everything it can see in the markup — `<img src>`, `<script src>`,
stylesheets. It cannot see **CSS background images**, because those live inside
a stylesheet. A `background-image` is only requested after:

1. every render-blocking stylesheet and head script has downloaded, **and**
2. the browser has done its first layout and knows the element exists.

On a GeneratePress "Page Hero" or a GenerateBlocks section background, that is
exactly the LCP element. So the LCP image starts downloading *last*, after the
whole critical path — and then still has to download.

`perf_audit.py` records this explicitly: `lcp_is_css_bg`, `lcp_discovery_ms`
(when the request actually started) and `lcp_preloaded`. When you see a CSS
background image discovered after ~1s with no preload, you have found it.

The fix is one line of HTML:

```html
<link rel="preload" as="image" href="…/hero.webp" fetchpriority="high">
```

The preload scanner sees *that*, so the image downloads in parallel with the CSS
instead of after it.

## Fix playbook — in order of payoff

Work down this list and re-measure after each step. Stop when the page is
"good"; do not chase a 100 score (Skill 15 §4 still applies).

1. **Preload the LCP image.** `python3 lcp_preload.py --domain D --page-id N
   --image URL --apply`. Biggest single win when the hero is a CSS background:
   worth ~1.2–1.6s. Idempotent, backs up the prior content, verifies the live
   page, and restores with `--restore`.
2. **Right-size the LCP image.** A 2400px-wide hero served to a 412px viewport
   is pure waste. Target < 100KB for a hero; WebP; the preload cannot help with
   bytes it still has to move. When the hero is heavy *and* its URL lives
   somewhere unreachable (the Customizer), `lcp_preload.py --css-selector` emits
   a `background-image` override alongside the preload. On a Jetpack/Photon site
   (`i0.wp.com/...`) you do not need to touch the media library at all — append
   `&quality=55&strip=all` to the same Photon URL. okchef.org's hero went 468KB →
   32KB that way.

   **The override and the preload must be the same URL.** If they differ the
   browser fetches both and you have made the page slower. Always confirm
   exactly one request for the hero after applying.
3. **Cut render-blocking head assets.** Every sync `<link rel=stylesheet>` and
   `<script src>` in `<head>` delays first layout, which delays *everything*.
   Google Fonts is a third-party blocking request — self-host or `media=print
   onload`. Defer JS that is not needed for first paint.
4. **CLS: set width/height** (or `aspect-ratio`) on images, ads and embeds.
5. **Server/TTFB.** Only if TTFB > 800ms. Check host caching is actually on
   before blaming the host.

**Never** lazy-load the LCP element. `loading="lazy"` on the hero is a
self-inflicted LCP failure; lazy-loading is for below-the-fold only.

**Never** remove or defer an ad/affiliate placement to win milliseconds. Ad
shortcodes are sentinel-protected (Skill 09; `push_expansion.py` aborts if the
inventory changes). Revenue beats a score. Defer, never delete — and if deferring
an ad script changes what renders, revert it.

## WordPress mechanics — what is automatable and what is not

The stack is WordPress + GeneratePress (+ GP Premium) + GenerateBlocks, mostly on
SiteGround. Hard-won specifics:

- **A `<link rel="preload">` in page content works.** WordPress renders it
  verbatim for an authenticated editor, and the preload scanner finds it during
  the initial byte scan — early enough, even though the tag sits in the body.
  This is what `lcp_preload.py` uses.
- **GP Elements hooks are the *proper* home, but REST cannot finish the job.**
  A hook element into `wp_head` is the clean mechanism, and `_generate_hook` /
  `_generate_hook_priority` *are* writable over REST. Its display rules live in
  `_generate_element_display_conditions`, which GP does **not** register with
  REST — so an element created over the API has no display rule and renders
  nowhere. Verified empirically. Setting that rule is a **[UI]** step. Until
  someone does it, content injection is the only automatable path.
- **The GeneratePress Customizer is not REST-writable.** Hero background image,
  colours and padding come out in `generate-style-inline-css`. Changing the hero
  image URL is therefore **[UI]**.
- **Content injection needs a page.** If a site's homepage is the posts index
  (`show_on_front=posts`, `page_on_front=0`) there is no page content to inject
  into. kaparalegalschools.com is in this state.
- **Widgets are not a substitute.** `wp/v2/widgets` accepts a text widget over
  REST, but its content is run through kses, which strips `<link>`. A hidden
  `<img>` survives kses and would work — except widgets created over REST did
  not render on kaparalegalschools at all (Dynamic Widgets is active and gates
  visibility). Treat the widget route as unproven.
- **Only 26 of 62 sites have a `wp_app_password`.** Without one there is no REST
  write path at all, so no automated fix — businessdegree.org and
  poweredelectrician.com are both blocked on this, not on technique. Generating
  app passwords is Adrian's job (Skill 12: credentials).
- **SiteGround Speed Optimizer has a full REST surface** at
  `/wp-json/siteground-optimizer/v1/` (`fetch-options` to read;
  `enable-option`/`disable-option` and per-feature routes to write). On
  automechanicschools every front-end optimisation was **off**: `optimize_css`,
  `combine_css`, `optimize_javascript`, `optimize_javascript_async`,
  `optimize_html`, `enable_browser_caching`, `enable_gzip_compression`,
  `disable_emojis` all `0`. That is a large untapped lever — and a large
  breakage risk.

**Rule for the SG toggles: never flip minification/combination unattended.**
Combining or deferring CSS/JS is the classic way to silently break a WordPress
layout or an ad script. Flip them one at a time, in a window when someone can
look at the site, and re-measure and eyeball the page after each. The safe ones
(`disable_emojis`, `enable_browser_caching`, `enable_gzip_compression`) still
deserve a visual check.

## Worked example — automechanicschools.com, 2026-08-06

The homepage LCP was **3304ms** on throttled mobile. The diagnosis:

- LCP element `<div class="page-hero">` — a GeneratePress Page Hero whose
  background image (`home_img.webp`, 2400×425, 49KB) is set in
  `generate-style-inline-css`.
- Nine render-blocking head assets finished at ~1294ms (jQuery, sync, was the
  long pole; Google Fonts and an esyoh stylesheet were third-party blockers).
- The hero image request therefore did not start until **1655ms**, then took
  1613ms while competing with a second background image and the esyoh widget.
- 1655 + 1613 ≈ **3304ms**. The image was never the problem; *when it was asked
  for* was.

Fix: one preload tag via `lcp_preload.py`. Result: **LCP 1740ms** (−1564ms),
verdict `good`. FCP was unchanged at ~1.6s — which is now the ceiling, and
step 3 of the playbook (render-blocking assets) is what would lower it further.

The lesson generalises: **measure when the LCP resource was requested, not just
how big it is.** Late discovery is usually worth more than compression.

okchef.org, same day, showed the other half of the rule. Same CSS-background
hero, but the image was a **468KB PNG** served through Photon. Preloading alone
would only have moved LCP to ~3.7s — still poor, because the bytes dominated.
Preload *plus* `&quality=55&strip=all` on the same Photon URL (468KB → 32KB)
took it from **4276ms to 1588ms**. Read the diagnosis before reaching for the
fix: `lcp_discovery_ms` says preload, `lcp_download_ms` says resize, and a big
number in both means you need both.

## The periodic review

`perf_audit.py --all --pages 2 --report --compare --html` runs **weekly, Sunday
04:10** (Europe/Madrid), before Monday's `weekly_performance.py` digest — so the
Monday digest reports fresh performance alongside rankings, traffic and revenue.
Output: `review/performance.html`, and a PERFORMANCE section in the weekly
digest listing pages that are poor or that regressed since the last run.

What to do with it:

1. **Regressions first.** A page that got materially slower since last week
   changed for a reason — a new plugin, a new ad, a bigger image. Recent causes
   are the cheapest to fix and the easiest to identify.
2. **Then poor pages by revenue.** Prioritise the same way Skill 15 does: a
   slow page on an earning site beats a slow page on a $0 site. Cross-reference
   the revenue tables, not the LCP ranking.
3. **Ignore small movements.** A throttled load carries real variance — server
   state, the actual network under the simulated one, CDN cache warmth. The
   audit already loads each page twice and keeps the faster run; on top of that
   the report only calls something a regression when it moves **> 500ms and
   > 25%**. Anything smaller is noise. Do not chase it, and distrust any single
   week's comparison until a few runs of history exist.

New sites inherit the review automatically — targets come from
`affiliate_sites`, so a site is covered the moment it is in the table.

## Related skills

- **Skill 15 (Technical SEO)** — the wider technical layer. §3–§4 define the
  metrics and the field-data checks; this skill owns the automated lab loop and
  the fix mechanics.
- **Skill 09 (Page Optimisation)** — §6 page speed, and the ad-placement rules
  that constrain what may be deferred or removed.
- **Skill 05 / INVENTORY.md** — `perf_audit.py`, `lcp_preload.py`, the
  `perf_audits` table, and the cron entry.
