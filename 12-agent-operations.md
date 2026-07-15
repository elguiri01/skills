# Skill 12: Agent Operations

Operating rules for any Claude agent (Claude Code on the droplet, Cowork
session, or chat) working on the Galena Hall portfolio system. This skill
encodes what the July 2026 build established. It is the constitution: when
in doubt, follow this file, and when this file is wrong, propose an edit
rather than silently deviating. Written 2026-07-15.

## PURPOSE OF THE SYSTEM

Update and optimise content across 62 affiliate and rank-and-rent sites to
maximise revenue. The human (Adrian) sets direction, reviews output quality,
and rules on judgement calls. Agents develop, patch, run, and report. The
end state per cycle: a daily list of updated pages to review and decisions
to take, delivered to Adrian, with nothing published un-gated.

## ENVIRONMENT MAP

- Droplet: DigitalOcean, Ubuntu, US (New Jersey) IP. User adrian.
- ~/orchestrator/ - the system. orchestrator.py (run loop, handlers,
  injection functions), orchestrator.db (SQLite: jobs, affiliate_sites,
  jrcert_programs, bls_oews, site_bls_socs, site_occupation_map, cip_soc,
  sp_sites/sp_pages/sp_listings/sp_colleges, url_checks, push_stage),
  logs/, config/api_keys.json (NEVER commit, NEVER print).
- ~/skills/ - the skills library, in git. Read 05 (orchestrator ops),
  09 (page optimisation), 10 (data sources), 11 (content style) before
  content work. This file is 12.
- Key scripts: review_expansions.py (read-only review reports),
  verify_facts.py (web-verify [VERIFY] tags), push_expansion.py
  (stage/apply/cleanup, single page), push_batch.py (batch driver),
  bls_loader.py, bls_socs_setup.py, cip_soc_loader.py, seopirate_import.py,
  verify_urls.py, queue_radiologyed_all.py.
- Orchestrator runs as systemd service `orchestrator`; restart after any
  edit to orchestrator.py, always after `python3 -c "import ast;
  ast.parse(open('orchestrator.py').read())"`.
- Telegram bot (SiteOrchestratorBot) delivers notifications and the daily
  summary at 00:00 UTC.

## THE CONTENT PIPELINE (order is mandatory)

1. QUEUE     jobs with structured input_data; JRCERT gate blocks state
             pages with zero scraped radiography programs.
2. GENERATE  handler injects: Skill 11 style block with current date,
             JRCERT data (radiography main + related-programs block),
             BLS wage data (site_bls_socs career sets, per state),
             verified outbound links (url_checks ok=1 only).
3. VERIFY    verify_facts.py resolves [VERIFY] tags via web search:
             verified -> rewritten with source link; unverified -> claim
             REMOVED, never hedged. Leftover tags go to human ruling.
4. REVIEW    review_expansions.py per job; index triage columns: dashes,
             stale dates, JRCERT coverage, overlaps, dup paragraphs.
5. STAGE     push_expansion --stage (or push_batch --stage-all) with
             --harmonise: merge at first replaced section's position,
             harmonisation removes superseded human content and tags
             >5-year facts [VERIFY-STALE], ads sentinel-protected.
6. PREVIEW   human reads the REVIEW draft in wp-admin. Human edits stale
             tags there; edited drafts must be synced back to push_stage
             before apply.
7. APPLY     push_expansion --apply --confirm. Pushes the exact staged
             content. Then --cleanup, then cache purge.
8. MEASURE   GSC baseline before batch pushes; revenue via esyoh tables.

## HARD GATES (never bypass, never "temporarily" disable)

- Ad placements: count and relative order identical before/after every
  merge. Sentinel protection through any LLM pass. A trip aborts the stage.
- Exact-path page resolution everywhere. /es/ translation paths are
  refused unconditionally.
- Never delete human-written content EXCEPT via the harmonisation pass
  with human preview (Skill 09 amendment 2026-07-12).
- push_to_wordpress defaults to draft; live pages are only written by the
  apply step from previewed staged content.
- Never invent facts, statistics, or URLs. Data comes from the DB tables
  or verified web research with source links. Unverifiable claims are
  deleted, not softened.
- Skill 11 style rules apply to ALL generated text including bridges and
  stitching. No em-dashes anywhere, including agent-written copy.
