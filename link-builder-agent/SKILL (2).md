---
name: link-builder-agent
description: Autonomous editorial outreach agent template. Reads from your publisher inventory, sends outreach in your brand voice, parses replies, manages thread state, posts updates to your team channel. Open-ended — drop your own inventory, clients, and compliance rules in.
---

# link-builder-agent

A template for an autonomous editorial outreach agent. Built around the two-layer pattern (Node agent.js for selection + Claude orchestrator for MCP work). The reasoning core is included; the specifics — your inventory, your clients, your brand voice, your channels, and your compliance posture — are placeholders for you to fill in.

## Compliance up front (read this before anything else)

Google's link scheme guidelines are explicit: any link placement that involves compensation — money, free product, exchange of services — must be marked `rel="sponsored"` or `rel="nofollow"`. Editorial coverage that's genuinely earned (no payment, no pre-arranged exchange) doesn't need this. If your outreach involves any kind of compensation, you MUST require `rel="sponsored"` or `rel="nofollow"` from publishers — bake that into your outreach copy and verification. This skill provides the agentic infrastructure; the compliance posture is yours to set, and getting it wrong puts your clients (and Google rankings) at real risk.

## What it does

1. Reads candidate sites from `[your inventory CRM/database]`.
2. Filters by client niche, geo, DR/traffic floor, deduplication against past placements.
3. Composes outreach in your brand voice (one writer profile per persona).
4. Sends via your email account (use a compliant ESP / transactional provider, not raw Gmail bulk-sending — see "What you provide").
5. Watches for replies, classifies intent (interested / not interested / counter / spam / autoresponder).
6. Negotiates terms (turnaround, content fit, link attributes) within rules you set.
7. On agreement, sends content/spec, tracks until live, verifies link attributes with Ahrefs MCP — including `rel` attribute, anchor, and target URL.
8. Posts daily summary to your team channel.

## Why it works

Most outreach "AI" tools fail because they treat outreach as mail-merge. Real publishers reply, push back, ask for samples, change terms, ghost. This agent is built around handling that whole lifecycle, not just step 1.

The reasoning core handles negotiation context across multi-message threads. The Tier-3 escalation pattern means it asks you when it's genuinely uncertain rather than making it up.

## What you provide

- **Inventory.** A list of publisher sites with email, niche tags, DR/traffic data, history. The agent doesn't scrape this — you provide it. (See companion skill `inventory-database` for the recommended schema.)
- **Client roster.** Per-client briefs: target URLs, anchors, niche restrictions, voice notes.
- **Voice profile.** 2-3 example outreach emails written by you. The agent matches tone.
- **Compliance rules.** Whether outreach is purely editorial (no compensation) or involves any compensation — and if so, what `rel` attribute is required (`sponsored` / `nofollow`).
- **Sending infrastructure.** A compliant ESP or transactional email provider that respects bulk-send AUPs. Don't blast cold outreach from a personal Gmail at scale.
- **Negotiation rules.** What terms the agent can agree autonomously vs. ones that need your sign-off.

## Optimisations vs. one-shot prompts

- **Two-layer architecture.** Selection + filtering runs in cheap Node code; only the MCP-touching outreach + reply handling runs through Claude. Cuts cost ~80% vs. doing it all in one Claude conversation.
- **Reasoning core preserved.** The negotiation logic isn't a static template — it's a multi-step reasoner that considers volume, relationship history, and partnership leverage. Don't strip this; it's what makes the agent worth running.
- **JSONL state boundaries.** Pending / sent / done queues are append-only files. Crash recovery is trivial — restart, re-read the queue, skip already-done.
- **Reply classification on Haiku.** Saves money — Haiku 4.5 handles 5-class intent perfectly.
- **Tier-3 escalation for genuinely ambiguous replies.** Not "I'm not sure, abort" but "this one specific reply is unparseable, ask the human, continue with the other 30."

## Architectural considerations

- **Inventory quality is the bottleneck.** A great agent on a junk inventory produces junk outreach. Audit your inventory before pointing this at it. Strip dead emails, mismatched niches, link-farm sites.
- **Brand voice matters.** Generic "Hi, I love your site" outreach gets flagged as spam by every smart publisher. Train it on YOUR voice via examples.
- **Compliance verification is non-negotiable.** When the link goes live, verify the `rel` attribute matches what the engagement requires. A "follow" link on a compensated placement is a Google policy violation that can hurt the client more than the link helps.
- **Humans on money + humans on sensitive decisions.** Any movement of money is human-only — agents flag, humans pay. Same for any thread that's gotten heated, ambiguous, or unusual.
- **Watch deliverability + sending compliance.** Outreach volume + a fresh inbox = spam folder + Gmail/Workspace AUP risk. Use a warmed mailbox or a transactional provider, throttle sends, monitor bounce rates.
- **Relationship is more valuable than the placement.** Don't let the agent burn a publisher relationship to chase one link. Code that into the negotiation rules explicitly.
- **Respect robots.txt + ToS when checking publisher sites.** If you're using Chrome MCP to check publisher pages before outreach, throttle, identify your user agent, and skip sites whose robots.txt forbids it.

## What this skill does NOT include

- A pre-built inventory of publisher sites — that's your IP / your moat. Build your own.
- Pricing tables — every market is different, set your own.
- Specific client briefs — you provide.
- Marketplace scrapers — out of scope (and often violates ToS).

## Setup

### 1. Provide your inventory
Either as a CSV, a SQLite/D1 table, or a JSON file. Schema:
```
{
  domain, contactEmail, niche, dr, monthlyTraffic, geo,
  notes, lastContactedAt, lifetimeOutcome
}
```

### 2. Provide your client roster
JSON or markdown files, one per client:
```
{
  code, name, domain, briefs: [{targetUrl, anchor, niche, cap}], voiceNotes
}
```

### 3. Provide your voice profile
2-3 example outreach emails in `voice-examples.md`.

### 4. Wire your channels
Slack/Discord channel IDs in `.env` for summaries + Tier 3 questions.

### 5. Drop the agent files
See `agent.js`, `orchestrator.md`, and `negotiation-rules.md` in this skill folder. Customise the placeholders.

### 6. Schedule
Run agent.js every 30 min, orchestrator 10 min after.

## Companion skills

- `agent-resilience` — required.
- `multi-llm-router` — recommended for Haiku reply classification.
- `two-layer-mcp-bridge` — the architectural pattern this is built on.
- `inventory-database` — recommended schema for the publisher list.
- `approval-gate` — for any outreach the agent shouldn't send without sign-off.

## Install

1. Drop this folder under `~/.claude/skills/link-builder-agent/`.
2. Replace placeholders in `agent.js` + `orchestrator.md` with your inventory path, client roster path, channels.
3. Provide voice examples.
4. Run a dry run (logs only, no actual sends) for 24h before going live.
5. Watch the first week of outreach manually — adjust the negotiation rules as you see what the agent does.
