# Opportunity model and measurement templates

## Opportunity map

Create one row per underlying information need, not per keyword variation.

| Field | What to record |
| --- | --- |
| Cluster | Stable name for the information need |
| Example queries | Neutral prompts and conventional searches |
| Intent | Learn, compare, validate, act, buy, troubleshoot |
| Audience/market | User segment, country, language |
| Business value | Why a qualified visitor matters |
| Existing best sources | Ranking and cited URLs by engine |
| Coverage weakness | Missing, stale, generic, unsupported, confusing |
| Unique contribution | Data, experience, tool, examples, expert access |
| Recommended asset | Canonical page type and URL target |
| Corroboration route | Legitimate external surfaces and reason |
| Evidence burden | Normal, elevated, or YMYL |
| Priority | Impact, confidence, effort, time, risk |

## Practical prioritization

Score each dimension from 1 to 5 only when evidence supports that precision:

- **User value:** frequency or importance of the problem.
- **Business value:** fit with a meaningful conversion.
- **Coverage gap:** weakness of current results and citations.
- **Right to win:** site's real expertise, data, access, or experience.
- **Feasibility:** ability to create and maintain the asset.
- **Risk:** factual, legal, compliance, reputation, or spam exposure.

Use this directional formula when comparable data exists:

`Opportunity = (User value + Business value + Coverage gap + Right to win + Feasibility) - Risk`

Do not disguise guesses as quantitative science. When inputs are uncertain, use High/Medium/Low and state why.

## Fixed prompt battery

Build a representative set across category discovery; how-to and mechanics; cost, risk, timing, requirements, and eligibility; comparisons and alternatives; brand checks; audience, location, and constraint-specific long-tail; and likely follow-up questions.

Keep wording neutral. Do not seed the target brand unless the prompt is explicitly a brand check. Freeze the first version before baseline capture.

## Citation capture schema

| Field | Example |
| --- | --- |
| Run ID | 2026-09-01-v1 |
| Date/time/timezone | ISO 8601 |
| Engine and mode | Google AI Mode, ChatGPT search, Perplexity |
| Locale and login state | en-US, signed out |
| Prompt ID and text | C07, exact prompt |
| Answer captured | Text, screenshot, or export reference |
| Target mentioned | Yes/No and wording |
| Target cited | Yes/No |
| Cited target URL | Canonical URL |
| Other cited URLs | Full list |
| Citation order | If visible |
| Accuracy/sentiment | Correct, mixed, incorrect, absent |
| Referral sessions | From analytics, if available |
| Notes | Variance, errors, personalization |

## Core measures

- **Prompt citation rate:** prompts citing the target / valid prompts tested.
- **Citation share:** target citation appearances / all citation appearances in the defined set.
- **Coverage:** query clusters with at least one eligible canonical asset / priority clusters.
- **Accuracy rate:** target mentions without material factual errors / target mentions reviewed.
- **Qualified referral rate:** qualifying sessions or conversions / tracked answer-engine referrals.

Report denominators and confidence limitations. Do not combine engines unless the blended total answers a stated business question.

## Experiment record

For each change, record the hypothesis, affected URLs and clusters, baseline, exact change and deployment date, discovery confirmation, comparison window, confounders, outcome, and decision to keep, revise, expand, or stop.

Prefer a small pilot with matched pages or clusters before scaling a new template.
