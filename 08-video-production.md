# Skill 08 — AI Video Production for Career Education Content

## Purpose
Produce short-form and long-form videos answering career and education queries
that rank in Google video carousels and YouTube search. Videos drive traffic
independently of Google organic rankings and build E-E-A-T signals through
author presence outside the site.

## Strategic context

### Why video matters for this portfolio
- Google video carousels appear for "how to become X", "X salary", "X training"
  queries — exactly the keywords this portfolio targets
- YouTube is the second largest search engine; career queries are heavily searched
- AI Overviews do not suppress video results the way they suppress organic listings
- Videos create citable, linkable assets that earn E-E-A-T signals
- One umbrella channel avoids the YouTube verification nightmare of 60+ channels

### The umbrella channel approach
One YouTube channel — working title "Career Path USA" or "Career Advisor" —
covers all niches in the portfolio. Each video links to the relevant site in
the description. Authority builds on one channel rather than being fragmented.

A single consistent on-screen persona (AI-generated presenter) appears in all
videos. This persona links to the author page on the relevant affiliate site,
creating the external author presence Google quality raters check for.

---

## The production workflow

### Overview
Total time per video: 20-30 minutes once the pipeline is established.

```
Query selection → Script generation → Voiceover → Transcription with
timestamps → Image generation (Higgsfield) → Video assembly → Upload
```

### Step 1 — Query selection
Target queries where:
- Your affiliate sites already rank positions 5-15 (video can appear above them)
- Google shows a video carousel in the SERP
- Search volume is 500-5000/month (enough to be worth it, not so competitive
  that a new video has no chance)

Sources for query selection:
- GSC data: queries with impressions but low CTR
- SerpAPI: check if video carousel appears for target keyword
- "how to become X", "X salary in [state]", "how long does X take",
  "X certification requirements", "X vs Y career" — these consistently
  show video results

Orchestrator job: weekly SerpAPI scan of top 50 keywords per Tier 1 site,
flag those with video carousel. Add to video queue.

### Step 2 — Script generation
Claude Sonnet generates the script. Target length: 90-180 seconds for
short-form (YouTube Shorts, TikTok), 4-7 minutes for standard YouTube.

Script prompt template:
```
You are writing a YouTube video script for Career Path USA, a channel that
helps working adults understand career options in healthcare and trades.

Target query: [how long does it take to become a vet tech]
Target keyword: [vet tech training duration]
Affiliate site to reference: [vettechnicians.org]

Write a [90 second / 5 minute] script that:
- Answers the query directly in the first 10 seconds (hook)
- Uses specific data: BLS statistics, typical program lengths, state
  licensing requirements
- Mentions 2-3 schools or program types by name
- Ends with a CTA to visit vettechnicians.org for a full program comparison
- Sounds conversational, not like a blog post being read aloud
- Has a persona voice: the presenter is a career advisor who has helped
  hundreds of people enter healthcare careers

Format the script with timestamps every 5-8 seconds like:
[0:00] Hook text here
[0:07] Next section text here
[0:15] etc.
```

Haiku for Shorts scripts (cheaper, faster). Sonnet for longer videos.

### Step 3 — Voiceover production
Adrian records real voiceover. This is the strongest possible option:
- Genuine human voice = no demonetisation risk
- Belfast accent is distinctive and memorable — do not try to neutralise it
- Authenticity signals E-E-A-T: a real person with real knowledge
- Consistent voice across all videos builds audience recognition
- No ongoing cost

**Recording setup:**
- Any USB microphone works (Blue Yeti, Rode NT-USB, even AirPods in a
  quiet room)
- Record in a small room with soft furnishings (bedroom, walk-in wardrobe)
  to reduce echo
- Read from the script but allow natural pauses and slight ad-libs —
  sounds more human than reading verbatim
- Record in one take if possible; minor errors can be cut in editing
- Save as WAV or high quality MP3

