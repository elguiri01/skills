---
name: agent-resilience
description: Three-tier fallback protocol for autonomous agents. Stops one bad data row, missing field, or external-tool blip from killing an entire batch run. Tier 1 = silent default, Tier 2 = skip + flag, Tier 3 = ask human. Adopted across every production agent.
---

# agent-resilience

The single biggest cause of "my agent died overnight" failures is brittle assumption: a missing field, a malformed reply, a Chrome viewport returning 0x0. Without a resilience protocol, one bad input kills the whole batch.

This skill defines the three-tier fallback pattern. Drop it at the top of every agent's prompt + wire the tiers into your code.

## The three tiers

### Tier 1 — Silent default
For missing fields where a sensible default exists. Don't notify, don't slow the batch down, just fill in and continue.

Examples:
- Missing email subject → generate from template (`"Outreach about {domain}"`).
- Missing anchor style → use mixed (60% branded, 40% keyword).
- Missing baseline date → use 6 months ago.
- Missing webmaster name → use "team" or "there".

### Tier 2 — Skip & flag
For missing critical fields where the agent literally cannot proceed without violating quality. Skip the row entirely, log the reason, continue with the rest of the batch. Surface skipped items in the run summary.

Examples:
- Missing webmaster email → skip outreach, log "No email for {domain}".
- Missing target URL → skip row, log reason.
- Missing client code → skip entry entirely.
- Output validation failed → skip and flag.

### Tier 3 — Ask human
For genuinely ambiguous situations a human needs to resolve. Post to your Slack/Discord/notification channel with context, pause that one item, continue with the rest of the batch.

Examples:
- Reply was unparseable → post the text, ask human how to handle.
- Budget would be exceeded → ask human if they want to proceed.
- Conflicting instructions between two source docs → ask which is authoritative.
- New entity with no profile in your CRM → ask for context.

## When to use

Every autonomous agent. Without exception. If your agent doesn't have a resilience protocol, it WILL die overnight on something stupid — a missing column, a renamed field, a flaky Chrome session.

## Setup

### 1. Drop the protocol doc
The `agent-resilience.md` in this skill folder is a clean version you can reference from every agent prompt:

```markdown
## Resilience
Read and follow: `~/.claude/skills/agent-resilience/agent-resilience.md`
```

### 2. Wire the tiers
The `resilience.js` helper provides three functions:

```javascript
const { tier1, tier2, tier3 } = require('./resilience.js');

const subject = tier1.default(row.subject, () => `Outreach about ${row.domain}`);
const validRow = tier2.skipIf(row, !row.email, 'No email for ' + row.domain);
if (!validRow) continue;
const decision = await tier3.askHuman({
  channel: process.env.NOTIFICATION_CHANNEL,
  question: 'Reply unparseable, what to do?',
  context: replyBody
});
```

### 3. Mandatory run summary
At the end of every run, the agent MUST post a summary that includes:
- Items processed / succeeded
- Items skipped (with reasons)
- Tier 1 defaults used (count is fine, no detail needed)
- Tier 3 questions raised

Without the summary, the protocol is invisible — silent failures stack up.

## Architectural considerations

- **Defaults must be SAFE.** If you're unsure whether a default is safe, escalate to Tier 2 instead. A skipped row is better than a wrong action. Default values that change behaviour silently (e.g. "missing budget → use a hardcoded budget") are bugs, not defaults — escalate those.
- **Tier 3 must include enough context.** "Got an unparseable reply" is useless. "Got reply X from publisher Y on thread Z, see attached" is actionable.
- **Don't loop on Tier 3.** If the human doesn't respond in N hours, retry once, then mark the item paused and continue. Don't block the whole batch waiting for one decision.
- **Log every tier hit.** Even Tier 1 silent defaults should be logged. After a month of logs you'll see where the upstream data is rotten and can fix it at source.
- **Test the resilience.** Write tests that intentionally pass malformed rows and verify the agent skips + logs cleanly.

## Why this beats one-shot prompting

A one-shot "be robust" instruction in a prompt produces inconsistent behaviour. Sometimes the agent invents a sensible default; sometimes it bails entirely; sometimes it does something dangerous. Codifying the tiers — both in the prompt AND in the helper functions — makes the behaviour predictable.

## Companion skills

- `slack-approval-gate` (or any notification adapter) — Tier 3 needs somewhere to ask.
- `multi-llm-router` — pair with router fallbacks for cross-model resilience.
- `cheap-tier-router` — escalate one tier up on failure as the same pattern.

## Install

1. Drop this folder under `~/.claude/skills/agent-resilience/`.
2. Reference `agent-resilience.md` from every agent prompt.
3. Wire `resilience.js` into agents that need programmatic helpers.
4. Audit one existing agent for resilience gaps. Pick the most painful one and start there.
