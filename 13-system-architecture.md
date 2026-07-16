# Skill 13: System Architecture

The map of the orchestrator system: the database tables and what their ids
reference, the code in orchestrator.py, the script inventory, and the data flow
from a GSC opportunity to a live page. Read this when you need to know where
data lives or how a piece connects, before touching the database or the code.

This is a companion to Skill 12 (the constitution) and Skill 05 (day-to-day
ops). Where 12 says what you may do and 05 says how to run it, 13 says how it is
built.

## PROVENANCE AND [INFERRED] MARKS

Everything here is built from three sources: the live schema (`.schema` on
orchestrator.db), the code itself, and Skills 05/10/11/12. Lines derived
directly from schema or code are stated plainly. Lines where the purpose or
linkage is a reasonable interpretation rather than something the schema or a
docstring states outright are tagged **[INFERRED]** so Adrian (and his chat
assistant) can verify or correct them. Row counts are a snapshot as of
2026-07-16 and drift; treat them as orders of magnitude, not fixed values.

Written 2026-07-16.

## THE THREE SITE TABLES (read this first)

There are three unrelated tables that each look like "the list of sites". They
have separate id spaces. Confusing them caused a near-miss mass deletion of job
history on 2026-07-16, so the disambiguation leads this document.

- **`sites`** (2 rows) — ONLY the two Spanish rank-and-rent sites
  (jardineriaalcobendas.com, piscinaslamoraleja.es). A separate subsystem from
  the affiliate business. `pages.site_id`, `rankings.page_id`→`pages`, and the
  `push_jardineria`/`push_piscinas`/`queue_jardineria`/`queue_piscinas` scripts
  belong to this world.
- **`affiliate_sites`** (62 rows) — the affiliate portfolio: the majority of the
  business (electricalschool.org, radiologyed.org, vettechnicians.org, etc.).
  **`jobs.site_id` references `affiliate_sites.id`.** id 33 = radiologyed.org,
  id 4 = vettechnicians.org.
- **`sp_sites`** (31 rows) — the seopirate.ninja import. Its OWN id space,
  unrelated to `affiliate_sites`. Radiologic Technologist is **id 22** here.
  A given real site therefore has two different numeric ids: e.g. radiologyed is
  `affiliate_sites.id = 33` but `sp_sites.id = 22`.
- **`site_bls_socs` and `site_occupation_map` add a fourth "site" context — and
  it is the `sp_sites` id space, not `affiliate_sites`.** `bls_socs_setup.py`
  seeds `site_bls_socs` via `SELECT id FROM sp_sites WHERE name = ?` (line 90),
  `get_bls_context` resolves the current page through `sp_pages.site_id`, and
  `site_occupation_map` is built from `sp_listings.site_id`. So there are **four**
  id-bearing "site" columns across the schema, not three. Joining `site_bls_socs`
  or `site_occupation_map` to `affiliate_sites` on `site_id` produces silent
  garbage — the ids belong to different spaces and will mostly not even overlap.

**The `jobs.site_id` foreign key is mislabelled in the schema.** The column is
declared `site_id INTEGER REFERENCES sites(id)`, but that FK is vestigial —
SQLite does not enforce it, and the live values are `affiliate_sites` ids. This
is proven in code, not just convention:

- `queue_radiologyed_all.py:60-63` — comment "Site id in affiliate_sites for the
  jobs table", then `SELECT id FROM affiliate_sites WHERE domain=?` before the
  job INSERT.
- `load_opportunity_jobs.py:220` — `JOIN affiliate_sites a ON j.site_id = a.id`.
- `review_expansions.py:192` — resolves a job's site by `affiliate_sites` id.

(`push_expansion.py` resolves site credentials by domain — `get_site_creds`
queries `affiliate_sites WHERE domain = ?` — sidestepping the id question
entirely, so it is not evidence either way.)

An empty `sites` lookup for a `jobs.site_id` is therefore NOT evidence of a
missing or orphaned row — the row is in `affiliate_sites`. Never conclude data
loss from querying the wrong table.