**On the Belfast accent:**
American audiences respond well to British Isles accents in educational
content — it reads as authoritative and trustworthy. Do not attempt a
neutral American accent. Lean into it.

Save voiceover as MP3. Filename: `[domain]_[keyword]_[date].mp3`

### Step 4 — Transcription with timestamps
Upload voiceover to Turboscribe (free tier: 3 transcriptions/day).
Export with timestamps every 5-8 seconds.

Output format:
```
[0:00] Becoming a vet tech takes between one and three years depending...
[0:07] Most programs are offered at community colleges as two-year...
[0:15] Some accelerated certificate programs can be completed in...
```

Turboscribe URL: turboscribe.ai

### Step 5 — Image generation (Higgsfield)
Higgsfield is an AI image/video generation tool with a Claude Code MCP
integration. It generates images or short video clips from text prompts.

**Installation (one-time setup):**
```bash
# Install Higgsfield CLI
npm install -g @higgsfield/cli

# Authenticate
higgsfield auth login

# Install the MCP skill for Claude Code
higgsfield mcp install
```

**For career education content, use the humorous stick figure style:**
- Simple stick figure drawings as if made quickly in MS Paint
- White background, black outlines, minimal colour
- Figures should be expressive and slightly comedic — conveys personality
- Text labels on figures ("YOU", "YOUR BOSS", "STUDENT LOAN") add humour
- Simple scene-setting: stick figure in scrubs, stick figure at a desk,
  stick figure crying next to a dollar sign
- Data can be shown as hand-drawn bar charts or simple arrows
- The deliberately rough style reads as intentional personality, not low
  budget — this is the key insight from the viral channel in the tutorial
- Consistent style across all videos builds recognisable channel identity

**Master prompt for Claude Code:**
```
You are generating images for a YouTube video about [topic].
Generate one image for every timestamp in the following script.
Each image must visually represent what is being said at that timestamp.

Style requirements:
- Simple stick figure drawings, as if made quickly in MS Paint
- White background, black outlines
- Figures should be expressive and slightly humorous
- Add simple text labels where helpful ("YOU", "EMPLOYER", "STUDENT LOAN")
- Data shown as rough hand-drawn bar charts or simple arrows
- No 3D, no cinematic lighting, no photorealism
- Deliberately simple — the roughness is the style, not a flaw
- Consistent across all images in this video

Here is the script with timestamps:
[paste timestamped script]
```

Send this prompt in Claude Code with the Higgsfield MCP skill active.
Claude Code will generate one image per timestamp automatically.

Download images with timestamp-based filenames:
```
Ask Claude Code: "Download all generated images locally with filenames
matching their timestamps (e.g. 0_00.jpg, 0_07.jpg, 0_15.jpg)"
```

**Alternative to Higgsfield:** Midjourney (better quality, manual process)
or DALL-E via API (automatable, moderate quality).

### Step 6 — Video assembly
Import to any video editor (DaVinci Resolve free, CapCut, Premiere).

Assembly process:
1. Import voiceover as audio track
2. Import images in timestamp order
3. Place each image on timeline at its timestamp
4. Extend each image until the next timestamp begins
5. Add Ken Burns (slow zoom) effect to each image to avoid static feel
6. Add lower thirds: site URL, presenter name
7. Add intro (3 seconds): channel logo, "Career Path USA"
8. Add outro (5 seconds): subscribe CTA + link to site

Total editing time: 10-15 minutes once template is set up.

Export: 1920x1080 MP4, H.264, for standard YouTube.
For Shorts: 1080x1920 (portrait) from the same content, re-cropped.

