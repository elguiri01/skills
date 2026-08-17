---
name: client-reporting-agent
description: Weekly client SEO reports done right. Pulls Ahrefs metrics + your delivered work from your CRM, generates HTML→PDF reports with smart display logic (hide what's bad, lead with what's good), posts to your client-success channel for review and forwarding. Built around the "make the client feel good about their investment" principle.
---

# client-reporting-agent

Most automated client reports look exactly like what they are: a templated dump of metrics, including the ones that went down. Clients see one bad number and start questioning the relationship. This agent applies smart display logic — it leads with wins, hides weak metrics intelligently, and never sends a report that makes a client feel they're wasting money.

## What it does

1. Reads your active client roster.
2. For each client, pulls fresh Ahrefs metrics: DR, referring domains, backlinks, traffic, keywords, top pages, AI visibility (Brand Radar).
3. Pulls "links delivered this period" from your CRM (count, sites, anchors).
4. Compares current vs. last month vs. signup baseline.
5. Applies SMART DISPLAY logic — picks which metrics to highlight, which to hide.
6. Renders an HTML report from your template, converts to PDF.
7. Posts to your client-success channel for human review before forwarding.

## Why it works

Three rules that turn a generic report into a relationship asset:

1. **Always show metrics that improved.** If DR went up, lead with it. If referring domains grew, that's the headline.
2. **Hide or de-emphasise metrics that declined.** If traffic dropped, don't highlight it. If keywords fell, focus on what's still ranking. Honest, not deceptive — but agile.
3. **Baseline beats month-on-month for tenured clients.** Even if last month dipped, baseline often shows great cumulative progress. Pick whichever comparison genuinely tells the better story.

## What you provide

- **Active client list.** API/DB call that returns active clients with domain + signup date.
- **Delivered links data.** Whatever CRM/sheet tracks placements — domain, anchor, target URL, date.
- **Ahrefs MCP access.** This skill uses the Ahrefs MCP tools (site-explorer-metrics, backlinks-stats, top-pages, brand-radar). If you don't have Ahrefs, the skill is mostly useless — it's the canonical baseline.
- **Report template.** HTML template with `{{TOKEN}}` placeholders. See `template-example.html` in this skill folder for the recommended structure.
- **PDF converter.** Any HTML→PDF tool (Puppeteer-based is easiest). See `html-to-pdf-example.js`.

## Optimisations vs. one-shot prompts

- **Smart display is the killer feature.** A one-shot "generate a client report" prompt produces a generic dump. The whole value here is the curated narrative — what to lead with, what to hide.
- **AI visibility section is conditional.** Brand Radar mentions are great when they're growing. When they're zero or declining, the section is hidden completely. Never show embarrassing AI data.
- **Traffic value hidden for restricted niches.** Adult, cannabis, gambling, escort niches never show traffic value (it's misleading and tone-deaf for those markets).
- **Sequential Ahrefs calls.** ~8 calls per client = rate limit risk if parallel. Sequential with brief pauses is more reliable.
- **Cheap-tier routes.** The "format the metrics" pass runs on Haiku 4.5; the "decide narrative + smart display" pass runs on Sonnet because it needs judgement.

## Architectural considerations

- **Always have a fallback if Ahrefs fails for one client.** Skip that client, note in summary, continue. Don't kill the whole batch.
- **Baseline date defaults to 6 months ago if unknown.** Better than no baseline.
- **Domain string hygiene.** Strip `https://`, strip trailing slashes, strip `www.` if Ahrefs is configured for naked domains. Single biggest source of "Ahrefs returned no data" errors.
- **PDF conversion can fail.** If it does, post Slack with a note about the issue and the saved HTML path. Don't silently swallow.
- **Human review is mandatory.** The agent posts to the team for review — humans forward to clients. Never auto-send to clients.

## What this skill does NOT include

- A pre-built HTML template (write your own — branding matters).
- Specific client integrations (provide your own CRM access).
- Pricing/revenue data — clients don't see your costs, only outcomes.

## Setup

### 1. Provide active client API
Endpoint or DB query that returns `[{name, code, domain, signupDate}]`.

### 2. Provide delivered links data
Same — endpoint or query returning placed links per client.

### 3. Configure Ahrefs MCP
Per Ahrefs MCP docs. Note: Ahrefs MCP is the only path; there's no direct Ahrefs API usable for this. Plan capacity accordingly.

### 4. Drop your report template
HTML with placeholders. See `template-example.html`.

### 5. Wire PDF converter
Puppeteer-based recommended. See `html-to-pdf-example.js`.

### 6. Configure team channel
Post-target for review.

### 7. Schedule
Weekly. Mondays often best — gives the team the week to forward to clients.

## Companion skills

- `agent-resilience` — required.
- `cheap-tier-router` — formatting on Haiku, narrative on Sonnet.
- `multi-llm-router` — the broader version.

## Install

1. Drop this folder under `~/.claude/skills/client-reporting-agent/`.
2. Replace placeholders in `agent.md` with your endpoints, channel, template path.
3. Run on one client manually first. Review the output yourself before scaling.
4. Schedule weekly once you trust the smart-display logic.
