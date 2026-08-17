---
name: gp-writer-agent
description: Autonomous guest post writer. Pulls assignments from your tracker, researches via Perplexity/web search, extracts on-page SEO requirements (NLP terms, headings) from your optimisation tool of choice, drafts in editorial voice, never fabricates stats, posts to team channel for review.
---

# gp-writer-agent

Most "AI guest post" tools produce content that sounds like AI. Generic, vague, no specific stats, no opinion. This agent is built around the principle that good guest posts read like editorial — written by someone with a point of view, supported by real facts, optimised quietly for search.

## What it does

1. Scans your content tracker for rows assigned to "AI Writer" with status "Briefed" or "To Write".
2. For each assignment:
   - Reads the brief (target keyword, target URL, anchor, voice notes, niche restrictions).
   - Pulls SEO requirements (NLP terms, headings, word count) from your optimisation tool (Surfer, NeuronWriter, etc.) — via Chrome MCP if there's no API.
   - Researches the topic via Perplexity API or web search. Saves the research blob to disk.
   - Drafts the article in editorial voice, hitting the SEO targets.
   - NEVER fabricates stats — uses only the research blob + the client's own website data.
   - Posts to team channel for human review before publication.

## Why it works

Three rules that most "AI writer" tools break:

1. **Never write blind.** If the optimisation tool isn't reachable (Chrome offline, viewport 0x0), the agent ABORTS. Doesn't write a generic article hoping for the best.
2. **Never fabricate.** All stats come from a research blob. The agent is told repeatedly: if a stat isn't in the blob, don't include one. Better to have fewer stats than fake ones.
3. **Editorial voice, not review voice.** AI tools love writing fake reviews ("after testing this for 6 months..."). This agent is told explicitly to write as a journalist, not a reviewer.

## What you provide

- **Content tracker.** Whatever you use (Google Sheet, Airtable, D1, Notion). One row per assignment with brief, target keyword, target URL, anchor, status.
- **Optimisation tool access.** Chrome MCP login to Surfer/NeuronWriter, OR an API integration.
- **Research API.** Perplexity, OpenAI web search, or whatever you prefer.
- **Voice profile.** 2-3 published guest posts you wrote yourself, for tone reference.
- **Per-client briefs.** Niche restrictions, banned topics, anchor styles.

## Optimisations vs. one-shot prompts

- **Routes long-form draft to DeepSeek.** Cost-efficient for bulk prose, comparable quality once wrapped in the editorial-voice prompt. (See companion skill `deepseek-writer`.)
- **Verifies viewport before writing.** A common failure mode — Chrome session died, viewport returns 0x0. The agent checks first, aborts cleanly if so.
- **Saves research blob to disk.** When a draft is questioned, you can audit exactly what facts were available. No "where did the agent get THIS stat from."
- **Skips rather than fakes.** Missing target URL → skip row. Missing keyword → skip row. Editorial voice over fake compliance.
- **Tier-3 escalation on new clients.** If there's no voice profile yet, the agent asks for one rather than guessing.

## Architectural considerations

- **Surfer/NeuronWriter score is a quality floor, not a goal.** Hitting 70+ is good; chasing 90+ produces unreadable keyword-stuffed prose. The agent is told to prefer readability over score above 75.
- **Word count discipline.** Most "AI writer" tools over-shoot by 30-50%. Hard cap at +5%, post-process trim if needed.
- **No first-person stories.** Banned in the prompt. Generic AI loves "I tested this for three weeks..." which is fabrication.
- **No personal names of individuals.** Brand names only. Reduces fact-check risk and personality-rights issues.
- **Save drafts to disk before posting.** If the team channel post fails, you don't lose the work.

## What this skill does NOT include

- A pre-built voice profile (provide your own).
- Pre-built per-client briefs (provide your own).
- Specific optimisation tool integration code (depends on what you use).

## Setup

### 1. Provide voice examples
2-3 of your best published guest posts as `voice-examples.md` in this skill dir.

### 2. Per-client brief files
One markdown file per client: `clients/CLIENT_CODE.md` with niche, banned topics, voice notes.

### 3. Wire optimisation tool
Prefer the official API of your optimisation tool (most have one). Chrome-based UI automation is a last resort — many tools' ToS forbid automated UI access, and your account can be suspended for it. If you go the Chrome route, check the ToS first and rate-limit accordingly.

### 4. Research API key
Perplexity or equivalent. Add to `.env`.

### 5. Tracker integration
Drop your tracker access in `tracker.js`. The skill works with any tracker that exposes a list-rows endpoint and an update-row endpoint. Load all credentials from environment variables — NEVER hardcode keys or tokens in `tracker.js` or anywhere else in the source. Add `.env` to `.gitignore`.

### 6. Schedule
5x weekdays during your working hours. Each run handles whatever's queued.

## Companion skills

- `deepseek-writer` — for the actual prose generation (cheap and good).
- `agent-resilience` — required (Tier 2 skip-and-flag on missing fields is critical).
- `two-layer-mcp-bridge` — architectural pattern this uses.
- `approval-gate` — for any niche-restricted clients that need pre-publication sign-off.

## Install

1. Drop this folder under `~/.claude/skills/gp-writer-agent/`.
2. Provide voice examples + client briefs + tracker integration.
3. Run a dry run on one assignment, review the output yourself.
4. Adjust the editorial-voice prompt + niche restrictions per your needs.
5. Schedule once you trust the output.
