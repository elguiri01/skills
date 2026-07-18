# Skill 17: GA4 Analytics Credentials & Onboarding

How to give the orchestrator Google Analytics 4 access to an affiliate site, so
`ga_connector.py` can pull its on-site behaviour. GA4 fills the gap between GSC
(search/traffic) and the revenue scrapers (final $): channel mix, engagement,
landing pages, and — directly relevant to the LLM-traffic objective — the GA4
**"AI Assistant" channel** (ChatGPT/Perplexity/etc. referrals).

Written 2026-07-18. This mirrors Skill 14 (GSC) and deliberately reuses the same
service account, so onboarding is lighter.

## What the connector expects (confirmed from code)

`ga_connector.py` uses the **same service account as GSC** (same Cloud project /
user):
- **Service-account key:** read from the GSC credentials CSV
  (`~/affiliate-agent/data/gsc_credentials.csv`, first row's `Key Path`, resolved
  relative to `/home/adrian`). No separate key or CSV — one service account
  covers GSC and GA4.
- **Property IDs are auto-discovered**, not configured per site. The Admin API
  lists every GA4 property the service account can see and maps each to its
  domain via the property's web data-stream URL (`https://radiologyed.org` →
  `radiologyed.org`). Discovered IDs are cached in the `ga4_properties` table, so
  discovery only has to succeed once.
- **Manual fallback:** if the Admin API isn't enabled, seed an ID by hand:
  `python3 ga_connector.py --set-property radiologyed.org properties/543321847`
  (find the numeric ID in GA4 → Admin → Property Settings). The connector then
  works off the cache without the Admin API.
- **Scope:** `analytics.readonly` (read-only; covers both Data and Admin).

## One-time: enable the APIs (same Cloud project as GSC)

In the **same** Google Cloud project the GSC service account lives in
(`linear-reporter-...`), enable both:
- **Google Analytics Data API** (`analyticsdata.googleapis.com`) — the report
  data. Essential.
- **Google Analytics Admin API** (`analyticsadmin.googleapis.com`) — property
  auto-discovery. Recommended; without it, use `--set-property`.

Do **not** enable the legacy "Google Analytics API" (Universal Analytics) — UA
was shut down in 2024 and returns nothing for GA4.

> ⚠️ **Propagation lag:** newly-enabled Google APIs take a few minutes (sometimes
> up to ~an hour) to propagate. During that window calls fail with
> `PERMISSION_DENIED: ... has not been used in project ... or it is disabled`,
> even though the API is enabled. The connector reports this as "still
> enabling/propagating — retry in a few minutes". Wait and retry; it is not a
> code or permissions problem.

No new key is needed — the GSC service account is reused.

## Per-site: grant access (repeat for each site)

The only per-site human step:
1. In **Google Analytics** → Admin → **Property Access Management** for the
   site's GA4 property, **Add** the service-account email
   (`orchestrator-gsc@linear-reporter-...iam.gserviceaccount.com`) with role
   **Viewer**. (Viewer is read-only, all the connector needs.)
2. That's it. Once the Admin API is enabled, the connector auto-discovers the
   property on the next run. If the Admin API is off, seed it once with
   `--set-property`.

Same service account, same project as GSC — if a site is already set up for GSC,
GA4 is just "add the same email as a Viewer on the GA4 property".

## Using the connector

```
python3 ga_connector.py --list                 # domain -> property map (cached + discovered)
python3 ga_connector.py --all                  # discover + scrape every accessible property
python3 ga_connector.py --site radiologyed.org
python3 ga_connector.py --site radiologyed.org --days 90
python3 ga_connector.py --report               # sessions + AI Assistant (LLM) summary
python3 ga_connector.py --set-property <domain> properties/<ID>   # manual fallback
```

Scheduled with the daily revenue scrape (see the crontab). Data lands in:
- **`ga4_traffic_daily`** — per-day sessions/users/engaged/conversions
  (per-day rows, so windows are always comparable — unlike the aggregated tables).
- **`ga4_channels`** — channel mix per window, incl. `AI Assistant`. Tagged with
  `window_days` so a 30-day and 90-day scrape are never silently compared
  (the lesson from the gsc_pages window bug).
- **`ga4_landing_pages`** — top landing pages per window.
- **`ga4_properties`** — the domain → property-ID cache.

## Conversions note

GA4 `conversions` returns 0 until **key events** are configured on the property
(a GA4 setup step — mark form submits / outbound clicks to providers as key
events). Until then, sessions/engagement/channel/landing-page data is the usable
signal. Flag key-event setup as a per-property task when conversion measurement
matters.

## Troubleshooting

- **"has not been used in project ... or it is disabled"** — the API is enabling;
  propagation lag. Wait a few minutes and retry.
- **"No GA4 property for <domain>"** — the service account isn't a Viewer on that
  property yet, or the Admin API is off (so no discovery). Add the Viewer grant,
  or `--set-property` the numeric ID.
- **Property discovered under the wrong domain** — the web data-stream URL didn't
  match the site's domain; `--set-property` overrides it.

## Related skills

- Skill 14 — GSC Credentials (same service account; set that up first)
- Skill 13 — System Architecture (`ga4_*` tables)
- Skill 12 — Agent Operations (config/ off limits; scripts read keys, agents
  don't)