## TABLE REFERENCE

Grouped by subsystem. "→" means "id references". Counts are the 2026-07-16
snapshot.

### Sites and identity

| Table | Rows | Purpose | Key columns / references |
|---|---|---|---|
| `sites` | 2 | Spanish rank-and-rent sites only | `site_type CHECK IN ('affiliate','rank_rent')` (only rank_rent present); carries `wp_app_password` |
| `affiliate_sites` | 62 | Affiliate portfolio; the main business | `domain` UNIQUE; `jobs.site_id`→ here. Carries credentials (see CREDENTIALS). Revenue/GSC columns populated by scrapers. |
| `sp_sites` | 31 | seopirate.ninja site export; own id space | `id`, `url`, `path`, `translation_path`, `constraints_json` |
| `persona_emails` | 60 | Per-domain persona email accounts | `domain`, `email_address` UNIQUE, IMAP/SMTP config; carries `email_password` |
| `niches` | 0 | Niche definitions (CN category, SOC, CIP, accreditor) | Empty. **[INFERRED]** intended as the master niche table; currently unused in favour of per-site config. |

### Jobs and content work

| Table | Rows | Purpose | Key columns / references |
|---|---|---|---|
| `jobs` | 207 | Generation job queue and history | `site_id`→`affiliate_sites.id` (declared FK to `sites` is vestigial); `page_id`→`pages.id`; `status CHECK` (see JOBS STATUS); `cost_usd`; `input_data`/`output_data` JSON |
| `pages` | 10 | WordPress pages, rank-and-rent side | `site_id`→`sites.id`; `wp_page_id`, `slug`, `word_count`. **[INFERRED]** affiliate page structure lives in `sp_pages`, not here. |
| `push_stage` | 42 | Staging buffer between STAGE and APPLY | `job_id` PK; `merged_content`, `original_content`, `ad_inventory`, `preview_page_id`, `staged_at`, `applied_at` |
| `spend` | 15 | API + web-search spend log the budget monitor reads | `UNIQUE(date, model, job_type)`; written by `log_spend`/`log_web_search` in database.py |
| `affiliate_actions` | 0 | Action log (content_expansion, social, schema…) | Empty. **[INFERRED]** an earlier/alternative action ledger superseded by `jobs`; kept but unused. |

### Content data sources (the injection tables)

These feed the GENERATE step. See INJECTION CHAIN.

| Table | Rows | Purpose | Key columns / references |
|---|---|---|---|
| `jrcert_programs` | 720 | JRCERT-accredited radiography programs | `state`/`state_abbr`, `program_type`, rates; the JRCERT gate reads this |
| `bls_oews` | 36,168 | BLS OEWS wage data by state × occupation | PK `(state, soc_code)`; `mean_annual`, percentiles, `data_year` |
| `site_bls_socs` | 56 | Per-site curated SOC career sets | PK `(site_id, soc_code)`; `role CHECK IN ('entry','core','advanced','related')`. **`site_id` is an `sp_sites` id** (seeded by `bls_socs_setup.py` from `sp_sites`), NOT `affiliate_sites.id`. |
| `site_occupation_map` | 54 | Site → program → CIP → SOC mapping | PK `(site_id, program_name)`; `primary_soc`. **`site_id` is an `sp_sites` id** (built from `sp_listings.site_id`), NOT `affiliate_sites.id`. |
| `cip_soc` | 6,097 | CIP-to-SOC crosswalk | `cip_code`, `soc_code` |
| `schools` | 0 | College Navigator programs per niche | Empty. `niche_id`→`niches.id`. **[INFERRED]** superseded by the `sp_colleges`/`sp_listings` import. |
| `url_checks` | 18,565 | Outbound URL verification cache | `url` PK, `ok`, `final_url`, `http_status`. Only `ok=1` links inject, and the injection ships `final_url or url` (the https-rescued address wins over the original), preferring a verified program page and falling back to the college website. If anyone audits live links against this table, compare against `final_url`, not `url`. |

### seopirate import (sp_*)

