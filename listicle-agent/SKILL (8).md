---
name: listicle-agent
description: AI-corroboration listicles. For a target keyword, finds which competitors AI search engines cite (ChatGPT, Perplexity, Gemini), drafts a "best X for Y" post that includes those competitors as social proof, optimised for AI snippets and human readers alike. The new SEO content angle nobody's running yet.
---

# listicle-agent

Traditional listicles are dead. Generic "10 best widgets" posts rank for nothing because AI search can read 1000 of them and pick its own answer. The new angle: write listicles that AI engines USE — that means including the brands AI already mentions, formatting for AI snippet extraction, structuring for both human and machine readers.

## What it does

1. Takes a target keyword: "best CRMs for small agencies."
2. Queries ChatGPT, Perplexity, Gemini with the same query.
3. Extracts which brands each AI cites.
4. Computes the union (the "AI consensus" set).
5. Drafts a listicle that includes the consensus brands plus 1-2 surprises, formatted for AI snippet extraction.
6. Optionally inserts your client / partner brand at a sensible position.
7. Posts to your CMS or saves as a guest-post-ready draft.

## Why it works

- **Inclusion in AI consensus = inclusion in future AI answers.** When an AI search engine cites your post as a source, your client/partner brand goes along for the ride.
- **Avoids the "fake review" trap.** You're not writing fake testimonials — you're aggregating the real consensus from AI tools, then adding your client.
- **Format optimised for snippet extraction.** Headings, lists, comparison tables — AI engines parse these reliably.

## What you provide

- ChatGPT, Perplexity, Gemini API access (or scrape if their ToS allow).
- DeepSeek for the prose.
- Your CMS or output destination.
- Client/partner brand list (which to insert into which listicles).

## Architectural considerations

- **Don't fake the AI citations.** This pattern works because the brands are real. Don't make up sources.
- **Position your client honestly.** If your client is genuinely #2 in the consensus, write them at #2. Forcing them to #1 makes the post fake-feeling and reduces AI engine trust over time.
- **Update quarterly.** AI consensus shifts. A listicle written last quarter is stale.
- **Watch for "this looks AI-written" tells.** Listicles are the most-AI'd content type — easy to detect. Use voice examples, real opinions, vary structure.

## What this skill does NOT include

- Scraping AI engines that prohibit it (use APIs).
- Pre-built brand inclusion logic (you decide which clients to insert and where).
- Faking testimonials or reviews — strict prohibition.

## Setup

### 1. AI engine API access
ChatGPT, Perplexity, Gemini — all have APIs.
### 2. DeepSeek for prose
### 3. CMS or output dest
### 4. Brand inclusion rules per client

## Companion skills

- `gp-writer-agent` — for the actual prose generation.
- `seo-strategist-agent` — picks the target keywords.
- `agent-resilience` — required.

## Install

1. Drop this folder under `~/.claude/skills/listicle-agent/`.
2. Wire APIs.
3. Run on one keyword. Audit the AI consensus extraction manually.
4. Scale once the inclusion logic produces sane output.
