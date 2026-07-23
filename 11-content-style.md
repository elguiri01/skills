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

Source of the anti-AI patterns below: the MIT-licensed `blader/humanizer`
skill (Wikipedia "Signs of AI writing", 33 patterns), merged with our own
rules. The reading-age target is ours. This is the single canonical block;
orchestrator.py `STYLE_REQUIREMENTS` is kept byte-aligned to it (the only
difference is the placeholder name: `{today}` in code, `{current_date}` here).

---
STYLE REQUIREMENTS (mandatory):
Today's date is {current_date}. Any year mentioned must reflect this; never
write guides dated to earlier years.

READING AGE (hard target): write for US grade 7. Average sentence about 14
words; keep most sentences under 20. One idea per sentence. Prefer common,
everyday words. The first time an unavoidable technical term appears (e.g.
"ASE accreditation", "OEM program"), define it in plain words in the same
sentence. Target Flesch Reading Ease 60-70 (Flesch-Kincaid grade 6-8). This
matters most for trades audiences and is not optional.

PLAIN, HUMAN VOICE:
- Use plain verbs: is, has, costs, takes, requires. Not "serves as", "boasts",
  "features", "offers".
- Never use em-dashes or en-dashes. Use a full stop, comma, colon, or
  parentheses. Use plain hyphens in institution and campus names.
- Never: "it's not X, it's Y", "not only X but also Y", or tailing negations
  ("no guessing").
- Do not use: delve, robust, seamless, vibrant, landscape (metaphor), leverage,
  boasts, elevate, unlock, journey, navigate (metaphor), tapestry, testament,
  underscore, showcase, crucial, pivotal, interplay, enhance, nestled,
  breathtaking, stunning, thriving, "it's important to note", "it's worth
  noting", "whether you're", "at its core", "the real question is", "let's dive
  in", "here's what you need to know".
- No stacked Moreover/Furthermore/Additionally. No rhetorical-question openers.
  No conversational hooks ("Honestly?", "Look,").
- No cheerleading closers ("the future looks bright", "exciting times ahead").
  End on a concrete fact or a clear next step.
- No significance inflation ("marks a pivotal moment", "underscores its
  importance"). No "-ing" filler for fake depth ("reflecting", "symbolising").
  State the fact.
- No vague attributions ("experts argue", "studies show") without a named
  source in the DATA.
- Do not force triplets or "from X to Y" ranges. Name one term for a thing and
  reuse it; do not cycle synonyms.
- Sentence case in headings (first word and proper nouns only). No emojis.
  Straight quotes only. No boldface to emphasise ordinary terms.
- No chatbot artefacts ("I hope this helps", "let me know"), no
  knowledge-cutoff disclaimers, no meta-commentary about the text.

FACTS: Only state specific figures (salaries, tuition, pass rates, program
counts) that appear in the DATA sections of this prompt. Never invent
statistics, names, dates, or citations. If a figure is not supplied, first ask
whether the page needs it at all: if it does not, omit the sentence or the whole
section and move on -- silence on a topic is perfectly acceptable and often
better. Only where a figure is genuinely essential to the page, write [VERIFY:
description of needed figure] in its place. A [VERIFY] marker is a signal for
human review, not a substitute for content, so use it sparingly.

Vary sentence length within the grade-7 ceiling. The introduction must contain
at least one fact specific to this exact location that would be false anywhere
else. Do not open with "X is one of the most ..." or any variant.

AUDIT before returning (two passes):
1. Rewrite to natural pacing, preserving every fact.
2. Ask "what still reads as AI?" and "did I invent any fact?" Fix both. Confirm
   zero em/en dashes and grade-7 reading level.
---
