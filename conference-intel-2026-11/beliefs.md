# Belief ledger: what the talks did to what we thought

Adrian asked for our ideas to be challenged. Each row is a position this
library held on 2026-11-18, what the conference evidence says, and a verdict:
**stands**, **sharpened**, **weakened** or **wrong**. Grades are from
`SKILL.md`. Where a verdict needs a decision rather than an edit, it says so.

## Wrong or materially weakened

### 1. "An AI-avatar YouTube channel is how we get into AI Overviews" (CLAUDE.md, Skill 22, Skill 08)

**Weakened, and the avatar part is close to wrong.**

- Stewart Vickers built the thing we are building: about 170 videos since July,
  up to 15 a day. Most sit at 19 to 27 views, about 10% take off, best example
  1,400. His scrape of AI-avatar channels found very few successes and many
  that removed their avatars. The note-taker's own standing measurement is that
  avatar video earned zero AI citations. Grade C, but it is the only direct
  evidence in the set and it points one way.
- YouTube as a citation source is an **AI Overviews** fact, not an AI fact.
  Moeller: video and social were 25 of 39 AIO citations and 1 of 38 in ChatGPT.
  McDowell: YouTube in about 99% of AIO answers in his set, far lower in
  ChatGPT.
- YouTube is not cited on every kind of query. Vickers found it cited for
  roofing, welding, HVAC and how-to, and not for local, legal, accounting or
  dental. Surfer: only 8.9% of a niche's core sources come from the global top
  20 domains, so do not assume.
- Our own figure (YouTube 11 of 98 recorded AIO citations) is real and still
  the best local evidence. It is a reason to make video for the queries where
  that happens, not a reason to make video.

**What changes:** pre-check each query, switch format to screen recording with
a voice and seconds of avatar, treat the description as the citable page. See
`youtube-for-ai-overviews/`.

### 2. "Our prompt battery and 0-of-98 tell us where we stand" (CLAUDE.md, grow-search-visibility)

**The method was right and the power was wrong.**

- Two runs of the same prompt share 40% of brands. 4% of brands appear in all
  of 20 runs. Overlap with the same prompt 90 days later is 28% (Surfer, about
  50M answers, grade A).
- Fewer than 1% of repeated runs return the same brand list (12 prompts, 60 to
  100 runs each, attributed to Fishkin via Search Engine Journal, not read at
  source).
- API answers are not what users see: 29 to 42% of an API answer's top-3 brands
  reach the chat interface's top 3, against a 49 to 54% ceiling for the
  interface against itself. `aio_citations.py` reads DataForSEO. That is an API.
- At 100 answers per prompt the margin is plus or minus 10 points. Showing a
  10-point move needs about 400 before and 400 after (Kiekbusch, arithmetic
  checked).

"0 of 98 citations are ours" survives as a direction, because zero is hard to
get by chance across 98. Anything finer than that, including any before and
after, does not. See `ai-answer-measurement/`.

### 3. "Use the lowest DR in the top 5 as the bar to clear" (seo-strategist rules)

**Weakened.** We already called it a heuristic. It is a worse one than we said.

- DR correlates with being cited at about zero: reported as -0.05 over 5
  billion citations (attribution garbled) and -0.01 for Common Crawl PageRank
  in Surfer's data.
- DR is cheap to fake. Three separate speakers described how, one with a
  Fiverr price.
- Takas's 30 markets (grade A, recomputed): brand search volume against
  page-one position correlates at +0.06. Thirteen of 30 number-one results are
  brands almost nobody searches for. Ten sites hold 41% of all page-one slots.

**Replacement:** the Door Audit. Inclusion rate across 50 target queries, and
the ten or so gatekeeper sites that hold half the page. See
`ai-answer-measurement/` and `link-and-domain-vetting/`.

### 4. "We have no clients, so the agency skills are shelved" (CLAUDE.md)

**Out of date.** Lisclare, Crecera, the freight kit and LoadLander are live
work. `client-value-reporting/` and `agency-economics/` are written for use.
The refusal of "hide what's bad" stands, and the reporting talk agrees with it:
never let a client see a bad number cold, which is the opposite of hiding it.

### 5. "ChatGPT and Copilot read Bing, so Bing is the substrate" (bing-and-non-google-search)

**Half right.** Keep the Bing work; stop calling it the substrate.

- The only number offered is that about 50% of brands ChatGPT recommends also
  rank in the Bing top 20, with no base (Moeller, grade D).
- OpenAI runs its own crawler for search (OAI-SearchBot) and speakers expect it
  to lean on Bing less. Claude's search is widely reported to run on Brave.
  Agent-facing search products (Exa, Tavily, Parallel) are a third family.
- Under all of them sits a layer we had not considered: Common Crawl, which
  feeds training, and the CDN edge, which decides who gets in at all.