The seopirate.ninja export. Accounts for most of the 128MB database size
(`sp_listings` ~60k rows, `sp_colleges` with many JSON blob columns) — the size
is import data, not deleted-row bloat.

| Table | Rows | Purpose | Key columns / references |
|---|---|---|---|
| `sp_sites` | 31 | Imported site list, own id space | `id` (e.g. 22 = radiologyed) |
| `sp_pages` | 2,424 | Imported page inventory per sp site | PK `(site_id, wp_id)`; `slug`, `state`, `is_alias`; `queue_radiologyed_all.py` reads state pages here |
| `sp_listings` | 60,652 | Program listings (school × program) | `site_id`, `college_ipeds_id`→`sp_colleges.ipeds_id` |
| `sp_colleges` | 3,766 | College reference data, IPEDS-keyed | `ipeds_id` PK; many `*_json` blob columns |

### Revenue and analytics

| Table | Rows | Purpose |
|---|---|---|
| `esyoh_leads` | 127 | Individual Esyoh (ed2go) leads |
| `esyoh_revenue_by_site` | 75 | Esyoh revenue rolled up per domain per report_date |
| `esyoh_revenue_daily` | 8 | Esyoh daily totals (ed2go + affiliate split) |
| `esyoh_revenue`, `esyoh_revenue_by_category` | 0 | **[INFERRED]** category/site-id-keyed variants, currently unpopulated |
| `asd_revenue_daily` / `asd_revenue_by_site` | 1 / 0 | All Star Directories revenue |
| `csn_revenue_daily` / `csn_revenue_by_site` | 1 / 0 | Career Schools Network revenue |
| `gsc_pages` | 916 | GSC per-page clicks/impressions/position by date |
| `gsc_keywords` | 1,000 | GSC per-keyword metrics by date |
| `gsc_traffic_daily` | 455 | GSC per-domain daily totals |
| `rankings` | 0 | **[INFERRED]** per-page query rankings for the r&r side; unused |

### Email

| Table | Rows | Purpose |
|---|---|---|
| `email_inbox` / `email_outbox` | 0 / 0 | Persona email in/out queues (send scheduling, reply tracking) |
| `persona_emails` | 60 | Account credentials + IMAP/SMTP config (also in Identity above) |

## JOBS STATUS VOCABULARY

`jobs.status` has a CHECK constraint. The ONLY legal values are:

```
CHECK(status IN ('pending','running','complete','failed','paused'))
```

There is no `queued` and no `rejected` — using either raises a constraint
error. `affiliate_actions.status` is a plain TEXT column (no CHECK) documented
as `pending, complete, failed`. `email_outbox.status` defaults to `pending`.

Note the completion value is `complete`, not `completed`; Skill 05's health-check
snippets query `status='complete'`.

## CREDENTIALS IN THE DATABASE

Three tables hold live secrets. Never `SELECT *` on them; name columns
explicitly (this is the standing rule in CLAUDE.md).

- **`affiliate_sites`** — `wp_password`, `wp_app_password`, `google_password`,
  `recovery_email`, `site_email`, plus social handles.
- **`sites`** — `wp_app_password`.
- **`persona_emails`** — `email_password`.

**[INFERRED] follow-up:** `review_expansions.py:192` runs
`SELECT * FROM affiliate_sites WHERE id=?`, which violates this rule. Worth a
patch to name only the columns it uses. Flag for Adrian, do not silently change
review tooling.

## orchestrator.py FUNCTION INVENTORY

The run loop, the job handlers, and the injection helpers. Locate by content,
not by the line numbers below (they drift).

**Budget / spend / API:**
- `check_budget()`, `budget_ok(min_remaining_gbp=5.0)` — read the spend table
  (via `get_monthly_spend`) and gate the loop.
- `call_claude(prompt, model, system, max_tokens)` — the SDK path; reads
  `config/api_keys.json` at runtime, calls `log_spend` (now in database.py).
- `push_to_wordpress(...)` — REST push; defaults to draft per Skill 12.
- `MODEL_ROUTING` — job_type → model id map.

