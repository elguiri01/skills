# Agent Resilience Protocol

Reference doc to be loaded by every autonomous agent. Defines the three-tier fallback behaviour.

## Three tiers

### Tier 1 — Silent default
Missing field has a sensible default. Fill in, don't notify, continue.

### Tier 2 — Skip & flag
Missing field is critical. Skip this item, log the reason, continue with the rest of the batch.

### Tier 3 — Ask human
Genuinely ambiguous. Post to the agent's primary notification channel with full context, pause this item only, continue rest.

## Per-agent customisation

Each agent should specify its own list of fields → tiers. Example:

```markdown
## RESILIENCE RULES
- Tier 1: missing subject → default. Missing anchor → mixed. Missing greeting → "Hi there".
- Tier 2: missing email address → skip + log. Missing target URL → skip + log.
- Tier 3: unparseable reply → ask human. Conflict between source A and source B → ask human.
```

## Mandatory run summary

Every agent run ends with a structured summary:

- Items processed
- Items succeeded
- Items skipped (Tier 2) with reasons
- Tier 1 defaults used (count)
- Tier 3 questions raised (linked threads)

## Anti-patterns

- Defaults that change behaviour silently in a way the user wouldn't expect ("missing budget → use $1000" is a bug, not a default).
- Tier 3 questions without context (the human can't help you with "something went wrong").
- Blocking the whole batch on one Tier 3 — pause that item, not the run.
- No logging — without logs, the tiers are invisible.
