---
name: client-wins-agent
description: Twice-weekly Ahrefs scan that detects ranking wins (and risks) for active clients, screenshots the SERP, and posts to your customer-success channel. Account managers walk into Monday meetings already knowing what to brag about.
---

# client-wins-agent

The dirty secret of agency client communication: the account manager finds out about a ranking win days after it happened, often AFTER the client noticed and asked. This agent inverts that — Mon and Thu it scans every client's keyword set, detects significant movement (up or down), screenshots the SERP, and drops it in your team channel.

## What it does

1. Reads active client list with their priority keywords.
2. For each keyword, queries Ahrefs SERP overview (via MCP): current position, last week, last month.
3. Detects significant movement:
   - Win: jumped into top 10, moved up 5+ positions, hit page 1 for the first time.
   - Risk: dropped 10+ positions, fell off page 1, lost a featured snippet.
4. Pulls SERP context via a compliant API (Ahrefs SERP overview, DataForSEO, SerpApi, or Google's Programmable Search JSON API). NOT via headless-Chrome scraping of Google — that violates Google's ToS.
5. Posts a structured update to your customer-success channel:
   ```
   :trophy: WIN: client.com — "best widgets for X" jumped from #14 to #6
   :warning: RISK: client.com — "widget reviews" dropped from #3 to #11 (lost featured snippet)
   ```

## Why it works

- **Account managers love it.** Walk into Monday's client call knowing what to lead with.
- **Risks surface early.** A 10-position drop on a money keyword often precedes a bigger problem (algo update, technical issue, lost backlinks). Catching it Tuesday morning instead of next month saves the relationship.
- **Visual makes it shareable.** Screenshot of the SERP is screenshot-able straight into client comms.

## What you provide

- Active client list with priority keywords.
- Ahrefs MCP access (or any compliant SERP data API).
- Team channel.

## Optimisations vs. one-shot prompts

- **Movement thresholds prevent noise.** A jump from #87 to #84 isn't a win. Thresholds filter to changes that actually matter.
- **Risks need bigger thresholds than wins.** A 5-position win is exciting; a 5-position risk is noise. Asymmetric thresholds.
- **Top-10 boundary triggers.** Crossing into top-10 is a special event regardless of magnitude. Same for dropping off.
- **Featured snippet detection.** Worth a separate flag — losing/winning a featured snippet has 5-10x the traffic impact of a normal position change.
- **Cheap-tier formatting.** The "format this finding into a Slack message" pass runs on Haiku 4.5.

## Architectural considerations

- **Twice weekly is the sweet spot.** Daily creates noise; weekly misses risks. Mon and Thu align with most client meeting cadences.
- **Cache the previous week's data.** Don't re-pull historical positions every run — cache them, only pull current.
- **No headless-Chrome SERP scraping.** Use compliant APIs only. SERP screenshots, when you need them, should come from approved providers (DataForSEO, SerpApi) that handle compliance for you.
- **Don't auto-forward to clients.** Internal channel only. Account managers cherry-pick what to share.
- **One post per client, not per keyword.** A post for every keyword movement floods the channel.

## What this skill does NOT include

- The keyword list (you provide).
- Specific Slack/Discord integration code (use your existing channel infra).

## Setup

### 1. Active client + keyword list
JSON or DB query: `[{client, domain, keywords: [...]}]`.

### 2. Ahrefs MCP
Required.

### 3. Team channel ID
For posting.

### 4. Schedule
Mon + Thu at start of business hours.

## Companion skills

- `agent-resilience` — required.
- `client-reporting-agent` — pairs well; this is the "live alerts" version, that's the "weekly summary" version.

## Install

1. Drop this folder under `~/.claude/skills/client-wins-agent/`.
2. Tune thresholds in `thresholds.md` to your taste.
3. Schedule Mon + Thu.