**Injection helpers (feed GENERATE):**
- `get_jrcert_context(domain, page_url)` — returns `(text, radiography_count)`.
  Radiography main block + related-programs block, read from `jrcert_programs`.
- `get_bls_context(domain, page_url)` — wage block from `site_bls_socs` joined to
  `bls_oews` per state.
- `get_program_links_context(domain, page_url)` — verified outbound links from
  `sp_listings`/`sp_colleges` filtered by `url_checks` (`ok=1` only).

**Job handlers (registered in `JOB_HANDLERS`):**
`handle_meta_description`, `handle_schema_generation`, `handle_content_brief`,
`handle_zone_page`, `handle_content_rewrite`, `handle_homepage_content`,
`handle_service_page`, `handle_content_expansion`.

**Loop:**
- `process_job(job)` — dispatches via `JOB_HANDLERS`; "Unknown job type" if a
  type has no handler.
- `run_scheduled_tasks(sched, jobs_counters)` — scheduler tick.
- `run(batch_size=5, sleep_seconds=60, max_iterations=None)` — the main loop;
  checks `budget_ok()` before working.

### The injection chain (order is enforced in code)

Inside `handle_content_expansion`, the order is jrcert → gate → bls → links:

1. `get_jrcert_context(domain, page_url)` → `(jrcert_text, jrcert_count)`.
2. **JRCERT gate:** if `'radiologyed' in domain and jrcert_count == 0`, the job
   returns `BLOCKED` — no state page without radiography programs (Skill 12 hard
   gate; this is why Vermont blocks).
3. `get_bls_context(...)` → `bls_text`.
4. `get_program_links_context(...)` → `links_text`.
5. The three blocks are concatenated (in that order) into the prompt.

## SCRIPT DEPENDENCY MAP

Grouped by role. `[db]` = imports `database`, `[nfy]` = imports `notify`.
Scripts with neither run standalone (own sqlite connection or pure API).

**Core runtime:**
- `orchestrator.py` `[db,nfy]` — the service (systemd `orchestrator`).
- `database.py` — schema + all DB ops; now also `MODEL_COSTS`, `log_spend`,
  `log_web_search` (shared spend logging).
- `notify.py` — Telegram send (send-only) + daily summary.
- `telegram_control.py` `[db,nfy]` — /restart /status /help listener (own
  service `telegram-control`; deploy files in `deploy/`).

**Pipeline (affiliate content):**
- `load_opportunity_jobs.py` — queue content_expansion from a GSC-opportunity
  list; resolves `site_id` from `affiliate_sites`.
- `queue_radiologyed_all.py` — queue every radiologyed state page (reads
  `sp_pages` for `sp_sites.id=22`, writes `affiliate_sites.id` into jobs).
- `verify_facts.py` `[db]` — resolve `[VERIFY]` tags via web search; logs spend
  and web searches.
- `review_expansions.py` — read-only REVIEW reports per job.
- `push_expansion.py` `[db]` — STAGE / APPLY / cleanup a single page; harmonise
  pass; sentinel-protected ads.
- `push_batch.py` — batch driver over `push_expansion`.
- `sync_draft.py` — pull a hand-edited REVIEW draft back into `push_stage`
  before APPLY.
- `verify_urls.py` — populate `url_checks` before links go live.

**Rank-and-rent pipeline (Spanish sites, `sites` table):**
- `queue_jardineria.py` `[db]`, `queue_piscinas.py` `[db]`,
  `push_jardineria.py` `[db]`, `push_piscinas.py` `[db]`, `push_contacto.py`.

**Data loaders (injection sources):**
- `bls_loader.py`, `bls_socs_setup.py` — `bls_oews`, `site_bls_socs`.
- `cip_soc_loader.py` — `cip_soc`, `site_occupation_map`.
- `jrcert_scraper.py`, `jcert_scraper2.py`, `jrcert_sitemap.py` —
  `jrcert_programs`.
- `seopirate_import.py` — the `sp_*` tables.
- `import_affiliate_sites.py` — `affiliate_sites`.

