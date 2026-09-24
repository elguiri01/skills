# prompts/

The prompt cheat-sheet from the source, once uploaded, plus our own. One
file per prompt, named for the pipeline step it serves.

Expected from the source's cheat-sheet:

| File | Purpose | Step |
|------|---------|------|
| `character-profile.md` | "Create a character profile for an AI influencer in the <niche> niche. Give them a name, a backstory, a distinct look, and a unique selling point." | 2 |
| `character-sheet.md` | full body plus close-up, look and wardrobe, white background, realistic skin | 3 |
| `scenes.md` | four or five home locations for the character | 3 |
| `voice.md` | the detailed voice description Claude writes from the profile | 5 |
| `profile-picture.md` | portrait variants for the account avatar | 7 |
| `b-roll.md` | silent clip with room for on-screen text | 6 |

Before using the character-sheet prompt, call Higgsfield
`get_workflow_instructions` with `{ workflow: "character-sheet" }`; the
connector's own workflow supersedes a pasted prompt where they differ.
