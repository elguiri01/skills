---
name: cfo-agent
description: Weekly autonomous CFO. Reads your P&L from FreeAgent / Xero / QuickBooks, calculates revenue trends, staff savings, margin, and ROAS, then writes a budget directive for your ad / spend agents to consume. Operating margin under 25% = no spend increase, no exceptions. Walks the line between human-judgement finance and machine-discipline budgeting.
---

# cfo-agent

Most agency owners look at their P&L once a month if they're lucky, twice a year if they're honest. By the time you notice that staff costs ate the margin or that ad spend outran revenue, the damage is two months old. This agent is the missing finance loop — every Monday morning it pulls the books, runs the numbers, and tells the rest of your agent fleet what they're allowed to spend this week.

It also forces the discipline most owners never actually maintain: **operating margin under 25% = no budget increase, no exceptions**. The agent is incapable of being talked into spending you can't afford because the formula runs before any human sees the number.

## What it does

1. Pulls last week's P&L from your accounting platform (FreeAgent, Xero, QuickBooks, or any bookkeeper export).
2. Computes the metrics that actually drive decisions: rolling revenue trend, gross margin, operating margin, staff cost ratio, ROAS on paid acquisition, free cash position.
3. Compares against the rolling 4-week and 12-week baseline — flags any metric that swung more than your tolerance band.
4. Calculates next week's permitted spend per channel using a transparent formula (not a black-box LLM "vibe" budget):
   - Margin > 35% AND ROAS > 2.5 → up to +20% on the spend channel.
   - Margin 25-35% → flat budget.
   - Margin < 25% → mandatory -20% until next review.
5. Writes a `budget-directive.json` file that your ad-spend agent reads on its next run.
6. Posts a one-screen Slack summary to you (DM, not channel — finance is private) with the inputs, the formula it used, and the directive it issued.
7. Logs everything to a run-ledger so you can audit a quarter of decisions in five minutes.

## Why it works

- **The formula runs before the LLM does.** This is the single most important architectural decision. The LLM's job is to fetch, format, and explain — never to decide budget. A deterministic formula on auditable inputs is the only safe way to delegate finance to a machine.
- **Bookkeeping data lags.** Most platforms reconcile a week behind. The agent always notes "incomplete period" on the most recent week so you don't act on partial data.
- **Operating margin is the lever.** Revenue is vanity, gross margin is sanity, operating margin pays the rent. The 25% floor is configurable but the principle isn't.
- **Budget directive lives in a file, not a Slack message.** Other agents (FB Ads Manager, Google Ads Manager) read the directive on their next run. Decoupling means the CFO agent can run weekly while spend agents run daily — they always read the latest authoritative number.

## What you provide

- **Bookkeeping access.** FreeAgent, Xero, or QuickBooks API key — or a manual P&L drop if your books live somewhere weirder. Direct API beats Chrome scraping every time.
- **A rolling baseline.** First run, the agent needs ~12 weeks of historic data to build the baseline. Run it in dry-run mode for the first cycle, sanity-check the numbers, then go live.
- **Your spend channels.** Which agents should consume the directive (FB Ads, Google Ads, LinkedIn, freelancer budget, etc.) and where each one stores its config.
- **Your tolerance bands.** The 25% margin floor and ±20% adjustment cap are sensible defaults. Tune them to your business and write the override to `config.json`, not the agent prompt.
- **A private Slack channel or DM.** P&L data is never posted in a shared channel.

## Optimisations vs. one-shot prompts

- **Deterministic budget math.** As above — the formula is in code, not in the LLM. The LLM grade on this calculation is "fail" because it occasionally rounds wrong, occasionally hallucinates a metric, and occasionally flatters you. Code doesn't.
- **One LLM pass per run.** The agent only invokes the model for two things: (a) write the human-readable Slack summary from the computed directive, and (b) explain anomalies in plain English. Both are cheap-tier tasks (Haiku 4.5).
- **Cache the bookkeeping pull.** Most accounting APIs rate-limit. Cache the raw P&L for 6 hours so manual re-runs don't burn quota.
- **Dry-run mode.** First two months should run in dry-run — writes the directive to `budget-directive.preview.json` instead of the live file. Lets you spot formula bugs before they shrink your ad budget by 20%.

