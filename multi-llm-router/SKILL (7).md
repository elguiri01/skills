---
name: multi-llm-router
description: Route prompts to the cheapest model that can handle them. Cuts Claude credit usage 60-80% by sending bulk/deterministic work to DeepSeek or GPT-4.1-mini, reserving Claude for reasoning-heavy tasks.
---

# multi-llm-router

A skill for cost-aware multi-model orchestration. Most agentic workflows over-spend on Claude because the same model handles classification, extraction, content drafting, and architectural reasoning. This skill routes each task to the cheapest model that can do it well.

## When to use

Invoke this when:
- A workflow makes >50 LLM calls per run.
- Tasks are heterogeneous (classification, extraction, drafting, reasoning).
- You're paying $X/day on Claude and want to drop it.

## Routing table

| Task type | Recommended model | Why |
|---|---|---|
| Reply classification (5-class) | Haiku 4.5 or DeepSeek-chat | Cheap, fast, accurate enough |
| Email/data extraction (structured JSON) | DeepSeek-chat or GPT-4.1-mini | Determinism, low cost |
| Long-form content (1500+ words) | DeepSeek-reasoner | ~10x cheaper than Sonnet, comparable prose |
| Code review + diff critique | GPT-5 or o3 | Different "eye" than Claude — catches different bugs |
| Architectural reasoning, novel cross-system | Claude Opus | Best at this, worth the cost |
| MCP tool loops, scheduled task orchestration | Haiku 4.5 | Fast, cheap, handles tool use well |
| Anything safety-critical with high blast radius | Claude Sonnet/Opus | Highest reliability, best at refusing |

## Setup

### 1. Get API keys
- OpenAI: https://platform.openai.com/api-keys
- DeepSeek: https://platform.deepseek.com/api_keys
- Anthropic: https://console.anthropic.com/settings/keys

### 2. Create `.env` in your skill folder
```
OPENAI_API_KEY=sk-proj-...your-key-here...
DEEPSEEK_API_KEY=sk-...your-key-here...
ANTHROPIC_API_KEY=sk-ant-...your-key-here...
```

### 3. Drop the router script
See `router.js` in this skill folder. Usage:

```javascript
const { route } = require('./router.js');

const reply = await route({
  task: 'classify_reply',     // matches table above
  input: emailBody,
  schema: { intent: 'string', confidence: 'number' }
});
```

The router picks the model, calls it, validates the response, and falls back one tier up if the cheap model returns garbage.

## Architectural considerations

- **Validation layer is mandatory.** Cheap models occasionally return malformed JSON. Validate with Zod or a schema check, retry once on the same model, then escalate one tier up.
- **Cache aggressively.** If you're calling the same prompt repeatedly (e.g. niche classification on a fixed taxonomy), cache by input hash. Saves 60%+ even before routing.
- **Track cost per run.** Log model + input_tokens + output_tokens to a JSONL. After a week you'll see exactly where money goes — and which routes to tighten.
- **Don't route safety-critical tasks to cheap models.** Refunds, cancellations, customer-facing emails, financial transactions — keep these on Claude Sonnet+. The savings aren't worth one bad output.

## Why this beats one-shot prompts

A one-shot "use the best model for everything" approach typically costs 5-10x what a routed setup costs at the same quality. The trick is most tasks don't need flagship reasoning — classification, extraction, and bulk drafting are commodity work. By routing them to commodity models, you free up your Claude budget for the work that actually requires it.

## Companion skills

- `cheap-tier-router` — finer-grained tier selection within Anthropic's models (Haiku/Sonnet/Opus).
- `openai-code-review` — uses GPT-5 as a second reviewer for Claude's diffs.
- `deepseek-writer` — pre-built DeepSeek long-form content pipeline.

## Install

1. Drop this folder under `~/.claude/skills/multi-llm-router/`.
2. Add API keys to `.env` as shown above.
3. Restart Claude Code or run `/skills` to refresh.
4. Reference in agent prompts: "Use multi-llm-router for any classification or extraction step."