**Analytics / revenue scrapers:**
- `gsc_connector.py` — `gsc_*` tables (reads domains from `affiliate_sites`).
- `esyoh_scraper.py`, `extract_esyoh_ids.py`, `debug_esyoh*.py` — Esyoh revenue.
- `asd_csn_scraper.py` — ASD/CSN revenue.
- `monthly_invoice.py` `[nfy]`, `send_invoice.py` — ASD commission invoices.

**Email / DNS infrastructure:**
- `email_client.py` `[nfy]`, `email_setup_servers.py`, `email_dns_audit.py`,
  `persona_emails` management.
- `sendgrid_dns.py`, `sendgrid_auth_all.py`, `delete_wpx_records.py` —
  Cloudflare/SendGrid DNS (these read `~/migrate/` credentials at runtime; see
  CLAUDE.md — scripts may, agents may not).

**One-off `apply_*` patch scripts:** `apply_bls_patch`, `apply_harmonise_patch`,
`apply_insert_patch`, `apply_links_patch`, `apply_related_patch`,
`apply_sentinel_patch`, `apply_spend_logging_patch`, `bls_handler_patch`. Each is
an idempotent, anchor-checked, backup-first edit to a runtime file (Skill 12
change-management pattern). `debug_*` scripts are throwaway diagnostics.

## DATA FLOW: GSC OPPORTUNITY → APPLIED PAGE

The end-to-end path for an affiliate content update. Steps 3-9 are the mandatory
pipeline from Skill 12; this shows where each reads and writes.

1. **Opportunity.** GSC scraping (`gsc_connector.py`) fills `gsc_pages` /
   `gsc_keywords` — clicks, impressions, average position per page.
   **[INFERRED]** the opportunity shortlist (converting pages at position ~8-25
   with high impressions) is currently a curated list inside
   `load_opportunity_jobs.py` (`OPPORTUNITIES`), derived from that GSC data by
   hand rather than queried live.
2. **QUEUE.** `load_opportunity_jobs.py` (or `queue_radiologyed_all.py` for the
   radiologyed rollout) inserts `content_expansion` jobs, `site_id` resolved from
   `affiliate_sites`, `status='pending'`. The JRCERT gate blocks radiography
   state pages with zero scraped programs.
3. **GENERATE.** The orchestrator runs `handle_content_expansion`, injecting the
   Skill 11 style block, JRCERT data, BLS wages (`site_bls_socs`+`bls_oews`), and
   verified outbound links (`url_checks` `ok=1`). Output → `jobs.output_data`,
   cost → `spend`.
4. **VERIFY.** `verify_facts.py` resolves `[VERIFY]` tags via web search:
   verified → rewritten with a source link, unverified → removed (never hedged).
   Spend and web-search count → `spend`.
5. **REVIEW.** `review_expansions.py` produces a read-only report per job.
6. **STAGE.** `push_expansion.py --stage` (or `push_batch --stage-all`) with
   `--harmonise`; writes `push_stage` (merged + original content, ad inventory);
   creates a preview draft in wp-admin. Ad sentinels protect placements.
7. **PREVIEW.** Human reads the draft; edits stale-fact tags there. Edited drafts
   are synced back with `sync_draft.py` before APPLY.
8. **APPLY.** `push_expansion.py --apply --confirm` pushes the exact staged
   content live, then cleanup, then cache purge. Requires Adrian's go (Skill 12
   sign-off matrix). Stage and apply are never issued together.
9. **MEASURE.** GSC baseline before batch pushes; revenue via the `esyoh_*` /
   `asd_*` / `csn_*` tables.

## RELATED SKILLS

- Skill 05 — Orchestrator Operations (health checks, queuing, budget commands)
- Skill 09 — Page Optimisation (the merge/harmonise rules)
- Skill 10 — Accreditation Data Sources (JRCERT/BLS/NCES loaders)
- Skill 11 — Content Style (injected into every GENERATE)
- Skill 12 — Agent Operations (the constitution)
