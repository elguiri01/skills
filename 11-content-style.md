# Skill 11: Content Style and Humanization

Applies to ALL generated content across all sites: content expansion, zone pages,
service pages, homepages, meta descriptions. These rules are non-negotiable and
override any stylistic tendency in the model's default output. A violation of a
HARD RULE means the output is rejected and regenerated.

Reference: this skill draws on the pattern catalogue in blader/humanizer
(github.com/blader/humanizer), which is based on Wikipedia's "Signs of AI
writing" guide. Clone it for the full list:

    git clone https://github.com/blader/humanizer.git ~/skills/reference/humanizer

## HARD RULES (automatic rejection)

1. NO em-dashes anywhere. No en-dashes except inside numeric ranges
   such as 2024-2026, and even then prefer a hyphen. Rewrite dash constructions
   as two sentences, a comma, or a colon.

2. NO "it's not X, it's Y" constructions or any variant:
   "not just X but Y", "more than just X", "X isn't about Y, it's about Z".
   State the point directly.

3. NO stale dates. The current year must be injected into every job prompt.
   Never write "2024 Guide" or "2024-2025" in content generated in 2026.
   If a year appears in a heading or body, it must be the current year or a
   deliberate historical reference to real data (e.g. "BLS May 2025 data").

4. NO templated openers repeated across pages. "X is one of the most rewarding
   states in the country to..." appearing on 28 state pages is a footprint that
   flags the whole network. Every state page intro must lead with something
   specific to that state: a named employer, a licensing quirk, a real number,
   a geographic fact. If the intro would still be true with the state name
   swapped out, rewrite it.

5. NO invented facts. Salary figures, pass rates, tuition, program counts and
   employer names must come from the data supplied in the job input (BLS,
   JRCERT, scraped listings). If the data is not supplied, do not fabricate it,
   and do not write vague filler in its place. Omit the section.

## BANNED VOCABULARY AND PATTERNS

Words and phrases that mark text as machine-written. Do not use:

- delve, tapestry, landscape (metaphorical), leverage (as a verb), robust,
  seamless, vibrant, nestled, boasts, elevate, unlock, unleash, journey
  (metaphorical), navigate (metaphorical), dive into, explore (as filler)
- "It's important to note", "It's worth noting", "That said", "In today's
  fast-paced world", "In the ever-evolving world of"
- "Whether you're a X or a Y" opener
- "The future looks bright", "exciting opportunities await" or any
  cheerleading closer
- Stacked transitions: Moreover / Furthermore / Additionally used more than
  once per page
- Rule-of-three padding: "fast, reliable, and affordable" triads used as
  filler rather than information
- Rhetorical question openers: "Thinking about becoming a rad tech?"
- Significance inflation: "pivotal", "crucial", "essential" attached to
  ordinary facts

## RHYTHM AND STRUCTURE

- Vary sentence length. A page where every sentence runs 15-20 words reads
  as machine output. Mix short declarative sentences with longer ones.
- Prefer plain verbs: is, has, costs, takes, requires. Avoid copula-avoidance
  contortions ("serves as", "functions as", "stands as").
- Bullet lists only where the content is genuinely list-shaped (program
  listings, requirements checklists). Never convert explanatory prose into
  bullets to fill space.
- No bold-scattering. Bold is for figures the reader scans for (salary
  numbers, deadlines), not for emphasis decoration.
- One H2 per major topic. Do not generate a heading for every two sentences.
- Write for a US reader in US English on US sites, Spanish (Spain) on
  Spanish sites. No mid-Atlantic hedging.

## HUMANIZATION PASS (required final step for every content job)

After drafting, run a self-audit before returning output:

1. Ask: "What makes this text obviously AI-generated?" List the tells.
2. Rewrite to remove every tell found.
3. Verify against HARD RULES 1-5 above.
4. Verify no banned vocabulary remains.
5. Read the intro with the state/city name swapped for another. If it still
   works, it is template filler. Rewrite it.

Output only passes when the audit finds nothing.

## PROMPT INJECTION BLOCK

Include this verbatim in every content-generation job prompt sent to the model:

---
STYLE REQUIREMENTS (mandatory):
Today's date is {current_date}. Any year mentioned must reflect this.
Never use em-dashes or the construction "it's not X, it's Y".
Never use: delve, robust, seamless, vibrant, landscape, leverage, boasts,
elevate, unlock, journey, navigate, "it's important to note", "whether
you're", stacked Moreover/Furthermore/Additionally.
Vary sentence length. Use plain verbs. No cheerleading closers.
Only use facts from the data provided below. Never invent figures.
The introduction must contain at least one fact specific to this exact
location that would be false anywhere else.
Before returning, audit your draft for AI tells and rewrite any you find.
---
