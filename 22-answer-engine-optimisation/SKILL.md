---
name: answer-engine-optimisation
description: Get cited by AI assistants (ChatGPT, Google AI Overviews, Perplexity, Copilot) rather than merely ranked. Use for AEO/GEO work: fan-out query research, brand gap analysis, citation-worthy content structure, third-party mentions, YouTube as a citation surface, AI crawler access, and measuring AI visibility when the platforms hide the data. Read alongside 11 (content style), 15 (technical SEO) and grow-search-visibility, whose rules override anything here.
---

# Answer Engine Optimisation

Ranking and being cited are different outcomes. This skill is about the second.

Sources: an Ahrefs AEO course transcript (Aug 2026) and Lily Ray's analysis of
evolving ChatGPT fan-out behaviour. **They disagree in two important places**,
and where they do, the newer fan-out research wins — it is measuring what
ChatGPT does now rather than what worked last year. Both are third-party
research, not our measurement; every figure below is attributed, and none of it
is a promise.

## Why this matters to us specifically

Our own numbers, measured 2026-08-18, are the argument:

- 8 of 8 sampled queries return an AI Overview.
- **0 of 98 recorded AIO citations are ours.** They go to .edu institutions,
  JRCERT, and YouTube.
- **YouTube is the single most-cited domain, 11 of 98.**

The traffic is being intercepted, not extinguished. See
[../11-content-style.md] for how anything we write must read, and the CTR
baseline in CLAUDE.md before judging whether a page is underperforming.

## 1. How AI search actually works

One prompt becomes many searches. "Plan me a five-day trip to Japan" fans out
into "best neighbourhoods to stay in Tokyo", "November weather in Kyoto", "is
the Japan Rail Pass worth it", run in parallel and synthesised. ChatGPT's deep
research mode was reported running 420 searches for one prompt about a phone
case.

**What changed in 2026** (Lily Ray, fan-out analysis):

| | before | after |
|---|---|---|
| prompts resolved by a single query | 94.0% | 43.5% |
| fan-out queries per prompt | 2.17 | 7.61 |
| sources retrieved per prompt | ~12 | ~24 |
| unique domains **cited** per response | 19 | **15** |
| `site:` operator used | 0.3% | 23% (64% by API) |

Read those last two rows together, because they are the whole point:
**retrieval went up and citation went down.** Only **3.1% of retrieved pages
become citations**. Being findable is now cheap; being chosen is not.

The number that should change your behaviour: **brands named in the fan-out
query were cited 68.9% of the time, against 2.1% for pages that were merely
retrieved.** Getting the engine to *name your brand when it constructs its own
sub-query* is worth roughly thirty times more than being a page it happens to
fetch. That is an entity problem, not a content problem.

**Do not chase individual fan-out queries.** Lily Ray is explicit: "don't play
whack-a-mole with trying to target individual fan-out queries." They are
generated per prompt and vary between runs. This is also the same conclusion
`grow-search-visibility` reaches from the other direction when it rejects
near-duplicate query permutations — and the same conclusion our own portfolio
reached, where 72% of traffic sits on the three worst-monetising sites.

**Three things raise citation probability** (Ahrefs):

1. **Consensus** — the same claim about you in many places.
2. **Freshness** — cited content averages 25.7% fresher than what ranks.
3. **Authority** — 76% of AI Overview citations are pages already in Google's
   top 10. Traditional SEO is the floor, not an alternative.

## 2. Brand gap analysis

Measure where you should appear against where you do. Three gaps worth
separating:

- **Missed citation** — the answer mentions your brand but does not link you.
- **Competitor gap** — queries where a rival is named and you are not.
- **Topic gap** — a topic the engine associates with someone else.

The video does this in Ahrefs Brand Radar. We do not have Ahrefs. `aio_citations.py`
already samples AI Overviews for our own queries and records who is cited;
bring it up to the measurement standard in section 6 rather than buying a tool.

## 3. Prompt research, and the filter that matters

People prompt, they do not type keywords, but seed-plus-modifier research still
works. Ask a model for seeds and modifiers, expand them in a keyword tool, then
run every candidate through one extra filter:

**Can an AI Overview fully satisfy this searcher?** If yes, the click is gone
and ranking for it is a trap. Target it for a *mention inside the answer*
instead, and never count it as expected traffic.

