---
name: lead-intel-suite
description: Three-agent pipeline that turns inbound form submissions into qualified, audited, CRM-enriched sales intel inside ~5 minutes. Scraper polls your form store hourly, auditor pulls Ahrefs DR / top keywords / SERP competition per lead, sales-team channel gets a brief with the "if you ranked, this would be worth $X/mo" pitch already written. CRM contact + custom fields + tags get synced automatically. By the time the setter calls, the lead is fully briefed.
---

# lead-intel-suite

The standard inbound flow looks like this: form submission lands → Slack notification with name + email → setter calls → setter spends ten minutes researching the prospect on Ahrefs while the prospect is on hold → setter wings a "hey, I noticed you're not ranking for X" line. Half the leads never get researched at all because the setter is on three calls.

This pipeline kills that. Three small agents, one clean handoff: every inbound lead arrives at the setter pre-audited with the SEO opportunity sized in dollars, and lands in your CRM with custom fields populated and the right segmentation tag applied. The setter opens the call already knowing the pitch.

## What it does

**Agent 1 — Scraper (hourly)**
1. Queries your form-submission store (your forms worker / WordPress REST / Typeform / direct DB) since `last_seen_id`.
2. Filters to your booking-call forms (skip lead magnets, downloads, spam).
3. Captures `fbclid` / UTM data so attribution is preserved.
4. Appends new leads to `new-leads.json` with status `pending_audit`.
5. Posts a "N new leads" line to your sales channel (only if N > 0).

**Agent 2 — Auditor (every 2 hours)**
1. Reads `pending_audit` leads from `new-leads.json`.
2. For each lead with a website:
   - Pulls Ahrefs DR + organic keywords + traffic via the standard Ahrefs MCP.
   - Sorts the keyword set by CPC descending — commercial intent first, vanity volume last.
   - For the top 3 keywords by CPC, queries `serp-overview` and finds the **lowest-DR site in the top 5** — the real competition signal, not the synthetic KD score.
3. Builds the dollar pitch:
   > "[N] people search for '[keyword]' every month. If you ranked, that's roughly [estimated_clicks] visitors. If 10% become customers and each customer is worth $[CLTV], that's $[monthly_revenue]/month. From one keyword."
