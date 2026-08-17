---
name: inventory-database
description: Recommended schema and ingestion patterns for a publisher inventory database — the foundation under any link-building operation. NOT a pre-built list of sites (that's your moat). This skill gives you the schema, the ingestion patterns, the quality flags, and the audit hooks.
---

# inventory-database

A link-building agent without a quality inventory is useless. The inventory IS the moat. This skill doesn't give you a list of sites (find those yourself). It gives you the structure for a queryable, auditable, quality-flagged inventory that your other agents can reliably consume.

## What it does

1. Defines a schema for publisher inventory rows.
2. Provides ingestion patterns for adding new sites (manual, scraped, marketplace exports).
3. Defines quality-flag dimensions (DR, traffic, niche fit, junk-traffic detection, link-farm risk).
4. Provides an audit hook — quarterly re-scan to detect rotting sites.
5. Provides a query API your link builder + strategist agents consume.

## Schema

```
{
  domain TEXT PRIMARY KEY,
  contact_email,
  niche,                        -- primary niche tag
  niche_secondary,              -- additional tags (comma)
  geo,                          -- US, UK, AU, etc.
  language,                     -- en, de, etc.
  dr,                           -- Ahrefs DR
  monthly_traffic,              -- Ahrefs organic
  monthly_keywords,             -- Ahrefs ranked keyword count
  trust_flow,                   -- Majestic if you use it
  spam_flags,                   -- comma-separated: ZERO_TRAFFIC, GEO_MISMATCH, JUNK_TRAFFIC, LINK_FARM_RISK
  health,                       -- active / dormant / blacklisted
  source,                       -- where you found it: manual, partner, marketplace_X
  added_at,
  last_audited_at,
  notes
}
```

## Quality flags — what to detect

- **ZERO_TRAFFIC** — Ahrefs reports zero organic traffic. Either dead site or new.
- **JUNK_TRAFFIC** — traffic exists but from low-value keywords (e.g., piracy terms, error queries, spammy redirects). Detect via DataForSEO ranked_keywords + a junk-keyword classifier.
- **GEO_MISMATCH** — site claims to be US but ranks only in DE. Likely a re-purposed domain.
- **LINK_FARM_RISK** — domain is in a known link cluster (similar templates, same hosting, cross-linked).
- **NICHE_DRIFT** — domain originally fit one niche but content has drifted.

Each flag = subtract from a quality score. Below threshold = excluded from outreach.

## Ingestion patterns

### Manual
- Account manager finds a site, adds a row. Required: domain, contact_email, niche.
- DR/traffic auto-pulled from Ahrefs.

### Partner/affiliate exports
- Some partners share lists. Validate with Ahrefs before ingesting; don't trust their data.

### Marketplace exports (handle carefully)
- Many marketplaces forbid scraping in their ToS. Read the ToS before any automated ingestion.
- If allowed, ingest with a `source: marketplace_X` tag so you can re-run quality flags differently for those.

## Audit hook

Quarterly job:
1. For every active row, re-pull DR + traffic from Ahrefs.
2. Re-run quality flags.
3. Domains that flipped from clean → flagged go to the account manager for review.
4. Domains untouched for 12 months get archived.

## Why it works

The agent on top is only as good as the inventory under it. With proper quality flags, the link builder agent can filter to "Tier 1 sites for client X" automatically. Without them, the agent is choosing randomly from a pile.

## Architectural considerations

- **Inventory entry gate is HARD.** Junk should never enter. Better to have 500 clean rows than 5000 mixed.
- **Per-client SELECTION gate is SOFT.** Already-clean rows can be selected with cycle-aware tier preferences.
- **Don't auto-blacklist.** Flag for human review. Account managers know which sites have a redemption arc.
- **Re-audit is non-negotiable.** Sites rot. Quarterly re-scan catches it.

## What this skill does NOT include

- A list of sites (find your own).
- Specific marketplace integration code (and most marketplaces forbid scraping).
- Any pre-classified niches — every agency has different rules.

## Companion skills

- `link-builder-agent` — primary consumer.
- `seo-strategist-agent` — uses niche/health/quality for planning.
- `publisher-crm` — relationship tracking layer; pair with this.

## Install

1. Drop this folder under `~/.claude/skills/inventory-database/`.
2. Run `schema.sql` against your storage of choice.
3. Wire ingestion paths.
4. Set up quarterly audit task.
