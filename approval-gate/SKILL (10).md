---
name: approval-gate
description: Human-in-the-loop pattern for any agent action that's high-blast-radius — sending money, posting public content, deleting data, contacting clients. JSONL queue + thread-based approval. Stops one bad agent decision from costing you a relationship.
---

# approval-gate

Some agent actions cannot be undone. Sending money, posting client-facing content, deleting data, contacting a customer with the wrong tone. For those, you want a human in the loop — not "the agent runs and tells you about it after," but "the agent stops, asks, waits."

This skill is the canonical approval-gate pattern.

## What it does

1. The agent reaches a decision that needs approval.
2. It writes the proposed action to a `pending-approval.jsonl` queue.
3. It posts a Slack/Discord/email message with the proposal + context + action buttons (or a thread reply convention).
4. It WAITS — does not proceed.
5. A human approves (`+1`, "yes", clicking a button, replying with "go"), and the agent reads the approval and acts.
6. If 24h passes with no response, the agent escalates (notifies a fallback person) or auto-closes the proposal.

## When to use

- Any outreach to clients (vs. internal).
- Money movement (invoices, refunds, ad spend changes >X%).
- Publication of content under a real person's byline.
- Deletion of data.
- Anything irreversible.

## When NOT to use

- High-volume routine tasks where waiting kills throughput. For those, use a confidence threshold instead — auto-execute above 0.9, queue below 0.7, ignore between (or vice versa).
- Things the agent has demonstrably handled correctly thousands of times. At some point you trust it.

## Setup

### 1. Drop the queue
JSONL file at `data/pending-approval.jsonl`. Append-only.

### 2. Wire the notifier
Whatever channel you use — Slack MCP, Discord webhook, email. The proposal post must include:
- The action being proposed (in plain English).
- The full context (relevant data, who/what/why).
- The thread ID for the human to reply to.
- A clear way to approve or reject.

Approval conventions (pick one):
- `+1` reaction = approve, `-1` = reject.
- Reply with "yes" or "no" in the thread.
- Click an action button (Slack interactive messages).

### 3. Wire the watcher
Either:
- Polling: every N minutes, check the queue for items with status='pending', look up the thread for an approval, act if found.
- Event-driven: Slack/Discord webhook fires on reaction, watcher picks it up.

Polling is simpler. Use it unless volume justifies events.

### 4. Wire the timeout
Items with no response in 24h either escalate (post to a fallback channel, page someone) or auto-close (mark as "rejected by timeout"). Pick per-action.

## Architectural considerations

- **Approvals are blocking for THAT item only.** The agent continues processing other items. One pending approval doesn't kill the batch.
- **Approval needs context, not just a question.** "Approve outreach to publisher X for client Y?" + the actual proposed email + the rationale > "Should I send this?"
- **Don't ask for the same approval twice.** If the agent has approval to send 5 emails to similar publishers, that's one approval, not five.
- **Fallback escalation matters.** If the primary approver is on holiday, the proposal sits forever. Configure fallback humans.
- **Log every approval.** For audit. Particularly for money movement.

## What this skill does NOT include

- A pre-built Slack integration (use your existing one).
- A specific approval UI — the convention is the value, not any specific implementation.

## Companion skills

- `agent-resilience` — Tier 3 escalation uses the same queue.
- `link-builder-agent` — uses approval-gate for any outreach that exceeds set rules.
- `gp-writer-agent` — uses approval-gate for any niche-restricted client.

## Install

1. Drop this folder under `~/.claude/skills/approval-gate/`.
2. Pick polling or event-driven.
3. Wire your notifier.
4. Test with a deliberately ambiguous action — make sure it queues, asks, waits, and acts on approval.
