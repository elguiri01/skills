---
name: agent-ready-audit
description: Run and act on Google Chrome Lighthouse's "Agentic Browsing" audit — the AI-agent readiness check — and fix a site so AI agents can actually navigate and use it. Use this skill whenever the user mentions agentic browsing, Lighthouse AI readiness, "is my site ready for AI agents", AI agent browsing tests, llms.txt, WebMCP, accessible names on buttons/links for agents, layout shift breaking agent clicks, or agent-readiness as part of AI SEO / GEO work — even if they don't name Lighthouse. Also use when they ask what to fix first to make a site agent-friendly, or want a site audited before an AI shopping/booking agent tries to use it.
---

# Agent-ready audit (Lighthouse Agentic Browsing)

## What this audit actually is

Chrome ships an **Agentic Browsing** category in Lighthouse that checks whether an AI agent — a shopping agent, a booking agent, an operator-style browser agent — can reliably parse and act on a page.

Three things about it are commonly misunderstood, and getting them right saves the user from wasted work:

**It is a checklist, not a grade.** Google's docs describe it as a fraction of readiness checks passed, deliberately *not* a weighted 0–100 score, because the standards are still emerging and Google wants signal rather than ranking. Some renderers (and the raw CLI JSON) still surface a number — ignore it. Read it as "which checks failed", and open each failure for the specific elements.

**Only two of the checks currently carry real weight.** `agent-accessibility-tree` and `cumulative-layout-shift` are scored. The WebMCP and llms.txt audits report **"Not applicable"** on most sites rather than failing them. So a site with no llms.txt and no WebMCP can still pass this audit cleanly.

**llms.txt is not required to pass, and is not a ranking factor.** Popular tutorials claim you must have an llms.txt to pass the agentic test. That is not what the audit does — the llms.txt check only grades the file's *quality* (has an H1, has links, isn't too short) *if the file exists*. Google has separately been clear it doesn't use llms.txt for ranking. Recommend it as a cheap, low-risk addition, not as a fix for a failing audit. If the user believes it's required, say so plainly once and move on — they may still want one for other reasons, which is fine.

## Running it

Pick the route that matches what the user needs.

**They want to see it themselves (Chrome DevTools).** Open the page → right-click → Inspect → **Lighthouse** tab → Analyze. In Chrome 150+ the Agentic Browsing category is on by default. In Chrome 130–149 it sits behind the experimental categories toggle and must be ticked first. Unticking the other categories makes the run faster and the result easier to read, and is worth suggesting. WebMCP audits additionally need the WebMCP origin trial registered, so they'll usually read "Not applicable" — that's expected, not a problem.

**You are auditing for them (preferred when you have a shell).** Use the bundled script, which runs Lighthouse headlessly and prints just the agentic checks plus the offending elements. It ships in two identical versions — run whichever matches the machine:

```bash
node scripts/run_audit.mjs https://example.com
```

```bash
python3 scripts/run_audit.py https://example.com
```

Both take the same flags: `--json-out path.json` keeps the full report for deeper digging, and `--mobile` audits the mobile rendering (agents increasingly drive mobile viewports, and a site can pass on desktop yet fail on mobile because of a collapsed nav full of unlabelled icon buttons).

Node must be present either way — Lighthouse is fetched via `npx` on first run, so there's nothing to install beyond Chrome itself.

**On a headless server or droplet**, two things bite. Chrome usually isn't installed, so install `google-chrome-stable` (or `chromium`) and, if Lighthouse still can't find it, point `CHROME_PATH` at the binary. And Chrome's sandbox can't initialise as uid 0, which is the default on most droplets — the scripts detect root and add `--no-sandbox` automatically, and `--no-sandbox` is available explicitly for containers that run as a non-root user but still can't sandbox. Dropping the sandbox is fine for auditing pages you already trust, which is the situation here.

If neither script can run — no Node, a locked-down machine, a page behind login — fall back to auditing the page directly with browser tools: read the accessibility tree and look for interactive nodes with no accessible name, then check for layout shift on load. That covers the two checks that actually count.

## What to fix, and in what order

Order matters more than coverage here. Fixing these out of order burns hours on things that don't change whether an agent can use the site.

**1. Accessible names on every interactive element.** This is first because it's binary: an agent that can't identify a control cannot act on the page *at all*. Agents read the accessibility tree — the same structure a screen reader uses — not the visual rendering. A button that is visually obvious (an icon, a styled `<div>`) is invisible to an agent if it has no programmatic name. This is also where `agent-accessibility-tree` failures almost always come from. See `references/accessible-names.md` for the specific patterns that break it and how to fix each.

**2. Layout stability (CLS).** Second because it's a *reliability* problem rather than a *possibility* problem: the agent can see the page, but if elements move between the moment it locates a target and the moment it clicks, it clicks the wrong thing. This shows up as agents that work sometimes and mysteriously fail other times. See `references/layout-stability.md`.

**3. llms.txt** — optional, ~15 minutes, only affects the quality check if the file exists. See `references/llms-txt.md` for a format that passes.

**4. WebMCP** — genuinely forward-looking. It lets a site expose explicit tools (e.g. "search products", "book appointment") so an agent calls them instead of guessing at the UI. Worth doing for transactional sites that expect agent traffic; premature for most. See `references/webmcp.md`.

Lead with steps 1 and 2 when reporting back. If the user asks for the full picture, give them all four with the effort/impact split visible so they can choose.

## Reporting findings

Give the user something they can act on without re-reading the Lighthouse report:

- Which checks passed and failed, as a plain list — no invented score.
- For each failure, the specific elements (selector or visible text) and the concrete fix, in the priority order above.
- Roughly how long the fixes take and what breaks if they're skipped, so scope is theirs to set.

One thing worth telling them, because it changes how the work gets budgeted: fixing accessible names and layout shift is the same work as fixing the site for screen reader users. It's not agent-specific overhead — it's accessibility work that happens to also serve agents, which usually makes it much easier to justify.

## Reference files

- `references/accessible-names.md` — the patterns that break the accessibility tree, with before/after fixes
- `references/layout-stability.md` — CLS causes and remedies, in impact order
- `references/llms-txt.md` — what the audit checks, plus a template
- `references/webmcp.md` — declarative and imperative tool registration, and when it's worth it

Both `scripts/run_audit.mjs` and `scripts/run_audit.py` produce identical output; they're kept in step deliberately so either runtime works. If you change the parsing in one, change the other.
