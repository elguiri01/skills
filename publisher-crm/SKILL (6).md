---
name: publisher-crm
description: A lightweight publisher relationship tracker. One row per publisher domain — last contacted, lifetime outcomes, voice notes, niche tags, payment history. Replaces ad-hoc spreadsheets and Gmail searches with a queryable surface your link builder agent can actually use.
---

# publisher-crm

Most link-building operations track publishers in a spreadsheet that nobody updates, or rely on Gmail search to "remember if we've talked to this person before." Both fail at scale. This skill is a deliberately tiny CRM schema + ingestion patterns that turn your publisher relationships into a real dataset.

## What it does

1. Stores one row per publisher domain. Schema:
```
{
  domain, contactName, contactEmail, niche,
  firstContactedAt, lastContactedAt, lastReplyAt,
  lifetimeOutcomes: { sent, replied, agreed, placed, paid },
  notes,                  // free-text relationship history
  paymentMethod,          // PayPal, bank, etc.
  preferredTopics,        // niches they accept
  bannedTopics,           // niches they refuse
  averageTurnaround,      // days from agreement to live
  health,                 // active / dormant / blacklisted
  tags                    // freeform
}
```

2. Ingests:
   - **Gmail backfill.** Scan past 1-2 years of jane@yourdomain.com inbox. For each thread, extract publisher domain, agreed terms, outcome.
   - **Live updates.** As your link builder agent sends/receives, write to CRM.
   - **Manual notes.** Account manager can drop notes on any record.

3. Exposes a query API your other agents use:
   - `getPublisher(domain)` — full record
   - `searchByNiche(niche)` — filtered list
   - `getStaleRelationships(daysSinceContact)` — re-engagement candidates

## Why it works

A spreadsheet rots because nobody updates it. A queryable CRM that auto-updates from your existing email + outreach activity stays fresh because it's a side effect of work that's happening anyway.

## Storage options

Pick one:

- **SQLite** — easiest. Single file, no infra, fast queries. Use this unless you have a specific reason not to.
- **Cloudflare D1** — if you're already on CF and want it queryable from Workers.
- **Postgres** — if you have it. Overkill for one table.
- **Airtable** — if non-engineers need to edit. Slower for agents to query.

Schema is the same regardless. See `schema.sql` (SQLite) and `schema.airtable.md` (Airtable).

## Setup

### 1. Pick storage, run schema
SQLite: `sqlite3 publishers.db < schema.sql`.

### 2. Backfill from Gmail
The `backfill.js` script in this folder reads Gmail (via API or MCP), scans for outreach threads, and populates initial rows. Run once; takes hours for a 2-year inbox.

### 3. Wire your link builder agent to write to it
Whenever the agent sends, replies, agrees, or places — write to CRM.

### 4. Query from agents
Other agents (writer, strategist, reporting) can query for context.

## Architectural considerations

- **One row per DOMAIN, not per email.** People change roles. You want continuity at the domain level.
- **Notes field is sacred.** Free-text history. Account managers drop notes here. The agent reads them before writing outreach. THE single most useful field.
- **Lifetime outcomes > recent metrics.** "Replied 50% over lifetime" tells you more than "replied last month."
- **Tag aggressively.** Tags survive schema changes; columns don't.
- **Don't auto-blacklist.** Health field defaults to active; only humans flip to blacklisted.

## What this skill does NOT include

- A pre-built publisher list (build your own — that's the moat).
- Pricing data (every publisher is different; track in your sales system, not the CRM).

## Companion skills

- `link-builder-agent` — primary consumer.
- `gp-writer-agent` — uses notes field for voice context.
- `seo-strategist-agent` — uses niche/health for inventory planning.

## Install

1. Drop this folder under `~/.claude/skills/publisher-crm/`.
2. Pick storage, run schema.
3. Backfill from Gmail (takes hours; run once).
4. Wire your link builder agent to write to it.