4. Posts a structured brief to your sales channel — contact details, audit data, top three keyword opportunities with the weakest competitor in each, and the dollar pitch.
5. **Updates lead status to `complete` IMMEDIATELY after the Slack post**, before any CRM call. The Slack post is the primary deliverable; CRM enrichment is additive. (This ordering matters — if the agent times out on the CRM step, the lead doesn't get re-audited next run.)

**Agent 3 — CRM enricher (chained from auditor)**
1. Find-or-create contact in your CRM (ActiveCampaign, HubSpot, Pipedrive, Mailchimp).
2. Add to your inbound-leads list / segment.
3. Push custom fields: domain, DR, keyword count, traffic, top opportunity, CPC, weakest competitor DR, estimated revenue, sales-angle text.
4. Tag the contact `audit-complete` (or `audit-blank` for no-website leads, so segmentation can target them differently in nurture flows).
5. Optionally: create a contact note in your sales CRM containing the same audit + pitch text, so the setter sees it natively in their normal call interface.

## Why it works

- **Pre-audited leads close at materially higher rates.** A setter walking into a call already knowing the prospect's DR, top keyword, weakest competitor, and dollar opportunity is a different setter than one starting cold.
- **Lowest DR top-5 is the real signal.** Synthetic KD scores hallucinate hard sites that have one weak ranker in position 4. Pulling the actual SERP and finding the weakest is the only honest way to size winnability.
- **Sort by CPC for commercial intent.** A 50,000-volume keyword with $0 CPC is a research keyword — useless for sales. Sort by CPC and you're looking at the keywords prospects already pay to rank for.
- **Form budget is unreliable.** Don't filter leads on the budget field. People lie on forms. Audit them all.
- **Status update before CRM call.** Every other lead pipeline I've seen marks status at the end as a batch, then re-audits leads on timeout. The "post to Slack → mark complete IMMEDIATELY → THEN do CRM" ordering is non-negotiable.
- **Skool / community email match catches the second-funnel lead.** Many high-intent leads come in *without* fbclid because they joined your free community first, then booked a call directly weeks later. Cross-referencing the lead's email against your community member list catches that funnel.

## What you provide

- **Form-submission store.** Your forms worker, WordPress REST, Typeform, Tally, direct DB — anything queryable.
- **Ahrefs MCP access.** The audit is the value — without Ahrefs the pipeline doesn't work.
- **CRM API.** ActiveCampaign, HubSpot, Pipedrive, Mailchimp. The skill ships generic adapters for all four.
- **Sales-team channel.** Slack or Discord. Tag your setters in every brief so they get notified.
- **CLTV proxy.** Per-customer-lifetime-value used in the dollar pitch. A flat number works; ideally tier it by industry. The agent ships with a placeholder map you must populate from your own numbers — do NOT use whatever defaults the example file contains, those are just shape.

## Optimisations vs. one-shot prompts

- **Two-layer.** The scraper + status updates run in cheap Node code. The audit reasoning + brief writing route through the LLM.
- **Cheap-tier the brief.** The Slack post is a formatting task — Haiku 4.5 ships it. Don't burn Sonnet on Slack messages.
- **Cache Ahrefs lookups.** Same domain across the day's leads — cache DR / metrics for 24h.
- **Bypass the form's budget field.** Audit ALL leads regardless of stated budget. Form budget is consistently wrong.
- **Retry queue, not in-line retry.** If Ahrefs blips, mark the lead `retry_audit` and pick it up next run. Don't stall the whole batch retrying mid-flight.
- **Async CRM enrichment.** The Slack post fires immediately; the CRM sync is a background pass on the same lead. Failures here go to a retry log, NOT back through the audit.

## Architectural considerations

- **No Chrome-MCP scraping of marketplaces / Google.** The Ahrefs MCP is the data source. Headless-Chrome scraping of platforms that forbid it is a ToS violation and a brittle dependency.
- **The agent NEVER modifies the form, the lead, or the ad campaign.** Read-only on the source side. The CRM enrichment is the only write and it's confined to your own CRM.
- **PII handling.** The brief contains the lead's name, email, and phone. The channel must be private to your sales team. Do not post to a community channel. The `new-leads.json` file is also PII — store it outside any version-controlled directory, set restrictive file permissions, and define a retention policy (90 days is a sensible default).
- **Spam list maintained in a separate datastore, not in the published prompt.** Any persistent troll emails get added to a hard-block list — but that list lives outside the agent's source files (a `spam-blocklist.json` outside version control, or a small DB table). Don't let the LLM decide who's spam, and don't bake personal email addresses into prompts that get shared.
- **Status-update ordering matters.** Slack post first → mark complete → CRM after. Reversing this re-audits leads on every CRM timeout.
- **No "Keyword Difficulty" anywhere.** KD is an Ahrefs/SEO-tool synthetic score that doesn't reflect SERP reality. The lowest-DR-in-top-5 method is the only competition signal that matters.

## What this skill does NOT include

- The form / landing page itself (you bring those).
- The Ahrefs subscription (you bring that).
- The CRM (you bring that — the skill ships adapters for the four named above).
- A predictive lead-score / qualification model (the audit IS the qualification — no opaque score added).
- Auto-dialler / outbound calling (deliberately — the call is human work).

## Setup

### 1. Wire the form store
Whatever you use, expose a JSON endpoint that returns submissions since a timestamp. **The endpoint MUST require authentication** (bearer token, signed request, or IP allowlist) and **MUST be served over TLS**. An unauthenticated submissions endpoint is a PII leak waiting to happen — every name, email, and phone you've ever captured is one URL away from a scraper. Treat the auth on this endpoint as production-critical, not a nice-to-have.

### 2. Wire Ahrefs MCP
Standard Ahrefs MCP setup. Make sure your seat has SERP API access (the lowest-DR-top-5 query depends on `serp-overview`).

### 3. Wire your CRM
Pick the adapter for your CRM (ActiveCampaign, HubSpot, Pipedrive, Mailchimp). Provide:
- API base URL
- API token in `.secrets/` (NEVER inline in the prompt)
- List ID / pipeline ID for inbound leads
- Custom field IDs (or let the adapter create them on first run)
- Tag ID for `audit-complete`

### 4. Configure CLTV
Either a flat number in `config.json` or an industry-tier map. Used in the dollar pitch — wrong here means the pitch sounds unbelievable.

### 5. Schedule
- Scraper: hourly (`5 * * * *`).
- Auditor: every 2 hours (`30 */2 * * *`).
- CRM enricher: chained immediately after the auditor for each lead.

### 6. Watch the first 20 leads land
Sanity-check the dollar pitch, the lowest-DR detection, the CRM field population. Tune the CPC sort threshold if the brief is leading with weak keywords.

## Companion skills

- `agent-resilience` — required (all three agents).
- `approval-gate` — wrap the CRM-write step in an approval gate for the first month if you're nervous about field collisions.
- `seo-strategist-agent` — for leads that close, the strategist takes over with deeper analysis.
- `multi-llm-router` — cheap-tier the briefs.

## Install

1. Drop this folder under `~/.claude/skills/lead-intel-suite/`.
2. Wire form store + Ahrefs MCP + CRM.
3. Configure CLTV + custom fields.
4. Schedule the three agents.
5. Watch the first 20 leads. Tune. Then walk away — this is one of the few agents that actually fires-and-forgets cleanly.
