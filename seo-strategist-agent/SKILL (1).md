---
name: seo-strategist-agent
description: Autonomous SEO strategist that handles handover, audits the client's site, runs proper keyword research (lowest DR in top 5, never KD), maps anchors, builds optimisation briefs. Acts as the "thinking" layer above your link builder + writer agents.
---

# seo-strategist-agent

Most agencies stop at "we run AI for content and links." The strategy layer — what content, against which keywords, with what anchors — is still done manually because most AI tools get it wrong. This agent is built to handle strategy correctly: real keyword research methodology, proper anchor mapping, briefs that writers can actually execute against.

## What it does

1. **Handover audit.** New client onboarding — pull existing rankings, backlink profile, content gaps.
2. **Keyword research.** For each priority page, find target keywords using the right methodology.
3. **Anchor map.** Compute anchor distribution from current backlink profile, plan future anchors to fill gaps without over-optimising.
4. **Brief generation.** Hand off to your writer + link builder agents with structured briefs.
5. **Re-audit on schedule.** Quarterly re-audit to refresh strategy as the site evolves.

## Why it works (the methodology)

Three rules most "AI keyword research" tools break:

1. **Never use KD (Keyword Difficulty).** It's a synthetic score. Use the lowest DR site ranking in the top 5 — that's the actual competitive bar to beat.
2. **Filter for buyer intent.** Sort by CPC where commercial intent matters. Volume without intent is vanity.
3. **Anchor distribution matters more than volume.** Most penalised sites have over-optimised exact-match anchors, not too many or too few links.

## What you provide

- **Client domain + niche.**
- **Ahrefs MCP access.** Required.
- **Niche restrictions.** Banned topics, geo restrictions, voice constraints.
- **Brief template.** What format your writer agent + link builder agent expect.

## Optimisations vs. one-shot prompts

- **Methodology is in the prompt.** A one-shot "research keywords for this site" prompt produces generic output. This agent is told explicitly: lowest DR top-5, sort by CPC, ignore KD.
- **Anchor analysis on real data.** Pulls actual current anchor distribution from Ahrefs. Identifies over-optimised anchors. Plans the next 30 anchors to bring distribution back into a natural-looking range.
- **Briefs are executable.** Output is structured for your writer + link builder agents to consume directly. Not a Word doc — JSON or markdown with required fields.
- **Re-audit cadence.** Quarterly by default. Catches when a strategy goes stale because Google changed something or the site evolved.
- **Tier-3 escalation on weird sites.** Brand-new sites with no rankings, sites with manual penalties, sites in tightly regulated niches — the agent flags rather than guessing.

## Architectural considerations

- **Strategist runs BEFORE writers + link builders.** Without a strategy, the downstream agents are guessing what to write/place.
- **Don't run strategist too often.** Quarterly audit + brief refresh on demand is enough. Daily strategy = thrash.
- **Feed strategist output to writer/link-builder via JSONL.** Not "Claude reads Claude's output in conversation." Persist the briefs to disk so the agents can read them on schedule.
- **Anchor over-optimisation is the silent killer.** Track exact-match anchor percentage; flag at 30%+ as a danger zone.
- **KD is a trap.** If you find yourself using KD, you're using the wrong methodology. The lowest DR top-5 method is more accurate AND less likely to mislead.

## What this skill does NOT include

- Specific client briefs (provide your own).
- Specific brief schema (depends on your downstream agents).
- A list of "good" niches — that's market judgement, not codifiable.

## Setup

### 1. Wire Ahrefs MCP

### 2. Provide brief schema
Define what your writer + link builder agents need. Typical fields: target URL, target keyword, anchor, niche, word count, voice notes.

### 3. Provide niche restrictions per client
JSON or markdown.

### 4. Schedule
On-demand for new clients (handover). Quarterly for re-audit.

## Companion skills

- `agent-resilience` — required.
- `link-builder-agent` — downstream consumer of briefs.
- `gp-writer-agent` — downstream consumer of briefs.

## Install

1. Drop this folder under `~/.claude/skills/seo-strategist-agent/`.
2. Customise `methodology.md` if your agency uses different rules.
3. Run a manual handover audit on a test client.
4. Compare output to what your human strategist would produce. Iterate the prompt.
