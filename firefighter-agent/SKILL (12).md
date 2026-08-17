---
name: firefighter-agent
description: Twice-daily proactive client retention. Scans your project mgmt tool for risk signals (tickets, churn flags, payment issues), pulls performance data from Ahrefs + your tracker, drafts data-backed retention briefs, and posts them to your customer-success channel. Account managers walk into Monday meetings with the saves already teed up.
---

# firefighter-agent

The expensive client save is always the one nobody saw coming. The signals were all there — a ticket about reporting two weeks ago, a missed payment last month, a quiet account manager — but no human was paid to connect them. This agent does that connect-the-dots pass, twice a day, and surfaces the at-risk accounts BEFORE the cancellation email lands.

It also does the boring half of the job — pulling the Ahrefs / tracker data the account manager would otherwise have to gather by hand to back up a save. By the time the AM walks into the retention call, the screenshot, the ranking trend, and the ROI projection are already drafted.

## What it does

1. Reads your project mgmt tool (Serpply, ClickUp, Asana, Linear, Pipedrive, HubSpot — whichever you run) for active risk signals: open tickets > 48h, payment failures, "thinking about cancelling" flags, low-activity accounts.
2. Reads your customer-success channel for unanswered AM questions that need data backup.
3. For each at-risk account, pulls performance signals from Ahrefs (DR trend, ranking deltas, organic traffic curve) and your conversion tracker (lead volume, CPL trend, revenue attribution).
4. Drafts a structured **Client Intel Brief** per at-risk account: the signal that fired, the data context, a recommended save move, and a one-line ROI projection.
5. Posts briefs to your customer-success channel (no @-tag — the AM monitors the channel; tagging breaks the calm-channel discipline).
6. If a brief replies in-thread asking for more detail, the agent answers in-thread with the underlying numbers.
7. Logs every fire and every save to a run-ledger so you can review your retention rate by signal type.

## Why it works

- **Two-a-day cadence.** Once a day misses morning fires; hourly creates noise nobody reads. Morning + late-afternoon catches both inbound (overnight tickets) and outbound (AM end-of-day questions).
- **No "nothing to fight" posts.** If the run found nothing, it skips posting and only logs to the ledger. Channel hygiene is the whole point — every post in #customer-success must be load-bearing.
- **Data does the talking, not opinion.** The agent never says "I think client X might churn." It says "Client X opened ticket #4421 about reporting on Tuesday, their org_traffic is down 18% MoM, here are the three keywords that lost position." The AM decides what to do.
- **The save move is suggested, not actioned.** Suggestions are templates ("offer a 15-min check-in", "send the wins doc", "schedule a strategy refresh") — the AM picks one. Auto-actioning anything in a retention context is a brand risk.
- **Reads the channel both ways.** Most retention tools push; few read. Reading the AM's questions and answering them with the right data tightens the loop.

## What you provide

- Your project mgmt API (Serpply, ClickUp, Asana, Linear, Pipedrive, HubSpot — pick the one your CS team actually uses).
- Ahrefs MCP access.
- Your conversion tracker (D1, BigQuery, Mixpanel, your tracking worker — whichever holds lead/revenue data).
- A customer-success Slack/Discord channel.
- A list of risk-signal definitions in `signals.json` (open ticket > 48h, payment failed, "cancel" mentioned in any thread, etc.) — generic defaults included, tune to your business.

## Optimisations vs. one-shot prompts

- **Risk signals run in code.** The "is this client at risk" check is a deterministic query, not an LLM judgement. Saves credits and produces consistent results.
- **One LLM pass per at-risk account.** The model only invokes for the human-readable brief — combining the signal, the Ahrefs data, the tracker data, into one Slack-ready post. Cheap-tier (Haiku 4.5) is plenty.
- **Cache Ahrefs lookups.** Same client appears in multiple runs across the week — cache DR / traffic for 24h.
- **De-dupe across runs.** If client X was flagged morning and afternoon for the same signal, only post once — re-post only on a NEW signal or a new data delta.
- **Dry-run the first month.** Have the agent post to a private channel (yours, not the team's) for the first month so you can tune the signal thresholds without alarming the AM.

## Architectural considerations

- **The agent must NOT post in the client-facing Slack-Connect channels.** Strict allowlist: only your internal customer-success channel. One leaked Client Intel Brief in front of a client is a fired AM.
- **Personal data hygiene.** Briefs should reference clients by their internal code or domain, never personal AM names of the client side. Your AM knows who they're calling without the agent naming them.
- **Don't fight battles you can't win.** Some accounts are leaving because the founder sold the company, the CEO changed strategy, or the budget was cut. Those are not save situations — they're handoff situations. Tag them differently in the brief so the AM doesn't burn time on a lost cause.
- **Tracker / project-mgmt endpoints must be authenticated.** If you expose a JSON endpoint for the agent to read, it must require auth (bearer token / signed request / IP allowlist) and run over TLS. An unauthenticated endpoint of "all our at-risk client signals" is a competitive-intelligence leak.
- **Briefs are PII.** They contain client identifiers, ticket content, possibly payment status. Channel scope must be private to your CS team. Run-ledger entries should redact ticket/message bodies — store IDs and references, not the raw content.
- **Risk threshold drift.** Re-tune the signals quarterly. As the agency grows, what counted as "at-risk" at 30 clients is noise at 100.
- **Pair with your weekly client-wins agent.** Wins surface what to brag about; firefighter surfaces what to defend. AMs need both.

## What this skill does NOT include

- The retention move itself — the agent suggests, the human acts.
- A predictive churn model (use risk signals you can name, not an opaque score).
- Client-facing comms (deliberately — saves are a human-touch job).
- The risk-signal definitions for your specific business (defaults included; you tune).

## Setup

### 1. Wire your project mgmt API
Start with read-only scope. Risk-signal queries should never write back.

### 2. Wire Ahrefs + your tracker
Standard Ahrefs MCP setup. Tracker is whatever holds your lead/revenue data — most tracker workers expose a JSON endpoint.

### 3. Define your signals in `signals.json`
```json
{
  "open_ticket_hours": 48,
  "payment_failed": true,
  "cancel_mention_in_thread": true,
  "low_activity_days": 14,
  "ranking_drop_threshold_positions": 10,
  "traffic_drop_threshold_pct": 15
}
```
Add or remove signals to match how your business actually leaks clients.

### 4. Channel allowlist
In `config.json`, hard-code the customer-success channel ID. The agent will refuse to post anywhere else.

### 5. Schedule
Twice daily — typically 09:00 and 16:00 local time. Skip weekends unless your CS team works them.

### 6. Dry-run period
First 4 weeks: post to a private channel (yours alone). Tune thresholds. Then graduate to the team channel.

## Companion skills

- `agent-resilience` — required.
- `client-wins-agent` — pairs naturally; wins and fires are the two halves of CS comms.
- `client-reporting-agent` — the weekly report; firefighter is the live-fire version.
- `approval-gate` — wrap any future "send a save email" extension in an approval gate. Never auto-send.

## Install

1. Drop this folder under `~/.claude/skills/firefighter-agent/`.
2. Wire APIs + define signals.
3. Run dry into a private channel for 4 weeks.
4. Promote to your customer-success channel when the signal-to-noise ratio is right.
