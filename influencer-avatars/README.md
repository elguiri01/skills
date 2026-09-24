# Influencer Avatars

A skills set for building and running AI-presented social accounts: a
consistent synthetic persona (face, voice, backstory, point of view) that
posts short-form video and funnels attention to a product. Created
2026-09-22 from a transcript of a 7-day "AI influencer" challenge video
(`sources/`), to be filled with the skills, scripts and prompt cheat-sheet
that video cites as Adrian uploads them.

First deployment target: **Vessa**, a stretching app Adrian is building in
Claude Code on his PC. See `vessa/`.

This is a different kind of deployment from the numbered skills. Those
operate the 62-site affiliate portfolio. This one builds a media property
that can point at anything: an app, a workbook, an affiliate offer, or one
of the portfolio sites. Skill 08 (video production) and Skill 16 (persona
authority) are the nearest relatives and their rules carry over.

## The play, distilled from the source

1. **Pick a niche** where people pay to feel better, get richer, or fix a
   relationship. The video's read: health, wealth, relationships. Lean into
   a real interest, because it is an edge nobody else has.
2. **Generate a character profile**: name, backstory, distinct look, unique
   selling point. Contrast with the niche's default presenter is the USP
   (a 101-year-old for longevity advice; a designer-clad grandmother for
   wealth, where every other account is a young man in a rented Lamborghini).
3. **Generate the character sheet**: full-body plus close-up on a plain
   background, realistic skin, then a set of home scenes the character
   lives in. Every later video references the sheet so the face stays
   consistent.
4. **Map content and write scripts** with a content-engine skill. Pick
   ideas that are relatable, advisory, or reveal a "secret". Podcast-style
   framing works.
5. **Give them a voice**: a voice prompt written by Claude, generated once,
   reused everywhere.
6. **Produce video** at 9:16, 1080p. Start with silent B-roll plus on-screen
   text (cheap, tests consistency), then talking-to-camera pieces.
7. **Launch several personas at once**, 10 videos each, and let the
   audience choose. Do not crown a winner early: the persona that came third
   at day 3 (Vivien) had the only 250k-view video by day 7.
8. **Monetise** with the shortest path available. Ranked by the video for
   speed: digital product (a structured, interactive workbook; not an ebook)
   > affiliate (TikTok Shop, which needs TikTok presence from day one) >
   physical product > brand deals. Instagram Reels pay no ad revenue.

Source result, stated as the source stated it: 23 sales at $12 in seven
days, $276 gross, $157 net after PayPal fees and the $99 tool budget. One
persona, one product, one platform. Treat it as an existence proof, not a
projection.

## Two corrections to the source, and why they matter here

**Post to TikTok and YouTube Shorts from day one, not later.** The video
crossed off TikTok Shop affiliate income because it only launched on
Instagram. Same video, three surfaces; the cost of the extra uploads is
near zero. YouTube is also the single most-cited domain in our own AIO
citation data (Skill 22), so Shorts carry a second value beyond views.

**The winner is not knowable at day 3.** The source doubled down on the
early leader and missed its own viral account. Keep every persona posting
until the numbers separate over weeks, and measure per video, not per
account average, because one outlier drives the total.

## Rules (read before generating anything)

These are not optional and they are not a drag on the play. The source's
own accounts said "your AI grandpa" in the bio and drew zero complaints.

- **Disclose the avatar.** The persona bio states it is an AI character.
  Platforms require labels on photorealistic AI video and audio (Meta "AI
  info", TikTok "AI-generated content"); verify the current label mechanism
  before the first post. The EU AI Act transparency duties for synthetic
  media apply from August 2026 and Adrian operates from the EU. Undisclosed
  synthetic presenters are the one thing that turns this into the
  "hardworking patriotic woodworker" fraud the source itself called out.
- **Skill 16's line holds.** No fabricated credentials, no impersonation of
  a real person's name, face or likeness, no fake reviews or testimonials,
  no sock-puppet engagement. The avatar can have a backstory; it cannot
  claim a licence, a degree, or a clinical qualification.
- **Health claims are YMYL.** For Vessa (stretching, mobility, pain) the
  avatar shares habits, routines and general guidance, and never diagnoses,
  never promises a cure, and never tells someone with an injury what to do.
  "Talk to a physio if it hurts" is a line the character says, not a
  disclaimer buried in a caption.
- **Publication is gated.** Per Skill 12, posting a video or social post is
  public-facing and needs Adrian's explicit go. The agent may generate
  characters, scripts, images, voices and videos to draft status without
  asking. Creating accounts, posting, and connecting payment are Adrian's.
- **Media spend is bounded, not free.** Higgsfield and HeyGen are
  subscription tiers (Skill 12). Check `balance` before a batch; do not run
  `generate_video_batch` on ten scripts without knowing the credit cost of
  one.
- **No em-dashes** in any generated copy, scripts included (Skill 11).

## Folder map

```
influencer-avatars/
  README.md          this file: the play, the rules, the map
  pipeline.md        the eight steps as an operating procedure, with which
                     tool or skill does each and where the human gate sits
  sources/           the transcript this was built from, and later sources
  skills/            drop zone for the cited Claude skills (content engine,
                     video prompt, digital product). Each in its own folder
                     with its SKILL.md, as uploaded, unmodified
  scripts/           any scripts that come with the skills, plus ours
  prompts/           the prompt cheat-sheet: character sheet, scenes, voice,
                     profile picture, B-roll
  personas/          one folder per persona: profile, media ids, handles,
                     posting log. _template.md is the shape
  vessa/             the first deployment: brief, persona candidates, the
                     product the funnel points at
```

## Where the tools already are

- Higgsfield MCP is connected to the Claude account (memory:
  `galena-media-mcp-access`). `get_workflow_instructions` with
  `{ workflow: "character-sheet" }` is the documented route to a consistent
  multi-view character; `create_voice` for the voice; `generate_video` with
  the sheet as reference for consistency; `tiktok_publish` exists but is a
  publish action and therefore gated.
- HeyGen MCP is also connected: `create_photo_avatar` from the character
  sheet and `create_video_from_avatar` is a second route to talking-head
  video. Render economics are in memory (`galena-heygen-render-economics`):
  0.53 credits per second at 1080p, so 720p for volume.
- The `exercise-animation` skill (synced to this Claude account) already
  validated Higgsfield model choice, prompt template and 9:16 mobile rules
  for Vessa's exercise illustrations. Reuse its settings for the avatar's
  B-roll rather than rediscovering them.
- Skill 08 has the YouTube upload and optimisation steps and the
  orchestrator integration shape if this is ever queued as jobs.

## Status

- 2026-09-22: folder created, README and pipeline written from the source.
  Awaiting upload of the cited skills, scripts and cheat-sheet. No persona
  generated yet. Nothing posted.
