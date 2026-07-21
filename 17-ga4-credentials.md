# Skill 17: GA4 Analytics Credentials & Onboarding

How to give the orchestrator Google Analytics 4 access to an affiliate site, so
`ga_connector.py` can pull its on-site behaviour. GA4 fills the gap between GSC
(search/traffic) and the revenue scrapers (final $): channel mix, engagement,
landing pages, and — directly relevant to the LLM-traffic objective — the GA4
**"AI Assistant" channel** (ChatGPT/Perplexity/etc. referrals).

Written 2026-07-18. Corrected 2026-07-19 (see "The per-site correction" below).
This mirrors Skill 14 (GSC) exactly: **one service account per site**, reusing
that site's existing GSC key.

## The per-site correction (read this if you remember otherwise)

The first version of this skill — and of `ga_connector.py` — assumed a single
shared service account covered every GA4 property. **That is wrong**, and it
fails in a way that looks like a permissions bug: querying radiologyed's
property with another site's key returns `403 User does not have sufficient
permissions for this property`.

`gsc_credentials.csv` holds **9 domains and 9 distinct key files, 1:1** — each
service account lives in its own Cloud project. There is no shared account.
Fixed in `ga_connector.py` commit `eb5172e`; verified on radiologyed.org
(2,710 sessions / 30d) and electricalschool.org (138 sessions / 30d).

Onboarding is **two per-site steps, and both are required**: enable the APIs in
that site's Cloud project, then add that site's service account as a user in
GA4. Doing only the first is the failure mode we hit twice — see step 2.

## What the connector expects (confirmed from code, commit `eb5172e`)

`ga_connector.py` uses **each site's own service account** — the same key GSC
already uses for that domain:
- **Service-account key:** `load_site_keys()` reads the GSC credentials CSV
  (`~/affiliate-agent/data/gsc_credentials.csv`) and builds a `Domain` →
  `Key Path` map, resolved relative to `/home/adrian`, skipping rows whose key
  file is missing. No separate key or CSV for GA4 — but no shared key either:
  the domain you pass selects the key.
- **A site with no row in that CSV cannot be scraped.** `--site` exits 1 with
  "No service-account key for <domain>"; `--all` simply never visits it. GSC
  onboarding (Skill 14) is therefore a hard prerequisite for GA4.
- **Property IDs are auto-discovered per site**, not configured. Discovery runs
  against *that site's* Admin API: it walks the account summaries and matches
  each property's web data-stream URL to the domain (`https://radiologyed.org` →
  `radiologyed.org`). Discovered IDs are cached in the `ga4_properties` table,
  so discovery only has to succeed once.
- **Discovery never guesses** (commit `e190bee`). If two or more properties
  match the domain, or none does, it refuses, lists the candidates with their
  display names, and asks for `--set-property`. See "Legacy properties" below —
  this is not a rare edge case.
- **Manual fallback:** if the Admin API isn't enabled, seed an ID by hand:
  `python3 ga_connector.py --set-property radiologyed.org properties/543321847`
  (find the numeric ID in GA4 → Admin → Property Settings). The connector then
  works off the cache without the Admin API.
- **Scope:** `analytics.readonly` (read-only; covers both Data and Admin).

## Per-site step 1: enable the APIs (in THAT site's Cloud project)

This is **not** a one-time central step. Each site's service account lives in its
own Cloud project, so the APIs must be enabled **once per project** — nine
projects for nine sites. Enabling them for radiologyed does nothing for
medassisting.

In the Cloud project that owns the site's GSC service account, enable both:
- **Google Analytics Data API** (`analyticsdata.googleapis.com`) — the report
  data. Essential.
- **Google Analytics Admin API** (`analyticsadmin.googleapis.com`) — property
  auto-discovery. Recommended; without it, use `--set-property`.

To find the right project: the key file named in that domain's `Key Path` column
is the project's key, and the project is identified inside the key file. Do not
open the key file to read it — match on the `Key Path` value, or read the
project name off the service-account email in the GA4 Property Access screen.

Do **not** enable the legacy "Google Analytics API" (Universal Analytics) — UA
was shut down in 2024 and returns nothing for GA4.

> ⚠️ **Propagation lag:** newly-enabled Google APIs take a few minutes (sometimes
> up to ~an hour) to propagate. During that window calls fail with
> `PERMISSION_DENIED: ... has not been used in project ... or it is disabled`,
> even though the API is enabled. The connector reports this as "still
> enabling/propagating — retry in a few minutes". Wait and retry; it is not a
> code or permissions problem.

No new key is needed — that site's existing GSC service account is reused. No
new key is *shared* either: the key differs per site.

## Per-site step 2: add the service account as a user in GA4

**This is the step that gets missed.** Enabling the APIs (step 1) only lets the
service account *call* Google Analytics; it grants no access to any data. Until
the account is added as a user inside GA4 itself, it authenticates perfectly and
sees nothing. Both sites onboarded so far failed here first.