### Step 7 — Upload and optimisation
YouTube upload checklist:
- Title: exact match to target query + year ("How Long Does It Take to
  Become a Vet Tech in 2026")
- Description: first 150 chars must include target keyword and site URL.
  Full description includes timestamps, related queries, site link.
- Tags: target keyword + variations + site niche
- Thumbnail: presenter image or data graphic with large readable text
- End screen: link to affiliate site, subscribe button
- Cards: link to affiliate site at key moments
- Chapters: add timestamp chapters matching the script sections

Description template:
```
How long does it take to become a vet tech? In this video we cover typical
program lengths, accelerated options, and what affects how long it takes
in your state. Full program comparison: https://vettechnicians.org

CHAPTERS:
0:00 How long does vet tech training take?
0:45 Certificate vs associate degree programs
1:30 State licensing requirements
2:15 Accelerated program options
3:00 Next steps

Career Path USA helps working adults navigate career training options.
Visit us at https://vettechnicians.org for a full comparison of programs
in your state.
```

---

## Orchestrator integration

### Automated pipeline (target state)

```python
# Orchestrator job: video_script
# Triggered when: SerpAPI detects video carousel for target keyword
# Model: Sonnet

# Input: keyword, domain, site_data
# Output: timestamped script saved to ~/videos/scripts/[domain]/[keyword].txt

# Orchestrator job: video_queue
# When script exists: add to Higgsfield image generation queue
# Human step required: voiceover recording or Fiverr commission
# Human step required: video editing and upload
```

Fully automated steps (orchestrator handles):
- Query identification (SerpAPI scan)
- Script generation (Claude API)
- Higgsfield image generation (Claude Code + MCP)
- Image downloading and renaming
- YouTube metadata generation (title, description, tags)

Human steps required:
- Voiceover recording or commissioning
- Video editing (until we build an automated editing pipeline)
- YouTube upload (or automate via YouTube Data API)

### YouTube Data API automation (phase 2)
Once a video is edited and exported, the orchestrator can upload it
automatically via YouTube Data API:
- Authenticate with the channel's Google account
- Upload MP4 file
- Set title, description, tags, thumbnail from generated metadata
- Schedule publication time

This requires the channel Google account to be verified and API access
granted. Add to the Telegram verification loop.

---

## Video topic queue — starter list by niche

### Healthcare (Tier 1 sites)
- "How long does it take to become a vet tech?"
- "Vet tech salary by state 2026"
- "Vet tech vs vet assistant: what's the difference?"
- "How to become a medical assistant with no experience"
- "Sterile processing technician salary 2026"
- "Is medical assisting a good career?"
- "How long does radiology tech school take?"
- "Pharmacy technician certification: which one is best?"

### Trades (Tier 2 sites)
- "How long does electrician school take?"
- "Electrician apprenticeship vs trade school"
- "Auto mechanic salary 2026"
- "Plumber vs electrician: which pays more?"
- "How to become a welder with no experience"

### Format that works best for this niche
- "Is X a good career?" — high volume, opinion format
- "X salary in [state]" — data-driven, state-specific
- "How to become X" — step-by-step, highly searched
- "X vs Y" — comparison format, strong click-through
- "X certification: everything you need to know" — comprehensive, long-form

---

## Tools and costs

| Tool | Purpose | Cost |
|------|---------|------|
| Claude Sonnet | Script generation | ~$0.05/script |
| ElevenLabs | AI voiceover | $5-22/month |
| Turboscribe | Transcription with timestamps | Free (3/day) |
| Higgsfield | Image/video generation | Free tier available |
| DaVinci Resolve | Video editing | Free |
| YouTube Data API | Automated upload | Free |
| Fiverr voice actors | Human voiceover | $10-30/video |

Target cost per video: $0.50-2.00 (AI voice) or $15-35 (human voice)

---

## Quality standards

Every video must:
- Answer the target query within the first 15 seconds
- Include at least one specific data point (BLS salary, program length)
- Reference the affiliate site by name in audio and description
- Have a clean thumbnail readable at small size
- Be at least 90 seconds (Shorts) or 4 minutes (standard) for algorithmic
  distribution
- Include closed captions (YouTube auto-generates, review for accuracy)

---

## Related skills
- Skill 06 — E-E-A-T (video builds author presence signal)
- Skill 07 — School listings (video content references program data)
- Skill 05 — Orchestrator operations (video queue management)
