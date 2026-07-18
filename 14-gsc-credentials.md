# Skill 14: GSC Credentials & Onboarding a Site

How to give the orchestrator Search Console access to an affiliate site, so
`gsc_connector.py` can pull its traffic. This is the manual, human-only setup
behind the "GSC data for only N of 62 sites" gap: each site needs a Google
Cloud service account granted read access to its Search Console property, then
one row in the credentials CSV. Once the row is in, scraping is automatic.

Written 2026-07-17. Facts about the connector are confirmed from
`gsc_connector.py`; the Google Cloud / Search Console UI steps are the standard
Google procedure (they can't be verified from code, but they are the established
flow — where a detail is an assumption it is marked [INFERRED]).

## What the connector actually expects (confirmed from code)

`gsc_connector.py` reads one CSV and nothing else for credentials:

- **File:** `/home/adrian/affiliate-agent/data/gsc_credentials.csv`, read
  BOM-tolerant (a spreadsheet export with a leading BOM is fine).
- **Columns the code uses:** `Domain`, `Key Path`, `Service Account Email`,
  `GSC Verified (Y/N)`. A row with an empty `Domain` or empty `Key Path` is
  skipped silently.
- **Columns stored but NOT used by the scrape:** `GSC Property URL`, `G-Account
  User`, `G-Account Password`, `Project`, `Service Account Name`, `Service
  Account ID`. Keep them for your own records; the code ignores them.
- **`Key Path` is resolved relative to `/home/adrian`** — the code does
  `Path('/home/adrian') / key_path`. So a `Key Path` of
  `orchestrator/config/gsc-portfolio.json` means the file lives at
  `/home/adrian/orchestrator/config/gsc-portfolio.json`. Do **not** put an
  absolute path or a leading `~` in the column.
- **Property type is always a Domain property.** The scrape queries
  `sc-domain:<domain>`, so the Search Console property must be the
  **domain-level** property (DNS-verified), not a URL-prefix property.
- **Scope is read-only:** `webmasters.readonly`. The service account never needs
  write access, so **Restricted** permission in Search Console is enough.
- Data window: the scrape pulls the last `--days` (default 30) ending 3 days ago
  (GSC's own reporting lag).

`config/` is off limits to agents (Skill 12), so the service-account JSON keys
living under `~/orchestrator/config/` are read by the connector at runtime, never
by an agent. This is why onboarding a site is a human task.

## One service account for the whole portfolio (the simplification)

The connector supports a **different** key per site (each row has its own
`Key Path`), but you do not need that. The simplest working setup:

- Create **one** service account.
- Add its email to **every** site's Search Console property.
- Point every CSV row's `Key Path` at the **same** JSON key file.

This keeps one credential to manage instead of 62. The original design comment
("each site uses its own service account, no cross-site footprint") is the more
paranoid option; use it only if you specifically want per-site isolation. For
onboarding the remaining sites, one shared service account is far less work.

## One-time: create the service account (Google Cloud Console)

Do this once (or once per shared account, if you ever rotate).

1. In Google Cloud Console, pick or create a project.
2. **Enable the Search Console API** for that project (APIs & Services → Library
   → "Google Search Console API" → Enable).
3. **Create a service account** (IAM & Admin → Service Accounts → Create).
   - **Grant it no project roles.** [INFERRED] Access is authorised per-property
     inside Search Console, not through project IAM, so the "Grant this service
     account access to the project" step is left blank.
4. On the new service account, **Keys → Add key → Create new key → JSON**.
   Download the JSON.
5. Put the JSON key under `~/orchestrator/config/` on the droplet, e.g.
   `~/orchestrator/config/gsc-portfolio.json`. (It is a credential; it belongs in
   `config/`, which is git-ignored and off limits to agents.)
6. Note the service account's **email** (looks like
   `name@project.iam.gserviceaccount.com`) — you paste this into Search Console
   and into the CSV.

## Per-site: grant access and register (repeat for each site)

For each affiliate site you want scraped:

1. **Confirm the site has a Domain property in Search Console** and that you own
   it (DNS-verified). If it only has a URL-prefix property, add the domain
   property and verify it by DNS. The connector will not use a URL-prefix
   property.
2. **Add the service account as a user on that property:** Search Console →
   Settings → Users and permissions → Add user → paste the service account
   email → permission **Restricted** → Add. (Restricted is read-only, which is
   all the connector needs.)
3. **Drop the JSON key** under `~/orchestrator/config/` if you haven't already
   (one shared key covers all sites).
4. **Add a row to** `~/affiliate-agent/data/gsc_credentials.csv`:
   - `Domain`: the bare domain, e.g. `automechanicschools.com`
   - `GSC Property URL`: `sc-domain:automechanicschools.com` (record-keeping; the
     code derives this itself)
   - `GSC Verified (Y/N)`: `Y` (once step 1-2 are done)
   - `Service Account Email`: the shared service account email
   - `Key Path`: the path **relative to `/home/adrian`**, e.g.
     `orchestrator/config/gsc-portfolio.json`
5. **Scrape it:**
   ```
   cd ~/orchestrator && python3 gsc_connector.py --site automechanicschools.com
   ```
   or scrape every verified row at once:
   ```
   cd ~/orchestrator && python3 gsc_connector.py --all
   ```
   `--all` skips any row not marked `Y`; `--site` runs the one row regardless.

Once a row is present and `Y`, the agent side is automatic — the connector (and
the daily brief) pick it up with no further help.

## Verifying it worked / troubleshooting

- After a scrape, `python3 gsc_connector.py --report` shows per-site totals; the
  new site should appear.
- **"key file missing — /home/adrian/…"**: the resolved `Key Path` doesn't exist.
  Check the column is relative to `/home/adrian` and the file is really there.
- **auth error / 403 on the API**: the service account email isn't added to that
  property yet, or was added to a URL-prefix property instead of the Domain
  property. Re-check step 2.
- **Row ignored entirely**: empty `Domain` or `Key Path`, or (for `--all`)
  `GSC Verified` is not `Y`.
- **No data but no error**: brand-new properties have little history, and the
  scrape ends 3 days ago by design. Give it a few days.

## Related skills

- Skill 05 — Orchestrator Operations
- Skill 09 — Page Optimisation (consumes GSC data to prioritise pages)
- Skill 12 — Agent Operations (config/ is off limits; scripts read keys, agents
  do not)
- Skill 13 — System Architecture (`gsc_pages`/`gsc_keywords`/`gsc_traffic_daily`)