1. In **Google Analytics** → **Admin**, add *that site's* service-account email
   with role **Viewer** (read-only, all the connector needs). Two places work:
   - **Account Access Management** — grants access to every property under that
     GA4 account. This is what fixed electricalschool.org on 2026-07-19, and is
     usually the one you want.
   - **Property Access Management** — grants access to that one property only.
     Finer-grained; fine if you prefer it.

   If discovery still fails after a property-level grant, add at account level.
2. The correct email is in that domain's row of `gsc_credentials.csv`, column
   **Service Account Email** — **not** the email you used for the previous site.
   Each site has its own. Reusing the last one is the most likely mistake, and
   it fails identically to having done nothing.
3. Re-run `--site <domain>`. Grants take a few minutes to propagate. Once the
   Admin API is enabled in that site's project, the property is auto-discovered
   and cached. If the Admin API is off, seed it once with `--set-property`.

**Telling the two failures apart** — the connector now does this for you:
- *"Admin API reachable, but this service account can see 0 GA4 properties"* →
  step 1 is done, step 2 is missing. The message prints the exact email and
  project to add.
- *"Admin discovery failed (… has not been used in project …)"* → step 1 is
  missing or still propagating in that site's project.

If a site is already set up for GSC, GA4 is "enable two APIs in that site's own
project, then add that site's own email as a Viewer". Both steps repeat per
site; neither carries over.

## Legacy properties: check the ID on every older site

**Several of the older sites have two GA4 properties — a legacy one and the
current one — and both expose the same data-stream URL.** The domain therefore
cannot identify the property, and the wrong choice produces data that looks
entirely plausible.

electricalschool.org, 2026-07-19:

| Property | Display name | 30-day sessions |
|---|---|---|
| `properties/253379016` | `electricalschool.org` | 649, 77% Referral |
| `properties/361551651` | `Electrical School - GA4` | **138**, normal mix |

Nothing about 649 sessions looks wrong on its face. Only the referral-heavy
composition hinted at it, and that is not a check you can rely on noticing.
Treat an unverified property ID as unverified data.

**So, when onboarding an older site:** get the numeric ID from **GA4 → Admin →
Property Settings** for the property you actually tagged, and seed it before the
first scrape:

```
python3 ga_connector.py --set-property <domain> properties/<ID>
```

The connector will refuse to auto-pick when it sees more than one match, so a
duplicate is now surfaced rather than silently resolved — but seeding first
avoids the round trip. Newer sites with a single property (radiologyed.org)
auto-discover correctly and need none of this.

If a site was scraped before the ID was verified, delete its rows from
`ga4_traffic_daily`, `ga4_channels`, and `ga4_landing_pages` and re-scrape.
That data is derived and fully re-scrapeable — unlike `jobs`, it carries no
provenance, so deleting it is safe and is the correct fix.

## Using the connector

```
python3 ga_connector.py --list                 # sites with a key, + resolved property map
python3 ga_connector.py --all                  # every site in the CSV, each with its own key
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

- **"403 User does not have sufficient permissions for this property"** — the key
  being used has no access to that property. Either the wrong site's service
  account was added as Viewer, or the grant was never made. Check the domain's
  row in `gsc_credentials.csv` against the email listed in GA4 Property Access.
  This was the original bug (see "The per-site correction"); if you find yourself
  reasoning about a shared service account, that assumption is the bug.
- **"has not been used in project ... or it is disabled"** — the API is enabling;
  propagation lag. Wait a few minutes and retry. Note it names the *project* —
  if it names a project you already enabled, you are looking at a different
  site's project, which is expected.
- **"No service-account key for <domain>"** — that domain has no row (or a
  missing key file) in `gsc_credentials.csv`. Onboard it for GSC first
  (Skill 14).
- **"No GA4 property for <domain>"** — the service account isn't a Viewer on that
  property yet, or the Admin API is off in that site's project (so no
  discovery). Add the Viewer grant, or `--set-property` the numeric ID.
- **"N GA4 properties share this domain (legacy + current?)"** — the site has
  more than one property, as older sites usually do. The connector lists them
  with display names; pick the tagged one in GA4 → Admin → Property Settings and
  `--set-property` it. See "Legacy properties".
- **Numbers look plausible but wrong** (traffic too high, an odd channel mix,
  history starting earlier than the tag) — suspect the legacy property before
  suspecting the connector. Check `ga4_properties` for the ID in use and confirm
  it against GA4 → Admin → Property Settings.
- **Property discovered under the wrong domain** — the web data-stream URL didn't
  match the site's domain; `--set-property` overrides it.

## Related skills

- Skill 14 — GSC Credentials (same service account; set that up first)
- Skill 13 — System Architecture (`ga4_*` tables)
- Skill 12 — Agent Operations (config/ off limits; scripts read keys, agents
  don't)
