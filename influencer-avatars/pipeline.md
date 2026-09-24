# Influencer avatar pipeline

The eight steps from `README.md` as an operating procedure. Each step names
what does the work, what it produces, where it is saved, and whether the
agent may do it alone. "Agent" means autonomous under Skill 12; "Adrian"
means the human-eyes gate.

Steps 1 to 6 are drafting and the agent owns them. Steps 7 and 8 touch the
public and money, and Adrian owns them.

| # | Step | Does the work | Output | Who |
|---|------|---------------|--------|-----|
| 1 | Niche and angle | Claude, with Adrian's interest as the edge | one paragraph in `personas/<name>/profile.md` | Agent proposes, Adrian picks |
| 2 | Character profile | Claude (prompt in `prompts/`) | `personas/<name>/profile.md` | Agent |
| 3 | Character sheet and scenes | Higgsfield `character-sheet` workflow, then `generate_image_batch` for scenes | media ids in `personas/<name>/media.md` | Agent |
| 4 | Content ideas and scripts | `skills/content-engine` | `personas/<name>/scripts/NN-slug.md` | Agent |
| 5 | Voice | Claude writes the voice prompt; Higgsfield `create_voice` (or HeyGen) | voice id in `media.md` | Agent |
| 6 | Video | `skills/video-prompt` for the prompt; Higgsfield `generate_video` 9:16 1080p with the sheet as reference; captions in CapCut or Instagram Edits | files, ids and cost in `personas/<name>/posting-log.md` | Agent to draft |
| 7 | Accounts and posting | Adrian, in the platform apps | handles in `profile.md`, each post in `posting-log.md` | **Adrian** |
| 8 | Monetise and measure | `skills/digital-product` for the product; store link in bio; views and sales per video | `posting-log.md` and `vessa/` | Product draft: Agent. Store, payment, price: **Adrian** |

## Step notes

### 1. Niche

The source's three: health, wealth, relationships. For Vessa the niche is
fixed (mobility and stretching) and the question is the angle. The source's
lesson on angle: be the opposite of the niche's default presenter. Fitness
content defaults to a 25-year-old in a gym; the contrast candidates are in
`vessa/persona-candidates.md`.

### 2. Character profile

Prompt shape from the source: "Create a character profile for an AI
influencer in the <niche> niche. Give them a name, a backstory, a distinct
look, and a unique selling point." Save the output as `profile.md` from
`personas/_template.md`. The backstory may be colourful; it may not contain
a credential (Skill 16).

### 3. Character sheet

Call `get_workflow_instructions` with `{ workflow: "character-sheet" }` and
follow it; do not free-hand the prompt. The source's prompt asked for a full
body shot and a close-up, a description of look and clothing, white
background, realistic skin. Age drift is real: the source's 101-year-old
came out looking 70 and needed "make him a few years older". Check the sheet
against the profile before generating scenes, because every video inherits
it.

Scenes: four or five places the character lives. Generate as a batch,
record every media id.

### 4. Scripts

The content-engine skill (when uploaded) produces an idea list, then
scripts for chosen ideas. Choose by the source's three winners: relatable
(the audience feels known), advisory (one concrete rule), and reveal (a
"secret" with a psychological hook). Podcast framing works for advisory.
Scripts are short: the source's talking pieces are 10 to 20 seconds. No
em-dashes. For Vessa, scripts pass the health-claims rule in `README.md`
before they go anywhere.

### 5. Voice

Claude writes a detailed voice description from the profile (age, accent,
pace, warmth, texture). Generate once, store the id, reuse. If the voice is
wrong the whole persona is wrong, so listen before step 6.

### 6. Video

Order of work, from the source: silent B-roll first with on-screen text
(cheapest, proves the sheet holds across generations), then talking to
camera. Check `balance` before a batch and record the credit cost of the
first render in `posting-log.md` so the batch estimate is a number and not
a guess. Reuse the `exercise-animation` skill's validated settings for any
movement footage.

### 7. Accounts and posting

Adrian creates accounts and posts. Bio carries the AI disclosure. Post to
Instagram, TikTok and YouTube Shorts together, ten per persona to start.
Every post goes in `posting-log.md` with date, platform, script id, and
views at 48h and 7d.

### 8. Monetise and measure

Product first choice for an advisory persona: a structured workbook or
challenge (one habit or one stretch a day, tick boxes, a printable
tracker), because generic PDF information is free from any chatbot. For
Vessa the product may be the app itself, with a 30-day stretch challenge as
the lead magnet or the paid entry point; that is a decision in `vessa/`.

Measure per video, not per account. Compare personas over weeks, not days.
Do not project revenue from the source's $276.