- AI Overviews appear on ~21% of keywords, but ~58% of question queries.
- 99.9% of AIO-triggering keywords are informational in intent.

Note how this cuts against a portfolio of state and city pages built from a
shared template: informational, question-shaped, and exactly the population
that gets intercepted.

## 4. Getting cited

### On your own site

- **Length does not matter.** Across 174,000 pages cited in AI Overviews the
  correlation between word count and citation is ~0; over half are under 1,000
  words. Stop writing 3,000-word pages for this reason.
- **Freshness matters a lot.** 89.7% of ChatGPT's top-cited pages were updated
  in 2025; **76% within the last 30 days.**
- **Format — and this is where the two sources disagree.** The Ahrefs figure is
  that 43.8% of ChatGPT-cited pages are lists, best-X, comparisons and reviews.
  The newer fan-out data shows **product pages at 16.39% of retrievals,
  displacing listicles**, which Lily Ray notes are "the formats most heavily
  spammed for GEO".

  **Our reading: build the canonical page for the thing, not another roundup.**
  A listicle is a fine format when the consensus in it is real — that is the
  standing rule in `listicle-agent/`, and it stands — but a roundup is now the
  option to justify, not the default. The spam signal is doing to listicles
  what it did to thin state pages.

Four structural rules, all cheap:

1. **BLUF — bottom line up front.** Answer in the first sentence of each
   section. Beginnings and endings are weighted more heavily than middles by
   readers and models alike.
2. **Atomic sections.** The engine chunks your page and you do not control
   where the cuts fall, so every section must survive being read alone. (We
   learned this the hard way from the other side: our own translation splitter
   cut a table in half and the model closed it.)
3. **Entity-rich writing.** Not "this tool helps with SEO" but "Ahrefs Keywords
   Explorer finds keywords with low difficulty and high traffic potential".
   Name the entity, state the relationship.
4. **Simple declarative sentences.** One idea each, subject-verb-object. If a
   sentence needs two reads, it is too complex. This is Skill 11's grade-7
   rule arriving from a different direction.

### Off your own site — the highest-leverage work

In a study of 75,000 brands, **branded web mentions correlate with AI Overview
visibility more strongly than backlinks, domain rating or referring domains**.
The single best move is getting named on other people's pages.

- **Tier 1, third-party editorial** — trade publications, review sites,
  authoritative comparison posts. Hardest to earn, most cited.
- **Tier 2, user-generated** — Reddit is among ChatGPT's most cited sources and
  a foundational training source. Answer questions you can genuinely answer.
- **Tier 3, your own properties** — YouTube, podcast, LinkedIn. All crawlable,
  all potential sources.

**Compliance, non-negotiable and unchanged:** any compensated placement carries
`rel="sponsored"` or `rel="nofollow"`. Earned editorial coverage is the only
kind that moves rankings and the only kind worth chasing. Never fabricate a
mention, a review, an author or a statistic.

### Buying listicle placements: two questions, two answers

FatJoe and linksthatrank.com both sell placement in listicles. Adrian raised
them, and they need separating into the ranking question and the citation
question, because the answers differ.

**For rankings, it is settled and not in our favour.** A paid link that passes
ranking signal violates Google's link spam policy; a paid link marked
`rel="sponsored"` passes no ranking signal. So the ranking value of buying one
is either zero or a policy violation. There is no third option, and CLAUDE.md
already closed this: compensated placements carry `sponsored` or `nofollow`,
and earned editorial coverage is the only kind worth chasing.

**For AI citation the mechanism is genuinely different**, and it is worth being
honest about that rather than waving the compliance rule at it. A model reading
a page reads the text; it does not weigh `rel` attributes. So a properly
disclosed sponsored mention could still contribute to consensus and to the
brand being named — legitimately, with no policy problem at all.

**And it is still the wrong buy.** The reason is in this skill's own data: the
fan-out research shows product pages *displacing* listicles precisely because
listicles are "the formats most heavily spammed for GEO". Bought placements are
by construction the spammiest tail of that supply. Buying into a format the
engines are actively discounting is paying for a depreciating asset in the one
channel we care about, and the spend competes with work that is not
depreciating.

The check to apply to any paid placement offer:

1. Will the publisher apply `rel="sponsored"`? If the vendor's value
   proposition depends on *not* disclosing, that answers the question.
