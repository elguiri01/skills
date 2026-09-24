# skills/

Drop zone for the Claude skills the source video cites, as Adrian uploads
them. One folder per skill, containing its `SKILL.md` and any supporting
files exactly as received. Do not edit them in place; if one needs a change
for our use, note it in the folder's own `NOTES.md` so the original stays
diffable against upstream.

Expected, from the transcript:

| Folder | What the source used it for | Pipeline step |
|--------|-----------------------------|---------------|
| `content-engine/` | "generate content ideas for <persona>", then scripts for chosen ideas | 4 |
| `video-prompt/` | takes a simple idea and writes a detailed video-generation prompt, referencing the character sheet as image 1 | 6 |
| `digital-product/` | proposes three product ideas with the reason each sells, then builds the chosen one (a 30-day workbook with daily tick boxes, a fridge tracker, and bonuses) | 8 |

The source described them as "found online for free" and "not sure how good
they are". Read each on arrival and note in `NOTES.md` what it assumes, what
it gets wrong for us, and what the Skill 11 style block needs to override
(em-dashes, reading age, hype).

Installation: on the Claude account these go in via Customize > Add > Upload
a skill. For Claude Code on this droplet they are read from here directly.
