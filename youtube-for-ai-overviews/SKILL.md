---
name: youtube-for-ai-overviews
description: Video made to be cited in Google AI Overviews, and why the avatar-led version does not work. Use before producing, scripting or scheduling any careerspy or client video, and before quoting YouTube as an AI channel. Covers the per-query pre-check, the format that replaces the avatar, the title and description template that is the actual citable surface, captions and chapters, a fail-closed QA list, unit costs and the upload quota, the scouting rules for finding what works, and what is refused. Supersedes the strategic section of Skill 08; production mechanics there still apply.
---

# YouTube for AI Overviews

CLAUDE.md calls YouTube being our most-cited AIO domain (11 of 98) "the
strongest argument yet for the careerspy channel". The argument for YouTube
holds. The argument for the channel as we planned it, avatar presenters at
volume, did not survive this conference.

## What we now know

**Avatar video mostly fails.** Stewart Vickers ran the experiment: about 170
videos since July 2026, at peak 15 a day. Most have 19 to 27 views. About 10%
take off. The best example he showed had 1,400. He scraped AI-avatar channels
and found very few that succeeded and many that had removed their avatars. The
people who compiled the notes had separately measured avatar video earning zero
AI citations, and say his channel data agrees.

**It is an AI Overviews channel, not an AI channel.**

| measure | AI Overviews | ChatGPT |
|---|---|---|
| Video and social among citations (Moeller, one contest query) | 25 of 39 | 1 of 38 |
| YouTube linked in answers (McDowell, 222 prompts, SE Asia) | about 99% | much lower |

**It depends on the query.** Vickers pulled thousands of queries and found
YouTube in the AI Overview for roofing, welding, HVAC and how-to, and absent
for local "plumber in [town]", legal, accounting and dental. No counts, so
direction only, but the trades on that list are our niches. Surfer's larger
dataset says only 8.9% of any niche's core sources come from the global top 20
domains. Check; do not assume.

**His one success is weak evidence.** A video on a term he invented the night
before appeared in a Google AI answer two hours later. One screenshot, no
competing source, and mostly screen recording rather than avatar.

## Rule 1: pre-check every query

Only make a video where the AI Overview for that query already cites YouTube.
His reading is that if YouTube is not there now, a new video probably will not
put it there.

We can do this for pennies. `aio_citations.py` already records cited domains
per query. The queue for careerspy is the set of queries where a YouTube URL
is among the citations and our page is not. That replaces the starter topic
list in Skill 08 and the "video carousel" trigger.

## Rule 2: the format

Screen recording and B-roll under a voice, with the presenter on screen for
seconds.

- Open on the voice over a screen share or footage. Watch time is decided in
  the first minute and an avatar face loses it.
- **Every claim gets a receipt.** A line that cannot be shown on a real page
  is rewritten or cut. For us the receipts are the pages we already hold: the
  BLS table, the JRCERT listing, the College Navigator page, the state board.
- The avatar, if used at all, is rendered only for the seconds it appears.
  That is also the cheap way: 720p HeyGen at 0.29 credits a second.
- A real voice is an asset here, not a problem. Skill 08 already says to lean
  into the Belfast accent rather than neutralise it.

This is good news for the moat. A video that films our crossed data on screen
is a thing a competitor cannot generate from a prompt.

## Rule 3: the description is the page

His phrase is that the description is "the part Google actually reads".

| element | rule |
|---|---|
| Title | The search phrase word for word, then the year or method |
| First line | The answer in one or two sentences, every entity named before any pronoun |
| TL;DR and steps | One definition per line; then Step 1, Step 2, each a sentence that stands alone |
| Chapters | One per step, so there is a timestamp to cite. Kiekbusch: word the timestamps as the target prompts |
| FAQ | Three or four questions phrased as people type them into an assistant |
| Captions | Upload your own track. Auto-captions mangle names, and a mangled name is not a mention |

In the script: title written first, the first spoken sentence is the answer,
and the claims, names and order mirror the answer Google already gives.
Headline answer by two minutes, strongest proof before three. He measured his
own speech at 2.8 words a second for timing.

The same rules as `answer-ready-pages`, on a different surface.

## Rule 4: checks that fail closed

His pipeline refuses to upload unless all pass, and the upload step re-runs
them. Worth copying whole into ours:

- **Picture**: no black or frozen frames; duration matches the script; text
  cards under a quarter of runtime.
- **Sound**: loudness normalised to -14 LUFS, peaks capped.
- **Words**: transcribe the final audio and check it against a pronunciation
  list and a blocklist.
- **Frames**: sample frames to a vision model for CAPTCHAs, blank pages,
  visible IPs and anything brand-unsafe.
- **Receipts**: too few real pages on screen is a hard fail.

`agent-resilience` already requires a run summary. This is its checklist for
video.

## Costs and limits

- His unit costs: avatar lip-sync about $3.50 a video when limited to seconds;
  generated B-roll $0.12 a second on one model and cheaper on another; cloned
  voice pennies. His all-in figure moved between $4 and $12 on stage, so treat
  it as unresolved.
- **Upload quota**: about 1,600 of the 10,000 daily YouTube Data API units per
  upload, so roughly six uploads a day per project. That is a ceiling worth
  knowing before planning volume.
- Our standing blocker is unchanged: careerspy uploads die weekly on
  `invalid_grant` until the OAuth consent screen is published out of Testing.
- **careerspy.org refuses training crawlers** (GPTBot, ClaudeBot, Meta) while
  serving search and assistant fetchers, per verified-bot analytics on
  2026-11-18. It can be cited live; it is kept out of training. See
  `ai-crawl-access`.

## Finding what works

Sarvesh Srivastava's scouting rules are for X but the arithmetic transfers to
any channel, including ours:

- Keep a watchlist of 60 to 70 channels, in and outside the niche.
- For each, take the median views of its last 30 videos. A video at five times
  its own channel's median is worth studying. Rank by that multiple, never by
  raw views.
- For each winner, name the mechanism of the hook and record it as a reusable
  pattern. Reuse the structure; never the wording.
- For our own uploads, compare each against our own 21-day median, ignore
  anything under 24 hours old, and flag anything over three times.
- "If nothing qualifies, say so. Don't lower the bar."

His rule for the writer is ours too: use only real facts and results supplied;
if one is missing, ask; never invent a number.

## Do, in order

1. Fix the OAuth expiry, and decide whether careerspy.org admits training
   crawlers.
2. Build the queue from `aio_citations.py`: queries where YouTube is cited and
   we are not.
3. Make ten in the new format on one niche. Not a hundred.
4. Measure: is the video cited in the AI Overview for its query, across
   repeated runs (`ai-answer-measurement`), against ten comparable queries left
   alone.
5. Scale only what the measurement supports.

## Refused or not copied

- **Buying aged channels and paying micro-workers for watch time** (Leo).
  Fake engagement.
- **Presenting an avatar as a real named person without the synthetic-media
  flag.** Vickers sets the flag on upload. So do we. Nobody's likeness or name
  without consent.
- **Filming pages through a residential proxy so they "see a person"**. If a
  site does not want to be filmed by a server, use a source that does not mind,
  which for government data is all of them.
- **Syndicating each video to hundreds of podcast sites with paid indexing.**
  One transcript page on our own site is the useful part.
- **Running the pipeline on consumer subscriptions with the API key left
  empty** to avoid API rates. Whether that is within the provider's terms was
  not checked by the speaker, and our spend discipline requires every call
  path to be logged.

## What this skill will not claim

That the new format earns citations on contested queries. Nobody has shown it.
It is the better bet on the available evidence, and step 4 is how we find out.