2. Would the page exist, and say the same thing, if nobody had paid? If not,
   it is not consensus — it is the appearance of consensus, and the method in
   `listicle-agent/` works only because the consensus in it is real.
3. Is the format one the engines are rewarding or discounting right now?

### YouTube deserves its own line

- Most-cited domain in Google's AI Overviews.
- **0.737 correlation between YouTube mentions and ChatGPT visibility** — the
  strongest single factor in the Ahrefs study.
- GPT-4 was trained on over a million hours of YouTube transcripts.

Our own data says the same thing independently: YouTube is 11 of the 98 AIO
citations we recorded, more than any other domain. This is the strongest
argument that exists for the careerspy channel.

**This is the careerspy strategy, and it is the one channel where two
independent sources and our own measurement all point the same way.** Skill 08
covers video production; `CAREERSPY.md` carries the channel's own state. What
this skill adds is the topic-selection rule below — the videos worth making for
citation are not the videos worth making for reach.

Chase **search hits, not viral hits**. A viral video spikes and dies; a search
hit earns from YouTube and Google search every month, and evergreen search
videos are what gets cited. Find topics by filtering a competitor's
`youtube.com/watch` subfolder for top-three organic rankings. Then: keyword in
the title and the first lines of the description, timestamps for chapters, and
**say the keyword out loud** — the audio is transcribed and read.

## 5. The technical check: do not block the crawlers

5.9% of 140 million sites block GPTBot, mostly by accident — inherited
robots.txt templates, or Cloudflare's "manage AI bot traffic with robots.txt"
feature, **which is on by default**.

Check `yourdomain.com/robots.txt` for `Disallow` against `GPTBot`,
`OAI-SearchBot`, `ClaudeBot`, `Google-Extended`, `PerplexityBot`. We already run
`cf_ai_control.py --probe` weekly across every Cloudflare zone for exactly this
reason; read its output before concluding a site has a content problem.

Keep search crawling and model-training controls conceptually separate: you can
allow the first and refuse the second.

## 6. Measurement, when the platform hides the data

Three signals, none sufficient alone:

1. **AI referral traffic.** Undercounted by design — ChatGPT source links pass
   referrer, in-content links on paid accounts do not. Directional only. Never
   quote it as a precise figure.
2. **AI bot activity on your pages.** If a citation bot keeps hitting one URL,
   that URL is probably being used as a source. We already collect this via
   `ai_crawler_demand.py`, daily, because Cloudflare retains only 8 days.
3. **Self-reported attribution.** Add "how did you hear about us?" to any
   sign-up or checkout. Ahrefs report AI search at 0.5% of visits but 12.1% of
   sign-ups — a 23× higher conversion rate than organic, invisible without
   asking.

**Our measurement rules override any of the above.** Use a fixed, versioned
prompt battery. Record engine, date, locale, login state, model and capture
method. Repeat samples, because outputs vary. Compare query by query, never as
a blended average. Prefer staged rollouts and matched page groups to
before-and-after. This is the control-group lesson written down: a +707%
that turned out to be seasonality is what happens without it.

## 7. A known failure mode to watch for

ChatGPT constructs `site:` queries against **incorrect domains** — Malte
Landwehr found it searching parked domains like `census.com` instead of
`getcensus.com`. Two consequences:

- A competitor or squatter on the near-miss domain can absorb your citations.
- If your brand name has an obvious near-miss domain you do not own, that is a
  real risk worth checking rather than a theoretical one.

## Order of work

1. **Technical check first.** If the crawler is blocked, nothing else counts.
2. **Set up measurement on day one**, including the attribution question.
3. **Take the largest gap from the brand analysis** and match it to the type of
   fix: a topic gap is a content problem; competitors being recommended and not
   you is a mentions problem; formats you do not produce is usually video.
4. **Refresh what already ranked and slipped** — freshness is the cheapest win
   available, and 76% of ChatGPT's top-cited pages were touched within 30 days.

## What this skill will not do

- Guarantee ranking, indexing, citation, traffic or revenue. Every projection
  reads as a projection.
- Invent authors, credentials, tests, reviews, customers, statistics or
  affiliations.
- Manufacture consensus. The listicle method works *because* the consensus in
  it is real; forcing our brand above where it honestly sits breaks the method
  and the trust at once.
- Quote a precise number off weak inputs. High / Medium / Low when the evidence
  is thin, and say which.