- New and free: Bing Webmaster Tools has an AI Performance report (preview
  since February 2026) showing citation counts and the searches the AI runs
  before answering. That is first-party fan-out data. Nobody mentioned
  IndexNow.

## Sharpened

### 6. Information gain

**Stands, with three refinements.**

- A fact only you state is "your best content and your weakest proof"
  (Niechciał). Engines trust what independent sources confirm on specifics. So
  a crossed-source figure needs one outside source to repeat it before it does
  its work. Information gain plus corroboration, not information gain alone.
- Fully unique articles did worse in Rank Up's own experience. The instruction
  is "distribute your unique knowledge" into pages that also cover the basics.
  Four to seven kinds of unique material per page was the sweet spot (vendor
  study, grade B, no link controls).
- The unique material that correlated with holding a top-3 place was first-hand:
  own experience in the intro (5.5x), own measurement (4.4x), customer proof on
  alternatives and pricing pages (3.6x), a test shown in a best-of list (2.4x),
  screenshots (2.4x). Length, FAQ blocks, fresh dates: no correlation.

The counter-evidence deserves stating. A $14 AI-written site with invented
authors was cited by ChatGPT within days and above Wired on some prompts
(Kiekbusch, by his own account not a scientific test, and it broke FTC rules).
Thin and fabricated can win for a while on the weakest engine. That is Mount AI
again, on a faster clock.

### 7. Listicles

**Stands and gets numbers.** A third-party list that is cited raises the chance
a brand on it is named from 57% to 73%. Slot matters: 52% at number one, 32% at
five, 13% from ten down. Our own lists are about 11% of citations and
third-party lists about 23%.

**Decided, 2026-11-18.** `listicle-agent` used to say never place our brand
above where it honestly sits. Surfer's data says a publisher that lists itself
first on its own list is named 38% of the time against 26%. Adrian's ruling: we
or a client may be listed first on a list we publish. The rest of the method is
unchanged: the other brands are the real consensus, competitor facts are true,
nothing is invented, and disclosure rules apply.

### 8. Measurement against a control

**Stands.** The conference's best method talk (Takas) is our rule with a
decision threshold added: lift of 5 points over the control funds five more,
under 2 points stops, in between extends once. Adopt the threshold.

### 9. Schema, entity markup, Wikidata

**Stands.** Senuto found no detectable citation effect from schema, author
boxes, question headings, lists and tables or domain strength (n=492). Surfer
found +3.7 points with JSON-LD and calls it a marker of maintained sites.
Knowledge panel work was asserted by three speakers and measured by none; a
Knowledge Graph resultScore moving from 1 to 19 is not a ranking measure.
Our skill's line, "no measured ranking or citation effect", is the accurate one.

### 10. llms.txt

**Stands.** "Close to zero, sometimes negative" (Surfer). Shopify ships agent
files by default on 99% of stores, so they are table stakes where they exist
and not an edge.

### 11. Scaled template pages are a risk

**Stands, from a new direction.** Common Crawl's lead says labs deduplicate and
filter before training, so thin template copy disappears at that stage whatever
Google does. Fourteen of 17 new articles earned no citation at all (McDowell).
David Quaid's "minimum viable content" (50-word pages for 2,000 keywords, see
what ranks) is the direct opposite. It is anecdote from one consultant, and the
part worth keeping is his allocation rule: put writing time only into pages
that already show buyer intent in Search Console.

## Stands, noted

- **Exact-match anchors.** Practitioners on the testing panel still use one or
  two, sparingly, on a page sitting around position five, after a brand-heavy
  base. Adrian's rule against them is his decision and no evidence here
  overturns it.
- **Dead-domain redirects "sometimes work".** Confirmed as the honest summary.
  Floate claims 12 to 15% success for expired against 90%+ for aged, with no
  base. One useful mechanical rule from Kyle Roof: redirect to a new slug,
  because the same slug carried a problem back after about three months.
- **Links are bought on our terms, not a vendor's.** Every link seller in the
  set told the room to stop trusting DR. Agreed, and they are describing their
  own inventory.
- **Official APIs only for GBP.** Leo's bought reviews killed some of his own
  listings. Joy Hawkins's client rose on bought reviews and fell when they were
  deleted.

## Unevidenced either way: run our own test

- **Markdown twins (Skill 19).** Recommended by two speakers, measured by none.
  `twin_performance.py` is the only evidence that will exist. Keep running it.
- **English versions of Spanish sites.** A claim that ChatGPT searches in
  English even for non-English prompts, and a vendor test showing +122% ChatGPT
  citations after adding an English folder. Grade D. It bears on the `/es/`
  pages and the `escuelas*` sites and is cheap to test on one.
- **"Good SEO is good GEO."** Contested inside the set. McDowell's data says
  rankings rose without AI mentions rising and engines move independently.
  Niechciał's one client says both rose together. Report per engine and stop
  assuming either.
- **Claude watermarks text.** Raised three times, verified by nobody. No change
  to the DeepSeek-then-humanizer route.