## Architectural considerations

- **Fail closed, not open.** If the agent can't pull bookkeeping data this week, the directive does NOT change — last week's directive stands. Never default to "no constraint" on a missing input.
- **Don't auto-implement the directive.** The CFO agent writes the file; the spend agents read it on their schedule. This decoupling is intentional — it gives you a window to override before any spend changes.
- **No client-level data.** The CFO agent works on aggregate financial data. It never references individual clients by name in its outputs (compliance + comms hygiene).
- **Audit log is the source of truth.** Every directive, every formula input, every override gets written to `directive-history.jsonl`. When you review the quarter, this is your read.
- **Don't let the agent see strategic context.** This agent isn't here to opine on whether to fire a client or hire a strategist. Its scope is "what can we spend next week given last week's books." Anything outside that scope is human judgement.
- **Lock down the directive file.** `budget-directive.json` is trusted by your spend agents to authoritatively set their budget. Restrict file permissions to the user the agents run as. If you want belt-and-braces, sign the directive (HMAC over the JSON body, key in `.secrets/`) and have the spend agents verify the signature before reading. A tampered directive is a tampered budget.
- **`.secrets/` hygiene.** OAuth refresh tokens for accounting platforms are highly sensitive. `.secrets/` MUST be excluded from version control, file permissions locked to the agent user, and tokens rotated on a defined schedule (90 days is a reasonable starting cadence).

## What this skill does NOT include

- Bookkeeping itself (use FreeAgent, Xero, QuickBooks, or a human bookkeeper).
- Tax / compliance advice (this is an internal decision tool, not an accountant).
- Auto-execution of the budget directive (deliberately — your spend agents read it, you're never more than one cycle from override).
- Investor / board reporting (different audience, different format).

## Setup

### 1. Wire bookkeeping access
- **FreeAgent:** OAuth app, store refresh token in `.secrets/freeagent.env`. Hit the `/v2/profit_and_loss` endpoint.
- **Xero:** OAuth 2 app, scope `accounting.reports.read`. Hit the `Reports/ProfitAndLoss` endpoint.
- **QuickBooks:** OAuth 2 app, scope `com.intuit.quickbooks.accounting`. Hit the `reports/ProfitAndLoss` endpoint.

### 2. Define your formula in `config.json`
```json
{
  "margin_floor": 0.25,
  "margin_target": 0.35,
  "max_adjustment": 0.20,
  "spend_channels": ["fb-ads", "google-ads"],
  "directive_path": "C:/agents/budget-directive.json",
  "preview_path": "C:/agents/budget-directive.preview.json"
}
```

### 3. Schedule
Weekly, Monday 06:00 local time. Must run BEFORE any spend agent's Monday cycle — typically the spend agents run at 08:00+, giving you a 2-hour buffer to override.

### 4. First two months: dry-run
Set `directive_path` and `preview_path` to the same value. Read the preview each Monday, sanity-check the formula output against your gut. When you trust it, separate the paths and let it write live.

### 5. Wire your spend agents to read the directive
Each spend agent (FB Ads Manager, etc.) reads `budget-directive.json` at the top of its run. If the file is missing or older than 7 days, the spend agent halts and asks for human input — this is the fail-closed behaviour.

## Companion skills

- `agent-resilience` — required.
- `fb-ads-monitor` — pairs with this; the CFO writes the directive, the FB Ads agent reads it.
- `approval-gate` — wrap the directive in an approval gate for the first month if you're nervous.
- `multi-llm-router` — the LLM passes here are cheap-tier; route accordingly.

## Install

1. Drop this folder under `~/.claude/skills/cfo-agent/`.
2. Wire your bookkeeping API + write `config.json`.
3. Schedule weekly. Run two months in dry-run before going live.
4. Wire your spend agents to read the directive file.