- JRCERT/BLS/links data gates: no state page content without radiography
  programs; wage claims cite "BLS May 2025 OEWS data".

## HUMAN SIGN-OFF MATRIX

Agent may do autonomously:
- Read anything except config/ secrets; run read-only scripts and reports
- Queue generation jobs within budget; run verify_facts
- Stage pages (creates preview drafts only)
- Patch and test scripts in ~/orchestrator with git commit per change
- Restart the orchestrator service after syntax-checked edits

Requires Adrian's explicit go (per batch or per standing rule he grants):
- APPLY to any live page
- Deleting anything (files, WP pages, DB rows beyond status updates)
- Spending above agreed batch budgets (see SPEND)
- Changing skills files (propose diffs; he commits)
- Anything touching DNS, email infrastructure, credentials, or billing
- New standing rules that expand agent autonomy

## SPEND DISCIPLINE

- Every direct API call path (harmonise, verify_facts, future scripts)
  MUST write to the spend log the orchestrator's budget monitor reads.
  The July incident: ~$20 spent invisibly, then the queue burned 19 jobs
  failing on an empty balance.
- On a credit-balance API error: PAUSE the loop and alert via Telegram.
  Never mark jobs failed for balance errors.
- Batch estimates before running: generation ~$0.15/page, harmonise
  ~$0.20/page, verification ~$0.15/page. State the estimate, get the go
  if it exceeds the standing budget (GBP 60/month total unless revised).
- Prefer the local model (ollama) for zero-value-of-error tasks:
  classification, dedupe checks, tag extraction, alt text. Claude models
  are for content that ships and judgement that matters.

## DAILY DIGEST (the human interface)

Sent via Telegram each morning, replacing ad-hoc terminal checks:
1. Pages applied yesterday (links) and pages staged awaiting review
   (preview links)
2. Decisions pending: VERIFY-STALE rulings, aborted stages with reasons,
   blocked jobs, leftover VERIFY tags
3. Spend: yesterday and month-to-date vs budget, all paths included
4. Revenue: yesterday's esyoh total, notable site movements
5. System health: scheduler ticks, scrape freshness, queue depth
Nothing in the digest is a request for permission already granted;
everything in section 2 is a genuine human decision.

## CHANGE MANAGEMENT

- git commit in ~/orchestrator and ~/skills at the end of every working
  session; meaningful messages. The repo exists because Skill 09 once
  vanished without one.
- Patches are files, never pasted heredocs (clipboard mangling caused
  real incidents). Patch scripts are idempotent, anchor-checked, abort
  without writing on any mismatch, and back up the target first.
- Line numbers drift; locate code by content, never by remembered line.
- After any handler edit: syntax check, restart service, verify with a
  single test job before batch work.
- Test scripts against reconstructions/synthetic data before deploying.

## INCIDENT LEARNINGS (why the rules above exist)

- Slug collision pushed English review onto a Spanish page path once in
  review tooling; exact-path matching is now everywhere.
- A pasted three-command block ran stage+apply+cleanup with no preview;
  stage and apply are never issued together, by anyone.
- Harmonise deleted an ad shortcode when instructed not to; obedience is
  not a control, structure is (sentinels).
- "Page not updating" was three different things in one day: browser
  cache, a stale editor tab, and content correctly appended at the
  bottom. Check origin truth (REST raw content) before touching caches.
- BLS/NCES block datacenter IPs; large government files are downloaded
  by a human in a browser, yearly, by design.
- OEWS May release: refresh bls_oews each spring (next: May 2027 file).

## CURRENT STATE AND BACKLOG (2026-07-15)

Live: California pushed (old format; re-touch pending). Staged awaiting
review: ~46 radiologyed states. Vermont correctly blocked (no radiography
programs). Washington needs manual heading mapping. Old vet-tech jobs 94+
superseded; vettechnicians is the next site rollout template.
Backlog: spend-logging patch (prerequisite), credit-error pause patch,
daily digest build, Cloudflare purge token + purge-on-apply, quarterly
url_checks re-check schedule, California re-touch, WPX nameserver cleanup,
SendGrid Tier 2/3 auth, app passwords for 37 sites, ASD/CSN scraper debug,
GA4 hvacprograms anomaly, schema updates, technical SEO, video pipeline
(Higgsfield/HeyGen/ElevenLabs MCPs).
