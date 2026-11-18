Agentic Sites — speaker addressed as "Alex" by the MC (surname and company not stated in the transcript)
Source: Granola https://notes.granola.ai/d/d3e9f4f8-eb3b-4af0-8902-ff0ab8de73b1 · recorded 2026-11-09 (2:21 PM GMT+7) · transcript-verified 2026-11-12 Vendor talk? Not evident. No product pitch in the recorded portion. Speaker mentions an engineer "who used to work at Yoast" and a tool called "agentwatch" (garbled) that "was built" for analytics; no company affiliation stated.
Transcript coverage caveat: the recording starts mid-talk (first words are "...add to the concise and data integrity that I was talking about before"). The setup of the experiments (what the sites were, which engine, how many queries) was said before recording began or is on slides. Slides were visible to the room, not to the transcript. Total transcript is about 17k characters. Q&A is complete except it ends mid-answer on the last question.
Thesis (3 bullets max)
Do the old-school SEO safe bets first (speed, static HTML, consistent product/variant/price data across every source); traditional SEO is the highest-impact activity; the new protocols are secondary.
Agent-built sites with zero human-written words can get cited quickly, but thin rephrased content is seen and not cited; add original information.
Do not chase every protocol (MCP, etc.); build for people, keep data consistent in every layer (site, merchant feed, schema), and own the source of truth via digital PR and link building.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Schema.org item-type adoption jumped | "top half" of chart went from 1M to more than 10M sites | Chart of how many item types are adopted on how many sites; data from schema.org's repo; window "between May and the end of August"; year not said; speaker said the repo has not been updated for the last two months | schema.org data, charted by speaker | Spoken over a slide | Clear on numbers; "top half" = upper section of the chart, NOT "top-tier sites" as the summary says. Which item types sit in the top half not stated |
| Shopify attribution | Speaker believes Shopify's enabling of UCP on every storefront drove it | Inference only, no test | Speaker opinion | Spoken | Clear that it is a belief ("I believe"); credits Harley Finkelstein by name |
| UCP-specific types (brand loyalty, logistics) not yet adopted | "that's not moved up" | Same schema.org chart | Speaker | Spoken | Clear; predicts it will move |
| New agent-built test sites got Copilot citations | Qualitative; "loads of Copilot citations" for two topics (garbled: "parental controls and Family Guy") | Synthetic/test answers across several topic sets; count, engine list, period not stated | Speaker | Spoken over slide | Topic names garbled; "Copilot" is clear. Fewest citations on the site that existed before (speaker's guess: it already had the data) |
| Visits on a launched, previously empty agent-built site | From about 114 per day to 11x ("elevenfold"), "instantly" at launch | Search Console data; grey dots = daily visits, lines = average; which site and which metric (clicks vs impressions) not clear; period not stated | Speaker, Search Console | Spoken over chart | "114" and "elevenfold" clear; site name not said |
| Second site relaunch uplift | From "500 odd" to "like 650" per day | Same chart type; site name garbled ("Presch Village"); timing "at the time" of relaunch | Speaker, Search Console | Spoken over chart | Site name garbled; numbers approximate (spoken "500 odd", "like 650") |
| Seen 100% / cited 0% | Site "on 100% of the queries that were tested" but cited "0% of the time" | Test queries (count not stated); engine not stated (context is the Copilot/synthetic answer set, but he never names the engine for this line); thin test articles; gov.uk was used instead and its content restated what his page said | Speaker | Spoken | Percentages clear; engine and sample size NOT stated |
| Zero human words | "not one word on that website was created by me", all by an agent | The 11x site | Speaker | Spoken | Clear. "Created by me" = by the speaker; whether an employee wrote anything is not said |
Asserted mechanisms (no evidence given in the talk)
Price consistency: $100 in one source and $95 in another and the agent "won't know what to do" and skips it; a competitor with one $100 reference vs your two consistent $95 references "may" choose you. Hypothetical, framed with "may".
Merchant-feed hygiene is now an SEO concern because of UCP; paid/feed owner and SEO must work together.
Claude-written prose has a recognizable "even balance" between first and second half of sentences that erodes reader trust. Speaker's own perception, not measured.
Hidden (invisible) watermarks in AI text could hurt SEO long term because engines get more sophisticated and do not forget; the question presumed Claude injects one; the speaker did not verify the premise.
Allowing bots costs little: observed server spikes came from rebuilds and natural research traffic, "not too much damage".
"You're nobody in this learning algorithm", so blocking AI bots only reduces visibility.
Traditional SEO is "the thing that is the best out of everything"; no data given on traditional SEO metrics before/after agentic setup.
WordPress remains the practical CMS for non-technical users; connecting a CMS to a GitHub repo is "way too dangerous" without guardrails.
Hollywood-set analogy (from his engineer): agentic production sites look good from the front and are messy behind; business owners only watch "the film".
NLWeb / schema maps: unclear if they matter (see Q&A).
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Closing task list ("some take a couple of minutes, some an hour"):
Look at traffic for the "UCM source" (WHITE). Speaker says there was a glitch/bug in it in the last week; check GA4 but "don't take that as gospel"; find your own analytics platform or an answer like "agentwatch" did for him. No price given.
E-commerce: shortlist product pages by pattern, optimize the shortlist first (WHITE).
Add "How did you find us?" to forms with AI options (ChatGPT, Claude, an agent). Make "I found you through AI bots" the first option and remove "Please select" so it becomes the default (GREY: default-bias is attribution inflation; flag it in reports).
Populate product data fully: sizes, materials, every variant, in a table, so agents understand each variation (WHITE).
New sites: make them fast; static HTML where possible so no extra resources load (WHITE).
MCP: only if there is a business reason, time, or tokens to let an agent build it (WHITE).
Bots: block only bots that damage you (copyright/IP/server); allow the rest (WHITE).
Images: AI images fine as filler; declare AI origin in caption/alt text (WHITE). Human images where images matter to the business.
Content: human editorial control on agent output; deliberately change some text; add data and original material first, then let the agent follow; a humanizer skill reduces "word salad" but does not replace human input (WHITE).
Seed perception: digital PR and link building (WHITE). Experiment pattern (not a how-to, but what he did): build nearly empty sites with an agent (Claude), launch, watch Copilot citations and Search Console. Hidden watermarking was apparently part of his experiments ("I'm probably just going to leave them and let them go dormant") (GREY: the sites were test/experiment sites; he implies he expects detection later).
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
UCP: protocol that "has a lot of good schema in it"; Shopify enabled it on all storefronts (per speaker). Full expansion never said in the transcript. No price.
schema.org repo: source of adoption chart.
Harley Finkelstein (Shopify): credited with enabling UCP across storefronts.
Copilot: engine where test sites got citations.
Search Console: visits/average chart; GA4: UCM-source check.
"agentwatch" (spelling uncertain): analytics-for-agents tool someone "built" for him.
Claude: speaker's chosen model ("brand choice"); tested Codex; mentions "anti gravity" (Antigravity) and "another couple".
Humanizer-type skill for Claude: reduces word salad.
"M Dash" (garbled; likely a WordPress-to-agentic CMS bridge): speaker said he has not used it.
Astro: not a CMS; content fed by CSV/session uploads; open-source Astro back ends exist, unchecked.
NLWeb and RV Guha: Guha approached "us" about building NLWeb; speaker said of course they would help; mentions Guha reports to the Microsoft CEO. Whether the speaker works at Microsoft is ambiguous in the transcript; do not assert it.
Yoast: former employer of his engineer.
Amazon bot: only named source of bot traffic.
gov.uk: the source Copilot cited instead.
Whova: conference app for questions.
Q&A (question → answer)
Invisible watermark Claude injects; risky if search engines detect AI text? → Use a humanizer plus your own voice, have a human read and deliberately change some lines, put real data in first; skill is only for minimizing word salad.
In a competitive commercial niche, prioritize technical SEO, entity/brand proof, or agent-ready setup? → All, in that order; lock down products and variants; befriend whoever runs the merchant feed (formerly "the paid folk"); consistent price across sources.
Original or AI images? → Mix; AI fine for filler, human where it matters; declare AI in alt text/caption.
Run content through AI detection? → No, and "don't check mine"; his sites would be flagged (the following exchange suggests the others would, too).
First three changes for a new site's AI search visibility? → Make it faster and use static HTML pages; only one change was given.
Crawl budget cannibalization or server spikes from LLM bots? → Spikes from rebuilds; no cannibalization; Amazon bot was the only notable one; cheap traffic.
Moving WordPress to Astro: which CMS? → WordPress; Astro is not a CMS; do not connect a CMS to GitHub for non-technical users; mentions "M Dash" (untested) or a custom back end; vibe-coded sites are bad under the hood.
Which LLM do you build in? → Claude, a brand preference; Codex is good; test everything on day one but wait months.
Impact on traditional SEO metrics? → Traditional SEO is the thing that works best; no metrics given.
Block bots after hitting server limit? → Only damaging ones; do not block all.
Hidden watermarks hurt SEO long term? → Yes, can; engines get cleverer and do not forget.
Entity map / schema map / other protocol that could have impact? → Unsure about schema maps; NLWeb anecdote with RV Guha; answer ends there.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
"Top-tier sites jumped from 1M to 10M+": transcript says the TOP HALF OF A CHART (item types) went from 1M to >10M sites. Not "top-tier sites". Year not stated; schema.org repo had stopped updating two months earlier.
"Shopify credited for enabling UCP": it is the speaker's belief, hedged; he says "I believe".
"Check GA4 for UCM source traffic": transcript says UCM source (probably a garbled UTM/source label; unverified), plus "bug", plus "don't take GA4 as gospel", plus find your own analytics (agentwatch-like).
"One site went from 114 daily visits to 11x immediately": consistent, but the chart is Search Console, site unnamed, and it is one of at least two sites; the second went about 500 to 650.
Summary omits that the "100% seen, 0% cited" engine is never named and no query count is given.
Summary says "Humanizer tools reduce word salad": correct, and added "not a substitute".
"No need to run content through AI detection tools": the speaker said he does NOT, and joked that his content would be flagged. The MC's "no need to detect" line is the MC's, not a recommendation.
"Hidden watermarks may become an SEO risk": speaker said yes it can; also admitted to leaving experiment sites dormant for that reason. The audience question's premise (Claude injects a watermark) was never verified.
"M-Dash potential bridge ... (untested)": speaker said he has not used it; the name is garbled in the transcript.
Summary left out: NLWeb/RV Guha anecdote; he tests tools day one; Amazon bot as the only named crawler; "faster + static HTML" was his only answer to the "first three changes" question.
"Order of priority" answer in the summary is fine; "two consistent sources at $95 can beat one source at $100" is hedged ("may choose you") in the transcript.
Core mantras are accurate. "Merchant fees" in the transcript is a mishearing of merchant feeds.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
"UCP": never expanded in the transcript. Summary and speaker use it as Shopify-linked commerce schema/protocol. Likely Universal Commerce Protocol; confirm against the slide or the source.
"UCM source": probably a garbled utm_source/source label; unverified. Check GA4 for ChatGPT/Copilot referral source labels directly.
"Presch Village": site name garbled.
"parental controls and Family Guy": topic names garbled.
"M Dash": garbled; possibly EmDash (Cloudflare's WordPress alternative). Unverified.
"agentwatch": spelling uncertain; could be a different tool name.
Which engine the 100%/0% test used; number of queries; which site; the period.
Which schema.org item types sit in the "top half"; year of the May-August window.
Speaker identity: "Alex" is the only name; the surname/company are not in the transcript.
How AI Consumes and Trusts Data (host's introduction; the slides are a set of AI-manipulation "tricks") — Alan CladX (French SEO since 1999–2001; CladX; says his group owns 500,000+ websites)
Source: Granola https://notes.granola.ai/d/8560ec77-6301-4563-aecf-b122c24dc6a3 · recorded 2026-11-14 (12:19 GMT+7; Granola shows 2026-11-13 21:19 PST), LLM Mastery 4.0 day (every slide carries the "LLM Mastery · 14–15 November 2026 · Chiang Mai" banner) · transcript-verified 2026-11-16 Resources: 10 slide photos saved to ../resources/alan-cladx/photos/ (all 10 read; bottom banners on several are blocked by heads). He offered his "CC Research Kit" free to attendees through the event team's WhatsApp; not obtained. The note-taker's private notes list two sites: cloaking-seo.com and seo-is-dead.com (not opened). Vendor talk? Partly. He gives tricks and a free tool away; he runs an SEO / reputation business (slide 09's Gemini bio lists "SOS réputation", founded 2016) and the tool is his. Nearly everything is a stunt or a self-run test on one entity, one prompt or one date, with no repeat runs. Presented as manipulation on purpose ("we are here to learn how to manipulate an AI").
The audio is heavily accented and garbled; slide text is used wherever it exists. He rode an inflatable horse costume throughout (visible in photos 02–10). No Q&A; the host broke for lunch.
Thesis (3 bullets max)
AI answers can be steered by whoever controls the sources the model reads: volume of English-language content, raw HTML it sees but people don't, and a few "validated" sources moved into the right country.
Models read source code, not the rendered page, and have no equivalent of Google's cloaking penalties, so 2010-era tricks work again.
People-facing facts are thin and easy to inject or erase: AIs lean on LinkedIn for people, and privacy-removal flows delete entities without notice.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Fictional persona | 1,000+ articles in six months (100 in the first month) about an invented woman; "every AI" now says she exists and is a famous social-media figure | engines, prompts and dates not named; name garbled ("Swinder Lane") | self | spoken | stunt; no runs shown |
| ⭐ GPT stance switch | ChatGPT (USA) on the conflict's cause: pro-Israel (01 Aug 2025 14:44) → pro-Palestine (08 Aug 2025 14:44) → neutral (15 Aug 2025 14:55); spoken: after pushing English pro-Palestinian sources, then pro-Israeli sources | one prompt, one country, three single responses, a year before this talk | self | slide 07 + spoken | one response per date; no repeat runs, so normal answer variance can explain it |
| Gemini stance switch | Gemini switched the same way, a week after each push | none shown | self | spoken | no slide |
| ⭐ LinkedIn injection | after adding a fake job, Gemini's answer to "Who is Alan CladX?" lists among his companies "Google Search Console: co-founded in 2015" and "Google: founded in 1998"; removing the job makes it disappear in 1–2 weeks | his own name | self | slide 09 (screenshot) + spoken | screenshot real; the 1–2 weeks is spoken only |
| Common Crawl size | >10 PiB total archive; latest crawl Oct 2026 = CC-MAIN-2026-43, 2.17B web pages, 371.2 TiB uncompressed, WET 6.0 TiB; spoken "160 terabytes" | Common Crawl's own figures | Common Crawl | slide 03 (some cells blocked) | slide clear; spoken 160 TB does not match the slide |
| CC Research Kit demo | commoncrawl.org: 242 matching URLs in the index, 260 captures | one domain | his tool | slide 04 | demo screen |
| "Link gem" example | text.blogosphere.app found in CC-MAIN-2026-39, oldest capture 2026-09-05 | one site | his tool | slide 06 | demo screen |
| Iframe "training" | 1,000 visitors a day = 1,000 prompts sent a day | arithmetic | none | spoken + slide 02 | not a measurement |
| Public-figure erasure | a head of state (heard as Emmanuel Macron; Putin and Trump also heard) unknown to Gemini France for ~six months after a personal-data removal request | none | self | spoken | audio too garbled to pin the names |
| Hoax sport | a fake sport (heard as "aquaponia"/"aquaponics") repeated by "famous media around the world" during the Paris Olympics | none | self | spoken | not checked |
Asserted mechanisms (no evidence given in the talk)
Training data and pipelines are English-dominant, so English content enters "default AI" first.
AI crawlers read source code; CSS, white-on-white text and visual design are irrelevant to them.
AI engines have no cloaking detection or penalty.
Engines keep a cache of scraped pages and later train on it (garbled).
A prompt sent through a visitor's browser ("chatgpt.com/?q=") "trains" the model; slide 02 calls it "forced memory".
Answers differ by country because each country's validated sources differ; seed a claim from a low-connectivity country (slide 08: Burundi, Chad, Central African Republic, Eritrea, South Sudan), then push those sources into the target country via Reddit and Wikipedia.
AIs read LinkedIn as the main source about people because privacy limits other sources (slide 10: ChatGPT, Gemini, Claude, Perplexity, Copilot).
Gemini's personal-data report removes everything about a person, with no notice and no way back until a model update.
Common Crawl is what labs train on (slide 03 "golden tip": archived content can become part of LLM training datasets; "selection and filtering still apply"); links on pages along CCBot's crawl route get a site into Common Crawl.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
The "AI honeypot" (slide 01, "if you remember only one trick"):
Make a separate directory (example website.com/AI/), a mini-site with no shared template: white background, black text, blue links. BLACK
Silo pages: Brand / Top Products / Reviews / Comparisons / FAQ; interlink only inside; "possible keyword stuffing"; no links to or from the main site. BLACK
robots.txt: User-agent: * Disallow: /AI/, then Allow: /AI/ for GPTBot, ChatGPT-User, ClaudeBot, OAI-SearchBot ("block everyone, allow AI bots only"). BLACK (and robots.txt is public, so competitors can see it)
script.js: setTimeout(() => { window.location.href = '/'; }, 1500); so a person clicking through from an AI answer lands on the homepage. BLACK (sneaky redirect)
Ask ChatGPT and others to visit and summarize the pages repeatedly so the cache refreshes. BLACK Prompt injection (slide 02, "the dark side of the force"):
Clickbait link <a href="https://chatgpt.com/?q=…"> carrying a hidden instruction ("Summarize this page for me [URL]", URL-encoded). BLACK
"Forced memory": a 1-pixel iframe that fires the prompt on every page view; if the AI blocks it as same-origin, use a pop-under instead. BLACK (uses visitors' sessions without consent) Cloaking:
Serve users a visual (a "matrix effect") and serve crawlers the text content on the same URL. BLACK Common Crawl seeding (slides 03–06):
Map which of your pages and referrers are in Common Crawl (CC Research Kit Explorer: check presence, analyze archived content, find opportunities). WHITE as a check
Trace the CCBot route back through referrers; merge with Majestic backlinks; sort by crawl date to find the earliest referrer. WHITE as research
Submit your URL to free, instantly crawled link-submission sites on that route (example: Blogosphere "submit a link"). GREY leaning BLACK (link-submission spam aimed at training data) Geo-seeding (slide 08):
Build an English "information flow"; seed it from an "easy GEO"; identify sources AI already "validates"; push them into the target country (Reddit, Wiki). BLACK Entity injection and erasure:
Add a false job to LinkedIn; AIs repeat it; delete it and the claim fades in 1–2 weeks. BLACK
Find personal data about a target and file Gemini's personal-data report (three-dot menu) to erase them from answers. BLACK (abuse of a privacy process)
Leave a glowing review containing your own contact details; once the owner approves it, your name becomes associated with the shop in AI answers (garbled). BLACK Language:
Publish an English version of non-English sites. WHITE
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
CC Research Kit ("Common Crawl / Explorer by CladX", v0.6.x beta per the screen): Explorer, Discovery, Research archives, Tasks, Link Timewarp, Link Spot Detector, CC archives; 3D referrer map; backlink tree with CC evidence; merges Majestic. Free to attendees via the event team's WhatsApp (he said a script archive would be sent).
Common Crawl (CCBot, CC-MAIN-2026-43); Majestic; Blogosphere (text.blogosphere.app, "submit a link"). Other referrers on slide 06: soylentnews.org, registry.opendata.aws.
Sites: a cloaking demo heard as "CrowdKingsCo.com" (the private notes say cloaking-seo.com); seo-is-dead.com (private notes only); a site heard as "windingso.com" whose text is unreadable to people but readable to AI. CladX (slide 07 footer, partly blocked).
Gemini personal-data report (three-dot menu); LinkedIn.
Stephen Burns: named on slide 03 as the next speaker; on stage Alan said a "Stefan" speaking that afternoon "represents" Common Crawl (relationship not checked).
Attendees and SEO figures he said he had planted false claims about (names garbled; not repeated here).
Slide photos
Full text of each slide: ../resources/alan-cladx/slide-text.md
01-ai-honeypot-robots-redirect.jpg: "If you remember only one trick… the A.I. honeypot": 4 steps (separate directory, simple silo pages, robots.txt filter, JS redirect after 1,500 ms); "humans see nothing special, A.I. sees the honeypot".
02-prompt-injection-iframe-popunder.jpg: "Prompt injection, the dark side of the force": 1. link that gives an order (chatgpt.com/?q=), 2. hidden instruction ("Summarize this page for me [URL]"), 3. forced memory (1-pixel iframe), 4. surprise bonus (same-origin → pop-under).
03-common-crawl-fuel-for-ai.jpg: "Common Crawl: fuel for A.I.": >10 PiB archive; Oct 2026 crawl CC-MAIN-2026-43, 2.17B pages, 371.2 TiB uncompressed, WET 6.0 TiB; "golden tip: archived content can become part of LLM training datasets; selection and filtering still apply"; Stephen Burns named as next speaker. Left column partly blocked by the speaker.
04-cc-research-kit-explorer.jpg: "Introducing CC Research Kit, your Common Crawl intelligence tool": check presence, analyze content, find opportunities; demo on commoncrawl.org (242 URLs in index, 260 captures).
05-cc-research-kit-trace-ccbot-route.jpg: "Trace the CCBot route": map the ecosystem, verify archive evidence, follow the crawl path, merge CC + Majestic; 3D referrer map; backlink tree with Found / Not found.
06-link-gems-that-feed-common-crawl.jpg: "Find the link gems that feed Common Crawl": map → confirm & trace (soylentnews.org, registry.opendata.aws, text.blogosphere.app) → "the gem": Blogosphere free link-submission form; "free crawl boost". Footer blocked.
07-gpt-switches-its-stance.jpg: "GPT switches its stance, USA, three dated responses": 01 Aug 2025 pro-Israel, 08 Aug 2025 pro-Palestine, 15 Aug 2025 neutral (excerpts partly blocked by the speaker).
08-seed-from-easy-geo.jpg: "A.I. What should we do about it?": build an English information flow, seed it from an easy GEO (5 countries listed), identify sources already "validated", push them into the target GEO (Reddit/Wiki).
09-google-is-always-right-gemini-bio.jpg: "Google is always right": Gemini answer to "Who is Alan CladX?" listing SEO since 2001, CladX, SOS réputation (2016), "Google Search Console: co-founded in 2015", H1seo (2004), "Google: founded in 1998", speaker at BlackHat SEO and Campus de l'Innovation Touristique.
10-ais-read-linkedin.jpg: "AIs don't guess who you are. They read LinkedIn": LinkedIn → ChatGPT, Gemini, Claude, Perplexity, Copilot; "it's not just a resume, it's a source, professional data travels"; bottom line partly blocked ("…isn't personal branding… LLM branding").
Q&A (question → answer)
None. The host announced the lunch break.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
The stance test: the slide is ChatGPT in the USA, dated August 2025 (not this year), and ends neutral, not "Gemini flipped to pro-Israel". Spoken: equal sources on both sides → neutral. Gemini was described only in passing.
"cladx.com (noted as cloaking-seo.com)": cladx.com is not in the audio; the cloaking demo is heard as "CrowdKingsCo.com"; cloaking-seo.com and seo-is-dead.com come from the note-taker's private notes.
"Block it in robots.txt… to hide from competitors": robots.txt is public. The slide's actual rules disallow everyone and allow four OpenAI/Anthropic agents.
"Silently sends a prompt to an LLM, training it": "training" is his claim; nothing shown proves a model learned anything.
"Aquaponics as Olympic sport": the audio is garbled ("aquaponia", "acopolis"); given the inflatable horse, the hoax may be a different word (possibly the French joke sport "aquaponey"). Not checked.
"Removed Emmanuel Macron from Gemini France for six months": names in the audio are garbled (Putin, Trump and Macron all heard); treat as unverified.
"Persona injection via LinkedIn: Founder of Google": slide 09 shows Gemini listing Google and Google Search Console among his companies, which is the visible evidence; the summary omits the screenshot.
Omits the Common Crawl tool walk-through (slides 03–06) and the "easy GEO" country list (slide 08).
Omits that the honeypot slide itself says "possible keyword stuffing".
Unclear / needs verification (mis-heard names, numbers you could not pin down)
Speaker surname: "CladX" from slides 09 and the Granola title; first name Alan. No web lookup done.
The persona's name ("Swinder Lane"), the hoax sport, the public figures "erased", the people he says he planted claims about.
Whether the CC Research Kit is public, what it sends home, and its license.
"160 TB" spoken vs 371.2 TiB (one crawl, uncompressed) and >10 PiB (archive) on slide 03.
Whether OpenAI or Google use visitor-triggered ?q= prompts for training or memory at all; not checked this pass.
The relationship of the next speaker to Common Crawl.
Modern Black Hat (2017 techniques reimagined for AI search) — Charles Floate (black-hat SEO; founder of the link marketplace heard as "Presswiz"; runs a paid Skool SEO community)
Source: Granola https://notes.granola.ai/d/148858cc-bb50-4584-a303-b3db16824573 · recorded 2026-11-13 (10:40 GMT+7; Granola shows 2026-11-12 19:40 PST), CMSEO 2026 main stage · transcript-verified 2026-11-16 Resources: no slide photos attached to the Granola note (0 saved). No handout or deck. The slides were shown but are not in hand; every figure below is from the audio only. Vendor talk? ⚠️ Yes. Owns a link marketplace (he says ~$1.5M MRR) and a paid Skool community (the update lab and satellite-site methods are sold inside it). Self-described black hat. Every number is his own or his team's "internal testing"; no base, period or control is given for any of them.
The talk ran over; he skipped the end of the deck ("I've run out of time"). No Q&A on the recording; the host sent questions to the event app.
Thesis (3 bullets max)
The 2016–2017 black-hat toolkit still works and maps one to one onto AI search: parasite pages → third-party citations, PBNs → "satellite sites" for mentions, spinning → scaled AI content, CTR bots → "click bombing".
AI models "can't verify anything, they just corroborate": consensus is the ranking input, so whoever manufactures consensus wins ("match the consensus for 80%, be different for 20%").
Google enforces with post-ranking re-rankers ("twiddlers"); reverse-engineer each update with SERP snapshots and a placebo-controlled comparison.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Link marketplace revenue | ~$1.5M MRR, 2 years old (anniversary Sept 2026) | none | self | spoken | self-reported |
| Skool community launch | $100k MRR in 8 days | none | self | spoken | self-reported |
| Parasite page | a $500 page went to #1 the day it went live (post dated Oct 2026); #1 from a US IP, #6 from a Thai IP on the day | one page; query not named | self | spoken (screenshot on a slide, not photographed) | one anecdote |
| Expired vs aged domains | success rate 12–15% (expired) vs 90%+ (aged) | "our testing"; no count, no definition of success | self | spoken | unbased |
| Link volume | "1,500+ quality links every day" plus parasite pages, hands-off | none | self | spoken | self-reported |
| Click bombing | under 2% of sent clicks touch Google Search; the rest only produce Chrome engagement signals | none | self | spoken | assertion with a number |
| Update lab | ~22,000 SERP snapshots a day since Aug 2026; 8-stage method with placebos | queries, markets, devices not counted | self | spoken | method described, data not shown |
| August 2026 spam update | category pages +4.7 pp, home pages −4.66 pp; no change for UGC, forum or editorial | his update lab | self | spoken | no denominator (share of what?) |
| Spam links in money SERPs | ~50% (Aug) and 44% (Sept) of links classified as spam "after filtering" | his lab; classifier not named | self | spoken | unbased |
| OpenAI news partners | partner outlets 300%+ more likely to be cited in ChatGPT than other news sources (BBC, Guardian, Fox named as comparisons) | "our testing"; no sample | self | spoken | unbased |
| JS-rendered forums | ChatGPT citation rate for JS-rendered forum CMSs "0.64" (unit unclear) vs PHP/HTML; similar gap on Perplexity; no gap on Google AI Overviews | forum sites grouped by CMS; counts not given | self | spoken | number unreadable in audio |
| Google-owned sources | YouTube 24.5% mention share (#1 AI Overview source), a second Google property 8.6% (#5) | "Ahrefs data" (heard as "AHS data") | Ahrefs (vendor) | spoken | source not seen |
| Forums vs AI Overviews | forums hold 41.4% of page-one results but 14.2% of AI Overview citations | his data or Resoneo's; unclear | unclear | spoken | unbased |
| Fake award | "Best SEO Awards": invented awards, judges and winners; #1 in about two days; cost "over $1,000"; site built in 45 minutes; still ranking six months after he revealed it was fake | one case | self | spoken | anecdote; query not shown |
| Skool search | 3,290 search visits → 21 members → $6,408 new MRR at $0 cost | his Skool community | self | spoken | self-reported |
| PDF training-data seeding | 12–18 PDFs per query; 2–3 years ago this "basically guaranteed" entry into ChatGPT models about two generations later | none | self | spoken | unbased |
| Google click history | 13 months (was 18 until ~2 years ago); rescored every 70 days | none | asserted | spoken | no source |
Asserted mechanisms (no evidence given in the talk)
Google "twiddlers" re-rank after the base algorithm. Names given: SiteBoost (generic category hosts survive, branded-first hosts don't), Starburst and Pulsar (consensus matching, relevance feedback), a "Bard filter" deciding AI Overview entry, plus video and image boosts. He credits the twiddler research to a French team heard as "Resino Resin" (likely Resoneo).
Off-niche parasites now fail a niche-match check (casino page on Goodreads fails, on a generic site builder passes); this is why press releases came back.
Chrome engagement data (good, bad, "last longest" clicks) feeds ranking and Discover.
Freshness is a triangulation of date fields; bumping only the schema date is "one vote of four".
Different models prefer different formats: Claude "loves" wiki-style and XML pages.
Google keeps citing its own properties after they are moderated (a deleted Merchant Center feed product still cited a month later); YouTube removals clear faster.
Consensus is "hard-coded" into LLMs; models cannot verify facts.
Buying third-party mentions or AI citations is a link scheme under Google's guidelines ("everybody is a black hat now"). Stated as his reading of the guidelines.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Parasite and citations:
Publish on high-authority third-party hosts; the page needs no link, only to be cited. Pick hosts that match the query's niche or are generic authorities. BLACK (site reputation abuse when done to rank someone else's offer) Satellite sites / PBN for mentions:
Buy aged domains (or expired ones that still hold equity); prefer domains with an active Google Business Profile (expiredlocal.com). BLACK
Rebuild from the Wayback archive within a "two-year cache window" (Astro or AI tooling), so the site matches its former equity; avoid identical AI-built templates. BLACK
Never link the network to the brand; publish mentions only. Build satellite sites per brand in several formats (wiki-style for Claude). Cost "a couple hundred to a few thousand dollars". BLACK Click bombing:
Route bought pop traffic through t.co, Reddit, YouTube and Facebook redirects so it looks social; under 2% goes through the SERP. BLACK
Pick pages at positions 4–50 with steady impressions, never fresh URLs; build a CTR curve from GSC; send SERP clicks in steps until #1, then maintain. BLACK
Traffic sources, cheapest first: PopCash ($5 minimum), HilltopAds, then one heard as "Rip Pops" / "Richbox" and PopAds; ask the ad manager for the bottom-of-barrel rate. BLACK Jailbroken models:
Use an "abliterated" (refusal-removed) local model for volume, frontier models for quality, an agent harness that turns refusals into retries, and an automatic model switcher. BLACK
Use it for scaled "humanized" content and for "AI lawyers" that email page owners, then hosts, then registrars until a page is removed. BLACK Training-data seeding:
Write a fact sheet; generate 12–18 PDFs per query in different genres; upload to shadow libraries; wait for the next model. BLACK Fake authority:
Invent an award with judges and winners, then reinforce it with "trusted sources" in the niche. BLACK Update forensics (method only):
Snapshot SERPs before, during and after an update; capture page code; pair winners with losers (including two pages on the same domain); score attribute families; add placebo attributes; report with placebo-adjusted confidence. WHITE as a method Freshness:
Make every date signal agree (visible date, page metadata, schema); refresh only on SERPs that visibly reward freshness. WHITE when the content really changed; GREY if dates move without changes Events:
Keep event URLs evergreen (no year in the slug); refresh just before the seasonal "flip"; land PR inside the window. WHITE Platform search:
Reverse-engineer a platform's own search (he did Skool's vector search with browser agents): slug, title, description and category weighted highest. WHITE on a platform you are allowed to list on
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
"Presswiz": his link marketplace (heard; likely Press Whizz). Ran a "black hat SEO day" earlier that week.
His Skool community (name not stated in audio; the note-taker's private notes say "Rainmakers"; the audio says "brainmakers" once).
SEO Neo, GSA, Money Robot: old automated link tools, still used for tier-2 links.
"Herman or Grockbot": tools to manage $10–20 local PBN domains (speech-recognition spellings; not identified).
"TubeCapture" (likely 2Captcha) and 5SIM: CAPTCHA solving and SMS verification for mass account creation.
expiredlocal.com: expired-domain marketplace that shows whether a domain still has an active Google Business Profile; "a friend's tool, no affiliation".
PopCash ($5 minimum), HilltopAds, "Rip Pops"/"Richbox", PopAds: pop-traffic networks.
Satellite sites heard as "Charles Flight dot info" and "charlesfield.uk" (likely charlesfloate.info / .uk; not checked).
"Best SEO Awards": his fabricated award site.
"Resino Resin" (likely Resoneo): French SEO team credited for the twiddler research.
Kalin ("Carlin") and Giga Links: cross-reference to C11 (thousands of PBNs, mention-only).
Ahrefs ("AHS data"): source of the YouTube 24.5% mention-share figure.
OpenAI news partners: The Atlantic named.
Slide photos
None attached to the Granola note. Slides with screenshots (parasite ranking, expiredlocal.com, Ahrefs mention share, Merchant feed citation, update-lab output) were shown but not captured.
Q&A (question → answer)
None recorded. The talk ran over; the host directed questions to the event app.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
"Best SEO Awards ranked #1 in 6 months for ~$1,000" is wrong: about two days to #1, cost "over $1,000", and still ranking six months after he revealed the hoax.
The "Next Steps" (sign up for 2Capture and 5SIM, explore expiredlocal.com, set up an abliterated-model pipeline, review his satellite sites, look up the awards case, join Rainmakers) are the note-taker's private jottings turned into tasks. They are not agreed actions, and most are BLACK.
Satellite site domains are given as "charlesflote.info, charlesflote.uk"; the audio says "Charles Flight dot info" and "charlesfield.uk". Neither spelling is confirmed.
"Tools: TubeCapture, 5SIM, 2Capture" lists the same CAPTCHA service twice under two garbled names.
Omits the training-data method (12–18 PDFs per query into shadow libraries).
Omits the Merchant Center feed example (Google still citing a deleted feed product).
Omits his own framing that buying AI citations or third-party mentions is a link scheme under Google's guidelines.
Omits that nearly every figure is "our testing" with no sample, and that he sells the update lab inside his paid community.
During the awards case he thanked an audience member by first name as one of the "trusted sources" he used to make the fake award credible; the summary drops it.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
Company name "Presswiz" (likely Press Whizz), the community name ("Rainmakers" in the private notes only), the satellite domains, "Resino Resin" (likely Resoneo), "Herman or Grockbot", "Rip Pops"/"Richbox".
The JS-forum citation figure "0.64": ratio, rate or share is not clear from the audio.
The forum 41.4% / 14.2% figure: whose data.
"There was a November core update yesterday": not checked.
Twiddler names are presented as fact; only Resoneo's analysis is cited and it was not read.
No speaker web lookup was done; the name is clear in the note title and audio.
Communicating SEO Value - CMSEO — speaker not named (slides branded "earned media"; agency owner/lead with Salesforce and Rippling as clients)
Source: Granola https://notes.granola.ai/d/88697a74-5cc4-449d-a3cf-6710a56bc793 · recorded 2026-11-11 (13:10 GMT+7) · transcript-verified 2026-11-12 Vendor talk? No tool pitch. She sells full-stack SEO/AI SEO agency services (local trades up to enterprise). Slide footer reads "earned media" (agency brand, not spoken). Semrush mentioned once as the tool that offered AI Overview visibility measurement at the time.
Thesis (3 bullets max)
Stop promising organic traffic; AI Overviews/LLMs/agentic checkout intercept clicks, so reset goals to AI share of voice, branded demand, and total enquiries/pipeline while still reporting traffic.
Raise the problem to the client BEFORE the numbers land, with the fix attached; relationship and framing (what / so what / now what) retain clients, not the metrics.
Translate every action into an outcome a CEO and a 10-year-old both understand; leave out technical-work detail except for the in-house marketer.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Salesforce original KPI: non-branded organic growth | +100% in a year | Salesforce, non-branded queries; set 4 months before AI Overviews launched | agency | spoken | transcript clear |
| Salesforce mid-year trajectory | ~150% up, then 70% up after "April" | same; year of April not stated | agency | spoken | clear (one later mention says "60" as a loose figure) |
| Salesforce revised goals | LLM traffic +100%; organic target cut to 70%; AI visibility goal "60-something %" ("I think") | same | agency | spoken | clear (AI visibility figure hedged) |
| Salesforce outcomes | LLM traffic +1,500% over the year; organic +67% (missed 70%) | same year | agency | spoken | clear |
| Salesforce prior agency | no measurable organic growth for ~2 years | before agency came on | agency (claim about predecessor) | spoken | clear |
| Salesforce branded vs non-branded (separate diagnosis, period unclear) | non-branded +~40% YoY; branded ~-20% YoY | Salesforce; cause traced to internal marketing changes (TV/radio/other, a site rebuild) | agency | spoken | clear on direction, hedged ("I can't remember what it was") |
| Example report: organic clicks | -15% | one unnamed client, YoY-style comparison | agency | spoken | clear |
| same client: branded searches in GSC | +24% | same | agency | spoken | clear |
| same client: direct visits | +18% | same | agency | spoken | clear |
| same client: sales enquiries | +7% | same | agency | spoken | clear |
| same client: LLM referral | "+18%" | said in the negative-results answer; earlier the same 18% was "direct visits" | agency | spoken | INCONSISTENT - one of the two is a slip |
| Tummy Shield time-to-change | within 1 month of publishing the piece | Australian client; one piece plus outreach | agency | spoken | clear; engine not named |
| AI lag for incremental changes | ~3 months minimum | general rule of thumb | agency | spoken | clear, asserted not measured |
| University client FAQ test | ~400% uplift on first page tested; ~150% increase on that page in Google "Generative AI" Search Console report | one university course page; metric basis and period not stated | agency | spoken | clear; base unknown |
| University audit backlog | same technical audit 3 years running, 1 item fixed | 1 university client | agency | spoken | clear |
| Illustrative share-of-voice example | Salesforce named in 47 of 50 bottom-funnel prompts (stated as "94%"; 47/50 is 94%), HubSpot 44, Zoho 32 | "I work with Salesforce. If I go in and I say..." | speaker framing, appears to be an ILLUSTRATIVE example not a stated Salesforce result | spoken | transcript clear; treat as hypothetical |
| Illustrative report line | "we're in 37 out of 50" | example of goals-at-top | hypothetical | spoken | clear; hypothetical |
| Rhetorical | "zero clicks but 17x more sales this month" | question to a client | rhetorical, not a result | spoken | clear; NOT a measured number |
| Salesforce client ask result | an ecom/global brand asked a list publisher to be added; got placed #5 | one client, one listicle | agency | spoken | clear, anecdotal |
Asserted mechanisms (no evidence given in the talk)
Branded search growth is now partly an SEO outcome (AI recommends -> people then search by name -> direct/branded).
LLM traffic converts better than other traffic (said "yes it does", no number; declined to give a percent when asked).
Google's goal is to keep users in its ecosystem and eventually buy for them (AI Mode); clicks will not return.
AI citations are shrinking: Gemini often returns no sources and says it used training data; Reddit sourcing dropped because AI surfaced very old posts.
Google Trends will show a market-wide decline so a client's drop is not unique (shown for Salesforce vs HubSpot/Zoho; no figures given).
Clients cut agencies because of top-down business decisions, not work quality.
Hreflang fixes "changed the world" for global companies (no numbers).
JavaScript-heavy pages hide content from AI (demo: disable JS and reload).
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Goal reset (slides verbatim in spirit):
Tell the client: search is changing how people find you, so we change how we measure; organic traffic is still reported; goals move to enquiries and sales. Slide caption: if you raise it while numbers still look good, nobody calls it an excuse. WHITE
Replace goals (slide "Agree on goals that survive a traffic drop"):
OLD "Grow organic sessions [15% spoken / slide photo reads 45%]" -> NEW "Recommended in [_] of 10 top buying prompts, against our top 3 competitors."
OLD "Rank top 3 for 50 keywords" -> NEW "More people searching for us by name, compared with the same month last year."
OLD "Organic conversions in GA4" -> NEW "Total enquiries and pipeline, including the ones GA4 doesn't credit to organic." WHITE
Monitor ~50 bottom-of-funnel prompts; report named-in count vs top competitors. Verify live before the meeting: she warns clients check on their phone in the room. Tool for AI visibility not named for this (Semrush was used for AI Overview visibility at the time). WHITE
Keep rankings as a monitored secondary metric. WHITE
Report non-paid channels as ONE pipeline: organic + direct + LLM referral + organic social + referral + YouTube clicks; exclude paid. Build custom GA4 reports to isolate LLM referrals (GA4 out of the box does not do it well). WHITE
Add branded impressions / branded search YoY; use it to surface non-SEO causes (TV/radio/paid search switched off, H1 changed to "Black Friday Sale" with brand removed, content removed from a page that had 300-400 branded clicks and now ~12). WHITE
Diagnose a branded drop: export branded GSC data, give to Claude, ask which pages are most impacted; check whether AI answers stopped naming brands/citing; ask client what changed in the specific date window (example given "May 2026, 15th-20th"). WHITE
Report layout and cadence:
Goals at the top (AI visibility count, e.g. X of 50, vs last month); prefer year-on-year where seasonality applies (ecom: Nov 2x Oct, Dec 3x Nov, Jan ~5% of Dec).
Monthly data report; quarterly strategy deck (in person, slides) for the in-house/broader stakeholders; ad hoc meeting when the landscape shifts (e.g. within ~3 weeks of AI Overviews she scheduled, ~3 months to meet almost every client).
No report template or mock-up was shown (she said none readily available). The speaker did NOT describe a "channel breakdown" section. WHITE
Deliver the report during the call, then send it right after. Calls in first 1-2 weeks of the month. If client needs it first (e.g. by the 3rd, meeting on the 7th), write the meeting narrative into the cover email: problem noticed, fix, discuss next week. Monthly call is "100% yes" mandatory even if all is well. WHITE
Enterprise: give contact 1-2 slides from a 20-slide deck plus screenshots to forward upward; offer to review what they send their boss. WHITE
"What / So what / Now what" for every metric. Run wording through AI: "would a 10-year-old and a CEO both understand this?" WHITE
Slide "Translate every metric into a sentence": share of voice -> "AI recommends us in X of 10 buyer questions. Our top competitor is Y."; AI citation -> "ChatGPT now names us as the best option for XYZ."; impressions -> "We're visible on Google X times more often than the same time last year"; organic sessions -> "Visits from people who clicked through across all organic channels."; branded search -> "X% more people are searching for us by name."; technical work -> "Leave it out. Say what it fixed." Slide "Stop selling maintenance": not "Fixing technical crawl errors" but "Ensure AI is able to read and understand our site, products & offerings so that it provides accurate results to our prospective buyers." WHITE
Slide "Three things they can understand": (1) Does the brand appear - "Are we on the list?" top 3 yes/no when buyers ask AI or Google; (2) Is AI telling the truth - monitor what AI engines say about prices, features and details and create strategies to fix it; (3) The full picture - "Is the business growing?" report direct traffic, brand searches and sales enquiries alongside organic clicks. WHITE
Negative results: never let the client see a bad number cold; pair every drop with rankings check, market context (Google Trends vs competitors), and the specific fix with timeline ("give me a month"); own the narrative. WHITE
If client will not share revenue: work up the funnel (SQLs, MQLs, units sold last month/last year); use units sold as the sales goal; revenue sharing usually follows trust. WHITE
Tummy Shield sequence (see below). WHITE
"Are we on the list" play: identify third-party lists/listicles AI sources; get the client added (ask the publisher; sometimes just asking works). Brand-new list on a new site can move AI faster than editing existing lists. WHITE (paid placement questions not discussed)
Ecom agentic-checkout readiness: tell clients it is coming, screenshot Google cart in results, check Shopify integration (said to work by default), for WooCommerce check plugins; test with JavaScript disabled; check AI can retrieve product data, features, pricing, schema; do a test purchase flow to the cart (do not complete). Don't push replatforming unless you will support the migration; she does not build sites. WHITE
Stalled audits: re-issue last year's audit with "what changed since last year"; find the one thing you can control (university FAQ sections on course pages), prove impact, scale it. WHITE
Tummy Shield (client: pregnancy seatbelt adjuster, Australia), sequence as spoken: (a) before: client not in AI results; competitor (a cheaper product that did not meet Australian standards, higher failure rate, name garbled "meaning belt") was cited; no web source corrected it. (b) one extremely strong article: what the product is, why it works in Australia, crash-test evidence against Australian standards; client was the only brand that had crash-tested. (c) outreach behind it: press release saying only crash-tested product, digital PR, link building into pregnancy/car-safety articles, all linking back to that article. (d) result within ~1 month: AI answer now calls it a "standout device"/the exception, instead of the usual "government recommends using the normal belt correctly"; sources cited were the insurer NRMA (heard as "NRMA ... plus one") and the client. Engine/surface not named (Google AI-style result implied). (e) Audience member said the press-release blasts at $100 for 50-100 sites are not good; editorial mentions matter even without a link. Corroboration across the web, not just own site, was the stressed lesson. WHITE
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Salesforce, Rippling: global clients. A former Salesforce contact taught "what, so what, now what". Local Salesforce web director passes slides up the chain.
Semrush: offered AI Overview visibility measurement during the AIO rollout.
GA4: LLM referral custom reports; GA4 files YouTube clicks under organic social.
Google Search Console: branded impressions/clicks; "Generative AI" report (everything except AI Overviews: Gemini, Discovery, AI Mode as she described it; AI Overviews are in the main performance report).
Claude: used on branded GSC export; AI to simplify wording.
Google Trends: market-wide comparison (Salesforce vs HubSpot, Zoho).
Shopify, WooCommerce: agentic checkout readiness.
Tummy Shield (client), NRMA (Australian insurer cited in AI answer).
"Muse" and a second platform "starts with an I" (she could not recall the name): AI platforms that purchase on behalf of the user; Google testing a cart in search results. Names unverified.
"Wova app" (garbled): she said she will contact attendees there.
Price named: extra $1,000/month example for adding AI work on top of 10 links/month.
Slide photos
Full text of each slide: ../resources/communicating-seo-value/slide-text.md
01-reset-the-goal-without-moving-goalposts.jpg: "Reset the goal without moving the goalposts." Three suggested client-facing lines about changing how search is measured, keeping organic traffic reporting, and building new goals around enquiries and sales; footnote says that if it is raised while numbers still look good, nobody calls it an excuse. Readable.
02-goals-that-survive-a-traffic-drop.jpg: "Agree on goals that survive a traffic drop". Three struck-through old goals (grow organic sessions 45%, rank top 3 for 50 keywords, organic conversions in GA4) mapped to new goals (recommended in [_] of 10 top buying prompts vs top 3 competitors, more brand-name searching vs same month last year, total enquiries and pipeline incl. those GA4 doesn't credit to organic). Readable.
03-stop-selling-maintenance.jpg: "Stop selling maintenance." Struck-through "Fixing technical crawl errors." replaced by "Ensure AI is able to read and understand our site, products & offerings so that it provides accurate results to our prospective buyers." Readable.
04-three-things-they-can-understand.jpg: "Three things they can understand". Three cards: does the brand appear (top 3, yes or no), is AI telling the truth (monitor prices, features, details), the full picture (direct traffic, brand searches and sales enquiries alongside organic clicks). Readable.
05-translate-every-metric-into-a-sentence.jpg: "Translate every metric into a sentence." Table of what we say vs what we should say for share of voice, AI citation, impressions, organic sessions, branded search and technical work ("Leave it out. Say what it fixed."). Readable.
06-stray-onfolio-slide-buyer-models-and-terms.jpg: "Buyer models and terms differ." A slide from a different talk: table of four data-licensing buyer programs with licensing route and what to watch for, plus a slides download URL. Readable.
Q&A (question → answer)
Convert rate LLM vs Google? -> No data for that client; look at holistic number; LLM traffic converts better (asserted).
Who gets which summary if the contact is not the CEO? -> Work with contact, hand them 1-2 slides/screenshots to forward; speak directly this way if the contact is the owner.
Include negative results? -> Yes, framed with what/so what/now what; rankings check; Google Trends; fix.
Client will not share revenue? -> Work up the funnel to what they will share (units, leads, MQLs).
Is a monthly call mandatory? -> Yes, 100%; report during the call.
Do you have a mock-up of your report? -> Not available; goals at top, YoY, monthly/quarterly.
Monthly or quarterly? -> Mostly monthly data; quarterly in-person strategy deck; ad hoc on shifts.
Pitch AI SEO separately? -> No: SEO is now AI SEO; fold in; trade off current tasks or add budget (example extra $1,000/month).
Organic fine but branded search down 15% (attendee)? -> Investigate not spin: H1/brand removal, lost page content, AI no longer naming brand, internal business changes; ask client what changed on that date; use Claude on the branded export.
B2B attribution when client says few qualified leads? -> Shift to holistic non-paid bucket; custom GA4 LLM reports; show prompts that went from 0-1 mentioned to half; a colleague (Nick, works with speaker) added the "negative space" framing: visibility earlier in the funnel converts elsewhere.
Client cut budget top-down? -> Business problem; give contact a version for the decision maker; some clients leave; market is strong.
How to handle clients who never implement audits? -> See step 19.
What are you proposing to ecom clients now? -> Send screenshot of Google cart / AI purchasing, say Shopify works, you are monitoring.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
Summary says "Muse" is an AI shopping platform. Transcript: she named "Muse" and a second one she could not recall ("starts with an I"); the same word "Muse" appears in the Dennis Yu talk as an AI model alongside Claude, ChatGPT, Grok. Treat the identity as unverified.
Summary: "Muse and Google's cart rolling out globally in 3-4 months." Transcript: she said a notice about AI purchasing was coming from the US and would roll out globally in 3-4 months (the sentence is garbled: "RAG doing purchases", "my notice"); Google's cart was only "just started testing". Timing is the speaker's loose estimate.
Summary lists "Reframe: zero clicks, but 17x more sales" as if a result; it is a rhetorical question.
Summary does not say the 47-of-50 / HubSpot 44 / Zoho 32 example is illustrative.
Summary says report format has a "channel breakdown": not said. She said goals at top and YoY.
"ChatGPT Business Profile": not part of the talk. It came from a hallway chat after the Q&A among attendees (not the speaker): someone said ChatGPT now has a business profile (listing, works like Google Business Profile), the group wondered about a multi-client dashboard, agency charging, and manager access vs a client-owned email; one attendee said they would ask Claude to research it; also mentioned a share from "Steve" (spelled "Todd"; likely Steve Toth, unconfirmed) in a group. No facts about the feature were given.
Summary says Salesforce KPI was "100% organic traffic growth"; it was 100% on non-branded queries.
Summary says "Client stayed, quote from the ANZ Director of Marketing": she said a case study with a quote from the director of marketing, "Anz" (audio garbled).
Summary omits: Salesforce branded -20% / non-branded +40% diagnosis; the three Google Search Console tactics (Generative AI report); the JavaScript-off demo; the university FAQ test; Black Friday H1 example; the $1,000/month upsell example; the second AI pivot (citations), then pivot to sales; "ask the list publisher to add you" tip; do not promise 4 blog posts, tell them you will be the obvious source for high-value bottom-funnel questions (the pool trick-shot analogy).
Summary omits that the example "-15% / +24% / +18% / +7%" is from one unnamed client and that the speaker mislabels +18% as LLM referral in one pass.
Tummy Shield: summary implies engine; the transcript does not name the engine.
"How did you find us" form tip: NOT present in this transcript.
Slide 6 attached to this note is NOT from this talk: it is an Onfolio Labs slide on AI-training data licensing buyers (Polyshares fixed license fee; micro1 company data partnership, 30+ staff stated, paid after acceptance; Mercor company data licensing, scope and compensation agreed; Troveo licenses to multiple buyers, an estimate is not a formal offer; "Download slides: onfoliolabs.ai/CMSEO"). Likely a different session captured by mistake.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
Speaker name and agency name: not spoken; slides show "earned media".
Slide 2 old goal: photo is blurry, reads "Grow organic sessions 45%" (spoken example was 15%).
Competitor product name in Tummy Shield story: garbled ("meaning belt").
Salesforce AI visibility target "60 something percent": speaker hedged.
Year of the April AIO drop: not stated in the transcript (Salesforce branded example says "May 2026" for a hypothetical date).
Second agentic-shopping platform name: not recalled by speaker.
"RAG doing purchases" probably refers to agentic/AI purchases: audio garbled.
Whether "+18%" was direct or LLM referral.
"Wova app": garbled.
7 Steps (deck footer "7 Steps to Ma…"): Minimum Viable Content, EMDs and Fast Channels — David Quaid (SEO consultant, New York; King of AEO competitor)
Source: Granola https://notes.granola.ai/d/beb2e008-7963-4833-87c9-75bf242c13cc · recorded 2026-11-14 (16:53 GMT+7), LLM Mastery 4.0, last talk of the day · transcript-verified 2026-11-16 Resources: 8 slide photos saved to ../resources/david-quaid/photos/ (8 of 8 attachments; all readable except where the speaker blocks the screen). No deck or handout. He said the evidence is on his X, LinkedIn and YouTube. Vendor talk? Consultant/agency, no product pitched. Self-promotion of his track record and channels. He says he signed up for a Giga Links account (C11's vendor). All results are his own client stories with no base or period.
The audio is moderately garbled. Where the slide and the audio disagree, the slide is used and the difference is listed under Corrections.
Thesis (3 bullets max)
About 90% of SEO is myth and malinvestment. Build many cheap, small pages, let rankings show where authority is, then feed the winners ("$10 on every table", photo 06).
Exact-match domains (EMDs) still rank on relevance with few links, convert better, and "firewall" the brand site (photos 03–05).
Fast channels (YouTube, Reddit, keyword press releases) rank in minutes to hours; file name and title do most of the work (photos 07–08).
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| EMD lead flow | 160 leads in week one; 50 leads/month for about 10 years | freeloadbalancer.com, Kemp Technologies, from 2015 | himself (then head of marketing) | spoken; photo 03 shows the site | anecdote; no traffic or conversion data shown |
| EMD conversion | 1–2% conversion on under 100 organic clicks vs 1–2 leads per 1,000 visits on branded sites | his clients; no count or period | himself | spoken | low; no base |
| EMD link need | under 1% of the backlinks the branded domain needs; "one or two links" | none | himself | spoken | assertion |
| Three EMDs = a quarter of leads | three EMDs delivered "a quarter of all our leads" | Kemp, period not stated | himself | spoken | anecdote |
| PAA pages | 100 PAA pages in two months; one ("does my dentist know if I'm smoking weed?") reached 2,000 clicks/month | one Texas dentist | himself | spoken | anecdote |
| Glossary leads | 28% of leads touched the glossary | one cybersecurity client (name garbled) | himself | spoken | anecdote; attribution method not given |
| Minimum viable pages | "even in the worst case, 50% will rank" | none | himself | spoken | assertion |
| GSC positions 11–17 | new pages for those queries reach the top 5 "within 36 hours" | none | himself | spoken | assertion |
| His own site | ranks for about 18,000 keywords; 20% of traffic from pages arguing E-E-A-T is "bullshit" | his domain | himself | spoken | self-reported |
| Fast video ranking | "page one of Google in 15 minutes" (spoken); "video ranks in Google and Bing in under an hour" (photo 08); one podcast video ranked three times in Google a few hours after recording (photo 07) | one podcast | himself | photos 07, 08 + spoken | anecdote; photo 07 still carries a draft placeholder "[Jabez — confirm]" |
| Reddit reach | "50–70 communities that accept video posts" (photo 08); spoken "50 to 170" | none | himself | photo 08 | slide figure used |
| Track record | seven companies taken above $200M in six years; Kemp sold for "$250M"; "Insights" bought by Rapid7 for $325M; most clients get 69.7% of revenue from inbound; average client under $3,000/month for paid search incl. agency fees | his clients | himself | spoken | self-reported; company names garbled |
| PR spend | PR agency at $26,000/month produced no coverage; Gartner relationship went from $15,000/year to $500,000 before the segment was dropped | Kemp | himself | spoken | anecdote |
Asserted mechanisms (no evidence given in the talk)
Google runs "PageRank nearest seed" (since at least 2024), similar to harmonic centrality; links still count but about 90% of backlink value is overweighted. Photo 02 says the opposite under "What hasn't changed": "Links. They matter so much."
LLMs spent two years reverse-engineering Google; their cached indices mirror Google's; rank order matters less once results are synthesized (photo 02, photo 06).
Google is "content-agnostic" (cites the DOJ v. Google trial) and on YouTube "doesn't dedupe — it ranks each placement" (photo 07).
EMDs rank for the same reason Nike.com ranks for "Nike": the name is in the domain. Google's EMD devaluation is "misdirection".
EMDs absorb exploratory traffic so the brand site has "no bounce-rate bloat, no pogo-sticking"; "the AI returns the brand — the EMDs make sure it finds you" (photo 04).
File name is the most important YouTube ranking element "because Google was built by Unix engineers".
E-E-A-T is "trust me, bro", not third-party validated.
Telling an LLM "most of this has been disproven" makes it rewrite its answer 9 times in 10. Spoken only; it shows sycophancy, not truth.
Crawl budget is not a constraint for Google (YouTube is about 25 exabytes).
Black hat "still works" (photo 02).
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Seven steps (photo 01): understand LLMs · test and think critically about output · build your own strategy · study competitors for weak spots · build at a scale you can manage · find data that proves it works · repeat.
Minimum viable content:
List the keywords you need (he cites up to 2,000). WHITE
Build a page for each at once, starting at about 50 words, with only 5 on-page elements; page title, document name and slug are "90% of the battle". GREY (thin pages at scale; see Rejected)
Watch which pages rank and which show buyer intent in GSC; put writing time into those only. WHITE
Import queries a page already ranks for as H2s, with a table of contents. WHITE
Queries ranking 11–17 in GSC → new pages. GREY (cannibalization risk he himself calls the biggest problem)
Publish pages empty and let topical authority pull them up, then add content. GREY
Five-minute PAA hack: 7. Search a niche question, expand People Also Ask repeatedly, copy the questions. WHITE 8. Have an AI write each answer from the client's own site; publish each as its own URL, title and H1; link them to FAQs and money pages. GREY (scaled AI content; Google's scaled-content policy) 9. Make a video for each and embed it on the page. WHITE
EMDs (the "market-analysis play"): 10. Start with one EMD; avoid .info, .biz, .net (CTR and spam perception); one or two links from the parent domain; wait a few weeks. GREY 11. Style it as part of the brand family: brand logo, palette and illustration (photo 03: freeloadbalancer.com beside Progress Kemp LoadMaster; "It reads as family, not as a disguise"). WHITE-to-GREY when the owner is visible 12. Or "make them look like a third-party site" and cover the whole market, competitors included (spoken; photo 05: "you can't keep G2 and Gartner out of the result set — but you can stop being only in theirs"). BLACK when ownership is hidden (undisclosed self-review) 13. Competitor takedown pages that IT managers mistake for the competitor's support page. BLACK (confusion with a rival's brand) 14. Do riskier things on EMDs to protect the brand domain (photo 04). GREY/BLACK depending on the thing
Fast channels: 15. Buy a press-release package (10–20 releases) and put keywords, not the brand, in them; tie them to news (end-of-life products, Microsoft/AWS/Google ecosystem). GREY 16. Publish the video standalone on YouTube with a keyword file name and title (photo 08). WHITE 17. Post the same video to 50–70 Reddit communities that accept video posts, each with a new title; never post links, tell readers to "go search for" the term. BLACK (cross-post spam; search-prompting to manipulate signals) 18. Re-upload the same video under different titles, or as a blog post with the video (photo 08 footer). GREY 19. Encourage juniors to buy $12 test domains and run experiments, not on client sites. WHITE
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
freeloadbalancer.com: Kemp (now Progress Kemp) EMD, live since 2015 (photo 03); "Exchange Load Balancer" EMD said to have won Amazon as a client.
Kemp Technologies / Progress: his former employer ("Kim Technologies" in audio); photo 03 shows Progress, Progress Kemp LoadMaster and the EMD side by side.
Giga Links: he says he just signed up for an account ("GigaByNX" in audio); same vendor as C11.
King of AEO competition: he says he is near the bottom; EMDs were "one of the biggest differentiators"; YouTube won it for "James" (James Dooley named; Goldie probably Julian Goldie). "Mark's talk" on the results is referenced; Mark not identified.
Charles Floate ("Charles Float"): estimated the CPC value of his site at $140k.
Gartner, G2: market gatekeepers (photo 05).
Edison Partners: Kemp's investor ($16M).
"Edward Stone Show": podcast where he presented the PAA hack (speech-recognition spelling).
"Henry Fudge": a UK TikTok creator on property capital (garbled; tangent).
"Quicken": New York PR agency at $26k/month (garbled).
Jabez Reuben: LLM Mastery host ("Jaggers Java's" in audio); appears as an unfinished placeholder on photo 07.
WordPress, Elementor: his page tools.
Reddit: he says he owns 25 communities including "the largest SEO community in the world" (about 500k members).
Slide photos
Full text of each slide: ../resources/david-quaid/slide-text.md
01-seven-steps.jpg: "01 · Open — The Seven Steps", the seven steps listed above.
02-everything-changed-nothing-changed.jpg: "Everything has changed. Nothing has changed." What changed: 2 years of LLMs reverse-engineering Google (Bing spent 20) · more indexes (Yandex, Baidu, Common Crawl) · close enough, synthesize the results · rank order "who cares". What hasn't: Links. They matter so much · Fast channels: news, video, QDF, forums · Blackhat. It still works · GBP for SaaS: still usable in a big city with wide reach. Speaker partly blocks the left column.
03-owner-brand-emd-design-ethos.jpg: "04 · Strategy — Owner, Brand, EMD: the design ethos". Three screenshots: Progress ("AI Enable Your Business"), Progress Kemp LoadMaster ("cream and yellow, blue buttons, flat illustration"), freeloadbalancer.com ("Free LoadMaster Load Balancer"; "the brand's logo, palette and illustration"). Caption partly hidden: "The EMD w… brand. It reads as family, not as a disguise."
04-firewall-your-domains.jpg: "04 · Strategy — Firewall your domains": EMDs take exploratory, task-driven, loosely relevant traffic · branded site stays clean (no bounce-rate bloat, no pogo-sticking) · a hit on one domain doesn't damage the whole · "the AI returns the brand — the EMDs make sure it finds you".
05-honest-caveats-market-analysis-play.jpg: "05 · The market-analysis play — The honest caveats": can't just trash competitors · covering the market feeds competitors too · can't keep G2 and Gartner out, but stop being only in theirs · "Don't build ten EMDs. Build one trusted advisor you own."
06-let-rankings-tell-you-authority.jpg: "06 · Implementation — Let rankings tell you where the authority is": when a page ranks, link to it · a page that ranks has authority · LLMs landed in the same place: ranking is the signal · "Build cheap. Watch what ranks. Feed the winners. $10 on every table."
07-youtube-ranks-in-minutes.jpg: "06 · Implementation — YouTube ranks in minutes": podcast with "[Jabez — confirm]" ranked in Google a few hours later, the same video three times · one video in three places = three results · "Google is content-agnostic on YouTube. It doesn't dedupe — it ranks each placement" · "I run these things daily — so I know when someone's lying."
08-how-to-do-it-video-reddit.jpg: "06 · Implementation — How to do it. Video ranks in Google and Bing in under an hour": 1 publish standalone video · 2 amplify through Reddit, 50–70 communities that accept video posts · 3 every post gets a new title · 4 (speaker blocks most of it) "…your entry into other LLMs… worth it". Footer: recycle the same video under different titles or as a blog post with video.
Q&A (question → answer)
None. He ran out of time; the host closed the day.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
"50–170 communities": the slide says 50–70.
"Can reach page one of Google within 15 minutes": spoken; the slide says "under an hour".
"Page unchanged since 2015; led to Amazon as a client": he said the page was redesigned but the content kept; Amazon came from a second EMD (Exchange Load Balancer), not freeloadbalancer.com.
"Took 7 companies above $200M, including Instabase ($2B) and Insights (acquired by Rapid7 for $325M)": company names are speech-recognition spellings ("Insights" is likely IntSights); not checked.
"#1 SEO in New York since 2020" is his own claim, stated as fact.
Omits the slide contradiction on links ("They matter so much") vs the spoken "90% of backlink value is overweighted".
Omits the deceptive tactics: EMDs styled as third-party review sites; competitor takedown pages mistaken for a rival's support page; "firewall" domains to run riskier tactics.
Omits the slide caveats ("don't just trash competitors", "build one trusted advisor you own") and the design-ethos slide that shows the EMD carrying the brand's logo, which conflicts with the spoken third-party styling.
Omits the keyword press-release tactic, the glossary 28% claim, the Giga Links sign-up, and the "most of this has been disproven" prompt habit.
"Made a video at 1am … to displace a competitor in the King of AEO competition": he said a video he made pushed "James" out of a position; details garbled.
"freeloadbalancer.com" in the private notes is the note-taker's line; it matches the slide.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
Company names: "Kim Technologies" (Kemp, confirmed by photo 03), "Insights" (likely IntSights), "Cybersecaine", "Quicken", "Edward Stone Show", "Henry Fudge", "Mark" (King of AEO results talk).
Kemp sale price: spoken "$250 million"; not checked.
"PageRank nearest seed since at least 2024": no source given.
Photo 07 carries an unfinished placeholder ("[Jabez — confirm]"), so the podcast story was not final on his own slide.
Photo 08 box 4 is blocked by the speaker.
Dennis Yu - CMSEO — Dennis Yu (named by meeting title and self-reference; company not named in the transcript; his program is called "Lighthouse" and he mentions a past search-engineer role at Yahoo)
Source: Granola https://notes.granola.ai/d/9ab9b433-44cf-46fe-a1ee-cda13de959d3 · recorded 2026-11-12 (10:44 GMT+7) · transcript-verified 2026-11-12 Vendor talk? Partly. He says he is not selling anything, QR codes shared, and offers free help with knowledge panels and installing AI agents; promotes his book on knowledge panels and a new book "Don't Get a Job" (out next week). Pitches the equity/profit-share agency model (his own "Lighthouse" setup) and advisory equity instead of fees. Also name-checks Colton Bollinger's Jumper Media (local SEO) and says he is not being paid to.
Thesis (3 bullets max)
SEO, PR, reviews, social, ads and reputation are one thing: accumulating verifiable proof tied to an entity (knowledge graph / KGMID) that Google and AI models both read; slow SEOs die, good SEOs plus AI agents multiply.
Harvest real proof from client operations (phones, shared drive, calls), let agents process and publish it, amplify with tiny ad budgets ($1/day), and turn it into a book.
Replace monthly retainers with equity/phantom equity or profit share by tracing work through revenue to profit to enterprise value; "last SEO play".
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Warriors ROI | $29 in sales per $1 spent | Golden State Warriors, agency client 5.5 years | speaker says he can prove it | spoken | clear; no method shown |
| Anthony Hill landscaper growth | extra $1M in revenue last year | Bloomington, Indiana landscaper; started 2011 with push mower and minivan ("that's what the AI said") | speaker | spoken | clear; unaudited |
| Anthony ranking | number one for tree removal in Bloomington (live search offered); bought fence repair company and 3-4 others; new Nashville location with knowledge panel | same | speaker | spoken | clear, not shown |
| Initial retainer | $3,500/month | Anthony Hill, "standard digital marketing agency" fee before equity idea | speaker | spoken | clear |
| Ads raise organic | "the more money we spent on ads, the more organic we have" | Warriors | speaker | spoken | clear, no numbers |
| Carl's knowledge panel | confidence score 86, unclaimed | Carl (conference organizer) | speaker (live) | spoken | clear |
| Phantom equity illustration | 1% of a $10M exit = $100K; 3% of a $30M company (growing from say $10M to $20M to $30M) | hypothetical | speaker | spoken | clear; HYPOTHETICAL |
| Value-add illustration | company valued $12M to $15M; $5,000/month work could be worth several million over lifetime | hypothetical | speaker | spoken | clear; hypothetical |
| Exit anecdote | "Yobl" sold for $347M cash by Nathaniel Stevens, who started with Dennis at 19 | third party | speaker | spoken | name garbled |
| Raise anecdote | "Evoker" (garbled) raised $130M at $1B valuation; Tyson Chen; two weeks ago, New York | third party | speaker | spoken | garbled |
| Anthropic S-1 | 90% of Anthropic's code is written by itself | claim | speaker, no source | spoken | clear, unsourced |
| 5% / 95% split | 5% of work needs frontier models, 95% can run on small/local models | his workflow | speaker | spoken | clear, asserted |
| DR 95 links | links with DR 95-ish from media after CNN clip; ranked #2 for "Facebook ads" | speaker's own site; Ahrefs/Semrush suggested as the way to see it | speaker | spoken | clear; no screenshot |
| Berry demo | ~99% of tasters find lemon sweet after chewing; "1% it doesn't work" | audience demo | speaker | spoken | clear, demo |
Asserted mechanisms (no evidence given in the talk)
Google and AI models (Claude, ChatGPT, Perplexity, Kimi, Grok) all hold entity "world models"; consistent, corroborated proof across platforms raises ranking in both.
A knowledge panel is a canary confirming entity-building works; Google "writes the entity, not the site."
Writing a book is "still the easiest way" to rank and get a knowledge panel.
Ad-driven watch time/engagement (e.g. other landscapers watching 20 minutes) is a good signal to YouTube/Instagram; not fake likes or CTR; ads do not directly help SEO but the signal does.
Ranking in ChatGPT: "we see how much traffic" comes from ChatGPT for landscaper queries (no number).
Equity aligns incentives and removes churn risk; "last SEO play".
Agents checking each other beat one model self-checking; validation matters more than the SOP.
AI agents shop and book; they do not care about ads, they care about proof.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Proof-harvest content factory:
Pick clients with strong real reputations and results (examples: Warriors, Philadelphia 76ers as the "most losing team" to prove method works). WHITE
Collect real raw ingredients: staff phones to a shared drive (photos, video), Zoom calls, CRM notes (privacy: get permission). WHITE
Agents (Claude and ChatGPT named; Codex as checker) process the drive and produce SEO and content outputs: blog posts, citations, YouTube, Instagram, Wikipedia, guest posts, press. Tie everything to the entity (KGMID), push consistently to knowledge graphs. WHITE (Wikipedia/guest-post volume could drift GREY if not real)
Shared context: agents store work in GitHub so any model can pick up; run several models (Claude, ChatGPT, Grok, "Muse", Gemini named) and let them argue; only return to the human on consensus; example prompt: interview prep for Colton Bollinger for a book chapter, research, validate, answer objections, store in GitHub, deliver a 10-page PDF by email. WHITE
Different model checks the doer (Claude works, Codex checks); never the same agent as referee. Agents can build SOPs from email, text, WhatsApp, Slack history; keep skill .md files; validation more important than the SOP. WHITE
Frontier model for reasoning (about 5%), small local/private models for the 95%; recursive loops where agents update their own docs ("RSI"). WHITE
Amplify with "$1 a day" ads (two uses): (a) push a credible clip (his CNN debate with Zuckerberg) at $1/day targeting employees of NYT, WSJ, LA Times, Fox News, NPR so other media pick it up and link; check links in Ahrefs/Semrush; (b) run $1/day against client videos (e.g. "how to grow a landscaping company") to a relevant audience to produce genuine watch-time engagement signal, not fake likes. (a) GREY (media targeting to earn links) / (b) WHITE
Case-study the result with the platform (e.g. Facebook case study that links to you) for a relevant authority link. WHITE
Turn the proof into a book: feed Zoom calls/CRM/talks into AI to assemble (not generate) a book; quote real examples; knowledge panel follows. He published "how to get a Google Knowledge Panel" and plans a new edition including Kyle Roof, Matt Diggity, Carl; "Don't Get a Job" next week. WHITE
Local SEO test pattern: document a free trial of a tool (Jumper Media or High Level) from map rankings to phone calls to revenue vs costs (tool, PPC, local services ads, VAs replaced by agents) and publish it. WHITE
Equity / profit-share model (as described, not a term sheet):
Trace the work: ranking/click -> calls -> revenue -> profit (revenue is vanity, profit is real) -> EBITDA x multiple -> company valuation. Have Claude teach/compute. WHITE
Show the valuation lift your work caused (e.g. $12M to $15M); argue a retainer undervalues lasting value (a $5,000/month effect has multi-million LTV). WHITE
Instead of or beside a monthly fee, negotiate: (a) equity in the client business; (b) "phantom equity": a contractual claim to a percentage of proceeds on a change of control (sale/acquisition), no formal share issue; example given with 100,000 shares and a percentage if you are still with the company on the event day (key employee use-case); (c) profit sharing; (d) super-affiliate / partner role; (e) advisory equity of "a percent or two" in agencies (garbled; "1 or 2 percent") plus cross-equity with underlying roofing company or SaaS. Percentages beyond the hypotheticals above were not given; triggers named: change of control/sale/exit, being present on that day. WHITE (legal and tax: he says "pay taxes if you're in America"; no legal advice given)
Anthony Hill structure as spoken: initially $3,500/mo; then moved to aligned equity; created an agency with Anthony as the face ("Lighthouse"), publishing his example to attract other landscapers; "equity going both ways" (exactly who holds what is unclear). WHITE
Knowledge panel check demo: asked a voice Claude why Carl and Matt Diggity lack knowledge panels; answer was non-committal; he then claimed Carl has one (confidence 86, unclaimed) and Kyle Roof has one unclaimed. WHITE
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Claude, ChatGPT, Codex, Gemini, Grok (heard "Rockbot"), "Muse", Perplexity, Kimi: models/agents; Muse used as an AI model here (compare talk 1).
GitHub: shared agent context.
Ahrefs, Semrush: to see where links came from; he says he was on Semrush's board before IPO.
Jumper Media (Colton Bollinger), High Level: local SEO/CRM; "23 accounts" Colton walked through; free trial to be documented.
"Lighthouse": his agency-with-client-as-the-face model.
Anthony Hill (landscaper), Golden State Warriors, Philadelphia 76ers, Nike, Starbucks, Red Bull (named as past clients/proof; claims not shown), Facebook case study.
Nick (agency, 17 SEO staff, talk turned into a book yesterday), "George Ra" (garbled), "Richard Ahre" (garbled), Carl Kanger/Kenberg (conference), Kyle Roof, Matt Diggity, Dan Henry, Affiliate World Dubai, Nathaniel Stevens ("Yobl"), Tyson Chen ("Evoker"), Aaron Rumba (opening story; garbled).
Miracle berry and lemon: demo only; the berry name is garbled in audio.
QR codes on slides for resources; no URLs spoken. No prices except $3,500/month and $1/day.
Q&A (question → answer)
None. Session ended at time; the host closed without questions. The Claude live-voice exchange with Carl was a demo.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
Summary names "Nathaniel Stevens (Yobl)" and "Tyson Chen (Evoker)" as if verified; both company names are garbled in the audio.
Summary states "3% of a company growing from $10M to $30M" as an example; it is hypothetical, with valuations introduced by "say".
Summary says Anthony Hill "agency took equity in the landscaping business and the agency itself": transcript is ambiguous on who holds what; he said equity "in our agency" and "going both ways".
Summary omits the "$1/day" method (two distinct uses), the $3,500/month starting retainer, "Lighthouse", Colton Bollinger/Jumper Media and the planned documented trial, the consensus-before-human agent workflow and different-model checker rule, 5%/95% model split, the SOP-from-message-history tip, Anthropic S-1 claim, his new book coming next week, and that the live Claude demo was unhelpful.
Summary lists agents as "Claude, ChatGPT, Codex"; he also named Gemini, Grok, "Muse".
Summary says "Nick had his conference talk turned into a book in one day": transcript names are garbled (the speaker called out "George Ra", "Richard Ahre" and "Nick" in the same passage; he says a presentation from a couple of days ago was turned into a book, and "we turned this thing into a book yesterday").
Summary says "Dennis appeared on CNN debating Zuckerberg on privacy": transcript says he was given the questions in advance and argued with Zuckerberg; he then pushed the clip as $1/day ads to journalists.
Summary does not note the opening Warriors story: he says he cannot take selfies; irrelevant.
Phantom equity mechanics in summary are generic; transcript adds the "must be with the company on the event day" condition and change-of-control trigger.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
"Yobl", "Evoker", Nathaniel Stevens, Tyson Chen, "George Ra", "Richard Ahre", Aaron Rumba, "Rockbot", "Fable 5.2", "Grot 4.7", "Gemini carbon/Argon" (all garbled model/person names).
"Muse" as an AI model: unverified.
Who owns what in the Anthony Hill equity deal; any actual percentage held; whether Anthony's $1M and ranking are audited.
"Just like percent or 2" for advisory equity: garbled.
The $29 per $1 Warriors ROI: no method or period.
Berry name ("day into siphon"): garbled.
Anthropic S-1 90% figure: unsourced.
Licensing company operational data to AI labs and data buyers — Dom Wells, CEO of Onfolio Holdings (Nasdaq-listed per speaker); subsidiary Onfolio Labs
Source: Granola https://notes.granola.ai/d/abda7298-f533-4599-b41a-05bab7e4ea46 · recorded 2026-11-11 (15:07 GMT+7) · transcript-verified 2026-11-12 Vendor talk? Yes, soft. The speaker states up front that "we're acting as brokers" and that the talk is partly why he is presenting. He is also an affiliate of data buyers (he refers to his "affiliate dashboard") and offers to split commission with attendees who go through Onfolio Labs (QR code to onfoliolabs.ai/start; the URL appears in David's private notes, not in the audio). Treat every price, "window" and market-size claim as coming from someone paid when deals close. He says he assembled the deck in a day and is "probably not a complete expert".
Thesis (3 bullets max)
AI labs have run out of crawlable internet; they now pay for complete operational company data (email, Slack, Drive, CRM, call recordings, SOPs, code) via intermediary "data partners".
Participation routes: license your own company's data (quotes seen $100K-$500K for him; checks up to $2M) or refer other companies for roughly 6-10% (or flat $10-20K).
The speaker believes there is a roughly 2-year window; the more durable play is broker / data-readiness services as regulation tightens (idea from the audience, he agreed).
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Quote from Micro1 | about $500K, no rev share | his own company ("about 39 employees" appears in the talk) | speaker, personally received, summer-to-Nov 2026 | spoken (Q&A) | clear |
| Quote from Polyshares | about $100K upfront plus perpetual rev share "25% or something" | same company | speaker, personally received | spoken | clear on $100K; garbled on the 25% ("or something") |
| He took the larger (Micro1) offer | $500K quote; amount actually paid not stated | — | speaker | spoken | clear that he chose the bigger one; "we've done a couple" is ambiguous, and he says elsewhere "we've only gone in with one" |
| Rev share break-even | 7-8 years to catch up with the upfront | scenario "if it was $200K, $100K", partly garbled | speaker's own calculation | spoken | garbled |
| Range of checks | $100K to $2M (offers he got: $100K-$500K) | "typically I've seen" | speaker, mixed own and heard | spoken | clear; he does not know what earns $2M |
| Referral commission | about 6-7% typical, "on average about 6%", some 10%, some flat $10-20K | across buyers he has seen | speaker, own affiliate dashboard | spoken | clear |
| Anthropic spend | about $1B/yr on data | claimed by Anthropic (as relayed); OpenAI "probably similar"; tier-2 labs also | second-hand | spoken (Q&A) | clear that he said it; unverified |
| Idler deal | "seven figure contract per year" with Anthropic; three people built it | one company | second-hand | spoken | clear that he said it; hedged ("I think") |
| OpenAI website purchases | about 200 websites/month at about $20K each, built as fake copies of real sites to train Codex's browser control | one anecdote | second-hand | spoken | clear that he said it; unverified |
| Headcount threshold | about 30 desk employees; bundle to about 35 | some buyers only | buyer statements to speaker | spoken | clear |
| Data age minimum | about 2 years; some none; more years pays more | "I think" | speaker | spoken | clear but hedged |
| Pay timeline | about 30-day inspection, paid about 30 days later (about 60 days) | "I think they have" | speaker, first-hand with one buyer | spoken | hedged |
| Mercor expert pay | $300-500/hr for experts validating environments (attendee: contacts earn $80-120/hr) | their application listings | speaker + attendees | spoken | clear but attendee figures are second-hand |
| Someone sold data instead of the business | about $1M | one person | second-hand | spoken | clear that he said it |
| Dental roll-up | 30+ staff could unlock about $500K | hypothetical | an audience member (post-talk chat), not the speaker | spoken, off-stage | clear (speculation) |
| Spirit Airlines benchmark | "Google paid Spirit Airlines" this much, per Polyshares | — | speaker relaying a buyer | spoken | garbled; looks like an ASR or recollection error, do not cite |
Asserted mechanisms (no evidence given in the talk)
Labs no longer train primarily on the web; they use "real data" for post-training (supervised fine-tuning, RL, evals).
Buyers either package data and resell, or build training environments from it (higher value). Some he suspects "just pretend" to build environments.
A lab told him completeness beats volume. He flags this "could just be a sales pitch".
Headcount is the biggest price lever at Polyshares; completeness at the environment builders.
Data is stripped of PII and anonymized before reaching labs; labs want synthetic data that is accurate; some mapping unknown to him.
The window is about 2 years; tier-2 labs, agent builders and consultancies will join; deals will improve for sellers as buyers compete (attendee view, speaker agreed).
Selling perpetual data can lower a business's sale price to private equity (like an AppSumo lifetime-deal base); a one-year exclusivity license likely does not. He has asked business brokers; no evidence.
Synthetic data from labs themselves may erode demand in 4-5 years (labs' claim as relayed).
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
A. License your own data (speaker's route)
Check eligibility: ~30 desk staff (full-time-equivalent, contractors count; "desk" means not logistics/drivers), English (some take other languages), US/UK/Canada preferred, 2+ years of data. WHITE
Fill the buyer's intake form: company name, website, headcount (now and at peak), size and years of Gmail, Drive, Slack, CRM, GitHub, Zoom recordings, SOPs, ClickUp/Salesforce etc, language, medium (text/audio/video). No data is shown at this stage. WHITE
Quote only the size of internal/operational data and exclude customer data (his "safest" guidance). He admits he first quoted the largest amount possible. GREY (over-quoting before knowing the cleaning rules)
Get several quotes; they differ widely. Bidding buyers against each other did not work for him. WHITE
Sign an LOI, then hand over data. About 30-day inspection, then pay about 30 days later. Quote may drop if only part is usable. Onboarding was painful, quote was the hard part. WHITE
Ask five things: what they are looking for, how it will be used, exclusive or not, fixed term or perpetual, deadlines; also whether they train on your data. WHITE
Review the privacy policy/terms first (audience advice, he agreed). WHITE
Raise headcount credibility: show contractors in HR/payroll tools (he regretted not loading his contractors into Gusto/Deel). GREY if padding; WHITE if real contractors
Companies under 30 staff: bundle with similar companies to reach about 35 with buyers that allow it. GREY (see privacy)
B. Refer others (affiliate)
Join buyers' referral programs: link (Polyshares gives one), or a form with the referred person's name and email (the Mercor-style form, and Polyshares also). WHITE
Build an intake form on your own site, take the lead's details, then pass them on or fill the buyers' forms for them. This is the common affiliate model; he notes some "data buyers" are really brokers like him (two tiers). GREY (data-handling and disclosure obligations unaddressed)
Or write review posts / social posts with referral links. WHITE
C. Ideas voiced, not done
Buy undervalued old businesses/affiliate sites (about $30K) with deep data history and sell the data for several hundred K. The speaker has not done it ("I think about it a lot"). GREY (depends on what was acquired and whether you may sell it; he caveated "assuming I'm allowed")
Add data-size questions to acquisition due-diligence forms. WHITE
Record more Zoom calls and document headcount to raise your quote. GREY
Joke from the room: hire people / record everyone all day to inflate headcount. Not endorsed. BLACK-HAT if actually padded
Sell data before selling the business (second-hand, one person, about $1M). GREY (valuation impact, disclosure)
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Onfolio Holdings (Nasdaq-listed, portfolio of online businesses) and Onfolio Labs (subsidiary exploring business experience for training/testing AI agents; also brokers data). URL onfoliolabs.ai/start is only in David's notes. Commission terms: "we can split the commission"; no percentage stated. No stated fee to attendees.
Polyshares (ASR spelling): about $100K upfront + perpetual rev share (about 25%, uncertain); prices by headcount; gives affiliate links and also a form. Cited "Spirit Airlines" benchmark.
Micro1 (ASR): about $500K quote, no rev share; "a number of factors"; he thinks they build products from the data.
"Merkle" / "Merco" / "Mirko" — almost certainly Mercor: started in data labeling, then company data; he is unsure whether you can sell directly now; pays experts $300-500/hr (per speaker) to validate environments; form-based referral; hires individuals not agencies; Role listings require named-firm experience. A rep or attendee's relatives work there.
Trovio (ASR, unverified): marketplace; you list data, multiple buyers can purchase; he had just asked them questions and had no reply.
Idler / "Idler AI" (ASR, hedged "I think"): built a digital clone of an e-commerce company's website plus 10 years of operations data, named "Shelf Life" in the Q&A; trains Claude per speaker; seven-figure/year contract with Anthropic per speaker. Three people built it.
OpenAI: anecdote about buying about 200 fake-copy websites per month at about $20K each (Codex browser training). Not a deal with Idler.
Anthropic / OpenAI: spend claims above.
Tools mentioned as data sources: Gmail, Google Drive, Slack, ClickUp, Salesforce, GitHub, Zoom, Gusto, Deel. AppSumo (valuation analogy).
Off-talk chatter (not the speaker): Profound valued at $1.8B and "prompt tracking is nonsense"; attendees building their own trackers; irrelevant to the data thesis.
Q&A (question → answer)
Do intermediaries package vertical data and sell to labs? → Some do; others build environments and sign contracts with labs (Idler "Shelf Life"/Anthropic). Some buyers dodge when asked what they do.
Are customer names mapped to anonymous tags consistently? → Unknown; they create synthetic data. OpenAI anecdote about fake websites.
What about the acceptance test / only-partial usability? → LOI, then deliver; about 30-day review, pay about 30 days later; quote may fall if only part is usable, though some buyers said subsidiaries would not raise it.
Does price vary by vertical? → Headcount moves it most (Polyshares); others weigh completeness; may depend on what labs want that month.
How do you make a company more attractive? → More verifiable headcount, recordings, GitHub, years of data; English.
Does a sale hurt later valuation? → Depends on buyer; PE likely discounts; a one-year license probably fine; compared to AppSumo base.
Exclusivity detail? → One contract allowed resale only to six named parties; others only historical data (new data free); others re-pull every 3 months for 2 years.
Rev share vs lump sum? → Rev share maybe takes 7-8 years to match; an attendee expects buyers to compete and improve terms; speaker agrees.
Media types? → Text, audio, video all taken; intake asks the medium; completeness better.
Headcount basis? → Both current and peak.
Did you do it? → Yes, quotes from Micro1 (about $500K) and Polyshares (about $100K); took the bigger; tried bidding them against each other, it failed.
Have you bought a company for data? → No, but thinks about it (old affiliate sites about $30K).
Size of the market? → Unknown; Anthropic said about $1B/yr; narrow now, expected to widen.
Why do firms sell? → Varies; some turned down $500K; one person sold data instead of the business for about $1M.
Contractor location? → Some buyers flexible (core 20 in Philippines might do); he is hunting a Mandarin buyer (he lives in Taiwan).
Why use you? → Better price or simpler, and "we can split the commission".
GDPR / Europe? → Doesn't know; large buyers do take EU data and use specialist anonymization firms, possibly American; most are California-based.
Terms of service? → Audience: check privacy policy before selling; speaker: change policy; also noted bought P&Ls often forbid training use.
Customer vs internal data? → Buyers care most about internal operations (simulating the business); only add customer data if it dwarfs internal data; employees may also need consent.
Minimum years of data? → About 2, some none, higher payers usually have minimums.
Ceiling on price? → Not standardized; very large firms could be higher.
Affiliate mechanics? → Link vs form; best approach is an intake form on your site; relationships are worth more than blog links.
Optimization-broker idea (audience)? → Speaker: yes, you can charge for the uplift; brokers may eventually license data for clients.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
Which lab for Idler: transcript says Anthropic both times (main talk and Q&A), hedged with "I think". OpenAI appears only in David's private note ("have a deal with OpenAI"), and the summary merged the two. Separately, the speaker told an OpenAI story about buying about 200 fake-copy websites per month at about $20K each; the summary left that out.
Idler details: "Shelf Life" was the clone's name; 10 years of operations data; three builders; the speaker does not know where the data came from.
Anthropic about $1B/yr "estimated spend": presented as a statement attributed to Anthropic; OpenAI "similar" is the speaker's guess.
"Merkle": the transcript says Merco/Mirko/Merkel; Mercor is the likely entity (data labeling roots, expert pay, individual applicants). The summary's "most established" is the speaker's word, "most well known"; he is "not sure" they sell company data directly.
Referral forms: the summary says Micro1 "requires form-based referrals". The transcript attaches the name/email referral form to Mercor (garbled) and says Polyshares offers both a form and an affiliate link. Micro1 referral method is not stated.
Dental practice roll-up was an audience idea in post-talk chat, not the speaker's example (the speaker only answered a dental valuation question).
Compliance/"SOC 2 equivalent for data readiness": an audience member's post-talk idea; the speaker's only comment on the broker role is that you could charge for the uplift and brokers may license data later.
"Charge for the uplift / baseline quote": also from the audience (Speaker C), agreed to by the speaker.
"Polyshares benchmarks against Spirit Airlines deal": garbled; the transcript implies a Google/Spirit Airlines comparison that looks mis-heard or mis-stated. Do not repeat.
"Smaller companies can bundle to hit the threshold": correct, about 35 total; buyers decide.
Rev share: summary says "25% rev share would take about 7-8 years to catch up if deal was $200K"; the transcript is jumbled ("if it was 200K, 100K").
Left out: payment process LOI to delivery to about 30-day inspection to payment; five questions to ask buyers; exclusivity patterns (six named buyers, historical-only, 3-month refresh for 2 years); the speaker could not get buyers to raise quotes by bidding; he quoted the largest possible size at first; contractors not in HR software; GDPR answer is "I don't know"; he's seeking a Mandarin buyer; affiliates often operate as front-end brokers ("two tiers").
Left out, commercial: Onfolio Labs' pitch is "better price or simpler pitch" plus commission split; no percentage; the summary presents the broker link as a neutral next step.
"Exclusivity: some want perpetual exclusive rights": roughly right, but the speaker says perpetual-exclusive buyers pay more and non-exclusive pay less.
Unclear / needs verification
Buyer names by ASR: Polyshares, Micro1, Trovio, Idler (AI), Shelf Life, Merkle/Merco/Mercor. Verify spellings and existence on their sites before any outreach.
Whether any buyer's "25% perpetual rev share" is accurate; speaker says "or something".
Whether Onfolio (or a subsidiary) actually closed the Micro1 deal and for how much; "we've done a couple" vs "only gone in with one".
"About 39 employees" appears in the transcript but may be Polyshares' hypothetical for his company.
Anthropic $1B/yr spend and OpenAI parity: unverified; also a garbled attendee calc ("2000 companies... 11 billion... 500K").
Spirit Airlines/Google benchmark: likely mis-heard.
Whether his lab contact's "completeness over size" was a sales line (he says it might be).
Whether the OpenAI "200 websites at $20K" claim is real; second-hand.
GDPR/consent: no real answer. Customer-data selling remains legally open; employees' consent flagged.
Onfolio Labs' commission split percentage and terms: not stated.
Actual payment received: not stated.
Death of SEO Playbooks - CMSEO — Emilio Takas (Head of SEO & Growth, Campeon Gaming, per his page; iGaming SEO)
Source: Granola https://notes.granola.ai/d/aa98b8e6-3f21-4ff9-9883-a74e998d62c4 · recorded 2026-11-12 (16:01 GMT+7) · transcript-verified 2026-11-12 Resources: https://emiliotakas.com/chiangmai/ (free, no email) · all 5 files saved to ../resources/emilio-takas/: slides PDF (99 pages, saved, not read page by page), Door Audit workbook, test card PDF (read), 30-market dataset CSV and e-bike audit CSV (both recomputed, see below) Vendor talk? No. In-house iGaming SEO, nothing sold. The third-party statistics he quotes are vendor- or agency-published, and he says so.
Thesis (3 bullets max)
Copying playbooks fails because case studies publish only wins, have no control group, and expire once they spread.
His own 30-market pull found no relationship between brand search volume and ranking position on page one. His reading: being known decides whether you are on the page at all, not where you rank.
Replace copying with a small controlled test: count inclusion rate on 50 queries, map the sites that hold the page, run one mention test against a held-back control set for 90 days.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Forbes Advisor traffic | 15.8M visits/month (Apr 2024) → 22,300 (Jan 2025), −99.86% in nine months; ~1.4M today | Semrush US organic, pulled 5 Oct 2026 | speaker | spoken + page | clear; third-party estimate |
| HouseFresh | 166 visits/month (Apr 2024) → #1 for "best air purifier" above NYT and Consumer Reports | Semrush US | speaker | spoken + page | clear; audio says "House Race" |
| 100 blogs study | median lost 85% of traffic; 49 lost 80%+; 12 went to zero; 21 grew | 100 blogs that had claimed $100K+/year, Apr 2022 → Apr 2026 | Daniel Stanica, "The Great Blogging Collapse" | spoken + page | clear; third party |
| ⭐ Brand vs rank | correlation +0.06 (0.08 without Reddit, YouTube, Amazon, Facebook) | 30 "best X" markets, 300 page-one results, 153 sites, Semrush US, 5 Oct 2026 | speaker | spoken + dataset | ✅ recomputed from his CSV: 300 rows, 153 domains, 30 markets; rank correlation 0.06 all, 0.08 non-platform |
| Typical #1 vs #8 | median 11,450 brand searches/month at #1 vs 246,000 at #8 | same | speaker | spoken | ✅ reproduces only with platform rows excluded (all rows: 36,800 vs 409,000); the talk does not say that |
| Low-brand winners | 13 of 30 #1 results are brands "almost nobody searches" | same | speaker | spoken | ✅ 13 #1s are at or under 8,100 searches/month in the CSV; his threshold is not stated |
| Concentration | 10 sites hold 41% of all slots; Reddit on page one in 27 of 30 markets, YouTube in 21 | same | speaker | spoken | ✅ recomputed: 41.3%, 27, 21 |
| Brand split | 24 big brands take 40% of the page; 71 small sites about a quarter | same | speaker | spoken | not recomputed (his size classes are not in the CSV) |
| AI answers vs signals | YouTube mentions 0.737 vs backlinks 0.218 | 75,000 brands, 2025 | Ahrefs (vendor) | spoken + page | clear; correlation, vendor-published |
| Mention then citation | brand cited 53% of the time when the model already names it vs 11% when it does not | 500K+ AI answers, Feb 2026 | Seer Interactive (agency) | spoken + page | clear; audio garbles the source |
| AI Overview sources | share of citations from the organic top 10 fell from 76% to 38% in a year | 863,000 SERPs, Mar 2026 | Ahrefs (vendor) | spoken + page | clear |
| Counter-evidence | 96% of brands described correctly when asked directly; 89% never appear for their category | Victorious via Search Engine Journal, Jul 2026 | agency | spoken + page | clear |
| Google testing | 719,326 experiments → 4,781 launched changes (0.66%) | Google "How Search works" | Google | spoken + page | clear |
| E-bike worked example | 8 sites hold half of page one; Reddit on 45 of 50 pages; "riderguide" has 0 brand searches and ranks #1 on 8 queries; example site inclusion 30% (test set 7/21, control 8/29) | 50 "best electric bike" queries, 80,850 searches/month, Semrush US, 30 Oct 2026 | speaker | page + test card | ✅ CSV has 500 rows, 50 queries, 21 test / 29 control |
| His own tooling | own Search Console tool covering ~1,770 properties | his sites | speaker | spoken (Q&A) | number garbled |
Asserted mechanisms (no evidence given in the talk)
"Being known decides whether you are on the page at all." His dataset contains only sites that made page one, so it cannot show this; he says so himself.
HouseFresh reached #1 because gatekeeper sites named it. He states he did not check links or mentions and "can't prove" it.
A model "decides who it will talk about first, then looks for a source" (inferred from the Seer 53% / 11% split).
Organic social video (Facebook, YouTube, TikTok, Instagram) and even spoken brand mentions count as mentions that help ranking ("1000%").
Correct schema for every entity matters for LLMs (one line in Q&A).
A new site shows within two to four weeks whether its structure and intent are right.
Core Web Vitals matter less than they did: most top-three sites he sees fail them.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
The Door Audit:
Inclusion rate: take 50 queries you want; count how many show you anywhere in the top 10. That share is the ceiling. Average position only describes pages you already got into. WHITE
Gatekeepers: across those 50 result pages, count slots per site and list the ~10 sites that hold half the page. The aim is to be mentioned there, not to outrank them. WHITE
One mention test against a control: one mention (review video, podcast, round-up) "for the same money as one link"; hold back a matched set of queries you leave alone; read on day 90, not before. WHITE (paid placements would need disclosure)
Test card, filled in before anything changes: hypothesis · metric (inclusion rate) · test set · control set · the one change · 90-day window · owner · day 0/30/60/90 counts. WHITE
Decision rule from the card: lift of 5 points or more over the control → fund five more; under 2 points → stop, log it, try a different mention type; in between → extend 60 days, once. Lift = test-set change minus control-set change, in percentage points. WHITE
Budget split test: the same money on links and on mentions for 90 days, judged on inclusion rate. WHITE
Change one thing at a time on a site and measure each. WHITE
Five questions before copying a case study: what was the baseline · how many tried it and never wrote it up · when did it work (before or after which update) · how long did it last · what else changed at the same time, and who benefits if you believe it.
Mentioned in Q&A, not for client use:
Recovering a tanked site by re-creating every page on new URLs without redirects or canonicals; says it picked up in two to three weeks. GREY
Burn-and-replace sites for high-value queries where a few hours of ranking pays ("best online casino"). BLACK
Autosuggest manipulation, referenced as common knowledge. BLACK
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Semrush: all of his own pulls ("a few hundred API units").
Will Critchlow / SearchPilot: controlled SEO tests; the same title change wins on one site and loses on another.
Daniel Stanica; Ahrefs (two studies); Seer Interactive; Victorious / Search Engine Journal; Google "rigorous testing" page. All linked on his page.
Kyle Roof: named as the tester the room knows. Ivana Flynn: parasite talk the same morning (C10).
Files: The-Door-Audit.xlsx (tabs: Start here · 1 Door · 2 Gatekeepers · 3 Test card · worked examples · both datasets), The-Door-Audit-Test-Card.pdf, serp-brand-dataset-30-markets.csv, ebike-door-audit-us.csv, slides PDF.
Q&A (question → answer)
Flat URL architecture → market-specific; in the Nordics his folder structure failed against sites pointing everything at the home page.
What separates top sites across the 30 markets → "only one: brand" (this contradicts his own +0.06 finding as stated; he means presence on the page).
Did links show up → he did not check links at all; the pull was built to test the "brand is key" claim.
Recovering a tanked site → new URLs (above).
Mention vs link → a named reference without a link or anchor; the words around a link have long mattered.
How long before trusting a test on a small site → two to four weeks shows whether a new site ranks; you still need some links.
Proving a change across hundreds of similar sites → one change at a time; AI audits contain errors and bundling fixes hides what worked.
Does organic social count as brand → yes; he built a brand through YouTube, influencers and broadcast instead of out-linking a richer competitor.
One Search Console for hundreds of sites → he built his own tool.
Growth-hacking brand with AI → links and mentions from different sites, plus correct schema per entity.
What to keep / drop → keep backlinks (anchor distribution, host relevance); Core Web Vitals matter less.
Advice → test a lot; collaborate.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
"HouseRace" is HouseFresh.
The summary presents "being known decides whether you are on the page" as what the data shows. It is his interpretation; the dataset has no sites that failed to make page one, and he lists that limit on stage.
Omits his stated limits: page one only; correlation runs both ways; brand search volume is a proxy; generic names inflate it.
Omits the counter-evidence he gave (96% described correctly, 89% absent from category answers).
Omits the decision rule (5 points / 2 points / extend once) and the definition of lift.
Omits that links were never checked, so the study cannot rank brand against links.
The #1 vs #8 medians hold only with platform sites removed (found on recompute; not in the talk or summary).
"Backlinks still matter… Core Web Vitals matter less" is Q&A opinion, not a finding.
Omits the grey and black tactics from Q&A (URL re-creation, burn sites).
Unclear / needs verification (mis-heard names, numbers you could not pin down)
"hostingstamp.com" as #1 for best web hosting: garbled; check the CSV before quoting.
Search Console property count (1,770 / 758).
How he classed "24 big brands" and "71 small sites".
The slides PDF was saved but not read; slide-only content is unverified.
Seer and Victorious figures were not checked against the original posts.
$50Bn in Biz Sales - CMSEO — speaker introduced as "Thomas Small" (audio); the company is FE International per the valuation link, whose founder is Thomas Smale (spelling to confirm)
Source: Granola https://notes.granola.ai/d/db38dfaa-bdc9-4cd2-98f0-f9c78d5e3481 · recorded 2026-11-12 (15:00 GMT+7) · transcript-verified 2026-11-12 Resources: https://www.feinternational.com/get-a-valuation (QR code at the end; a lead form, not opened or submitted) Vendor talk? ⚠️ Yes. M&A advisory firm; the close is a free valuation by his team. He also buys businesses with his own capital ("seven, eight figures a year").
Thesis (3 bullets max)
There is far more acquisition capital than sellable businesses, most of it in the US; any size of online business has a buyer.
AI has not changed what drives valuation: revenue growth, recurring revenue with net dollar retention above 100%, and profit.
In 2026 he would build an AI-native agency with recurring contracts, buy bloated agencies that have not adopted AI, and avoid buying businesses that depend entirely on organic search.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Private equity dry powder | $2.3T, up 2.5× in 10 years; down ~$100B in the last two years | end of 2025 | not sourced | spoken (slide graph) | clear; unsourced |
| Deal volume | over $2.8T in deals | H1 2026 | not sourced | spoken | clear; unsourced |
| Tech / online share | ~$650B, about a quarter of the total, growing 90% year on year | H1 2026 | "data we have internally" + Claude as analyst | spoken | clear; unsourced |
| Regional growth | EMEA +89% · Americas +74% · Asia-Pacific +24% year on year | same | same | spoken | clear; unsourced |
| Example deal | ~$75M sale (rounded) to a private equity firm; 11 offers; 90% cash at close, 10% after 12 months | one SaaS business, sold ~12 months ago | speaker (his firm ran it) | spoken | clear; anonymized, unverifiable |
| Example business metrics | 8-figure ARR · 43% growth year on year · 110% net dollar retention · 17% customer churn · one founder · 75 staff · remote · product-led, no real sales team · profitable | same business | speaker | spoken | clear |
| E-commerce multiples | 4–8× profit for businesses making $500K+ profit; multiples change above ~$10M profit | 2026 | speaker | spoken | clear; his range |
| His own group | ~250 team members across his businesses, cut ~20% this year, more to come | his companies | speaker | spoken | clear |
| Peer anecdote | someone cut their team 90% this year with better output | one conversation | hearsay | spoken | hearsay |
| ⭐ His firm's lead sources | ChatGPT went from almost no traffic 12 months ago to the number one source of leads; organic traffic has fallen over the same period | FE International | speaker | spoken | clear; no numbers given |
| Anthropic | going public "next week"; net dollar retention "something like 800%" | — | speaker, "I think" | spoken | unsourced; do not quote |
| First business | bought for ~$50, sold for ~$150 | personal | speaker | spoken | anecdote |
Asserted mechanisms (no evidence given in the talk)
Number of founders, and remote vs office, have "zero correlation" with valuation (no data shown).
Year-on-year growth decides sellability "in 99.99% of cases".
Losing low-paying customers on purpose raises valuation if net dollar retention stays above 100%.
The 75-person example could now run on 15–25 people with AI (his guess).
Agencies are the most undervalued model; businesses that rely only on free organic traffic with no moat are the most overvalued.
A good M&A process gets most of the cash at close; bad outcomes come from bad processes.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
What he says raises valuation:
Add a recurring element to revenue, whatever the model. WHITE
Build ways for existing customers to pay more over time (usage, upgrades), so net dollar retention is above 100%. WHITE
Stay profitable while growing, unless venture-funded software. WHITE
Fire high-hassle, low-paying customers. WHITE
Do not add headcount where AI can do the work; cutting later is hard. WHITE
Build / buy / avoid (2026):
Build: an AI-native agency with recurring contracts, selling to businesses, in a category where the spend is non-discretionary; or SaaS with a single developer; and only something you are interested in. Invest in reputation early (16 years in, he says he does essentially no marketing).
Buy: creator / influencer businesses where the founder can be removed (faceless channels, YouTube); bloated agencies and service firms not using AI; businesses with distribution that is hard to copy but a weak product or margin.
Avoid buying: businesses that are already AI-native where the founder knows more than you; businesses 100% reliant on organic search; anything picked because someone else said so.
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
FE International: his advisory firm; free human-made valuation at https://www.feinternational.com/get-a-valuation.
Claude: his "analyst" for the market slides.
Carl (conference organizer): reviewed the draft slides and asked for a real deal and for the build/buy/avoid list.
Q&A (question → answer)
Favorite business bought → the first one ($50 → $150); the first dollar is the hard part.
Most undervalued / overvalued → agencies / organic-only businesses without a moat.
Model for a $10–50M exit in 5–7 years → agency or SaaS; he would pick an agency, B2B, non-discretionary spend, reputation first.
Good at SEO sites: scale that or build SaaS → double down on what works; diversifying was a mistake for him. He explicitly tells site owners to ignore his "avoid organic" line if their portfolio is working.
Vibe-coded businesses → fine for internal process tools, not something you can build to sell.
What sold most → by deal value, SaaS and AI companies (he treats them as the same thing).
E-commerce multiple to aim for → do not aim for a multiple; take the dollar figure you would retire on.
Is SaaS dying → no; he expects a record year, but buyers now ask how exposed the product is to AI.
Thousands of sites: sell as one or split → ten years ago together; now he leans to smaller groups, but says there is no single answer (audio partly garbled).
A business he could not wait to exit → the ones he bought without real interest.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
"Fein International" is FE International.
Omits the most relevant line for us: ChatGPT is now his firm's top lead source while organic traffic declined.
Omits that every market figure is unsourced and partly produced with Claude from internal data.
Omits that "avoid organic-reliant businesses" is acquisition advice only; he says such a business can still be a good one to own.
Omits the "zero correlation" claims (founder count, remote work) and that no data backs them.
Portfolio question: the summary says "no universal answer"; he also said his default has moved from selling together to splitting.
The Anthropic IPO / 800% retention remark is speculation and should not be repeated.
The title's "$50Bn" figure is never explained in the recording (it starts mid-introduction).
Unclear / needs verification (mis-heard names, numbers you could not pin down)
Speaker surname (Small / Smale).
Sources for the $2.3T, $2.8T and $650B figures.
"fake Hoffman" after "11 offers": garbled.
Whether the 90% in "growing 90 year on year" is the tech share's growth or total deal growth.
Scale Content: Agentic system for unique content — speaker addressed as "George" by the MC (summary says "Georg"); co-founder of Rank Up, an SEO tool
Source: Granola https://notes.granola.ai/d/3dfb6a60-7cf9-4e0d-9d4d-d8486703fc3f · recorded 2026-11-10 (4:00 PM GMT+7) · transcript-verified 2026-11-12 Vendor talk? Yes, lightly. Speaker presents "Rank up, our own SEO tool" (ranks #1 for "best SEO AI writer" and "B2B SEO tools" per speaker) and runs client work (Guardian Home, Cream). He mentions his co-founder. The knowledge-base system itself is given away via a Google Slides link with no email gate. Focus here is what was spoken beyond the deck.
Thesis (3 bullets max)
Originality is pushed by Google guidance and, per the speaker's ongoing study, unique first-party material (own experience, own measurement, customer proof, tests, screenshots) is associated with holding top-3 positions; formatting tricks are not.
A four-part agent system (knowledge base, new content, existing content enrichment, feedback loop) distributes unique material into as many pages as possible and interviews the human for what is missing.
Goal is "distribute your unique knowledge", not "make every article fully original"; fully unique articles did worse in his experience.
Measured claims
All numbers below are the speaker's own; the study is "ongoing" and not independently verifiable from the transcript. No sample base for any percentage beyond the headline is given.
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Study scale | 7 markets, 250 SERPs, 3,000+ ranking pages, 400,000+ statements ("points made in the content") | Last 90 days; seven B2B software and service markets | His company (Rank Up) | Spoken over slide | Clear |
| Own experience in intro | 5.5x | Multiplier = how much more often pages that held top 3 had it, compared with pages Google dropped; denominators not stated | Rank Up | Spoken over slide | Clear |
| Own measurement in explainers | 4.4x | Same definition | Rank Up | Spoken | Clear |
| Customer proof in alternatives and pricing pages | 3.6x | Same | Rank Up | Spoken | Clear |
| Test shown in best-of lists | 2.4x | Same | Rank Up | Spoken | Clear |
| Screenshots (general) | 2.4x | Same | Rank Up | Spoken | Clear |
| Four to seven kinds of unique material | "20% of the pages" with 4-7 kinds held top 3, vs pages with 0-2 or 3 kinds (their percentage not said) | Same 90 days; statement is ambiguous: 20% of pages in that bucket held top 3, comparator rate not stated | Rank Up | Spoken | Partly garbled; comparator missing |
| Four-plus kinds vs zero-to-two | "almost two times as often" held top 3 | Same | Rank Up | Spoken | Clear |
| Intro vs elsewhere | 1.8x in intro vs 1.5x anywhere else on page | Top-3 holders vs dropped pages | Rank Up | Spoken | Clear |
| Small sites with 6+ kinds | "as often as 17% of the time" held top 3; then he says "70% of the small site pages ... held the top three" | "Small site" never defined (no DR/traffic cutoff); base not stated | Rank Up | Spoken | GARBLED: 17% vs 70% in the same sentence. Summary used 17% |
| Formatting correlation | Zero correlation for length, FAQ blocks, fresh dates, prices section, and "40 other" factors (garbled phrase) | Same pages | Rank Up | Spoken | "40 other" garbled |
| Output of his system | 299 (about 300) blog posts by him in the last six months; ranked and held top three for 481 searches, top five for 1,200 searches | Counts are SEARCHES (queries), not posts; his sites; period 6 months | Speaker | Spoken | Clear |
| Cyrus Shepard study | 92% of winning sites have proprietary assets | Cyrus Shepard's study; sample not stated | Cyrus Shepard | Spoken | Clear (third-party) |
| Google March 2024 core update | 45% less low-quality, unoriginal content | Google's claim | Google | Spoken | Clear |
| Stat example from competitors | "checkout converting 55% higher" | Example in a Cream (merchant of record) article | A competitor | Spoken over slide | Illustrative only |
| Test example for Rank Up | A feature took about 25 minutes; one tool's average article was 700-900 words | Rank Up article on best SEO AI writer | Rank Up | Spoken over slide | Illustrative only |
How "held top 3" and "dropped" were defined (as spoken):
"Held the top 3" = a page that stayed in Google's top 3 over the 90-day monitoring period.
"Dropped" = pages that "went in and out of the top 10" or that Google "dropped from the top 10 results". He uses both phrasings; the comparator group is pages that fell out of the top 10 versus pages that held the top 3.
Multiplier = frequency of a given unique-material type in the top-3 holders divided by frequency in the dropped group (inferred from "5.5 times more ... in pages that held the top 3"; the arithmetic is not explained).
Unique material is defined as information unique to the business/product, not claims of being first in the world.
"Statements" = points made in the content, 400,000+ of them, presumably classified (method of classification not stated; presumably an LLM, not stated).
Caveats the speaker admitted:
The study is "ongoing".
"Not the single thing you need" and he is not promising top rankings.
Too much uniqueness hurt: fully unique articles did worse and sometimes did not reach the top 10 (anecdotal from their own content; no number).
Intro advantage (1.8 vs 1.5) is "not a crazy difference".
Four to seven kinds is "not a crazy amount" but a sweet spot.
The system took 3-6 months of testing; it will need refinement, and agents will make mistakes at first.
He has not tested reusing a fact where it does not fit; only relevant reuse; saw no harm.
He does not address generic AI copy or brand voice (scope).
Not stated: backlink/domain-authority controls, significance tests, geography, query intent mix. Treat as correlational, vendor-run.
Asserted mechanisms (no evidence given in the talk)
Google is pushing originality: added an originality section to its Creating Helpful Content guidance on 5 October 2026 (per speaker), defined as the extent to which the content offers unique original information or perspectives not available elsewhere; the AI optimization guide lists unique information types. Date and wording are as spoken, unverified here.
Small sites can beat big brands with unique material.
Intro placement matters most.
Decision-stage pages (best-of lists, reviews, X vs Y) deliver the most return; then how-tos and top-of-funnel.
Agent interview plus knowledge base is the best way to capture missing material.
GPT is a safer writer than Claude because Claude may watermark (precaution, no evidence).
Distribution of the same unique facts across many pages is not harmful if relevant.
Lily Ray's agency recommended first-hand experience, primary sourcing and original data (summarized by speaker; no figures).
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
He gave the design, not prompts (prompts are in the slide deck; "not quite as simple"; 3-6 months to figure out). (all WHITE unless noted)
Build the knowledge base ("filing cabinet", one per client, folders/MD files). Five drawers: tests (e.g., feature timings, average word counts); customer stories (e.g., a YouTube video supporting product claims); photos/screenshots/videos of product or service; research/statistics (own versions of stats that winners use); own experience (hands-on testing, screenshots of the feature).
Mine stats the winning competitor articles use; create your own versions (e.g., original surveys/data).
Build a claims table: each product claim mapped to proof (case study, video, testimonial, demo). Back up what you can, not every claim.
New content: replace the content brief with a "content blueprint": outline, points per section, and unique knowledge mapped to each section from the knowledge base or from new insights. Cover the basics first, then add unique material.
If knowledge is missing, the agent interviews the human (during blueprint creation, or after the outline). Answers feed back into the knowledge base automatically.
Have the agent add comments inside the draft (Notion, Google Docs) for follow-ups; answer the comments.
Existing content: compare your page to the current top result for the main keyword, list gaps, fill from the knowledge base, interview for the rest. The agent proposes each edit; human accepts or rejects (he uses Claude for other content types here).
Prioritize: decision pages first (best-of, reviews, X vs Y); big proof (case studies) inserted immediately; small facts batched.
Loop: new insights feed the knowledge base, which enriches future pages and existing ones.
Agency rollout: start with about 5 clients (those performing worst or most in need of a win), refine, then scale; separate knowledge base per client; "everything shown is the minimum viable system". Tools and models: Claude for the systems and for proposing edits; GPT for the actual content writing, with handoffs from Claude to GPT, because of the watermarking concern. Notion and Google Docs for comments. No prices given.
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Rank Up (spelled "Rank up"): speaker's own SEO tool; examples used.
Guardian Home: client; elderly-care software and hardware; #2 for "best nurse call systems".
Cream: merchant-of-record platform; #2 and in AI Overviews for "merchant of record versus payment processor".
Phrase: reviewed product; Rank Up is #2 for "phrase review" below Trustpilot, also in AI Overviews.
Lily Ray's agency: research recommending first-hand experience; agency name not said.
Cyrus Shepard: "proprietary assets"; 92% of winning sites.
Google: March 2024 core update; Creating Helpful Content guide; AI optimization guide.
Claude: his systems and edit proposals; GPT/ChatGPT: content writing; Notion and Google Docs: draft comments.
Google Slides deck (from private notes): https://docs.google.com/presentation/d/12YjcBemWtJdjveibelxsGK9mJg85fYAX/edit; contains prompts, notes, and a link to the study (QR code shown).
Salt and Fire rooftop bar: event after-party, irrelevant.
Q&A (question → answer)
I rewrite 20-30% of Claude output; is that a waste? → He uses ChatGPT for content writing now (because of the Claude watermark worry); rewriting is fine; his own rewrite share is higher; this system adds substance and does not fix copy.
Minimum viable setup for a small agency with 30 clients? → The whole system shown is the minimum; nothing in it is optional if you do not already have a version; give the deck and prompts to Claude/GPT to build it; new folder or MD files per client; start with a few (about five) of the clients that most need a win, refine, then scale.
Concerned about AI watermarking? → Yes for Claude; that is why he writes with GPT, with handoffs from Claude; will find another fix when GPT starts watermarking.
Can you reuse the facts across pages; will it limit impact? → He has not seen harm; reuse where it adds substance to a claim; system is built not to inject into every article; the opposite case is untested.
How to stop agent-written content from sounding generic? → Out of scope; offered to give another talk on brand voice.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
Speaker name: MC says "George" at the end; the summary note says "Georg" in the task prompt; the transcript never gives a surname.
"Small sites with 6+ kinds held top 3 17% of the time": the transcript has both 17% and 70% in the same breath; garbled, not safe to cite.
"Personal results: 300 blog posts, 481 ranking in top 3, 1,200 in top 5": the 481 and 1,200 are SEARCHES (queries), not posts, over the last six months.
"Too much uniqueness actually hurt rankings" is listed as a study finding; the speaker presented it as experience from their own content, not as a study number.
"Multipliers (top 3 vs dropped pages)" correct; the summary left out that "dropped" is also described as pages that went in and out of the top 10.
"20% of pages with 4 to 7 kinds held the top 3": comparator rate not stated.
Summary omits: the Oct 5, 2026 Google guide change (as spoken), Lily Ray's agency, Cyrus Shepard's 92%, March 2024 update 45% claim, that it is a Rank Up vendor study, and the 3-6 months build time.
Summary omits the specific client examples (Guardian Home, Cream, Phrase) and the rankings claimed.
Summary "Formatting has zero correlation": right; "40 other" factors garbled.
Summary omits that no prompts were shown and that the deck holds them; also that the agent proposes edits and adds comments in Notion/Google Docs (the summary has the latter).
Summary Q&A "20 to 30% rewriting ... fine": fine, but the answer is mostly about his switch to GPT.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
17% versus 70% for small sites with 6+ kinds; definition of "small site".
"40 other ones" for non-correlating formatting factors.
Comparator percentage for the 20% (4-7 kinds) claim.
Meaning of "91" and "quo plan" in the free-plan aside (garbled).
The claim that Google changed its guide on 5 Oct 2026; verify against Google's page.
How "statements" were classified and how unique material was tagged (not said).
Is "Rank up" spelled RankUp; the link to the study (QR code, not spoken).
Surname and company spelling: "George"/"Georg" and "Rank Up".
Building company agents: twelve pieces in four layers — Ian Borders (Claude ambassador for Thailand; founder, Kybernesis; venture investor in Thailand)
Source: Granola https://notes.granola.ai/d/9ad2ee5e-a71e-4ef7-8b5e-797f597b29b2 · recorded 2026-11-15 (14:59 GMT+7; Granola shows 11-14 23:59 PST) · transcript-verified 2026-11-16 (full transcript read, 28.3k chars, about 35 minutes incl. Q&A) Resources: 7 slide photos saved to ../resources/ian-borders/photos/ (all read; 01–03 are the same slide). URL from the note-taker's private notes: https://ian.kybernesis.ai/ (not spoken). He made the slides "in the car" with his own agent. Vendor talk? ⚠️ Yes. Kybernesis is a forward-deployed engineering company that sells company agents (mostly on Claude Enterprise / Claude managed agents) to large Thai companies, and a memory product (Arcana, formerly called Kybernesis); a school program was announced at the end. He also points to agentid.dev without stating his relationship to it. Every number is his own.
Thesis (3 bullets max)
Models are now good enough that a company needs one agent, not many: one named agent the whole company talks to, routing work to declared sub-agents nobody sees.
A company agent needs twelve pieces in four layers (who it is, what it knows, what it can do, what keeps it safe); "leave one out and you have a demo, not a teammate" (photo 01).
Safety comes from programmatic layers outside the model (identity, policy, vault, control plane), not from the model's judgment.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Memory recall | 99.8% "perfect", later 99.7% recall accuracy | no benchmark, dataset or test named | his company (Arcana) | spoken | vendor claim, untestable as stated |
| Memory token cost | ~40,000 tokens per query → ~500–600 with his memory system | one example ("ask your Claude agent about a marketing campaign") | his company | spoken | single illustrative example; no method |
| Vercel's internal agent | used daily by 2,000+ employees | spoken as "AT B… E to Agent from Vercel" | relayed | spoken | ⚠️ product name garbled; not checked |
| Ambient voice cost | ~5 cents a minute → ~$30/day at 10 hours | his own use | speaker | spoken | arithmetic checks (600 min × $0.05 = $30) |
| Software factory | Docker sandbox with ~15 agents doing end-to-end tests before merge | his setup | speaker | spoken | description, no defect or speed data |
| Spend cap example | $5,000 virtual-card limit; every purchase needs a phone approval | his setup | speaker | spoken | example |
| Memory build | "sleep-time compute" runs hourly over all memories; now two databases (vector store + a basic store for clusters), once five | his system | speaker | spoken (Q&A) | description |
| Agent age | his agent "Samantha" ~3 years old | — | speaker | spoken | anecdote |
| Big-lab PR volume | "Boris" at Anthropic and someone at Grok push 2,000–4,000 PRs a day | hearsay | relayed | spoken | ⛔ unsourced; do not quote |
Asserted mechanisms (no evidence given in the talk)
There is "no reason to separate agents" any more; multi-agent products that look like a team are one agent isolating context (he cites a product spoken as "Rockbot"; the note-taker's private note says Grok).
Agents hallucinate when they cannot afford the tokens to fetch the real data; good memory removes the shortcut. Hallucinated business numbers do the most damage (Q&A).
A policy engine outside the model makes manipulation "impossible": the policy decides, not the LLM.
A persistent computer beats tool calls and connectors for systems without good APIs.
A cheap reasoning gate comparing signals across systems lets an agent act proactively, and trust grows as the owner approves repeated actions.
A queued, end-to-end-encrypted mailbox beats A2A/HTTPS because both agents need not be online.
The stack should be model-agnostic and run on servers you control (rented private servers are enough).
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
The twelve pieces (photo 01) with what he does for each:
Identity: the agent gets its own name, @mention handle, lookup address and a signed card proving ownership (photo 04: "samantha.agent", badges "owner verified · connected · signed card"). He buys a ".agent" identity via agentid.dev (built on Handshake, per him). "Without it: it runs on somebody's personal login; when that person leaves, the agent's access, history and accountability leave with them." WHITE
Multiplayer: one agent, many people; in each conversation it uses that person's connectors and memory plus its own, and never mixes them across people (he names Claude Tag in Slack as an example of the pattern). WHITE
Declared sub-agents: the named agent is a router to unnamed specialist agents (engineering, marketing, sales, finance); cross-department data passes only where permissions allow. WHITE
Memory: intake engine decides what to keep → memory pipeline → entity graph + vector store → hourly "sleep-time" job builds relationships and clusters; multi-hop retrieval. WHITE
Its own computer: a persistent VM with desktop and browser that people can watch, take over and hand back, with a screenshot for every click (photo 05). WHITE
Vault: logins are pasted programmatically from an encrypted vault (1Password-style) so the model never reads passwords or environment variables; or a human takes over the VM and types the password. WHITE
Payments: prepaid virtual cards (Mercury) with a hard cap; every purchase triggers an approval on the owner's phone. WHITE
Engineer ("software factory"): a sub-agent spins up a Docker sandbox with ~15 agents that build and run end-to-end tests before anything reaches production. WHITE
Routines + "Magic": scheduled routines, plus proactive mode: compare signals across systems, a low-cost model decides whether to reason further, then act (his example: a Facebook ad burning budget too fast → alert, later auto-pause once trusted). WHITE (GREY if auto-acting on client accounts without a recorded approval rule)
Voice: an ambient "multiplex" voice agent in an earbud $30/day); a decisions model trained on his voice decides when to respond and ignores other speakers (spoken "JED"/"Jedi… Decisions API"). WHITE (GREY: it listens to client meetings; consent not discussed)
Agent to agent: end-to-end-encrypted mailbox bus; messages queue when the other agent is offline. WHITE
Control plane + ownership: per-person grants managed centrally, each speaker resolved to a verified identity, exportable audit and inspectable memory, revoke anyone "everywhere in seconds", admin alerts on access attempts (photo 06); model of your choice on servers you control. WHITE
The test (photo 07): twelve yes/no questions; "a no on any of them means you have an assistant, not a company agent."
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Kybernesis (his company; spoken "Kyber Uses", "Kybernesis", "Kyrenesis"): forward-deployed engineering; sells company agents and a school program. https://ian.kybernesis.ai/ (from the note-taker's notes). No prices.
Arcana: his memory system, formerly named Kybernesis.
agentid.dev: buy a ".agent" identity; ties ownership and permissions to the agent. Built on Handshake (per him).
Cedar (AWS open-source policy language): the policy layer behind his identity system; approvals are counter-signed and logged.
Claude Tag (Claude in Slack), Claude Enterprise, Claude managed agents: what he deploys on. Also names OpenClaw-type tools generically ("Mont, Hermes"), Muse, Duet (garbled list).
Vercel internal agent (spoken "AT B", "Eve"; garbled).
1Password-style vault; Mercury virtual cards; Stripe (Link) mentioned for agent payments; "card sh…" (garbled).
"JED"/"Jedi… Decisions API" for voice turn-taking; the note-taker's notes say JEV, which matches TypeSafe Jev, a decisions model available via OpenRouter.
Clients named: CP Group (owns 7-Eleven in Thailand), "PT Gas" (likely PTT). First official Anthropic event in Bangkok "next Friday the 20th". Anthropic opened a Singapore office (per him).
He says he built a national payment back end in Thailand ~17 years ago (spoken "prom to pay"; possibly PromptPay; unverified).
Slide photos
Full text of each slide: ../resources/ian-borders/slide-text.md
01-anatomy-twelve-pieces-four-layers.jpg: "The anatomy. Twelve pieces, in four layers. Leave one out and you have a demo, not a teammate." Who it is: 01 Identity, 02 Multiplayer. What it knows: 03 Memory. What it can do: 04 Its own computer, 05 Vault, 06 Payments, 07 Engineer, 08 Routines, 09 Voice, 10 Agent to agent. What keeps it [safe]: 11 Control plane, 12 Ownership.
02-anatomy-twelve-pieces-duplicate.jpg: same slide.
03-anatomy-twelve-pieces-full-labels.jpg: same slide, shows the full row label "What keeps it safe".
04-identity-samantha-agent-card.jpg: "01 · Identity. It has a name other agents can verify. A company agent needs its own identity, not a borrowed employee account. A name people can find and @mention, an address other systems can look up, and a signed card that proves who owns it." Card: Samantha, samantha.agent, "Company agent. Sales, engineering, finance, research and ops, for the whole team." Badges: owner verified, connected, signed card. A "since" date on the card is too small to read.
05-its-own-computer-take-over-hand-back.jpg: "04 · Its own computer. A persistent computer, not a tool call that pretends. Connectors cover the systems with good APIs. For everything else, the agent needs a real desktop and browser it can see: one people can watch, take over and hand back, with a screenshot for every click." Mock: a checkout page at $2,556.00, "Samantha-computer · live · take over · hand back". The "without it" text is partly hidden (mentions bank portals and government sites).
06-control-plane-between-person-and-agent.jpg: "11 · Control plane. A control plane sits between every person and the agent. This is the piece that makes the rest safe to share. It decides who can talk to the agent, who it acts as and what needs a yes, and it keeps the record. Revoke someone and they're out everywhere in seconds." "Who can talk to it: grants per person, managed centrally." "Who it acts as: each speaker resolved to a verified identity." "What it remembers: …exportable audit… memory you can inspect, correct" (partly hidden by phones). Diagram: four people → control plane → Samantha ("4 grants · 4 ve[rified identi]ties").
07-twelve-questions-for-any-company-agent.jpg: "The test. Twelve questions to ask of any company agent. A no on any of them means you have an assistant, not a company agent." 01 own name and identity? 02 does every turn run as the person who asked? 03 remembers the company and keeps each person's memory private? 04 own computer for systems with no API? 05 uses logins without the model ever seeing them? 06 [does every] purchase need a person's yes? 07 can it ship code without touching production on its own? 08 recurring work without being asked? 09 can you talk to it, with the sa[me] memory and tools? 10 works with other ag[ents only on] edges you granted? 11 can you revoke anyone [and] export the audit? 12 runs on your serve[rs with the mo]del of your choice? (Bracketed words hidden by the speaker.)
Q&A (question → answer)
(Host) Where do hallucinations do the most damage? → Business numbers.
(Attendee) Do you run local models (Mac Mini, DGX) or cloud (Vertex/Gemini)? → Garbled; he says they use state-of-the-art models and the choice is per company. No clear answer.
(Robert) What databases sit behind the memory? → Once five systems, now essentially two: a vector store and a basic database holding clusters; an hourly sleep-time job builds relationships between vectors and clusters; retrieval is multi-hop.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
"Programmatic, not LLM-based, so access decisions are non-deterministic": backwards. He said "non deterministic" but his point is that the policy layer, not the model, decides, which makes access deterministic.
"Four layers: identity, memory, compute (own VM), control plane": the slide has twelve pieces in four layers: who it is (identity, multiplayer), what it knows (memory), what it can do (own computer, vault, payments, engineer, routines, voice, agent to agent), what keeps it safe (control plane, ownership).
"Grok's agent feature is a facade": the transcript says "Rockbot"; Grok comes from the note-taker's private note. Unresolved which product he meant. "Rockbot" is also said to have its own VM and a calling feature.
"JEV (Decisions API)": spoken "JED"/"Jedi"; JEV is the note-taker's spelling.
"Arcana system" and "99.7–99.8% recall": vendor claims with no test named.
The summary omits the twelve-question test, the vault take-over path (human types the password in the VM), the "without it" failure for identity (agent leaves with the employee), model-agnostic hosting from a Claude ambassador, and that Kybernesis sells all of this.
The private notes ("look at @claude tag", "look at agentid.dev", "look up multiplex voice systems") are the note-taker's to-dos, not the talk's next steps.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
Speaker name: "Ian Borders" is from the Granola title only; the transcript intro is garbled ("your warriors").
"Rockbot" vs Grok; the Vercel agent's name ("AT B", "Eve"); "Mont, Hermes, Muse, Duet".
Whether "JED/Decisions API" is TypeSafe Jev.
His relationship to agentid.dev (owner, partner or user).
"Prom to pay" (PromptPay?) and the "entire country runs on it" claim.
Memory figures (99.7–99.8%, 40,000 → 500–600 tokens): no benchmark.
Agentic Search and Optimizing for Agents (opening talk) — Jabez Reuben (LLM Mastery host)
Source: Granola https://notes.granola.ai/d/08b4e7bf-a4f6-4cd7-b5a8-6e4c16b26897 · recorded 2026-11-14 (10:18 GMT+7; Granola 11-13 19:18 PST), LLM Mastery 4.0 day · transcript-verified 2026-11-16 Resources: ../resources/jabez-reuben/photos/: 6 slide photos saved and read (slides 21, 31, 34, 35 ×2, 36 of 38). Slides offered by QR code at the end; not obtained. Vendor talk? Partly. He hosts LLM Mastery (the event, rebranded from "link building mastery"); no product or price pitched in the recorded part. Several examples are his clients' campaigns, unnamed.
Recording is about 8.5 minutes and starts mid-talk ("agentic race" section); slides 1–20 were not recorded. At 8:46 the host introduces the next speaker (Robert Niechciał, C15).
Thesis (3 bullets max)
Agent traffic and agent token use now exceed human use, and agents get their own search, review and commerce infrastructure.
Agentic optimization has two stages: get onto the agent's shortlist (top 5–10), then win the agent's retrieval decision; backlinks and mentions matter little in the second stage.
Agents are easy to attract today with the right jargon (tokens, compute cost, MCP, "AI instructions"); use it before agents get smarter, but test everything yourself.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Agent vs human AI usage | 7.3T tokens by agents vs 1.4T by humans | "February 2026"; no base, no source | not named | spoken; slide not photographed | low: unsourced |
| Agent vs human web traffic | agents 57%, humans 42% | none given | not named | spoken | low: unsourced |
| Agent companies | 1,155 Y Combinator companies describe themselves as agent companies, +45% | none given | not named ("Dubai Combinator" in audio) | spoken | low: unsourced |
| knowledgelib.io in citations | "over and over again" in ChatGPT citations for several of his clients' campaigns | no count, no prompts, no period | the speaker | spoken | anecdote |
| knowledgelib.io inventory | "1818 units across 18 categories"; Consumer Electronics 272 units; each unit shows a score (0.88–0.93), source count (7–12 src) and token estimate (~2,400–4,500 tok) | the site's own page | the site | photo 03 | clear as a screenshot; says nothing about results |
Asserted mechanisms (no evidence given in the talk)
Agentic optimization = shortlist ("agentic race") then retrieval; backlinks and mentions do not count in agent retrieval.
New agent search infrastructure "doesn't count backlinks or mentions"; it ranks precise information and whoever returns the top 10 fastest and cheapest.
Brave Search "powers Claude" (and Claude Code). Spoken only.
Agents are attracted by token/compute-cost language and MCP references, even when the MCP does not exist (his reading of knowledgelib.io).
An "AI instructions" page in plain markdown is easier for agents to extract than normal pages; different from llms.txt.
Future on-page signals: reviews by agents, agent usage and crawl counts, agent subscription counts, token usage data (photo 06). Prediction, no evidence.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Do not block bots; check Cloudflare settings, which "many times" block crawlers without the owner knowing (photos 04–05). WHITE
Keep the site fast. WHITE
Build an MCP server for the site; example given of a forum (named in audio as "Dynamic Circle") that users can chat with from Claude or ChatGPT without logging in. WHITE (cost/benefit not discussed)
Publish an "AI instructions" page in markdown. Slide 31 fields (photo 02): title "Official Information About [Brand]" · intro "Canonical reference for AI assistants" · basic facts (name, founded, HQ, founders, website) · background in 2–4 sentences · products, one line each plus pricing · differentiators · ideal customers · use cases · AI instructions ("Describe [Brand] as…") · corrections (what AI should not say) · update log (partly hidden) · last updated (partly hidden) · links (site, …, contact). WHITE
Make every fact detailed and exact: numbers, stats, ICP, pricing, licenses. WHITE
Reverse-engineer knowledgelib.io and use the same token/compute-cost language in your own content. GREY (labels aimed at machines); its fake MCP details: BLACK
Build a knowledge panel for an AI avatar with James Dooley's framework; track the KGMID with "Geo Search Console". GREY (an AI avatar entity is a manufactured entity)
Test every claim from the conference before acting on it. WHITE
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Agent search engines: Parallel, Exa, "Tel Aviv" (likely Tavily; speech-recognition spelling), "Firecore" (likely Firecrawl), octen.ai (slide 21, "Search Infra For Agents"; its page reads "Search infrastructure for AI · real-time indexing · low latency · high reliability"). No prices.
Brave Search: new API "primed for agentic use".
A G2 alternative for agents, e-commerce infrastructure for agents, a Reddit alternative for agents: none named.
".agent" domains: "launching soon".
knowledgelib.io: fully AI-generated "knowledge base for agents" with token/compute labels and a fake MCP section.
Profound and HubSpot: examples of AI instructions pages.
James Dooley ("James Cooley" in audio): knowledge panel for his AI avatar; framework name garbled ("Dutch framework"; Granola: "DUDs").
"Geo Search Console": said to track KGMID; not identified.
Slide photos
Full text of each slide: ../resources/jabez-reuben/slide-text.md Saved in ../resources/jabez-reuben/photos/ (6):
01-search-infra-for-agents-octen.jpg — slide 21/38 "Search Infra For Agents · octen.ai" with a screenshot of the Octen homepage ("Search infrastructure for AI"; real-time indexing, low latency, high reliability). Lower half blocked by heads.
02-ai-instructions-page-13-fields.jpg — slide 31/38, the 13-field AI instructions page (listed in tactic 4). Items 11–13 partly hidden by a head: "Update log … changes", "Last upda… …rter" (likely "quarterly"), "Links: site, … contact".
03-knowledgelib-knowledge-units.jpg — slide 34/38, knowledgelib.io page "Available Knowledge Units (1818 units across 18 categories)", Consumer Electronics (272 units), Audio list, e.g. "Acoustic Guitars Beginners (2026) — 0.90 · 11 src · ~3,600 tok", "Av Receivers (2026) — 0.93 · 12 src · ~4,500 tok".
04-on-page-essentials-for-agents-partial.jpg — slide 35/38, same as 05, speaker blocks items 3–5.
05-on-page-essentials-for-agents.jpg — slide 35/38 "On Page Essentials for Agents": 1 not blocking any bots (Cloudflare settings) · 2 speed · 3 MCP · 4 instructions & guidelines for agents · 5 detailed information (numbers, stats, ICP, pricing, etc.).
06-future-of-on-page-for-agents.jpg — slide 36/38 "Future of On Page for Agents": 1 reviews by agents · 2 agent usage & crawl count · 3 agent subscription count · 4 token usage data.
Q&A (question → answer)
None. Opening talk; the host moved straight to the next speaker.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
"30 guidelines available for creating one": the slide shows a 13-item list. "30" is probably a mishearing of "13".
"Firecore" is a speech-recognition spelling (likely Firecrawl); the summary drops "Tel Aviv" (likely Tavily) and octen.ai, which is on the slide.
"Look up the DUDs framework", "Download Brave", ".agent domains", "Knowledgelib.io: mcp guidelines / write about token usage" are the note-taker's private notes; the summary turns them into speaker next steps.
"KGMIT" is KGMID (Google Knowledge Graph machine ID).
The summary presents the 7.3T / 1.4T, 57% / 42% and 1,155 / +45% figures as facts; no source was given for any of them.
Omits that the recording starts mid-talk and that the talk's own rule was "test everything before acting on it".
Omits the "future of on-page for agents" slide.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
Sources of the token, traffic and YC figures.
Whether Brave Search powers Claude's web search (widely reported, not checked here).
"Dynamic Circle" forum MCP; "Geo Search Console"; the Dooley framework name.
"Tel Aviv" = Tavily and "Firecore" = Firecrawl are guesses from sound.
Slides 1–20 not recorded; the deck was not obtained.
Jacob Kettner - CMSEO — Jacob Kettner (agency owner; "First Rank" named only in a host question, ~30 people; toolkit titles the talk "Why Good Agencies Fail")
Source: Granola https://notes.granola.ai/d/a4ba37da-e860-48a5-a457-56afdaa64e6b · recorded 2026-11-12 (14:03 GMT+7) · transcript-verified 2026-11-12 Resources: public Google Drive folder (no opt-in) https://drive.google.com/drive/folders/1bd5QGe0xAyn0PYrMDF8pVyqXOXmUn4au · all 7 files saved to ../resources/jacob-kettner/ and read (PDF + both .md in full; the 4 workbooks downloaded, not opened cell by cell) Vendor talk? No. Nothing sold; the whole framework is given away. Agency is ~80% SEO by his own description.
Thesis (3 bullets max)
Agency margins erode as non-revenue hires (managers, admin, sales, marketing) are added, because pricing was set for the smaller agency. Price for the cost structure you are growing into, before you get there.
Every revenue dollar belongs to one of six buckets (fulfilment, overhead, profit, sales, account management, marketing). A fulfilment overrun has exactly three causes: pricing, utilization, or over-delivery. Selling more fixes only one of them.
"You can't delegate what you can't measure": give the leadership team the instruments (per-department, per-deliverable cost %) and let them hit the targets.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Last year's result | $3.2M revenue, 12% margin, $380K net profit after a market-rate owner salary | his agency, last full year | speaker | spoken | clear; self-reported, unaudited |
| This year's result | $2.7M revenue, 21% margin, $580K profit | Jan–Sep (9 months) | speaker | spoken | clear; note 21% of $2.7M is ~$567K, so one figure is rounded |
| Growth | "about 16%" revenue growth, placed in the departments with the most bottom-line effect | year on year | speaker | spoken | clear; base not stated |
| Six-bucket split | 35% fulfilment · 25% overhead · 20% profit · 10% sales · 7% account management · 3% marketing | his agency (~$300K/month) | speaker | spoken + toolkit | clear; toolkit calls these "sample targets" |
| Smaller-agency split | 50% fulfilment · 30% everything else · 20% profit | illustrative $100K/month, ~10 people | speaker | spoken | clear; illustrative |
| Fulfilment line, January | 39% of revenue vs 35% target | whole agency | speaker | spoken | clear |
| By department, January | SEO/GEO 33% · paid media 53% · web dev 198% · hosting 205% (cost as % of revenue the department generates) | his agency | speaker | spoken | clear |
| Paid media | −7% net profit in February at 44% utilization → 15% by August (target 20%) | 2-person team | speaker | spoken | clear |
| Over-delivery example | team at 50% billable but 83% of time going into client work | paid media | speaker | spoken | clear |
| Utilization ceiling / break-even | 75% max billable · 55% break-even | his agency | speaker | spoken | clear; 55% is engineered backwards from a $200/hour market rate, by his own account |
| Team-size floors | 2 people 37.5% · 3 people 50% · 4 people 56% minimum utilization | arithmetic from the 75% ceiling | speaker | spoken | clear; pure arithmetic |
| Hourly rate | $5,500 ÷ 0.35 ÷ 143 h = $110/hour at 100% sold; ÷ 0.55 = $200/hour; ÷ 0.375 = $290/hour | assumed average employee cost $5,500/month | speaker | spoken | clear; illustrative |
| Price reset | legacy clients at ~$1,000/month moved to a $2,000 minimum with a $200/month lifetime discount (so $1,800); he thinks none were lost, two pushed back, one was re-scoped at the old price | his agency | speaker | spoken | clear; recalled, not shown |
| Annual increase | 3% price rise every year | his agency | speaker | spoken | clear |
Asserted mechanisms (no evidence given in the talk)
The first non-revenue hire is where margin erosion starts (he calls his own chart "exaggerated").
Teams of four or more cannot fall below break-even utilization; teams of one to three can.
Letting an under-used team put spare hours into client work is hard to take back; spare hours should go to internal projects.
Long-tenured teams inflate average cost per head; either re-price or promote the expensive people into management and backfill cheaper.
A leadership team given clear KPIs "will figure out ways to win".
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Layer 1, tracking (not supplied): record every deliverable per client per campaign, in hours, words, links or fixed cost. He uses a system built on a platform the audio gives as "Mac"; ClickUp, Asana or Google Sheets are fine. WHITE
Employee Cost Calculator: fully burdened cost per person, then cost per billable hour (toolkit default 75% billable, 37.5 h/week). WHITE
Set the six bucket targets; profit is what is left after the five cost buckets. WHITE
Per-client Pricing Calculator: quantities × per-unit prices = contract; each month re-plan the bundle so budgeted value still equals contract value (within 5%). One file per client. WHITE
Summary of Client Inputs: budgeted vs delivered per client per month; mark non-billable work so it uses capacity without inflating revenue. WHITE
Financial Model: per-department and per-deliverable cost % against target, with a verdict that names the cause: pricing (cost % high while utilization is healthy), capacity (under minimum utilization) or scope creep (delivered far above budgeted). WHITE
Third check: reconcile the model against the accounting software (he uses Xero) because contractor invoices land late; smooth over three months. WHITE
Fixes he applied: a sales incentive on one under-utilized department only; per-client billable-hour KPIs for an over-delivering team; a raised minimum price with a grandfathered discount; 3% annual increases. WHITE
Starting order he recommends: employee cost calculator → capacity calculator → one simple department (he began with paid media, not SEO). WHITE
Adapt with AI: load all files into a Claude project or ChatGPT and have it re-fit the model to your services and costs. AI_CONTEXT.md carries the formulas and five prompt recipes. WHITE
Toolkit formulas (from AI_CONTEXT.md, not spoken):
Minimum acceptable utilization = max billable % − (max billable % ÷ team size).
Break-even utilization = total team cost ÷ (target fulfilment % × hourly rate × total team hours).
Required rate = total team cost ÷ (target fulfilment % × total team hours × minimum utilization).
Next month MRR = prior MRR × (1 − churn + upsell) + new sales.
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Google Sheets + Claude: his answer to "best financial tools for a new agency". Xero (his) / QuickBooks Online: third-check accounting source.
EOS (Entrepreneurial Operating System): accountability chart; one-year and three-year hiring outlook so non-revenue hires are priced in before they arrive.
"Kiera" (operations manager): runs the model monthly.
Toolkit sample prices: GBP post $45 · blog post $0.45/word · press release $250 · citation $12 · technical hour $200 · GEO hour $200 · link $250 · page content $0.45/word · self-generated content edit $0.05/word (deliberately broken example) · graphic design $120/hour.
Q&A (question → answer)
Pricing AI input → two views: overhead (already inside the hourly rate) or direct cost (divide by the fulfilment target like any other cost). Three ways he has considered charging: mark up token cost; raise the human rate because people are more productive; charge "agent runtime" (human $200/hour, agent $20/hour as an example he is "playing with").
Cutting headcount with AI → no firings; people who quit were not replaced.
When did margins suffer most → before the framework, hiring on feel (a graphic designer who fit no department) and giving raises on gut feel.
Three tools for a new agency → Google Sheets, Claude, accounting software.
Resetting over-delivered clients → the $2,000 minimum with the grandfathered discount (above).
Sales and marketing share → 10% and 3%.
Skill measurement → six-month reviews with a matrix; "not frequently enough".
Result-based pricing vs retainer → valid as risk reversal when you lack proof, but must be priced higher than a retainer because you carry the risk (trades: fixed price is always above time-and-materials); or when you are confident enough to out-earn a fee (he references Dennis Yu's talk).
Org structure → EOS accountability chart; map hires one and three years out.
Advice → the best connections come from being among the last six people at the parties.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
The summary is accurate on the headline numbers. Omissions that matter follow.
Omits the three-layer system (tracking → budgeting → diagnosis) and the accounting reconciliation as a third check.
Omits that 55% break-even is reverse-engineered from a $200/hour market rate, and the $290/hour alternative.
Omits the $100K/month vs $300K/month split comparison, which is the actual argument for "price for where you are going".
Omits the over-delivery numbers (50% billable vs 83% of time on client work).
"Lost almost none" is softer than what he said: he thinks none were lost.
Omits tenure-driven cost inflation and gut-feel raises as margin leaks.
The toolkit is labelled for a different event ("SEOST 2026"), so the files were not made for this talk.
Toolkit default hours (37.5 × 52 = 1,950/year, ~162/month) differ from the 143 hours/month used on stage; check which basis a sheet uses before comparing rates.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
Tracking platform "Mac": garbled.
The profit figure the 50% formula produces at $300K/month: inaudible (arithmetic gives 5%).
"First Rank" and "around 30 people" come from an audience question, not from him.
All agency financials are self-reported.
The four workbooks were not audited for formula errors.
SEO as a System: Own What Happens After the Click — Jeremy Burgos (HighLevel)
Source: Granola https://notes.granola.ai/d/b0007e04-78e9-4549-abdd-6e1a55971df8 · recorded 2026-11-13 (12:21 GMT+7), Chiang Mai SEO, final day (lunch slot) · transcript-verified 2026-11-16 Resources: no photos attached to the Granola note (0 saved; no resources/jeremy-burgos/ folder created). He showed a starter prompt and a repro checklist on slides ("take a photo") and offered to share his "personal skills" at the HighLevel booth. Nothing collected. Vendor talk? ⚠️ Yes, mildly. He joined HighLevel (CRM and marketing automation platform, also sold as GoHighLevel) this year, mentions "the HighLevel tool we're building" for AI crawl questions, ran an iPad raffle via QR code, and the post-click section (AI voicemail capture, automated first messages) maps onto HighLevel features. No product named or priced on stage.
Recording note: the talk ends at about 31:40. From 32:59 the recording is a hallway conversation between the note-taker and a link vendor, then the next session's host. That part is not the talk and is not used here.
Thesis (3 bullets max)
SEO is a system: segment → map → plan → fix → compare. If you cannot show before and after, it did not happen.
Bind AI to the crawl per page segment with one narrow question each; it is cheaper and gives usable answers.
The same five moves apply after the click (lead source, funnel, first message, response speed), because clients judge SEO on leads and revenue.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| ⭐ Segmenting AI crawl questions | unsegmented: 351 model calls, 894,000 tokens; segmented: 111 calls, 138,000 tokens; "85% reduction" | one 39-page site he was building to flip, July 2026, Screaming Frog with an LLM API key | himself | spoken | arithmetic checks: 138k/894k = 15.4% → 84.6% fewer tokens (≈6.5× fewer); calls −68%. One site |
| Lead response speed | "about seven times more likely to qualify" when contacted within an hour (spoken jumbled with "five minutes") | no source, sample or date given | not named | spoken | low as stated; resembles a widely quoted older lead-response study, not checked |
| SMS vs email open rates | SMS "over 90%", email "around 20%" | "studies have shown"; none named | not named | spoken | low; unsourced |
| Brand-variant counting bug | one AI-visibility tool counted only one of HighLevel / GoHighLevel / GHL; vendor fixed it in about a week | one tool, unnamed, side-by-side with another tool | himself | spoken | anecdote; useful as a check, not a stat |
| Location changes AI answers | answers "crazy" different for Poland, the US and Switzerland | manual, 3 runs on 3 disposable cloud browsers in different locations; no prompt count or numbers | himself | spoken | qualitative |
Asserted mechanisms (no evidence given in the talk)
Sitewide header/footer links make pages look more linked than they are; content links carry the weight.
GA4's AI assistant channel undercounts: a user who sees a brand in an AI Overview and then visits directly is counted as direct.
Users reach an answer through 7–8 prompts, so optimize for the answer rather than the keyword. Spoken only.
Setting a goal before the crawl "tricks the mind" into working harder for the client. Opinion.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Move 1, segment:
Check the stack (builtwith.com); feed the sitemap to an AI to map the architecture. WHITE
Split pages by type; every segment gets a decision (products/services = money segment, top priority; tag pages always noindex). WHITE
Move 2, map: 3. Crawl with header/footer navigation links stripped; size each page by in-content links. WHITE 4. Flag orphan pages and pages more than 3 clicks deep. WHITE 5. Cannibalization: in GSC, check whether competing URLs pull the same queries; pick the owner (usually the money page); if the other page carries nothing needed, redirect it; if it does, keep it, link it to the owner and recheck in 28 days. WHITE
Move 3, plan: 6. Turn the crawl into one row per URL per element in a working dashboard (he uses AI "skills" and markdown files to do this after every crawl). WHITE 7. Priority: P0 blocks indexing or misidentifies the page · P1 duplicates or dilutes (cannibalization) · P2 improves · P3 polish (for example a date refresh). WHITE 8. Sort by upside: what already ranks (GSC, Bing Webmaster Tools), whether AI answers cite it (10–20 test prompts; he names OpenRouter), content links, which pages drive leads, what competitors do differently. WHITE
AI in the crawl: 9. Give each segment its own question, never "is this page good for SEO?". Service page example: "Is it clear who this is for and what they get? Answer yes, partly or no, then 1–3 sentences." One value per URL. The crawler must capture full page text. WHITE (note: Screaming Frog's integration bills to the user's OpenAI/Anthropic API key) 10. Before acting on an AI answer: does the crawl data agree; does it fit the page's job; is it a real gap or a preference; can it be measured after. WHITE
Move 4, fix and recrawl: 11. Fix template issues first (one fix repairs every page), then page issues. WHITE 12. Recrawl with the identical setup: same profile, segment rules, AI questions and rendering settings. Run both a JavaScript-rendered and a raw-HTML crawl and compare. WHITE
Move 5, compare: 13. Before changing anything, pick a changed group and an unchanged group of similar size in the same segment; log the change date; read at 28 days. WHITE 14. Report order: signups/activations → sessions and key events → impressions → AI citations. WHITE 15. AI answers: keep the prompt set steady, 3 runs per engine; report mentions (name in the answer) and citations (page in sources) as two numbers; branded and unbranded prompts; check the tool counts every brand variant. WHITE 16. Label every number by source: crawl · client-reported · official documentation (GSC etc.) · third-party estimate · your inference. WHITE 17. Report row: URL · fix · what changed and when · value before · value after · label. WHITE
After the click: 18. Segment leads by source (SEO, paid, events, social); map where they drop; change one thing; measure. WHITE 19. Test the client's phone yourself at off-hours (his opening story: the client blamed call tracking; nobody answered). WHITE 20. First message within 5 minutes, on the channel the lead used, opening with a quick qualifying question (his example: "Have you ever worked with an SEO expert before?") instead of "book your audit here". Hand to a human when needed. WHITE 21. If the client will not answer calls, add AI voicemail capture. WHITE (disclose automated handling where required) 22. Map the "nine places a lead goes quiet" (example: "I need to think about it" → next-day follow-up with an incentive). WHITE
His own limits slide ("where it breaks"): the two groups may not start equal (the changed pages may already have been rising); a model only knows what you tell it; structure is easier to measure than content; one site is one site, the method carries over, the numbers do not.
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
HighLevel (GoHighLevel, "GHL"): his employer; building its own crawl tool with AI questions. No price.
Screaming Frog: crawler; accepts OpenAI or Anthropic API keys to run AI questions per segment.
builtwith.com: identify a site's technology.
Google Search Console, Bing Webmaster Tools: ranking and impression data.
OpenRouter: suggested for testing what different AIs say about a query.
GA4: AI assistant traffic channel, "still not that accurate".
Orangetheory Fitness: former employer where he learned fast lead response ("Orange Theory" in audio).
Slide photos
None attached to this Granola note.
Q&A (question → answer)
None. No Q&A; he invited questions at the HighLevel booth and moved to the raffle.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
"Responding within 5 minutes is 7x more likely to qualify a lead vs. waiting an hour": the audio jumbles 5 minutes and 1 hour, and no source was given. Treat as unsourced.
"Run 3 prompts per engine": he said keep a steady prompt set (start with 10–20 prompts) and run it 3 times per engine.
The glossary defines "Funnel" as a data integration platform; he meant the lead funnel.
Omits the number-source labels (crawl, client-reported, official, third-party estimate, inference) and the report row format.
Omits his own limits slide (unequal groups, one site is one site).
Omits that the 85% token saving comes from one 39-page site of his own.
Omits that he works for HighLevel, a sponsor with a booth, and that the post-click advice lines up with its features.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
The 7× lead-qualification figure and the SMS/email open rates: no source.
Which AI-visibility tool had the brand-variant bug: not named.
The starter prompt and the repro checklist were on slides; no photo was taken, so their wording is not available.
Example brands in the cannibalization story ("UFC Gym vs Orange 30 Fitness", "Joe Schmo Law Firm vs Baker Mayfield Law Firm") are illustrative and partly garbled.
Perception Engineering — Jonathan Kiekbusch (founder, SwishDM; formerly SEO Butler)
Source: Granola https://notes.granola.ai/d/b094472b-4bd2-4ac5-8cc2-98f860f9a182 · recorded 2026-11-13 15:21 GMT+7 (00:21 PST), Chiang Mai SEO main stage · transcript-verified 2026-11-16 Resources: 9 slide photos saved to ../resources/jonathan-kiekbusch/photos/ (all 9 read; all legible; the speaker blocks a few words on 5 of them). No deck or handout offered. Photo 1 downloaded from the signed URL; photos 2–9 copied from the local copy the Granola tool saved (byte-identical to the URL download, checked on photo 1). Vendor talk? ⚠️ Yes, agency. SwishDM sells SEO + "GEO" services to e-commerce brands; the case (Geekom, mini PCs) is his client. No product sold from stage. Speaker surname is not spoken (stage intro says "Jonathan"); slides carry the SwishDM logo; one web search confirmed Jonathan Kiekbusch as SwishDM founder and former SEO Butler head (theseoshow.co episode 092, swishdm.com/about).
Thesis (3 bullets max)
Being named is not enough: read what the answer says about you. Cited as "budget" or "overheats" can be worse than absent.
Five steps: Discover (prompts from owned + shared data) → Diagnose (100+ answers per prompt, four failure types) → Design (retrievable facts that answer the fan-out) → Distribute (corroboration across third parties) → Defend.
AI "weighs evidence, it does not adjudicate truth": a few documents that answer the fan-out query can move the answer.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Geekom starting visibility | 51% | the client's KPI prompt set; start of 2026; platforms "a bunch", not named | SwishDM | spoken | one client; no prompt count, no engine split, no end number given |
| Geekom outcome | answers moved from "budget / overheating" to "extremely positive" by year end | same client, Feb diagnosis → April publishing → year end | SwishDM | spoken; the before/after slide was not photographed | ⚠️ no measure shown in the photos; several changes at once (thermal data on site, paid gaming placements, paid roundups, readable specs); no control |
| Answers per prompt | 100 = floor (±10 points); 400 = ±5 points; 800 = 400 before + 400 after to show a 10-point move | margin of error on a share near 50%, 95% confidence | his rule of thumb | photo 04 | ✅ arithmetic checks (1.96 × √(0.25/n): 9.8 at n=100, 4.9 at n=400). Assumes independent draws; repeated runs of one prompt minutes apart may not be independent |
| Answers needed in a day | 100 per prompt within 24 hours by batching API calls every minute | DataForSEO "or whoever" + a Python script | his method | spoken | method, not a result |
| ⭐ $14 fake review site | see the next section | 45 prompts, daily, 5 platforms, action cameras | SwishDM | spoken only; no photo of the result | ⚠️ his own words: "not a scientific test" |
| Bing AI Performance panel | 1.9M total citations, 722 avg. cited pages (screenshot on slide) | one unnamed site in Bing Webmaster Tools → AI Performance | screenshot | photo 01 | illustration only; site not named |
The $14 fake review site experiment (method and result, exactly as stated)
What was built: a brand-new domain; the whole site written with AI; review content for action cameras ("a pretty competitive market"). The site name is garbled in the audio ("real icon reviews").
Process (spoken + photos 07–09): prompt set from the Discover step → a brief per prompt → a test sheet per product (product, maker's specs, purchase record, hands-on log, measurements, use-case trials, opinion ratings, verdict, scores and ranks, sign-off) → AI writes the review in "the tester's voice" → AI publishes. He added trust signals ("how we test", author bio) and kept it crawlable.
Authors: invented. Q&A: "we just made them up", from a fake-name generator or Claude. Test data: he left open whether it was real ("whether you're getting your data legitimately or illegitimately").
What was tracked: 45 prompts, daily, across 5 platforms (only ChatGPT and Bing/Copilot named).
Result: cited "really quickly" with no authority; cited above Wired for some prompts; ChatGPT cited it; Bing and Copilot "a little bit"; the other platforms did not ("better at detecting spam").
Duration: "showing up for 33 hours before we [garbled]". The next sentence says a removed site keeps being cited for "quite a while" because of caching. Read as: taken down after about 33 hours, still cited for a while after. Not certain.
Cost: $14, the domain registration.
What was controlled: a fixed prompt set (45) tracked daily on fixed platforms.
What was NOT controlled or not reported: no baseline per prompt; no control site or control prompts; one site, one run, one category; no count of answers or citations; no share numbers; the five platforms not named in full; whether the site named the client's product is unclear in the audio; which prompts it won not shown. His "attribute axis" lesson (stabilization, price and resolution get you considered; frame rate and weight alone do not) is stated as a counterfactual. No variant was described as tested.
His verdict: "this breaks quite a few rules… you could get yourself in trouble with the FTC"; "I test black hat… to reverse engineer a legitimate way".
Contradiction on his own slides: photos 07 and 09 say "AI writes it. It never invents it", "The tester owns every number", "Never invent a figure", "First person is fine when the person is real". The Q&A says the authors were invented.
Asserted mechanisms (no evidence given in the talk)
AI weighs the evidence it can retrieve; it does not decide what is true. A small number of documents that answer the fan-out query can tip the answer (photo 06: prompt "best mini PC for gaming" → model searches "mini PC thermal throttling", "mini PC cooling performance" → finds a 2023 forum thread, one paywalled review, a spec table → "your page?").
Branded prompts inflate citation frequency if mixed into category tracking. Spoken only.
Category prompts are mid-to-bottom funnel, not bottom: people find a brand in a list, then ask follow-ups. Opinion.
For many US e-commerce queries ChatGPT's fan-out already adds brand names (his example: "best uphill running shoe" → Nike, Adidas). Displace it by "poisoning the axis" AI compares on or by growing the brand. Spoken; attributed in part to Jabez Reuben.
Natural outreach for links is "pretty much dead in 2026, 2027". Opinion.
No one can tie a prompt to a sale today; comparison prompts are the most likely to affect conversion. Opinion, stated with that hedge.
HCU-hit sites and abandoned YouTube channels are still cited heavily in AI and are cheap to buy. No data.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Discover:
Owned data first (photo 01): Google Search Console (regex for long-tail questions), Microsoft Clarity, Bing Webmaster Tools → AI Performance ("Bing shows the searches AI runs before it answers: these are your fan-outs"), support tickets, live chat, pre-sales email. He also named the ChatGPT business panel (data missing in it). WHITE
Shared data for ideas only (photo 02): Amazon Q&A and reviews, Reddit and category forums, People Also Ask, competitor reviews and Q&A, fan-outs from your prompt tracker. "Your own data is more reliable." WHITE
Sort with AI into three buckets (photo 03): Branded ("Is GEEKOM premium or budget?", "you can nearly always win these") · Category ("Best mini PC for the office", "the battlefield") · Jobs-to-be-done ("Can a mini PC handle video editing?", where rivals get to show up). Track small clusters, not everything. WHITE
Diagnose: 4. Freeze the prompt set; run it; keep the full answer text, tables, citations and fan-out queries; track branded separately. WHITE 5. Start with a burst of 100+ answers per prompt (up to 800 for small sets), then run on a schedule. WHITE 6. Use AI to count the most common positive and negative descriptions of the brand across all answers. WHITE 7. Classify each problem (photo 05): Absent → Distribute · Mis-framed → Design · Out-ranked ("you're second, and it says why") → Distribute · Wrong axis ("compared on terms you didn't set") → Design. WHITE 8. Read comparison tables and "best for" labels in the captured answers to find the attributes the engine compares on. WHITE
Design and retrieve: 9. Publish the evidence that fixes the record on the brand's own site (Geekom: thermal test data for an old overheating problem; warranty, partnerships, hardware fixes). WHITE 10. Specs and features as text, not images, on product and listing pages. Show the client or the developer a competitor's product page with JavaScript off (his example: DJI) to win the argument. WHITE 11. Do not chase use cases the product does not fit; buyers will flame you on Reddit and review sites. WHITE
Distribute: 12. Critics: send a cease-and-desist "if egregious", or "pay them money if they're willing". GREY (legal letter) / BLACK (paying a critic to change a review without disclosure) 13. Rival listed and you are not: "you just pay them". Paid roundups for Geekom; paid placements on gaming platforms. GREY: disclosure required 14. YouTube: advise creators on metadata, not the script; fix auto-captions where product or brand names are mangled; write description timestamps that match target prompts ("best mini PC for video editing", "what the three-year warranty covers"). WHITE 15. Brief independent reviewers on use cases, test protocol and benchmark rivals. WHITE if the reviewer stays independent and any relationship is disclosed 16. Start-ups: get into the big category roundups, do PR, and work with affiliates on how their content is structured. WHITE if affiliate links are disclosed 17. Build your own review site (the $14 method) or buy an HCU-hit site or abandoned channel that AI still cites: run the seller's inventory through Ahrefs or Semrush for AI citation counts, make "a really rude, underpriced offer". Publishing reviews of your own client's products on it without disclosure is BLACK (FTC; his words). Buying a site is GREY. 18. Buy backlinks on a small budget ("services like [Giga] Links", marketplaces, direct negotiation). GREY/BLACK under Google's link-spam policy; behind the gate. 19. Use an "abliterated" model when Claude refuses to write the content. BLACK in the context given (writing made-up material)
Defend: 20. Re-run on schedule; positions move often and leaders get unseated. WHITE
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
SwishDM: his agency (logo on every slide).
Geekom: client case, mini PCs.
DataForSEO "or whoever": source of AI answers via API, batched by script. No price.
Bing Webmaster Tools → AI Performance; Microsoft Clarity; Google Search Console; ChatGPT business panel.
Ahrefs, Semrush: to see how often a for-sale site is cited by AI.
"Gig links" / "bigger links": most likely Giga Links (C11's seller); speech-recognition spelling.
"Obliteration": abliteration, a way to strip refusals from open-weight models; not a vendor. Credited to a "Charles" from an earlier talk.
Namecheap: domain for the $14 site.
People: Matt Diggity (founded the event; garbled as "Matt"), Jabez Reuben ("Javez"), Lee Stewart (audience question), Jacob Kettner (question).
Slide photos
Full text of each slide: ../resources/jonathan-kiekbusch/slide-text.md
01-discover-owned-data.jpg — "01 Discover · Owned data · Start with the data you already own": GSC, Microsoft Clarity, Bing AI Performance, support tickets and live chat; Bing AI Performance screenshot 1.9M total citations, 722 avg. cited pages; "Bing shows the searches AI runs before it answers… these are your fan-outs" (last words hidden by the speaker).
02-discover-shared-data.jpg — "Then look where your buyers already ask": Amazon Q&A and reviews, Reddit and category forums, People Also Ask, competitor reviews and Q&A, fan-outs from your prompt tracker; "Use these for inspiration. Your own data is more reliable."
03-three-prompt-buckets.jpg — Branded / Category / Jobs-to-be-done with Geekom examples and labels "You can nearly always win these" / "The battlefield" / "Where rivals get to show up".
04-100-answers-is-the-floor.jpg — "100 answers is the floor. Not the target." Margin of error on a share near 50%, 95% confidence: 100 → ±10 points; 400 → ±5 points ("a number you can put in a client report"); 800 = 400 before + 400 after → a 10-point move.
05-four-ways-you-lose-the-answer.jpg — Absent → 04 Distribute; Mis-framed → 03 Design; Out-ranked → 04 Distribute; Wrong axis → 03 Design.
06-why-one-page-can-move-it.jpg — prompt "best mini PC for gaming" → model searches "mini PC thermal throttling", "mini PC cooling performance" → finds a 2023 forum thread, one paywalled review, a spec table → "YOUR PAGE?"; bottom line partly hidden ("…re almost nothing… [bett]er exists wins").
07-own-the-source-ai-writes-it.jpg — "Own the source · How we built it · AI writes it. It never invents it.": 01 prompt set → 02 brief → 03 test sheet → 04 AI writes → 05 sign-off; "The tester owns every nu[mber]. AI does the typing."
08-test-sheet-columns.jpg — "Every review starts as a spreadsheet": product, maker's specs, purchase record, hands-on log, measurements, use-case trials, opinion ratings, verdict, scores and ranks, sign-off; row labels "The tester enters it" / "Pulled from the site" / "Formula" / "AI [names?]… the winner" (partly hidden).
09-writing-prompt-three-rules.jpg — "Then AI writes it, in the tester's voice. First person is fine when the person is real and the numbers are theirs." Rules: 1 Never invent a figure; 2 "Not published" is content (say what the maker won't tell you; never leave a blank, never estimate); 3 Every page c[onc]edes something (a named rival… test, by a st[…]: partly hidden).
Q&A (question → answer)
E-commerce in 2027 (Jacob Kettner) → small and mid-size stores get squeezed; big brands win because they are already in the data; small local businesses can dominate local AI answers with one listicle or award.
What has changed how AI describes a known brand → "see the slides".
New app with zero mentions → with budget: big roundups + PR; without: review sites and third-party listicles; aggressive affiliate programs, shaping how affiliates structure content.
Language and country differences → only works in English; "probably easy" to show different things per market; no test case.
Training priors vs retrieval (Lee Stewart) → fan-outs already insert big brands; displace by changing the comparison axis or growing the brand.
Where to buy citations and for how much → Giga Links-type services, marketplaces, outreach, digital PR; no prices.
Buying backlinks and traffic → does not buy traffic ("I don't dispute that it works"); "definitely buy backlinks"; tests black hat, works white hat for listed-company clients.
How to measure perception work → it may not raise frequency; it changes what is said when you appear ("AI conversion rate optimization").
Which prompts decide sales → nobody can attribute a prompt to a sale today; comparison prompts are the best bet; be included first, then improve what is said.
Author and E-E-A-T on the third-party site → "nothing. We just made them up."
Multi-brand retailers → ask the platform to improve its PDPs; else off-site work or info sites saying where to buy; schema sameAs.
Personal advice → "charge more money"; use the community; "staying in the game is the game".
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
Speaker name missing; he is Jonathan Kiekbusch (SwishDM).
"Run a lot of tests per prompt… See the screenshot on creating prompts", "Can understand attributes from testing" and "Look at Abliteration… if Claude doesn't comply" are the note-taker's private notes; the summary presents them as talk content. Abliteration is a technique for stripping refusals from open models, not "an LLM".
"Misbranded" and "wrong comparison basis": the slide words are Mis-framed and Wrong axis, each mapped to a step (Design or Distribute).
"Cited for 33 hours before removal": the audio is garbled at that point; removal is inferred from the next sentence about caching.
"Only ChatGPT and Bing/Copilot cited it": ChatGPT cited it; Bing and Copilot only "a little bit".
Omits the sample-size table (100 = ±10, 400 = ±5, 800 for a 10-point change).
Omits that his own slides say "never invent a figure" and "the tester owns every number" while the Q&A says the authors were invented.
Omits that the Geekom result has no number in the photos and bundles paid roundups, paid gaming placements and on-site data.
"Natural outreach largely dead": stated as his opinion.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
The fake site's name ("real icon reviews") and whether it promoted the client's own product.
What happened at 33 hours (removal or end of tracking).
Which five platforms were tracked.
"Gig links" = Giga Links (likely).
"Charles" who mentioned abliteration in an earlier talk: not identified.
Geekom before/after figures: the slide comparing answers was not photographed.
Local Search: Reviews, AI Local Packs and What Still Moves the Map — Joy Hawkins (owner, Sterling Sky)
Source: Granola https://notes.granola.ai/d/adc24d4f-ab81-4124-9480-08d0e05c42a4 · recorded 2026-11-13 (11:58 GMT+7), Chiang Mai SEO, final day · transcript-verified 2026-11-16 Resources: no photos attached to the Granola note (0 saved; no resources/joy-hawkins/ folder created). Slides were offered by QR code on stage. The note-taker's private notes carry https://www.sterlingsky.ca/chiang-mai-takeaways/ as the deck page; the URL is not spoken in the transcript and was not opened. Vendor talk? Agency. Sterling Sky is a local SEO agency; she plugged its YouTube channel and hiring. No product sold. Every number is Sterling Sky's own testing or a study run with Yext; none has a base, period or sample stated on stage except the Yext screenshot count.
⚠️ The recording starts mid-talk (first words: rankings "start to drop pretty quickly" if reviews stop). Only about 7 minutes of the talk and about 14 minutes of Q&A were captured. The earlier sections of the talk are missing.
Speaker identity: the host names her ("Joy Hawkins one more time") and an audience quote in the talk addresses her as "Joy". Sterling Sky is named by her.
Thesis (3 bullets max)
Reviews, on-site SEO and a keyword in the business name are still the levers; reviews are "king" (frequency, volume, average rating).
Google now runs five competing local formats (local pack, AI local pack, three-pack ads, LSA, organic). When one drops another rises, so be present in all of them rather than chase rank positions.
Rankings and attribution are breaking (organic volatility, AI local packs, GA4 cannot separate AI clicks). Report leads over time from call tracking.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Average rating moves rank | 4.5 → 4.6 gave "a ranking boost" | client measurements; no count, size of lift or period | Sterling Sky | spoken | low; direction only |
| Review velocity gap | "competitors get 5 a month, you get 1 a month" used as the cut-off in client reports | example, not a measured threshold | Sterling Sky | spoken | heuristic |
| AI local packs show fewer businesses | 88% of markets looked at; 3 listings → about 1.5 (second listing half hidden) | number of markets and queries not given | Sterling Sky | spoken | medium; no base |
| Organic volatility after the May core update | organic results 48% more volatile; Maps "not poisoned" so far | over 8 million search-result screenshots, incognito, logged out | Sterling Sky with Yext (Yext took the screenshots) | spoken | medium; study not read; vendor partner |
| Service-area businesses rank worse | "do not rank as well" | "studies"; no numbers on stage | Sterling Sky | spoken (C37 shows the same study as before/after map grids) | medium; study not read |
| Second office revenue | +$500k revenue in a year from a second office | one electrician, his own estimate | the client, told to her | spoken | anecdote |
| Links and the local pack | "tons of links" created with almost no local pack movement; links measurable on organic | tests "a few years ago"; no counts | Sterling Sky | spoken | low; dated, no numbers |
| Google Posts | no measurable ROI; Sterling Sky stopped doing them | own tests; no counts | Sterling Sky | spoken | low-medium |
| Lead-gen listings in AI | has "yet to see" an exact-match lead-gen listing rank in an AI Overview | personal observation | her | spoken | observation |
| "Best of" list sites | traffic over the last year "wild" in Ahrefs; one site quadrupled its prices | no site or number given except "Best of Houston", "Best of Tampa", "Best Law Firms" | her, via Ahrefs | spoken | low |
| Bought reviews tank rankings | former client: rankings rose on bought reviews, then fell when Google deleted them | one Las Vegas law firm, watched after Sterling Sky fired them | her | spoken | anecdote |
Asserted mechanisms (no evidence given in the talk)
Google keeps a review "trust score" per business; once broken by bought reviews, legitimate new reviews stop sticking. Source: "in-depth talks with ex-Googlers". Not checkable.
AI local packs weight reviews less than the classic pack. Evidence offered: one personal-injury law firm that fails her review metrics ranks well in AI local packs (grid tracked by the client).
The organic volatility is "SERP poisoning"; a named commentator (speech recognition: "Ian Evans") thinks Google does it to defeat CTR manipulation and scraping.
GEO is not good SEO: the signals for AI answers and classic local rankings now differ.
For AI, mentions matter, not links; the brand name in every mention should match the Google Business Profile name exactly.
Black-hat "Posts help rankings" results came from sending traffic to the posts, not from the posts.
Fake-review detection uses IP/location signals and VPN filtering, and is "very flawed".
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Review benchmark (the part of the talk that was recorded):
For the client's target terms, list the top-ranking competitors. WHITE
Score each on review frequency (per month), total volume and average rating; compare with the client. WHITE
If the client cannot match the velocity, retarget a smaller keyword set the client can win. WHITE
Do not buy reviews; do not bother reporting competitors' bought reviews (Google rarely acts). WHITE (buying = BLACK and illegal, per her)
Rank tracking: 5. Stop reporting single rank positions. If tracking, sample each keyword dozens of times across the grid so the leader order shows through volatility (she says this is now expensive and working less well). WHITE 6. Make sure the tracker's screenshots include ads; many do not, especially logged out. WHITE 7. Track presence across all five formats (local pack, AI local pack, three-pack ads, LSA, organic). WHITE
Attribution: 8. UTM-tag every Business Profile link, but expect AI local pack clicks to land on either the profile or the site and sometimes show as organic. WHITE 9. Call tracking is the reporting backbone; report leads over time. Ask every inbound lead where they heard of you and what they searched (Sterling Sky does this; often multi-channel). WHITE
From the Q&A: 10. Service-area businesses: open a small office with branded signage where demand is; she says this is one of Sterling Sky's biggest home-service strategies. WHITE (a real, staffed office only) 11. Verification for a service-area business = video verification; the home address is not shown publicly. A branded-domain email may reduce the chance of video verification. WHITE 12. For Ask Maps / "Know before you go" (Gemini in Maps): publish very granular, long-tail detail on the website, even zero-volume phrases (her example: appliance error codes for an appliance repair shop, which lifted rankings "across all services"). WHITE 13. Ask customers to add photos to their reviews (Maps AI features lean on user-generated content). WHITE 14. Get onto established local "best of" lists (not self-made ones). WHITE if editorial; paid placement = GREY unless disclosed 15. Keep the brand name identical to the GBP name everywhere it is mentioned. WHITE 16. Competitor listings created through bulk-verification feed abuse (casino niche example) can be reported and removed. WHITE 17. Add an ads person rather than skip ads; Google's formats are here to stay and ad conversion is "the best it has been". WHITE
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Sterling Sky: her agency; YouTube channel with local SEO videos; hiring.
Yext: partner on the 8M-screenshot volatility study.
Ahrefs: used to view traffic of "best of" list sites.
"Best of Houston", "Best of Tampa", "Best Law Firms": example local list sites; one quadrupled prices (which one not stated).
ChatGPT business profiles ("ChatGPT business new feature"): Sterling Sky "just added" theirs, had not logged in yet; she expects LLMs to supply their own data for tracking.
GA4: only current source of AI click counts; cannot separate Google AI clicks.
"Charles" (fellow speaker, casino niche): pointed to for GBP creation methods. Surname not spoken.
"Ian Evans": speech-recognition spelling; commentator on SERP volatility.
Deck: QR code on stage; sterlingsky.ca/chiang-mai-takeaways/ from the note-taker's private notes, not spoken.
Slide photos
None attached to this Granola note.
Q&A (question → answer)
SEO-only agency, no ads expertise → hire an ads person; ads formats are not going away.
Rebuild local SEO from zero in 2027 → reviews, on-site SEO, keyword in the business name (20 years, no sign of change).
Bypass GBP verification with no address → she does not bypass; video verification is the only route for service-area businesses; get a storefront.
Tracking AI local pack positions → no good solution; third-party tools inaccurate; GA4 cannot separate AI clicks; hopes Google/LLMs expose data.
Local SEO for B2B SaaS → "not really"; would not waste the time.
Why avoid bought reviews if not penalized → illegal; lawyer clients will not risk it; Google removes at scale; trends suggest it will work less.
Lead-gen sites/listings selling leads → viable for some, extremely volatile (60% of sites or profiles can be removed overnight); she does not do it; her clients report such listings.
Optimizing "Know before you go" / Ask Maps → granular site detail and review photos (step 12–13).
How Google detects fake reviews → many signals, IP among them; flawed.
Proximity/citations vs CTR and entity signals → she does not do CTR manipulation; hears CTR works less on AI results; third-party "best of" lists are the biggest current win.
ChatGPT business feature → just added; likely the future tracking route; attribution messy (AI search → branded Google search gets credited to Google).
Links for local pack vs organic → much weaker for the pack; for AI, mentions not links.
Do Google Posts help → no; no measurable ROI; stopped.
Do bought reviews work → yes until removed; then rankings tank and the trust score may block legitimate reviews.
How casino operators create GBPs in many geos → ask Charles; old bulk-verification feed trick was shut down and listings removed.
Final advice → call tracking; report leads over time.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
"Look at running local ads and the Google Ads API" and the "Next steps" built on it are the note-taker's private note, presented as the speaker's recommendation. She said "hire an ads person"; she never mentioned the Google Ads API.
"Review Sterling Sky's Chiang Mai takeaways deck" cites a URL from the private notes; the speaker gave a QR code.
Omits that the recording starts mid-talk; the summary reads as if it covers the whole talk.
"Saw a Vegas law firm's rankings tank after bought reviews were removed, then couldn't recover": the firm was a former client Sterling Sky fired; another vendor then bought the reviews. "Couldn't recover" is the general trust-score claim, not stated for that firm.
"AI local packs appear to de-weight review signals": based on one law firm plus her not having seen lead-gen listings in AI Overviews; the summary states it more firmly.
"ChatGPT business profiles likely the future solution": an answer to an audience question; she had not yet looked at Sterling Sky's own profile.
Omits: B2B SaaS answer ("not really"); lead-gen model volatility (60% overnight); video verification and branded-domain email; the 2027 three-activity answer; the fake-review IP answer; the casino bulk-feed story; high-volume grid sampling as the rank-reporting workaround.
"Feature Awards" in the private notes is the note-taker's line; it does not appear in the transcript.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
"Ian Evans" is a speech-recognition spelling; identity unknown.
The 88% figure: base (markets, queries, date) not stated.
The Yext study (8M screenshots, 48%) was not read; date and method unknown beyond "incognito, logged out".
The service-area-business study: no numbers in this recording (C37 shows map grids from it).
Which "best of" site quadrupled prices.
The first part of the talk was not recorded; deck not downloaded.
The Chinese SEO Blue Ocean — JP Chan ("John" in China; SEO Action Blog; runs "SEO Connector" and an SEO conference in Shenzhen)
Source: Granola https://notes.granola.ai/d/f9f549b9-f1ba-4afc-9c85-1a0cb944b85b · recorded 2026-11-13 23:54 PST = 2026-11-14 14:54 GMT+7, LLM Mastery 4.0 day (lightning slot) · transcript-verified 2026-11-16 (full transcript read, 33,160 chars) Resources: 4 slide photos saved to ../resources/jp-chan/photos/ (all 4 viewed and read). Slides are numbered x/38, so most of the deck was not photographed. Vendor talk? ⚠️ Yes. He brokers introductions between Chinese businesses and Western agencies ("SEO Connector") and runs the Shenzhen SEO conference he recommends as the place to meet clients and middlemen. Market figures on the slides carry a partly hidden source line ("…MOF…", "…earch, industry ben…"); none were sourced aloud.
Thesis (3 bullets max)
Chinese companies going global are strong on product and supply chain and weak on marketing; few local agencies do SEO, so Western agencies face little competition ("blue ocean": 752 businesses per agency on the slide).
Pick one segment, borrow trust through local middlemen, show up in person, close one deal and let the case study travel.
Keep the offer; change the channels (WeChat/WhatsApp, Tencent Meeting/Lark) and match "China speed" in sales while keeping delivery expectations slow.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Market size | 865,000+ enterprise brands expanding into global markets; 1,150 marketing agencies, "only 150 of them do SEO"; 752 : 1 businesses per agency | source line partly hidden ("MOF…", "industry ben[chmarks]") | not stated | slide, photo 01; spoken as "about 1 million businesses" and "a little more than 1,000 agencies" | slide figures clear; source unreadable |
| US comparison | ratio heard as "265" / "255" (red ocean); 33 million US businesses | none | not stated | spoken only | garbled; no slide photo |
| Going global after Covid | ~90% of businesses chose to go global (2023) | his opinion | speaker | spoken | estimate |
| B2B manufacturing & trade | 700,000 official → 2M–3M real players; total marketing $5K–$15K/month mid-range; SEO retainer $3K–$4K/month median, range $500 (blurred, could be $600) to $8K | official count misses micro-businesses and multi-entity owners | not stated | slide, photo 02 | clear except the low end of the range |
| Three segments side by side | B2B trade & mfg 2M–3M, SEO budget median $3K–$4K, English weakest · E-com & DTC ~500,000, $5K–$6K, English best · AI & tech 150,000+, median partly hidden ("…$6K"), English above average | not stated | not stated | slide, photo 03 | clear except the AI & tech budget and the third "catch" |
| His ICP | B2B manufacturers/traders with 20–100 staff, ~$15M revenue/year | his SEO Connector business | speaker | spoken | self-reported |
| Amazon sellers | 60% of Amazon sellers are Chinese; ~32% of those are in Shenzhen ("one in five" overall) | none | not stated | spoken | unsourced |
| AI & tech budgets | cash cows: SEO retainers $4K–$10K, mostly one-off projects; solopreneurs: $500–$10K/month, 20–30% of revenue on marketing; indie hackers ~85% of the AI/software count | none | speaker | spoken | estimates |
| AI use in China | ~50% of internet users, a little over 500M people | none | not stated | spoken (slide not photographed) | unsourced |
| His conference | 51% of attendees from outside China this year; of the Chinese attendees ~40% e-com/B2C, ~30% AI/tech, ~20–25% B2B | his conference | speaker | spoken | self-reported |
Asserted mechanisms (no evidence given in the talk)
Chinese buyers do not trust strangers; remote closing rarely works; deals with older owners happen at the dining or drinking table.
Email to Chinese clients often lands in spam (QQ / NetEase mail) and is rarely checked; use instant messaging.
E-com/DTC brands treat SEO like paid ads and want results "yesterday"; app and game giants come only after a Google update hits them.
Chinese companies already mass-produce English content with AI, so content-only offers sell poorly; unique content at scale (he cites Georg's talk, C5) still can.
Western AI tools are blocked in China; ByteDance leads business AI use (Volcano Engine), then Alibaba Cloud; DeepSeek and Tencent named.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Pick one segment and subsegment (slide 04): cash cows for small agencies (lead with strategy, backlinks, resources their in-house team lacks); brand builders for big proven agencies (case studies, senior strategists); indie hackers for productized fixed-price packages (links, PR, SEO audits, manual-action recovery); app and game giants with caution. WHITE
Borrow trust: work through local SEO consultants and KOLs who already serve these companies; meet them at SEO conferences (Chiang Mai had up to 50 Chinese attendees; his Shenzhen event). WHITE
Show up in person; China is visa-free for 80+ countries. WHITE
Close one deal, publish the case study, let word of mouth carry it. WHITE
Move communication to WeChat or WhatsApp and meetings to Tencent Meeting or Lark. WHITE
Answer fast in sales; set slow expectations for SEO delivery; drop clients who will not accept that. WHITE
Do not build a Chinese site or entity to sell to them; keep your existing offer. WHITE
Slide photos
Full text of each slide: ../resources/jp-chan/slide-text.md
01-blue-ocean-865k-brands-1150-agencies.jpg: "The Blue Ocean" — 865,000+ enterprise brands expanding into global markets · 1,150 marketing agencies, "Only 150 of them do SEO" · 752 : 1 businesses per agency, "relatively untapped, with high budgets". Bottom line and source partly hidden by the speaker and heads.
02-b2b-manufacturing-trade-budgets.jpg: "Carriage #1 B2B Manufacturing & Traditional Trade" — 700,000 official → 2M–3M real players; factories and trading companies, husband-and-wife shops to 1,000+ staff, little brand awareness; decision-maker the owner or marketing/operations lead, met at expos and SEO conferences; SEO maturity lowest, moving from expos and B2B platforms to their own site; English weakest; catch: fragmented sizes, long education cycle; $5K–$15K total marketing/month (Google and LinkedIn ads, social, SEO); $3K–$4K SEO retainer/month median, range $500–$8K (low end blurred). Motion-blurred but legible.
03-three-carriages-side-by-side.jpg: comparison table — real market size, decision-makers, SEO budget/month median, English, the catch for B2B (2M–3M; $3K–$4K; weakest; fragmented sizes, long education), e-com & DTC (~500,000; $5K–$6K; best; bureaucracy, extreme impatience), AI & tech (150,000+; "…$6K" with the low end hidden; above average; "broad mar[ket] expectatio[ns]", partly hidden).
04-recommendation-four-ai-tech-segments.jpg: "My recommendation — match the client to the size and the offer of your agency": Cash Cows / Brand Builders / Indie Hackers / App & Game Giants with the one-line advice in step 1 above. Slide 22/38.
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
SEO Action Blog: his Chinese-language blog (nine years); SEO Connector: his matchmaking business; his Shenzhen SEO conference. No URLs spoken.
Wondershare: his first in-house job; ~500 staff, about a third in marketing; buys backlinks on TechCrunch, Macworld, PCWorld at "a few grand" each.
DeepSeek and "Timmy" (heard twice; most likely Kimi, since a Kimi speaker was in the room and he calls Kimi Beijing-based) as brand builders.
ByteDance / Volcano Engine (heard "San Yiqing volcano engine"), Alibaba Cloud, DeepSeek, Tencent: China's AI platforms.
WeChat, WhatsApp, Tencent Meeting, Lark; QQ Mail and NetEase Mail (spam risk).
"Jonathan" in the room: an agency owner who serves Chinese e-com brands (surname not said). "Jason" ×2: solopreneurs in the room. Georg (Rank Up, C5) cited for unique content at scale.
Q&A (question → answer)
None; the host closed the slot ("slowest lightning talk ever") and started the break.
Conference break (note-taker's own side task, not part of the talk): an account and credit setup with a link vendor's team, then unrelated hallway chat; not recorded here.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
"US ratio 2:5:5, China 7:5:2" is wrong. The slide shows 752 : 1 businesses per agency for China; the US figure was spoken as "265"/"255" and is not on any photo.
"~1M businesses, ~1,000 agencies" — slide figures are 865,000+ brands and 1,150 agencies, of which only 150 do SEO.
"Brand builders (e.g. DeepSeek, Temu)": the audio says "Timmy", most likely Kimi, not Temu.
"Dominant platforms: ByteDance (Doubao)": Doubao was not said; he named ByteDance's Volcano Engine for business use.
Omits every budget figure on the slides ($3K–$4K median B2B SEO retainer, $5K–$6K e-com, $5K–$15K B2B total marketing, $500–$8K range).
Omits that the speaker is a broker and conference organizer pitching his own event.
The "Conference Break: Service Account Setup" section is the note-taker's side task, not the talk.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
Source of the market figures (the slide's source line is hidden; "MOF…" may be China's Ministry of Commerce).
The US ratio; the AI & tech median budget's low end; the low end of the B2B retainer range ($500 or $600).
"Timmy" = Kimi (likely) or Temu.
His full name and surname spelling (only "JP" and "John" are said; "Chan" comes from the note title).
Kalin - CMSEO sponsor keynote — speaker introduces himself as "Kellen" (title says Kalin; spelling unverified), founder of SEO Domains and Giga Links, plus the charity "I Grow Younger"
Source: Granola https://notes.granola.ai/d/37df1d36-c817-4de2-976a-b1ba83770adb · recorded 2026-11-12 · transcript-verified 2026-11-12 Vendor talk? Yes, and openly a pitch. SEO Domains (aged and archive-restored domains, PBN rent / buy / management, homepage links, link-placement API). Giga Links (guest posts WITHOUT links, sold as "citations for AI", $40 each, cheaper in volume; reseller API). Sister company "Me Up" (garbled) sells guest posts / media placements. Conference promo: 6,000 Giga Links credits for $25,000. Note: the file has two parts: (A) the keynote (about 25 min of speech), (B) a hallway conversation after it. The keynote contains almost no SEO method; roughly two-thirds is a philosophy / brain-state framework, the last third is the product pitch.
Part A — Keynote
Thesis (3 bullets max)
He says he has no goals, discipline or tracking; success came from occupying a unique, defensible position early ("a place on the map" that fits only one company, like Cloudflare), by intuition he cannot explain.
SEO value comes from "flows" not "boxes": aim high, outsource technical SEO and auditing; links pass trust (guest posts / media) and power (homepage links, anchor text); "quality links / quality content" and "pass link juice" are called empty phrases (rent or create link juice; creating = own PBNs).
AI has "no penalties", so cite-for-AI products (Giga Links) and owned domain networks are the opportunity; the company is cash-strapped with illiquid domain assets and is pivoting from selling domains to selling links and citations.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Company size | "eight figure company"; 100+ employees (Bulgaria); 3 board members | company-wide | speaker | spoken | clear |
| Cash position | company "pretty broke", ran out of cash; sponsorships were paid about half a year ahead | now | speaker | spoken | clear, unverifiable |
| Revenue from SEO | "30 million from SEO" | cumulative, undefined | speaker | spoken | clear, unverifiable |
| Audience of owned web properties | visited by "more than 1 billion humans" | cumulative | speaker | spoken | clear |
| Time in business | "last 12 years"; says he has loved link spam "since 2008" |  | speaker | spoken | clear |
| Giga Links price | $40 per post, "even less for volume" | list price | speaker | spoken | clear |
| Promo | 6,000 credits for $25,000; he calls it "$4 per citation" (25,000/6,000 = about $4.17) | today only, at the stand, no promo code | speaker | spoken | clear |
| Case study (second-hand) | Giga Links posts cited in Google AI Overviews "in quite a significant amount" for main queries, in a campaign that targeted fan-out queries | one unnamed case, "they found" | unnamed third party / customer | spoken | clear that no numbers were given |
| Results from small buys | "people are achieving results with like 50" | credits | speaker | spoken | clear, no data |
| Link experiments | "a gazillion of experiments"; links without traffic "absolutely move the needle" | PBN testing | speaker | spoken | clear, no data |
Asserted mechanisms (no evidence given in the talk)
Brain state / "boxes vs flows": goals, structure, measurement are harmful; overthinking is the main enemy; technical SEO and auditing are "left-brain" and damage outcomes. No evidence; it is personal philosophy.
Links pass trust (guest posts, media) and power (homepage links, PageRank, anchor text). Traffic "may give some bonus" but PageRank governs.
Value of a link = combination of placement and recipient; there is no universal "quality link". Examples: aged domain repurposed (restaurant to casino) after about a thousand casino links.
Archive-restored PBNs keep link structure, so link juice holds despite poor homepages and no traffic; "zero fingerprints" at scale.
Placing links "inflates" the link pool like fractional-reserve lending (value from thin air).
Penalties scare people (amygdala); "AI has no penalties".
Throwing a large volume of Giga Links posts will probably get something into training data; he says they cannot guarantee it but the network includes domains with "very good harmonic centrality" (HC claim unverified).
In the AI age labor becomes free, so land (domains, websites, space) becomes the scarce asset.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Rent or buy aged / archive-restored domains from SEO Domains (BLACK-HAT / GREY: PBN; he states "I have been loving spam" and calls penalty risk "calculated"). Price: not given; "very good prices", "$1 links", Borrow links mentioned (garbled).
Place homepage links (power) from SEO Domains' owned network using their API; use for parasite pages, interlinking, and geo citations with "basically zero fingerprints" (BLACK-HAT / GREY).
Buy trust links from guest-post / media placements, e.g. his sister company "Me Up" (GREY: paid placements).
Manage your own PBN, now possible inside SEO Domains (BLACK-HAT).
Buy Giga Links: guest posts without links, designed to be cited by AI; aim at fan-out queries; $40 each, volume discount; promo as above (GREY: paid placement presented as organic content; no links, so lower Google risk, but the intent is to seed citations).
Resell via API (no permission needed; reseller-native).
No other actionable step is given (he said so at the start). Casino is the example niche for repurposed aged domains.
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
SEO Domains (domains, PBNs, homepage links, API, rent or buy; no price). Giga Links ($40/post; 6,000 credits $25,000 today at stand). Me Up (garbled sister company; guest posts / media articles). I Grow Younger (his non-profit; magnet-based "analog language" about brain states).
Named people: "Chris Houghton / Chris Colton" from "Phoenix U" (garbled; earlier CMSEO speaker on Black Cat / iGaming SEO); "Corey" (speaker whose technical talks he finds too left-brain); "Damian" (a board-related person in the room); Simon Sinek (Finite and Infinite Games). Cloudflare as the analogy.
No URLs given. Contact: come to him or the stand today.
Q&A
None. The host said the Q&A was out of time and asked him to answer questions in the event app (he agreed).
Part B — Hallway conversation (business content only; personal/expat chat omitted)
Speakers: unnamed. The transcript labels them E, F and D; no names stated. The recorder is the user's account (David); speaker E (AEO/GEO consultant with hotel clients, lives in Granada, Spain, formerly Seattle) is most likely the recorder, inferred not confirmed.
E on the market: lots of business-owner confusion, so lots of opportunity; clients need a guide or "therapist". E says his business is growing.
E on KPIs: clicks are falling so success definitions must change; explaining that fewer clicks do not mean the brand is failing helps retention. Thailand search results are mostly ads and AI Overviews.
E on work: moving toward AEO / GEO; mentions that Steve Toth spoke last year on "truth alignment" and brand gaps and E does "a lot of that". Process: ask which product features and documentation are undiscussed, extract them from product teams, publish them, then test and show "nobody knew this, now you are in it". Hotels example: event space and features not clearly marked out.
E asked F what they do; F is a LinkedIn lead-gen operator ("everything is done on LinkedIn"; E's reaction line "Legion" is garbled).
F's LinkedIn process: combine content, connection requests, DMs, lead magnets; treat LinkedIn as a networking room, not a pitch channel; read the prospect's profile and find non-sales topics; no automation for early outreach; do not share 2FA / log in as the client; a system with tunable speed ("how fast do you want to burn leads"); aim to get past "page two" equivalent.
F's onboarding model: crash course with the business owner, show month-one workload, get one person in the client org to own it with your support; about six weeks if dedicated, hardest part is knowing the ICP and content voice; then a maintenance bracket plus more training.
E on LinkedIn: inbox is spammed by automation; asked how to get replies.
Recorder pitch / contact offers: none explicit. E described his own services only. No names, companies, emails or contact exchanges appear in the transcript. D (Bangkok-based, ex-UK) made no business offer.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
Speaker name: summary writes "Kelin"; speaker says "Kellen" in the intro, title says "Kalin". Spelling unverified.
Summary frames the thesis as "intuition and map reading". Accurate, but it omits that the talk is a sales pitch and an open pivot: the stated goal is to transition the company from selling domains to selling links and citations.
Summary says "Giga Links ... $40 each" and "6,000 credits for $25,000 ($4/citation)". Transcript confirms; it omits "volume discount", "only valid today and only at our stand, no promo code", "people achieve results with like 50", and the training-data statement: no guarantee, "throw spaghetti at the wall", domains with good harmonic centrality.
Summary says "Cited by Google AI Overviews in case studies targeting fan-out queries". Transcript: one second-hand case, no numbers, unnamed.
Summary omits his claims: "AI has no penalties", "$30 million from SEO", more than 1B human visitors, 12 years, link spam since 2008, "I have been loving spam" and "spam is real quantity", the casino repurposing example, and the "SEO resources company" framing.
Summary lists "Use cases: parasites, interlinking, geo citations with low fingerprint risk". Correct, but those are PBN uses (BLACK-HAT / GREY) and the summary does not label them.
Summary says "Sponsored conferences months in advance before cash ran out". Transcript: sponsorship money was paid about half a year ahead; the company then ran out of cash.
Hallway: summary says "one attendee focused on truth alignment". The speaker (E) said Steve Toth talked about it last year and that he does a lot of it; this is a reference to another CMSEO speaker, not original to the attendee.
Hallway: summary's "onboarding ~6 weeks to self-sufficiency" is right but comes from the LinkedIn operator (F), who also advises no automation and no 2FA sharing; the summary says only "avoid automation".
Summary omits E's AEO / GEO process (extract undocumented features from product teams, publish, test) and the hotel example.
Unclear / needs verification
Speaker spelling (Kellen / Kalin); the "Me Up" sister company name; "Borrow links", "$1 links", "Atlanticity links", "IKMG yostlide Scandinavian" (garbled product or domain lists).
"Chris Houghton / Colton from Phoenix U" (name and company garbled).
Actual definition of "citation" in the $4/citation price (per credit, i.e. per post).
Whether $25,000 and 6,000 credits is stated per credit price of $4.17 (math) versus "$4".
Hallway speakers' identities; "Legion" line; whether E is the recorder.
The "30 million from SEO" figure (cumulative revenue? profit?).
Kimi K3.1: three use cases for non-technical founders — speaker not named (self-described Kimi AI ambassador for Southeast Asia; runs an AI consulting and education company in Singapore; co-founder of a global women-in-AI community)
Source: Granola https://notes.granola.ai/d/fbe97ee4-13c2-4697-823d-54ab2f65411d · recorded 2026-11-14 (14:05 GMT+7; Granola shows 11-13 23:05 PST) · transcript-verified 2026-11-16 (full transcript read, 19.6k chars, about 22 minutes) Resources: no slide photos attached to the Granola note (0 saved; no resources/ folder created). The speaker says all demo sites are live; no URLs are audible. Vendor talk? ⚠️ Partly. Kimi ambassador (says ambassadors are unpaid "power users"); wears a Kimi-designed T-shirt. Also sells AI consulting and corporate training, and the quiz-game demo is the funnel for that training. No price for Kimi or for her services.
Thesis (3 bullets max)
Kimi's brand is built on "taste": the model produces good-looking output, and premium branding is how small firms charge more.
Three uses any non-technical founder can run: a WhatsApp personal assistant (Kimi Claw), quizzes rebuilt as games with an upsell on the result screen, and 3D models of a venue, place or product to sell before you build.
Run many builds in parallel (about 10 windows), then test each with a small ad spend.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Context window | 1M tokens, "about 1,500 pages" in one thread | vendor spec as relayed | Kimi, relayed | spoken | plausible; not checked |
| Computer-use parity | "almost as well as" Claude Opus 5.5 on real computer tasks | no benchmark, task set or date named | Kimi, relayed | spoken | low: no benchmark named; the model names around it are garbled ("clock verge 5.5", "clock paper 5.2") |
| High-speed mode | answers 2–3× faster | none | Kimi, relayed | spoken | vendor claim |
| Cost | "very cost effective" vs US models | no price given | speaker | spoken | no number |
| AI persona audience | 8,900 TikTok followers in about 3 months | one account ("Aira") | speaker | spoken | self-reported; handle garbled ("Ira Cantillove") |
| Who uses Kimi | 66% mainland China; US second; then Japan and Korea | no period or source | speaker, as ambassador | spoken (Q&A) | unsourced |
| Market test budget | about US$50 of ads per prototype | her practice, no results shown | speaker | spoken | tactic, not a result |
No conversion, revenue or engagement data for any of the three use cases.
Asserted mechanisms (no evidence given in the talk)
People finish a game where they would drop a quiz, so the result screen converts better. No numbers.
AI agent features across vendors are converging (scheduled tasks, agent modes, coding tools) because labs are racing for go-to-market and IPOs.
Taste can perhaps be replicated by AI; she poses it as an open question.
Chinese open-weight models will gain ground because top researchers concentrate at US labs. Garbled; her reasoning is unclear.
Data for users in the Chinese region is stored on servers in China.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Use case 1, personal assistant:
On kimi.ai open Kimi Claw, create it with one click, link it to WhatsApp by scanning a QR code. Give it a persona file ("soul.md"-style; spoken "Sol MD"). WHITE
Use it as an always-on assistant and as a community "member" with its own personality. WHITE
⚠️ She disabled one-to-one chat because the persona was repeatedly socially engineered (a community member got it to take instructions it should only take from her). Lock the agent to its owner's instructions before exposing it to a group. WHITE (lesson)
Personal-growth use: upload Zoom transcripts and WhatsApp chats, ask for recurring behavior patterns and blind spots, then have the agent send a daily 10-minute exercise at noon and a self-care prompt in the evening. WHITE, but uploading other people's chats raises consent questions she did not address
Use case 2, quiz to game: 5. Take an existing quiz (examples: the "36 Questions" intimacy quiz; a Human Design profile from birth date, time and place). One prompt: rebuild it as an interactive two-player game. Kimi hosts the back end. WHITE 6. Put the offer on the result screen: email capture, upsell, or a referral to a specialist for a revenue cut. WHITE if the referral cut is disclosed 7. Open about 10 windows, build 10 projects in about an hour, spend about US$50 of ads on each, keep what the market responds to. WHITE 8. Her own use: the game is the top of the funnel for corporate AI training. WHITE
Use case 3, 3D before you build: 9. Give Kimi a URL, photo, sketch or brief; ask for a 3D model. Her demos: the Meliá Chiang Mai hotel and surroundings from a prompt under 10 words (360° view, downloadable); a Women in AI venue in Sarawak, Malaysia (28 Nov) restyled "softer" with 36 decoration items and a 90-minute setup plan, from the venue's photo; a mascot ("Clobie the cat") from a sticker sketch to a 3D merchandise line. WHITE 10. Share the model with the client, let them walk around it, close the sale before spending on the build. WHITE
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Kimi K3.1 Pro (Moonshot AI's Kimi; Beijing team): 1M context, high-speed mode, 3D generation, hosted back ends. No price.
Kimi Claw: one-click agent linked to WhatsApp; she says the Kimi team is deprioritizing it.
Other Kimi features listed as "replicable" elsewhere: scheduled tasks, an agent mode, Kimi Work, Kimi Code.
OpenClaw (mentioned as the earlier, similar product), ChatGPT, Claude: comparison points.
Yang Zhilin (spoken "Yang Chi Lin"): Kimi founder, quoted on taste. ASR spelling.
"Aira": her WhatsApp/TikTok AI persona (8,900 TikTok followers).
36 Questions (spoken "36 questions in love.com"), Human Design: quiz sources.
Meliá Chiang Mai (venue of the talk), Sarawak Women in AI event (28 Nov), "Women Include" community and mascot "Clobie" (both ASR spellings, unverified).
She plugs the next day's speaker on 0 → 500,000 followers (that is C40, Sarvesh Srivastava).
Slide photos
None attached to the Granola note.
Q&A (question → answer)
Should Western brands care how they show up in Kimi? → Only if they want Chinese customers or business in China; Chinese models are becoming more competitive.
Who asks Kimi questions? → 66% mainland China, then the US, then Japan and Korea; Asian users are mostly developers on the API, driven by cost; data for Chinese-region users is stored in China.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
"Coding benchmark: near-parity with Claude Opus 5.5": no benchmark was named. She compared "real computer tasks" and named no test.
The summary omits that the quiz-game demo is her own funnel for corporate training, and that she sells AI consulting; "ambassadors are unpaid" is not the whole conflict picture.
It omits that Kimi is deprioritizing Kimi Claw (her own words), which matters for anyone building on it.
It omits the consent problem in the personal-growth use (uploading other people's chats) and that the persona was socially engineered by a community member, not just by "prompt injection".
Speaker identity: the summary gives none; neither does the transcript.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
Speaker name and company not spoken. One web search (2026-11-16) found an Instagram post about a 28 November "Digital Bloom" women-in-AI event in Kuching (Sarawak) run in partnership with Kimi AI, and a Singapore speaker page (Soh Wan Wei) with a "Women in AI" talk. Neither confirms the speaker; do not attribute.
Model names in the parity claim ("clock verge 5.5", "clock paper 5.2", "open 5.5") are garbled.
"Around four times as much as code" (her usage comparison) is garbled.
The persona's TikTok handle, the community name "Women Include" and the mascot name are ASR spellings.
"66% from mainland China" has no source or date.
Links, Lies, and LLMs — speaker addressed as "Michael" (host) / "Mike" (own anecdote); surname and company NOT stated in transcript
Source: Granola https://notes.granola.ai/d/3d8d7ef4-b3e4-40d4-a6ce-33070870a5b7 · recorded 2026-11-10 · transcript-verified 2026-11-12 Vendor talk? Yes. Speaker says "we sell links" (Q&A). Poland-based link-building / media-house provider; closes by inviting SEO agencies and in-house teams to contact him on a platform the transcript renders as "Kevin" (almost certainly LinkedIn, unverified). The company name is not recoverable: a host question reads "trust Luna's revenue" (garbled). Caveat: the recording starts mid-talk (the "Lie 1" section is already in progress, the opening is missing). Slides are not in the transcript; all numbers below were spoken only.
Thesis (3 bullets max)
Metrics sellers use (DR, "relevant" domain name, traffic) are cheap to fake; he says buyers pay about $12K/yr for DR 65 sites and get no real authority.
Choose publishers by what LLMs already cite: run seed queries through ChatGPT, Perplexity and Claude, capture cited pages and sub-queries, rank pages by how many sub-queries they cover, and treat DR as the last column.
Authority = link-gap analysis with fakes filtered + LLM-citation-mapped publishers + well-built guest posts + monthly consistency.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Correlation of DR with LLM citations | -0.05 (about zero; "predicted none") | 5 billion citations | Attributed to a third-party study, probably Ahrefs; the transcript text is garbled ("errors... trouble check") | spoken | garbled (number and "5 billion" clear, source tool not clear) |
| Mia Khalifa-type site: traffic share from celebrity terms | 80% | one site seen in a new client's link profile (last year); shown with high DR, "traffic over 274" (unit garbled), categories business/crypto | speaker (client audit) | spoken | clear on 80%; garbled on traffic figure |
| That site's sales | 60 posts/month at avg $150 | same site | seller's stats, via speaker | spoken | clear |
| FinTechZoom.com traffic | 1.3M visits/month; "organic traffic over 1 million" | single domain, current | "the tool" (unnamed; speaker says citations come from "the tool", not named) | spoken | clear (host later says "2.3 million" in Q&A, inconsistent) |
| FinTechZoom AI citations | 86 | across "every AI platform", unnamed tool | unnamed tool | spoken | clear |
| FinTechZoom traffic that is branded | "almost 100%" | same site | speaker | spoken | clear |
| FinTechZoom price/volume | $350 per publication, about 40 posts/month | seller data | via speaker | spoken | clear |
| Second celebrity-net-worth site | over 500 citations, all from celebrity topics | one site | speaker | spoken | clear |
| Link-gap crawling reveals more links than Ahrefs | about 30% more | own crawler + proxies on competitors; no sample size | speaker (own claim) | spoken | clear, unverified |
| DR 41 page vs DR 85 page in his ranking output | DR 41 covers 5 sub-queries; DR 85 covers none | illustrative example in his tool output | speaker | spoken | clear, illustrative |
| Sports e-commerce case (a big Polish / European retailer, unnamed) | traffic "over 300%"; "84% of AI Overview"; cited-in-AIO keywords about 10,000 to 18,000 in 12 months | one client, "20 miles of work" (garbled, presumably months) | speaker's agency | spoken | partly garbled: what "84% of AI Overview" measures is not defined |
| Own site ranking for "geo agency" | #1 organic; guest post #4; also in AI Overview / AI Mode / other LLMs | one keyword, own agency | speaker | spoken | clear |
| SaaS client case | first on list in AI Overview mention; guest posts also #1 organic | one client; "one keyword 10,000 per lead" garbled | speaker's agency | spoken | garbled |
| Revenue from outside Poland | "20 or 40%" | speaker guess | speaker | spoken (Q&A) | clear but hedged |
| Per-link cost, Poland / Scandinavia / US | about $200 / about $1,000 / $300-600 | speaker's general view; niche-dependent | speaker | spoken (Q&A) | clear; earlier answer was different, see Q&A |
| Indexing recovery time | 5 to 10 minutes after resubmitting | own indexing system | speaker | spoken | clear |
| "Good" citation-to-traffic ratio | a 5,000-traffic site with 500 to a few thousand citations is "really good" | rule of thumb | speaker | spoken (Q&A) | clear, no data |
Asserted mechanisms (no evidence given in the talk)
LLMs split a prompt into sub-queries and cite from those results, not from the original prompt. The "top 10 for each sub-query is the pool the model picks from"; single citation runs are only a sample.
Branded-keyword traffic is the easiest to fake, so a mostly-branded traffic profile means someone is paying for it.
Bot-traffic fake recipe (taught as what sellers do): see tactics (BLACK-HAT, what to detect).
Google "loves" high-traffic sites (offered as why traffic is trusted, then undercut).
Competitor link-gap with filters (red / yellow / gray / green) beats a blind gap; no data on hit rate.
Guest post with subpage internal links, tier-2 links and sub-query coverage gives more "link juice" and more citation chances; "nobody does it".
"Even a bit of traffic" on a guest post beats none; a link with some traffic and a few citations beats a link with nothing.
Future authority signals: mentions (best with links), Wikipedia, brand search volume; things hard to manipulate.
Europe: law restricts "we are the best" rankings, so brand-promoting listicles are riskier there than in the US.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Build or pull a competitor link gap (WHITE). Output he showed: price column, and a column of how many competitors bought each domain; use it to estimate monthly spend and domains needed. Gaps come from "agencies, media houses, freelancers" (unnamed tool: Ahrefs is the only tool named, as the source of competitor links).
Filter the gap before buying (WHITE): select competitor categories and keywords; filter by link source, by value and by AI presence; drop red = penalized / traffic-hit domains, yellow = forum / profile links, gray = manipulated metrics; keep only green. Then add one more column: AI-cited yes/no. Agencies that skip this resell toxic links (anecdote: an agency refused to drop forum/profile links).
Crawl competitor backlinks yourself (WHITE/GREY): write a crawler, give it good proxies and a database of WordPress or other platform footprints; he says this shows about 30% more competitor links than Ahrefs. Tool not named beyond "build a crawler".
Map publishers by LLM citation (WHITE): enter keyword; run it through ChatGPT, Perplexity and Claude; save cited pages and the sub-queries each run uses; for each sub-query add Google and Bing top 10 plus AI Overview sources; rank pages (not domains) by number of sub-queries covered; DR last. Then buy guest posts on those pages or do outreach. DIY version: check the top 10 for the searches the model actually runs, count pages repeated across sub-queries. Own tool is internal; alternative named: "Sellutor" (see unclear section).
Guest post production (WHITE if disclosed / GREY if paid link): pick a high-position keyword with the right intent so the post ranks; long-form copy using Surfer or a "demo writer" (Semrush writer per summary; the transcript says "demo writer", garbled); internal links from other subpages of the publisher; natural anchor mix; always include a brand mention AND a link; use listicles; answer the sub-queries inside the article (one article, many questions); buy links from other subpages of the publisher to the guest post and build tier-2 links to it.
Buying paid guest posts / link insertions (GREY): the whole model is paid placement; he categorizes budgets as white / gray hat.
Fake-DR / fake-traffic recipe (BLACK-HAT, described to teach detection, not recommended): set up a simple site, connect to Search Console, connect to Ahrefs to feed data, buy cheap junk traffic on branded keywords, results appear in Ahrefs "in weeks"; he says his Polish infrastructure can generate large volumes of traffic that shows in Ahrefs (stated as a joke/warning, unclear whether his firm does it).
Detection checks for any target (WHITE): open organic keywords, top pages, and AI-citation count; compare traffic with citations; if almost all traffic is brand name, treat as bought; ask whether the top pages (e.g. celebrity net worth) are your audience.
Monthly: check indexation of every placed link; re-submit through an indexing system; unindexed = wasted (WHITE/GREY).
Budgeting: run gap analysis, estimate competitor spend, match or exceed; do not compete if a rival spends $10K and you have $1K.
Pricing signals: guest posts Poland about $200; Scandinavia about $1,000; US $300-600 (earlier: about $500 for the US; Poland medium clients "2 or $3,000" per month, unit garbled).
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Ahrefs: DR / traffic data that can be faked; fake traffic fed into it. Competitor links.
Google Search Console: connected to fake sites in the botnet recipe.
ChatGPT, Perplexity, Claude: queried for citations and sub-queries by his internal tool. Gemini not named.
Google, Bing, AI Overviews: top 10 and AIO sources added per sub-query.
Surfer; "demo writer" (garbled, summary says Semrush Writer): long-form drafting.
Internal AI-citation tracker (proprietary); "Sellutor, a Polish company" as alternative (name likely mis-heard).
Own Polish indexing system: re-indexes in 5-10 minutes.
FinTechZoom.com (example of high traffic, 86 citations; sells posts at $350); an unnamed celebrity-content site (Mia Khalifa traffic, $150 posts); "turbogeek" two domains (name garbled) as botnet-traffic examples.
Financial Times and a second garbled domain ("elepa.com"): examples of links nobody can afford.
A "Corey" and a "Plat" (mastermind) mentioned in Q&A banter; not business content.
Contact route: "find me on Kevin" (probably LinkedIn). No URL given.
Q&A (question → answer)
Share of revenue from international markets; ROI Europe vs US? → "20 or 40%" outside Poland; small markets (Estonia, Slovakia) move rankings cheaply; Norway / Denmark guest posts are expensive and need volume; US has huge competition and big budgets.
Realistic cost per Tier-1 link given low-tier guest-post devaluation? → depends on client size; medium Polish clients about $2-3K (unit garbled), Scandinavia about $1,000, US about $500.
Backlinks boosting ChatGPT citations without Google rankings? → different algorithms; you can appear in one, in both, or one only.
Ahrefs keyword data unreliable after updates, how to check ranking terms before buying? → check manipulated metrics, relevance, traffic manipulation and "other things", then pick best price/quality. No tool named.
Buy links that fail your criteria if budget unlimited? → no longer reach the top 10 with cheap links; bet on quality and volume, but not cheap ones; maybe in some industries.
Automation of link acquisition? → many in-house tools; in Poland you must also phone publishers; first step can be automated.
How to communicate authority ROI to stakeholders? → show the link gap and what competitors spend; budget needed for top 5 or top 10.
Value of zero-traffic backlinks? → traffic is easily faked; in casino / gambling you cannot get Forbes-type links, so pages that get cited are a good choice.
Unindexed links? → monthly check; re-submit via own system (5-10 minutes).
AI citation tracking tool? → internal; Sellutor as alternative.
Slides? → host says they will be emailed.
Cost per link? → Poland about $200, Scandinavia about $1,000, US $300-600; depends on niche; not for local things.
Distinguish real-ranking links from DR / DA-only? → "the presentation was about it".
Strongest brand-authority signals in 12-24 months? → mentions, best with links; hard-to-manipulate things such as Wikipedia; invest in things that make people search and write about the brand.
Budget for backlinks? → check what competitors spend, show the client, price by average cost.
Ratio of citations to traffic for a legit site? → depends on industry and country; 5,000 traffic with 500 to a few thousand citations is very good.
Where do you buy links? → "We sell links."
Communicate ROI of backlinks vs insertions? → same: show competitor spend, cost to reach top 10; if client spends $1K against a rival's $10K, do not fight; black-hat has other tactics, but with white / gray hat the budget is the constraint.
Limited budget: backlinks, digital PR, expert mentions, proprietary data? → proprietary data is best but hard at scale (needs case studies and data); otherwise legal / editorial-style placements; always guest posts with brand mentions and links.
If competitors already cover the topic, same angle? → same topic; listicles with brand ranking where law allows (hard in Europe, easier in US); link from the publisher's other subpages and tier-2 links to your post.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
Summary states "Ahrefs study: DR predicted zero of 5B citations". Transcript attribution is garbled; the speaker cites a study of 5 billion citations with correlation -0.05, source not clearly "Ahrefs". Treat as unverified.
Summary calls the sports case "300%+ traffic growth, 84% AI Overview coverage in 12 months". Transcript: traffic over 300% and "84% of AI Overview" (undefined); the 12-month change is about 10,000 to 18,000 keywords cited in AIO. The case is unnamed and self-reported.
Summary gives US cost as $300-600 only. Transcript: first answer was about $500; Poland medium clients "2 or $3,000" (unit garbled) in the earlier answer, about $200 per link in the later one. Inconsistent figures, not one benchmark.
Summary omits that the speaker sells links ("we sell links") and ends with a sales invite; all case studies are vendor-reported.
Summary says the tool adds "Google and Bing top 10 per subquery"; transcript also adds AI Overview sources, and says single citation runs are only a sample (top 10 is the pool).
Summary omits: the fake-traffic recipe (Search Console + Ahrefs + bought branded traffic) and that his Polish infrastructure can generate Ahrefs-visible traffic; tier-2 links and buying links from other subpages of the publisher; the EU legal limit on "best company" listicles; the 5,000-traffic / 500+ citations rule of thumb; first revenue figure (20-40% outside Poland).
Summary says "Sellutor (Polish company)". Likely a mis-hearing of a Polish SEO / AI-visibility vendor (see below).
Summary says "Real authority has four lines on the invoice"; transcript confirms but the lines are muddled in the audio (the speaker mislabels "line 2/3"); the sequence is the same.
The "FinTechZoom 1.3M visits, 86 citations" number is right; host later misquotes it as 2.3 million.
Unclear / needs verification
Speaker's full name and company ("Michael"/"Mike"; company could not be recovered; "trust Luna" is garbled).
"Sellutor": likely a mis-heard Polish vendor name (Senuto is a Polish SEO / AI-visibility company, unconfirmed); check before citing.
"Kevin" as contact platform: probably LinkedIn.
"traffic over 274" for the Mia Khalifa site (units lost); "turbogeek" and "elepa.com" (garbled domains).
Which tool produced "1.3M visits / 86 AI citations".
Meaning of "84% of AI Overview" and "20 miles of work".
"demo writer" (summary says Semrush Writer; unconfirmed).
The 5B-citations source and whether the -0.05 is a correlation coefficient.
Opening of the talk is missing from the recording.
Lunch conversation, LLM Mastery day — a local-SEO agency owner + an unnamed speaker on Bing / ChatGPT retrieval (both anonymous)
Source: Granola https://notes.granola.ai/d/bc0eafee-681c-4d47-bc13-55ede19587cc · recorded 2026-11-13 22:00 PST = 2026-11-14 13:00 GMT+7, conference lunch, LLM Mastery 4.0 day · transcript-verified 2026-11-16 (full transcript read, 58,018 chars) Resources: none. No photos attached; one screen was shown on a phone (a US SERP) and is described only in audio. Vendor talk? No. Informal table conversation. The local-SEO owner runs an agency; the other speaker had presented earlier and uses a vendor tool (WebIQ).
Template adapted: no thesis from a stage, no Q&A. Personal and social chat (travel, health, family, careers) is left out. The note-taker's own remarks are one line under "Note-taker" below.
Who said what (transcript labels):
J = a local-SEO agency owner. Not named here: this was an informal conversation.
A / H = a speaker who presented on replicating engine retrieval ("this was my presentation"); name not said. Heavily garbled.
B = the note-taker.
What others said (3 bullets max)
Local: Google's logged-in US mobile SERP for some verticals now shows ads, then an AI-style local block, and no local pack; logged-out, incognito and rank trackers still show the old layout, so tracked rankings no longer match what customers see (J).
Local agency value now has to be shown in leads and revenue; clients get the same return as last year, but traffic and rankings as proof are "screwed" (J).
ChatGPT visibility is "a mention game", not a backlink game (A/C labels, garbled).
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| New local SERP layout | logged-in users see ads + AI local results, no local pack; incognito shows the old layout | her team searching from phones, logged in, across the US; one person outside the US did not see it; started ~1 week before 11-14; personal-injury queries shown | J | spoken + phone screen (not photographed) | observation, one week, one vertical shown |
| Rank-tracker mismatch | DataForSEO screenshot tool (built into Asana) returns the traditional 3-pack, no ads | same queries | J | spoken | observation |
| Places Scout lag | grid reports run up to ~20 hours late, so the time of day is wrong and closed businesses skew the local pack | her account, recent | J | spoken | observation |
| Retrieval replication | his model replicating Google's fan-out: ~30% two years ago, "above 60%" now; older Gemini (up to "4.5") ~75% | his own studies; metric not defined | A/H | spoken | garbled; unclear what is being correlated |
| GBP-only survival | a client lost ~90% of organic traffic (penalty from old link building) and had its best year ever on Google Business Profiles | one client | J | spoken | anecdote |
| Retainer floor | minimum $4,000/month; average client $5M+ revenue, 2–5+ locations; ads included up to ~$2,000/month spend, more time at $5–10K | her agency | J | spoken | self-reported |
| AI-rewritten site | a client's site redone with all-AI content on a new build; forms went from about 1 to 10 (garbled) | one client | J | spoken | anecdote; she does not yet know the ranking effect |
Asserted mechanisms (no evidence given in the talk)
Citation (NAP) consistency barely matters; only the website and a few sources count, and the AI Overview lists the sources Google uses for that business (J).
Service descriptors in a business name beat location descriptors (e.g. "Painters" over "Detroit"); match the name on the landing page (J).
CTR manipulation holds rank only while it continues (J, from what CTR vendors told her).
Larger clients get cheaper per hour, scrutinize more and implement less (J).
Hotels are "pay to play"; not worth SEO for her agency (J).
"Labrador" and WebIQ: the unnamed speaker describes a Bing-side ranking pipe feeding ChatGPT, with "Harix"(?) open-source Microsoft embeddings; scraping Bing was easy ~4 years ago and is harder now (A/H). Mostly inaudible.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Put UTMs on every GBP post link; if posts get no clicks, stop treating them as a channel (J). WHITE
Run SERP checks logged in on mobile from the client's market, not only incognito or via a tracker (J's team does this across the US). WHITE
Reviews page on the client's own site targeting both "[brand] reviews" and "[category] reviews", instead of a separate review or wiki domain (J; she heard the satellite-site idea on Edward Sturm's podcast and prefers one domain). WHITE
Award sites (Best of [city], Angi industry awards, legal award sites) as trust signals; they cost money (J). GREY (paid awards)
Coupon mailer with a QR code that opens a GBP post instead of the website, to send traffic to the GBP (J, heard on Reddit, never tried, worries the lift lasts only while it continues). GREY
Test backlog: keep a list of untested ideas from conferences (~200 pending) and rank by expected impact and how many clients it applies to (J). WHITE
Lawyers publishing listicles naming themselves the best: FTC and state bar risk; she will not do it (J). (Recorded as a warning.)
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Places Scout (heard "Place to Scout"): local grid tracking, currently unreliable.
DataForSEO: SERP screenshots return the old layout.
Whitespark (Darren Shaw): good tools, but citation work matters less (J).
Jumper Media: sends traffic to GBPs and builds links to them; J "won't touch it". About $600 was mentioned at the table.
WebIQ: the unnamed speaker uses it as a non-Bing index with Microsoft embeddings.
SEO Spring Training (Arizona), SEO Rockstars: US local conferences she calls black hat in practice; SEO Neo for tier-2 spam.
Charles (likely Charles Floate, speech-recognition "Charles float"): she rates him as straight-answering; his ~15 corroboration sites came up via the note-taker.
Edward Sturm podcast (heard "Edward Stern").
Giga Links: the note-taker asked whether its placements are traceable; she avoids anything she would have to hide from a client.
Note-taker: described the LLM-info page / truth-alignment setup he runs for clients (HTML on a reverse-proxied subdomain, client approval app) and named Bonafide as a comparable commercial product.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
The summary does not identify the main informant; she is a local-SEO agency owner and is left anonymous here.
"Correlation between Bing and ChatGPT results ~60%, up from 30%" is not what was said: the speaker was replicating Google's query fan-out with his own model; the metric is undefined.
"Labrador (likely internal Microsoft/Bing)" is the summary's guess; nothing in the transcript identifies it.
"Tested on 30-hotel group with positive impact" and other note-taker details are the note-taker's own claims, not findings from others.
"Steve Toth shoutout noted from Neils": it was a shout-out to someone at the table for a tool; the recipient is unclear.
The summary keeps personal details (communities to join, house visit); they are dropped here.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
The unnamed speaker's identity, "Labrador", "WebIQ" details, "Harix" embeddings, and every percentage he gave.
Whether the new local layout is a test or a rollout; vertical coverage beyond personal injury.
The AI-rebuilt site's form lift (garbled).
AI Visibility in Southeast Asia — Mark McDowell (Founder & CEO, Primal; agency in Thailand and Malaysia)
Source: Granola https://notes.granola.ai/d/2f5ec9d0-efbb-47b9-a8ca-1844517fef67 · recorded 2026-11-14 19:07 PST = 2026-11-15 10:07 GMT+7, LLM Mastery 4.0 · transcript-verified 2026-11-16 (full transcript read, 17,556 chars) Resources: none. No photos attached to the Granola note; slides were not captured, so every figure below is spoken only. Vendor talk? ⚠️ Agency. All data are his agency's client tracking; contact details shown at the end. Name and company settled by one web search (Primal's site and its post about the talk: "tested on 260 brands across Southeast Asia"); the Granola title spells it "Marc MacDowell".
⚠️ The recording starts mid-talk: the setup slides (who, how many brands, which tool, which period) are missing. The opening line says the study tracked the same queries and prompts over the same period across markets including Malaysia and Singapore.
Thesis (3 bullets max)
Google AI Overviews, ChatGPT and Gemini pull from different sources and move independently; optimize and report each one separately.
In Southeast Asia, social platforms (Facebook, YouTube, TikTok) dominate AI Overview sources; ChatGPT prefers specific, data-rich service and product pages.
AI concentrates mentions on the top two brands; push the queries where you sit third or fourth.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Logistics group | ChatGPT mentions 6.5% → 20% after new service pages + 10 blog articles; AI Overviews did not jump the same way | one client; period not given | Primal | spoken | one client, no control |
| Global mattress brand | AI Overview mentions doubled after 9 new how-to guides; ChatGPT down slightly | one client | Primal | spoken | one client, no control; no base given |
| Social sources in AI Overviews | Facebook linked in 100% of AI Overview answers; YouTube ~99%; TikTok 78%; much lower in ChatGPT, TikTok none | 222 prompts, "for this particular data point" | Primal | spoken | base unclear; 100% across every answer is implausible as stated, likely a subset |
| ChatGPT sources in Thailand | most-linked: Thai government sites, then Wikipedia, KTC (bank), MyBest (Japanese comparison site) | 196 Thai brands where ChatGPT linked the brand's site at least once in 30 days | Primal | spoken | clear; no counts per source |
| Page types cited | ChatGPT cited service/product pages (a logistics warehouse page with SLAs and operating data; a finance company's loan product pages); AI Overviews cited blog articles and how-to guides | two clients | Primal | spoken | two clients |
| Platforms move separately | 133 cases where AI Overviews rose 10 points saw minimal rises elsewhere; a 12-point ChatGPT rise came with ~6 points in AI Overviews; Gemini did not follow AI Overviews | client set (one name garbled as "Delaware") | Primal | spoken | clear direction; base not given |
| Rankings vs AI mentions | two-week windows where Google rankings rose showed no significant jump in AI mentions vs normal two-week windows | client set | Primal | spoken | no numbers |
| Content volume | 14 of 17 new articles got no citations; 3 got an AI Overview link; ChatGPT linked 1 of those 3 | 17 articles across two clients; checked ~30 days after publishing | Primal | spoken | small sample |
| Search location | searching from Thailand surfaced Pantip; from the US, UK and Australia, Reddit appeared consistently | 19 hotel, travel and OTA brands | Primal | spoken | clear |
| Concentration | top two brands get 81% of AI mentions | Thailand, Malaysia, Singapore | Primal | spoken | base not given |
| ⭐ Telecom network supplier | AI mentions 16% → 76% | target question (Thai): "which supplier offers after-sales service across Thailand"; period not given | Primal | spoken | one client, no control |
| Pickup time | AI Overviews used new pages in as little as ~3 days; ChatGPT ~7 days | his observation | Primal | spoken | anecdotal |
| Platform share in SEA | Google AI Overviews "95% up", then ChatGPT; Gemini rose fast in Thailand, ChatGPT back ahead | none | speaker | spoken (Q&A) | assertion |
Asserted mechanisms (no evidence given in the talk)
"Good SEO is good AI search" (Google's line) did not hold in his data; strong brands with poor SEO still appeared.
AI "plays favorites": once outside its top two, a brand gets mentioned far less.
ChatGPT "loves specificity": prices, SLAs, operating numbers on service pages raise citation.
Who posts on Facebook matters less than what is posted (Q&A).
Articles that got no citations missed the buyer's intent or answered questions few people ask.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Track the same prompts over the same period, per platform; report each platform as its own number, never one blended figure. WHITE
Find queries where the client appears but ranks third or fourth (or on page two); work the query fan-out topics for those to push into the top two. WHITE
"Source of truth" pages: in-depth company and service facts in the local language across product pages, plus a complete Google Business Profile for every location (telecom case). WHITE
Mine buyer questions from first-party data: the client's call-center recordings were transcribed and analyzed with AI, then turned into FAQ pages, YouTube videos and Facebook posts aimed at mid-funnel questions. WHITE
Put specifics on service pages: prices, SLAs, operating data, numbers. WHITE
Answer buyer questions in ordinary Facebook posts and YouTube videos; the agency added a social team for this. WHITE
Track AI answers from where the client's customers search, not from the client's office (Pantip vs Reddit). WHITE
Localize fully per country; English content can still rank in Thailand (Q&A). WHITE
Request crawling fast after publishing; check citations per page at ~30 days. WHITE
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Primal: his agency (from the web search; not said in the recorded part).
MyBest: Japanese product-comparison/listicle site cited by ChatGPT in Thailand (the note-taker's private note: check it).
Pantip: Thai forum cited when searching from Thailand.
KTC: Thai bank cited by ChatGPT.
Q&A: "Jamie" (runs an agency in the US, type garbled as "ADO"); "Jason" (company garbled). Next speaker introduced: Michal Suski (Surfer; heard "Michal Sukhe").
No tracking tool named in the recorded part; no prices.
Q&A (question → answer)
Most popular AI in SEA? → Google AI Overviews by far ("95% up"), then ChatGPT; Gemini rose quickly in Thailand but ChatGPT is back ahead.
What works on Facebook, and who should post? → The content matters more than the poster: answer real buyer questions (e.g. typical service timelines) for the mid-funnel.
Were the 14 uncited articles just slow? → Pages can be picked up in ~3 days (AIO) or ~7 days (ChatGPT); they check at ~30 days; the misses were intent and demand problems.
Can English content rank in Thailand? → Yes.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
Name and company: Mark McDowell, Primal (one web search), not "Marc MacDowell, consultant".
The summary omits every base: 222 prompts (social), 196 Thai brands over 30 days (ChatGPT sources), 133 cases (platform independence), 17 articles across two clients, 19 travel brands.
"Facebook: 100% of AI Overview responses linked to it" drops the qualifier "for this particular data point"; the base is unclear.
The 6.5% → 20% and 16% → 76% results are one client each, with no period or control; the summary presents them as findings.
Does not say the recording starts mid-talk, so method and sample size are missing.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
Tracking tool, engine settings and period behind all figures (not in the recorded part).
What the 100% / 99% / 78% social figures are a share of.
"Delaware" (likely a client name, garbled).
The 260-brand figure comes from his company's post, not the recording.
King of AEO Tactics — Marc Moeller (SEO agency owner, Perth, Western Australia)
Source: Granola https://notes.granola.ai/d/8213e8d7-d31c-475d-8ba2-2e00ed11668c · recorded 2026-11-14 (11:33 GMT+7; Granola 11-13 20:33 PST), LLM Mastery 4.0 day · transcript-verified 2026-11-16 Resources: ../resources/marc-moeller/photos/: 5 slide photos saved and read. Tool kit offered via QR code → brand search → download button on his site (Granola note lists https://marcmoeller.au/tools/; not opened, not verified). Several attendees could not scan or download the QR on the day (audio after 25:31). Vendor talk? ⚠️ Partly. Runs an agency for listed brands ("spend a million dollars per month on Google Ads"); gives away his own tool kit, positioned as replacing paid tools. He is a competitor in the contest he analyses and claims to have won it.
Context: the "King of AEO" contest is the same stunt the note-taker measured on 2026-09-15: a press-release play that won one invented prompt. This talk is a competitor's account of the October phase. Every contest number below is from his own tracking dashboard; no engine run counts, dates or locations were given.
Thesis (3 bullets max)
AEO is a velocity game: whoever publishes the same claim fastest across the most channels (press releases, socials, Reddit, video) wins; lower the cost of publishing until an AI agent can do it by voice prompt.
AI trusts third parties over self-praise: own-site claims alone lose; the same claim on external sources wins.
AEO is still SEO: to be recommended you need to rank top 10 in Google, and in Bing for ChatGPT.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| AI Overview presence | AIO on 80% of search results | no base, no source | not named | spoken | low: unsourced |
| Dooley citation share | AI cited Dooley as King of AEO 75 of 117 times | his contest tracking; engine(s), period and prompt count not stated | speaker | spoken; not on a photographed slide | low: no method |
| Own site vs own + external | recommended 10% of the time with own-site article only; 39% with own site + an external independent source | "in these cases"; no base, no engine split (says "especially Google's AI Overviews") | speaker | spoken | low: no base |
| Exact-match domains | 31 EMDs tracked at the start, 7 left in Google after about one month | contest domains; "left" = still indexed/ranking (not defined) | speaker | spoken | medium: count, no method |
| Formats | 4 of the 5 named first combined multiple formats (Instagram, YouTube, etc.) | contest | speaker | spoken | low |
| Citation types by engine | AI Overviews cited video/social 25 of 39 times; ChatGPT 1 of 38 | contest prompts; he warns it varies by industry | speaker | spoken | medium as a contest count; one invented query |
| Bing ↔ ChatGPT | about 50% of brands ChatGPT mentions/recommends also rank in Bing top 20 | no base, no period, no prompt set | speaker | spoken | low |
| ChatGPT bot page types | 36% articles and guides, 38% "other pages"; homepages most visited for local businesses; product pages for manufacturers and e-commerce | his clients' server logs; no counts | speaker | spoken (garbled) | low |
| ChatGPT fetch pattern | opens one page, then 2–3 linked pages from it | his logs; no counts | speaker | spoken | low |
| Contest results page | top 3 pages for the query have "no quality linking sites"; 6 of the first 6 visible results have the query in the title; 7 of 8 visible rows name Dooley, 1 names Quaid | his dashboard, one query | speaker's tool | photo 03 | clear as a screenshot of one query |
| Paid tools replaced | Peec AI US$95/month; SerpApi US$75/month; total paid equivalent "~$170 a [month]" (bottom line partly hidden) | his comparison | speaker | photo 04 | clear for the two named prices |
Asserted mechanisms (no evidence given in the talk)
Freshness and velocity decide the answer; another competitor's YouTube videos and press releases "superseded" his answers overnight. Anecdote.
Repeating one claim across many voices makes the LLM treat it as consensus ("overwhelmed the LLMs with the same evidence").
Backlinks did not move the contest: "Julian Dolly" (likely Julian Goldie) had 2,000 backlinks and was not recommended. One case.
A self-made "official rulebook" site can redefine who won: AI Overviews named him winner and ChatGPT showed Dooley "disqualified" after he published rules requiring the winner to be an educator. Screenshots were shown on stage but not photographed.
ChatGPT uses Bing's index heavily, is building its own index (OAI-SearchBot), and will rely on Bing less over time (inferred from rising OpenAI bot activity in his logs).
Pages not in Google's or Bing's index cannot be cited.
PDFs uploaded to high-authority sites get crawled into LLM training data even if not cited.
EMDs survive only if they look like real businesses (schema, LinkedIn company page, About and privacy pages, press releases, backlinks).
Google and Bing are poisoning scraper data: a DataForSEO query "who won the World Cup" returns a lawnmower ad; "dentist near me" returns Microsoft sign-in pages. Spoken only.
ChatGPT "loves" citing .gov and .edu sites.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Copy what the winners did (photo 02):
Map who holds the top 10 for the target query and how strong they are. WHITE
Win the smaller searches first, then grow. WHITE
Pick the client's real advantage and express it as entity–attribute–value (his example: small-business CRM · setup time · 2 minutes, vs 20 minutes for a rival); prove it with video and statistics. WHITE if true
Publish press releases and share them on social; automate the press-release platform so an AI agent writes and submits from a voice prompt. WHITE if disclosed as releases and true; GREY at volume
Get many voices to say the brand is best: influencers, partner sites, LinkedIn, Reddit, Instagram, Facebook, YouTube. WHITE if earned or disclosed
Create your own subreddit rather than posting in moderated ones; he also seeded comments in a competitor's subreddit and was deleted. GREY (own subreddit) / BLACK (seeding rivals' communities)
Build an "official" arbiter: a rulebook site for the contest, a Wikipedia-style "wiki" site about the client in entity–attribute–value form. GREY (wiki look-alike) / BLACK (self-written rules that disqualify a rival)
Buy Fiverr gigs (~US$25) to upload PDFs to high-authority sites. BLACK (parasite placement)
Make EMDs look like real businesses (schema, LinkedIn page, About/privacy pages). GREY (purpose is ranking a keyword domain)
Run the query fan-out tool on the main query, then check whether you rank in Bing for each sub-query. WHITE
Check indexation in Google and Bing for every placement; indexing tools named: "Speed Bins"/"index now fast" (garbled), "Rapid Indexer". WHITE for checking; submission services GREY
Read Cloudflare or server logs for OpenAI bots; verify real vs spoofed by IP; check no .env credential files are exposed (fake bots probe for them). WHITE
Buy aged LinkedIn/Reddit accounts on accsmarket.com; run them from broken phones bought on eBay, controlled by an AI agent, to look like real users. BLACK
Name a Trustpilot listing "Top 10 Best Personal Injury Lawyers" and recommend yourself in it (seen in a Trustpilot group). BLACK
Use scrapers he trusts when rank trackers are poisoned: "Prism Crawl" and "Fuel Myself" (garbled), or his own Bing/Google scrapers after warming up a logged-in Bing profile. GREY (scraping logged-in results)
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
His kit (photos 04–05; free, "saved on your computer"):
Query fan-out tool: "see the searches ChatGPT really ran, not guesses". Demo shows query_fanout.py --replay examples/… with the prompt "How does IndexNow work for a small website" (a replayed example).
AI visibility tracker: "replaces Peec AI, US$95 a month".
Bing scraper: "Bing rank and index checks with no paid API". Demo JSON shows "source": "offline_fixture", "bing_indexed": true (fixture data, not a live check).
Google scraper: "replaces SerpApi, US$75 a month". Demo serp.py "best coffee grinder" --demo, "provider": "demo".
AEO dashboard: rankings and AI Overview sources, stored locally.
Ahrefs free DR check: "vet sites without a paid Ahrefs plan"; he says Ahrefs' DR API became free "a couple of months ago" and can check millions of expired domains.
Rank and Index Tracker (King of AEO): Google, Bing and indexing in one dashboard.
OpenAI bot log checker: collect.sh > hits.tsv, analyze.py; checks each IP against published ranges → "verified" or "spoofed". Others:
OpenAI crawlers (photo 01): OAI-SearchBot builds ChatGPT search ("block it and you leave ChatGPT search answers"); GPTBot collects pages for AI training ("blocking it does not affect ChatGPT search"); ChatGPT-User fetches a page when a person asks ("OpenAI says robots.txt may not apply").
accsmarket.com: aged social accounts. Trustpilot. Fiverr. eBay (broken phones). DataForSEO (named as poisoned).
"Prism Crawl", "Fuel Myself": scrapers he trusts; the note-taker's own notes say "Prismcrawl and cloro".
People (audio spellings in brackets): James Dooley (Louis, Cooley, Gooley, Duly, Doobie) · Charles Floate likely (Charles Lo) · David Quaid (Quay; "royal charter of SEOs") · Julian Goldie likely (Julian Dolly / Cody) · "Davis Wayne", "Jenny Child" (unidentified) · Jesper Nissen (on photo 03, reddit/facebook/jespernissen.com) · Edward Sturm (linkedin.com/posts/edwar…, photo 03).
Slide photos
Full text of each slide: ../resources/marc-moeller/slide-text.md Saved in ../resources/marc-moeller/photos/ (5, all readable):
01-openai-crawlers-three-bots.jpg — OAI-SearchBot / GPTBot / ChatGPT-User with the three one-line rules above.
02-copy-what-the-winners-did.jpg — "Copy what the winners did": map who holds the top 10 and how strong · win the smaller searches first, then grow · publish press releases, share them on social · get many voices to say your brand is b[est] (partly hidden).
03-king-of-aeo-top-pages-table.jpg — his dashboard for the contest query. Banner: "[co]ntent, not links. The top 3 pages have no quality linking sites. A page answering this exact query, plus a few rea[l lin]ks, can take it." Rows: 1 reddit.com/r/jespernissen… "James Dooley has been crowned as the King…" (forum, names Dooley) · 2 usatoday.com/press-relea… "The King of AEO Founds Decision Engine Opt…" (press release, Dooley) · 3 primaryposition.com/blog… "Who is the King of AEO and AI Visibility?" (article, owner David Quaid, names Quaid) · 4 linkedin.com/pulse/who-k… "Who is the Official King of AEO?" (open-platform article, Dooley) · 5 linkedin.com/posts/edwar… "The King of AEO competition is my favorite t…" (social post, Dooley) · 6 seodanmark.dk/seo/king-… "King of AEO is crowned - James Dooley the…" (article, Dooley) · 7 facebook.com/jespernissen… (Dooley) · 8 jespernissen.com/king… (cut off). His own site does not appear in the visible rows.
04-tool-kit-list-with-paid-equivalents.jpg — 8 tools with one-line purposes and two named paid equivalents (Peec AI US$95/month, SerpApi US$75/month); bottom line "…d equiva… …$170 a…" partly hidden.
05-tool-kit-screenshots-grid.jpg — screenshots of the 8 tools; the Bing and Google scraper outputs are labeled offline fixture / demo.
Q&A (question → answer)
None on stage ("we're not doing Q&A live"). After the talk, attendees reported the QR download not working.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
"Google AI Overviews ignores self-praise ~90% of the time … own site + external ~39%": no base, engine split or prompt count was given; treat as his estimate.
"~50% of brands recommended by ChatGPT also rank in Bing top 20": no base or method; the summary states it as a finding.
"Tools to check indexing: SpeedBins, IndexNow Fast, Rapid Indexer": the first two are speech-recognition guesses; IndexNow (the protocol) was not named in speech. IndexNow appears only as the sample prompt in his fan-out demo.
"Prismcrawl and FuelMyself": "Fuel Myself" is garbled; the note-taker wrote "cloro".
"Bing rankings still align heavily with Open ai results", "PDF gigs on Fiverr", "Wiki sites", "Accsmarket.com" headings come from the note-taker's private notes as well as the talk; the summary does not separate them.
Omits how he "won": a self-written rulebook site that disqualifies the contest's founder. The summary lists wiki sites and EMD hygiene as client next steps without the BLACK/GREY labels.
Omits that his tool demos ran on fixture/demo data, and that the paid equivalents are Peec AI and SerpApi.
Omits the .env credential-theft warning about fake OpenAI bots.
"Next Steps" (set up automated press releases, PDF seeding, wiki sites) are Granola's, not commitments from the talk.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
He "ranked for best [Tencent?] SEO specialist within 24 hours" after press releases and awards: query garbled (possibly "Perth").
"Ahrefs free DR API": a free Ahrefs DR endpoint exists in Ahrefs' API (public-domain-rating-free); whether it allows "millions" of checks was not verified.
The AIO and ChatGPT screenshots naming him winner were not photographed; the note-taker's 09-15 measurement found the title wins one invented prompt only.
"Julian Dolly", "Davis Wayne", "Jenny Child", "Charles Lo" are speech-recognition spellings.
DataForSEO poisoning examples: spoken only; not reproduced.
marcmoeller.au/tools/ not opened; tool code not reviewed.
What Moves the AI Answer: Measurement, Proxies, Levers — Michał Suski (co-founder, Surfer)
Source: Granola https://notes.granola.ai/d/c29dd37a-531d-4497-995c-ddd3942435df · recorded 2026-11-13 16:20 GMT+7 (01:20 PST), Chiang Mai SEO main stage · transcript-verified 2026-11-16 Resources: 10 slide photos saved to ../resources/michal-suski/photos/ (prefix t1-). 7 legible, 3 too blurred for the body text (t1-01, t1-04, t1-07; the headline and one number read on t1-04 and t1-07). Photos copied from the local copies the Granola tool saved. He offered a free data form (QR) and, via LinkedIn, a findings file "you can put into your processes". Deck: the speaker published the full talk at https://msu.ski/chiang-mai-seo-2026/ under the title "The story of 50M scraped LLM answers" (56 slides with the line he said for each, a playbook, two audit prompts with the number behind each check, and a method note). Saved 2026-11-17: the page text as ../resources/michal-suski/chiang-mai-seo-deck-page.md and the PDF as ../resources/michal-suski/the-story-of-50m-llm-answers-michal-suski-chiang-mai-seo-2026.pdf. Figures marked "deck" below come from the page text; the PDF slides were not re-read one by one. Vendor talk? ⚠️ Yes. Every chart is "Data From Surfer AI Tracker", Surfer's paid product. All findings are winners-vs-losers comparisons and correlations inside Surfer customers' tracked prompts. No controlled test was shown. Asked how he separated correlation from causation, he did not answer it ("I will do them all").
Thesis (3 bullets max)
AI answers are noisy: measure many runs, every day, intents not phrasings, the real interface not the API, and each engine separately.
The usual proxies (PageRank, domain age, links to trusted sites, llms.txt, schema, GEO checklists) barely separate cited pages from uncited ones.
What does: match the intent and answer in the first 50 words, self-contained chunks, more facts about the entity, concrete specifics, and lists (yours and others').
Measured claims
All figures: Surfer AI Tracker, Surfer customer prompt sets, five engines (ChatGPT, Perplexity, Gemini, AI Overviews, AI Mode; Claude excluded because it cannot be scraped), winners vs losers or correlation. None is a controlled test.
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Dataset | about 50 million answers; ~100,000 prompts a day | 5 engines daily since March 2025, scraped from the real interfaces | Surfer | spoken + deck (slides 2–3, method note) | the deck settles it at 50 million; the "15 million scrapes" in the audio is a mis-hearing |
| Run-to-run overlap | two runs of the same prompt share 40% of brands | sample on the slide footer, not in the page text | Surfer | spoken + deck (slide 7) | base not in hand |
| Brands surviving repeats | 4% of brands appear in all of 20 runs; with 5 daily runs, 16% of brands and 16% of cited domains appear in every run | sample on the slide footer | Surfer | spoken + deck (slide 8, tracking-audit calculator) | base not in hand |
| Overlap over time | brand overlap 40% the next day, 36% after 7 days, 31% after 30 days, 28% after 90 days. Cited-domain overlap falls faster: 37% the next day to 13% after 90 days | sample on the slide footer | Surfer | spoken (36 / 31) + deck (slide 9: 40 → 28; audit prompt: 37 → 13) | the metric is overlap of brands (or cited domains) in answers to the same prompt |
| Rewording vs new intent | rewording a question keeps about three quarters of its brands; a different intent keeps barely a third. Brand overlap lost: −8 pp by rewording vs −19 pp by asking another engine | sample on the slide footer | Surfer | deck (slide 10, audit prompt) | base not in hand |
| API vs scrape | only 29–42% of an API answer's top-3 brands make the top 3 in the chat interface (chat against itself: 49–54%) | sample on the slide footer | Surfer | spoken ("very little overlap"); t1-02; deck (slide 12) | the fair comparison is 29–42% against the 49–54% ceiling, not against 100% |
| Engine overlap | spoken: 40–50% between engines. Deck: ChatGPT and Perplexity track other engines at 0.32–0.40; Google's three surfaces track each other at 0.58–0.70 | sample on the slide footer | Surfer | spoken + deck (slide 13, audit prompt) | the two figures use different measures; no per-pair table in hand |
| Big domains | only 8.9% of a niche's core sources come from the global top 20 domains (Reddit, LinkedIn, YouTube…) | 4,000 reports (spoken) | Surfer | spoken + deck (slide 17) | average across niches |
| ⭐ PageRank vs citation | correlation with the page being cited: all engines −0.01; AI Overviews −0.05; AI Mode +0.02; Perplexity +0.01; ChatGPT −0.01; Gemini −0.04. With the brand being named: +0.05 to +0.06 on every engine | Common Crawl PageRank; Jul–Sep 2026; axis −0.2 to +0.2 | Surfer | t1-03 | correlation; both sides are tiny. He reads +0.05 as "it helps the brand"; on this scale it is near zero too |
| Harmonic centrality | "positive but very low": the one authority metric that always points up, but covering the facts matters about eight times more | — | Surfer | spoken + deck (slide 21) | ratio only, no values |
| Organic traffic | helps brand naming a lot; little or negative for URL citation | — | Surfer | spoken | no number |
| Domain age | no big difference between 2- and 10-year-old domains; slight positive for Google engines, slightly negative / near zero for ChatGPT and Perplexity. Deck: old domains win on volume because they have more pages; inside one prompt, age barely matters and flips sign on ChatGPT and Perplexity | — | Surfer | spoken + deck (slide 23) | "66 for 30-year-old domains" garbled |
| GEO checklist items | FAQ section, expert quotes, table of contents, relevant statistics: "barely nothing" without intent match and an early answer. Deck: every checklist item sits at the bottom of 20 page features; answering the query early is worth four to five times more | — | Surfer | spoken + deck (slides 24–25) | ratio only |
| Links to trusted sites | correlation 0.031 all pages; 0.007 blog posts | — | Surfer | spoken; t1-04 (blurred) "External links in blog posts vs being cited: ≈ 0.007" | correlation |
| llms.txt | "close to zero, sometimes negative"; flips sign by engine: "plus 4 on Gemini, minus 2 on AI Mode"; −0.04 pp once big hosts are excluded | — | Surfer | spoken + deck (slide 30, audit prompt) | unit of the +4 / −2 not stated in the page text |
| Schema | "always positive but not that high": citation rate +3.7 pp with vs without JSON-LD; Product markup +0.1 pp | — | Surfer | spoken + deck (slide 31, audit prompt) | he calls it correlation, not causation ("it marks sites someone actually maintains") |
| Ranking overlap | 95% of cited domains rank in Google's top 10 for at least one keyword | — | Surfer | spoken + deck (slide 34) | weak test (domain-wide, any keyword) |
| Own site cited first | first citation of your own site = about +25% visibility; later ones add little | — | Surfer | spoken + deck (slide 35) | no base |
| ⭐ Answer position | 29% of cited passages come from the first 50 words; another ~10% from words 50–100 | passage analysis | Surfer | spoken; t1-05 "Answer in the first 50 words"; deck says "almost a third" (slide 37) | descriptive share of cited passages |
| Intent match | aligned pages most cited, somewhat-aligned less, misaligned informational pages close to zero; "[?]0% more citations when the page matches the intent, the strongest of 20 page features" | three buckets graded by an LLM | Surfer | spoken; t1-05 (leading digit hidden by the speaker); deck (slide 38): an on-intent page is a source 42% of the time, an off-intent blog post 13% | footnote says "values read from chart, approximate". The hidden headline percentage is still not confirmed |
| Chunk features | general-to-specific progression, introduction section, inter-section connectivity, semantic triplets, self-contained paragraphs, clear concept definitions, information density, top-level headings, subheading navigation | share cited per feature, scale 0–25% | Surfer | t1-06 | bar values not readable; footnote "values read from chart, approximate" |
| Fact coverage | winners cover more facts: 39% of the facts in the top 3 sources, 26% by rank 50 | — | Surfer | spoken + deck (slides 40–41) | what counts as "the facts" is not defined in the page text |
| ⭐ Unique angle | correlation 0.12 between uniqueness and being cited | "on every engine" (caption blurred) | Surfer | t1-07 (blurred) | ⚠️ the bar chart under it is the share of high-uniqueness pages that show each feature (t1-08 footnote), not each feature's effect on citation. "Concrete specs beat original data" is read from prevalence, not effect |
| Listicle share | stable Jan–Sep 2026: third-party lists 23–25%, own (self-promo) lists ~10–12% | same tracked prompts | Surfer | spoken | no slide photographed |
| Cited list → named | +16% visibility; also a higher position | — | Surfer | spoken | C36 slide gives the definition: +16 pp, 57% → 73% |
| Competitors on your list | each gains ~4 points | — | Surfer | spoken | no base |
| Listed first | on your own list, named 38% of the time when listed first vs 26% when not ("+12" is percentage points) | — | Surfer | spoken + deck (slide 46) | no base |
| "best" in title (own site) | 29% of winners vs 43% of losers for brand naming | 201,534 self-promo pages, 5,162 reports, Jul–Sep 2026 | Surfer | spoken + t1-09 | winners-vs-losers |
| Four or more lists | brands with four or more cited lists of their own are mentioned in 38% of answers vs 26% with none (spoken: "+10 points") | — | Surfer | spoken + deck (slide 48) | no base; likely confounded by brand size |
| Slot on others' lists | #1 gets named about half the time, #10 barely at all | — | Surfer | deck (slide 49); the LLM Mastery deck gives 52% / 32% / 13% | no base |
| ⭐ Two games (t1-09) | Gets the page cited, winners vs losers: brands on the list 11 vs 8; table cells 30 vs 0; answers the query early 96% vs 80%; flagged AI-written 82% vs 71%. Gets the brand named: internal links 11 vs 7; words on the page 2,350 vs 2,660; "best" in the title 29% vs 43%; flagged AI-written 63% vs 75% | writing-factors study, 201,534 self-promo pages, 5,162 reports, Jul–Sep 2026 | Surfer | t1-09 | winners-vs-losers; "AI-written" = an AI detector's flag |
| ⭐ Content age (t1-10) | 57–74% of citations in AI Mode, AI Overviews, ChatGPT and Perplexity go to pages older than six months (AI Mode 57, ChatGPT 62, AIO 64, Perplexity 74). Gemini is the exception: 45% under three months, 38% older than six. Older than two years: Gemini 14, AI Mode 23, ChatGPT 23, AIO 27, Perplexity 38 | citations by page age since publication date; Mar–May 2026; pages with an explicit date only | Surfer | t1-10 | descriptive share, not a lever; he said "60–70%" and "a quarter" and did not mention Gemini |
| Brand outlasts citation | brand name stays in answers after the citation drifts away | "a lot of reports" | Surfer | spoken + deck (slide 52): 83% of the mention survives eleven weeks | the LLM Mastery deck adds that citation frequency falls to 26 (first month = 100) |
| ChatGPT source cut (Q&A) | early 2026 ChatGPT dropped 30% of all cited sources but only 20% of listicles | — | Surfer | spoken | no base |
Asserted mechanisms (no evidence given in the talk)
AI resolves the underlying intent, so paraphrases of one question collapse into one answer; track intents, not wordings (t1-02). The overlap data was not shown.
Making extraction cheap in tokens is what gets a page cited ("we already work for the machines").
Brand naming is driven by "the amount of sources that cite your brand"; "if you've got a lot of money, just flood the web" (Q&A).
AI-written pages are cited more because "AI understands AI better".
Long, refreshed, information-dense YouTube descriptions move the needle. Second-hand study, source not remembered ("PKI data" garbled).
Getting your own site cited first, then third-party sources, is the right order. From the +25% number, no test.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Measure (t1-02):
Many runs: treat each prompt as a probability, not a position. WHITE
Every day: drift is "real and silent". WHITE
Intents, not strings: count unique intents before deciding how many prompts to track. WHITE
The real interface: scrape the consumer UI; the API is a different product. WHITE
Each engine separately: no single AI visibility number. WHITE
Find the "core sources" cited every day in your niche; do not assume Reddit / YouTube dominate. WHITE
Write (t1-05, t1-06): 7. Answer in the first 50 words; skip the introduction. WHITE 8. Match the intent: a how-to query gets a how-to page, not a pitch. WHITE 9. Each paragraph stands alone, general to specific. WHITE 10. Cover more facts about the entity instead of keywords. WHITE 11. Add concrete specs only you state (his example: "weighs 300 g"). WHITE
Lists: 12. Own-site lists: put yourself first; choose the competitors you list (they gain too); avoid "best" in the title; build several comparison pages ("versus", "alternatives") rather than one. WHITE if competitor claims are true 13. Push for a higher slot on lists that already cite you rather than new listings at low positions. WHITE when editorial; GREY when paid (gate) 14. Keep older pages; update them rather than replace them. WHITE 15. "Flood the web" with brand mentions if you have money (Q&A). GREY/BLACK depending on method; behind the gate 16. Write citation-bait pages entirely with AI (Q&A). GREY; based on a detector correlation
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Surfer AI Tracker: source of every chart (scrapes five engines daily). No price given. The agency has Surfer access, including AI Tracker tools.
Common Crawl ("Common Pro" in the audio): PageRank and harmonic centrality data.
Earlier speakers he cites: Jonathan Kiekbusch (C22), "Felix" (repeat runs), "Frederick Shopman" (garbled, previous speaker), Jabez Reuben ("Chavez Rubin": prompted the content-age study), Kalin (C11, joke), Matt Diggity ("do all the things").
QR codes: a free data form (deck slide 55: "a free AI visibility report"), and his LinkedIn for a findings file. URLs not legible in the photos.
https://msu.ski/chiang-mai-seo-2026/: his page for this talk (slides, playbook, two audit prompts, PDF). https://msu.ski/llm-mastery/ is his page for the follow-up listicles talk.
Slide photos
Full text of each slide: ../resources/michal-suski/slide-text.md
t1-01-blurred-five-item-list.jpg — a numbered 1–5 list with a headline; too blurred to read.
t1-02-how-to-measure-five-rules.jpg — 1 Many runs (a probability, not a position) · 2 Every day (drift is real and silent) · 3 Intents, not strings (paraphrases collapse into one answer) · 4 The real interface (the API is a different product) · 5 Each engine separately (no single AI visibility number).
t1-03-pagerank-myth-correlations.jpg — "Myth: PageRank doesn't get you cited": correlation with page cited / brand named: all engines −0.01 / +0.05; AI Overviews −0.05 / +0.05; AI Mode +0.02 / +0.05; Perplexity +0.01 / +0.05; ChatGPT −0.01 / +0.06; Gemini −0.04 / +0.05. Jul–Sep 2026, scale −0.2 to +0.2, Surfer AI Tracker.
t1-04-linking-to-wikipedia-myth-blurred.jpg — "Myth: Linking to Wikipedia won't save you"; "The Data: External links in blog posts vs being cited: ≈ 0.007". Rest blurred.
t1-05-how-to-write-for-ai-five-levers.jpg — "Lever: How to write for AI. Format beats gimmicks": 1 Answer in the first 50 words; 2 Match the intent; 3 Write chunks AI can lift; 4 Cover the facts; 5 Be specific, not original. "[?]0% more citations when the page matches the intent, the strongest of 20 page features" (first digit hidden); footnote "…read from chart, approximate".
t1-06-write-in-chunks-ai-can-lift.jpg — nine features with bars (general-to-specific progression, introduction section, inter-section connectivity, semantic triplets, self-contained paragraphs, clear concept definitions, information density, top-level headings, subheading navigation); footnote "…feature is cited. Scale 0–25% (same as #8). Values read from chart, approximate." No bar values legible.
t1-07-unique-angle-0.12-blurred.jpg — "Lever: Unique angle 0.12", caption blurred (reads like "Correlation between … and being cited … on every engine").
t1-08-unique-angle-feature-labels.jpg — concrete specs and detail; niche sub-angle / segment; expert perspective / POV; practical how-to guidance; comparison / scoring framework; deep single-entity focus; original / first-hand data; local / regional specificity. Footnote "Share of high-uniqueness pages showing e[ach]…".
t1-09-cited-vs-named-two-games.jpg — "Lever: Cited vs. named: two games": figures in the Measured claims table; "Writing-factors study. 201,534 self-promo pages, 5,162 reports. Jul–Sep 2026."
t1-10-older-content-still-gets-cited.jpg — "Lever: Older content still gets cited": per-engine age bands (in the table above); "57–74% of citations in AI Mode, AI Overviews, ChatGPT and Perplexity go to pages older than six months"; footnote "…by page age (since publication date). Mar–May 2026. Pages with an explicit date only."
Q&A (question → answer)
Do third-party mentions beat backlinks, rankings or own content, and how did you separate correlation from causation → "do all the things"; testing separately takes too long while things change. Not answered.
Top three factors for being recommended, with numbers → user intent first; for brand naming, the number of sources that cite the brand ("flood the web").
Which tactics were disproven → keywords without context (replaced by facts); "don't do listicles" (ChatGPT cut 30% of sources but only 20% of listicles in early 2026).
AI-written vs human-written → pages flagged by "a simple AI detector" as AI are cited more; human-like pages do better for brand naming.
Why Claude was excluded → cannot be scraped.
YouTube → long, refreshed, dense descriptions (second-hand study).
Listicle language → follow what the market's answers cite; English sources in a non-English market can be an edge.
Non-English answers and the "advice for a new SEO" question → not answered before the session ended.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
"60–70% of cited pages are 6+ months old": the slide says 57–74% for four engines, and Gemini is the exception (45% under three months). Period Mar–May 2026, dated pages only.
"Domain authority… helps brand naming": the PageRank correlation with naming is +0.05 to +0.06 on a −0.2 to +0.2 axis; near zero too.
"Unique concrete specs are a stronger differentiator than original data": the chart shows how common each feature is on high-uniqueness pages, not its effect on citation.
"Avoid 'best' in titles… winners 29%, losers 43%": that is the brand-naming side; the talk does not say "best" hurts citation (C36 shows +0.05 for citation).
"Scrapes are more reliable": he said the API is a different product; "more reliable" is the summary's word.
"Schema… causation artifact": he said correlation, not causation.
"Request Michał's raw dataset": he offered a free data form and a findings file via LinkedIn, not raw data.
"Track intents not recordings" is the note-taker's private note ("rewordings").
Omits that every chart is Surfer AI Tracker data, that the footnotes say values were read from charts and are approximate, and that he did not answer the causation question.
Omits the 50 million vs 15 million discrepancy (the deck says 50 million).
Unclear / needs verification (mis-heard names, numbers you could not pin down)
The intent-match headline percentage on t1-05 (first digit hidden). The deck gives 42% vs 13% for the same point but does not show that headline in the page text; check the PDF.
The 20 page features list and the chunk-feature values.
Sample sizes and periods for the noise tests: the deck says each slide lists them in its footer; they are in the saved PDF, not in the page text.
The unit behind llms.txt "plus 4 on Gemini, minus 2 on AI Mode".
"66 for 30-year-old domains".
"Frederick Shopman", "Felix", "PKI data": speech-recognition spellings.
Three photos too blurred for body text (t1-01, t1-04, t1-07). The matching deck slides are in the saved PDF: t1-04 is slide 28 and t1-07 is slide 42; t1-01 is a five-item list that could not be matched from the page text alone.
His own caveat in the deck: these are correlations and comparisons within prompts and niches, not proven causes.
Listicles: Getting Cited vs Getting Named — Michał Suski (co-founder, Surfer)
Source: Granola https://notes.granola.ai/d/f8eb14f7-67ea-4e63-b400-e1700cf5a777 · recorded 2026-11-15 10:29 GMT+7 (2026-11-14 19:29 PST), LLM Mastery 4.0 day · transcript-verified 2026-11-16 Resources: 9 slide photos saved to ../resources/michal-suski/photos/ (prefix t2-). 8 legible; t2-04 blurred but its four pairs of numbers are readable. Footnotes partly hidden by heads on 5 photos. Photos copied from the local copies the Granola tool saved. He again offered a free data form (QR) and, via LinkedIn, the full findings as a file. Deck: the speaker published the full talk on 2026-11-16/17 at https://msu.ski/llm-mastery/ (55 slides with the line he said for each, a playbook with effect sizes, three copy-paste AI instruction sets, and a method note). Saved 2026-11-17: the page text as ../resources/michal-suski/llm-mastery-deck-page.md and the PDF as ../resources/michal-suski/who-writes-the-list-michal-suski-llm-mastery-2026.pdf. Figures marked "deck" below come from the page text; the PDF slides were not re-read one by one. Vendor talk? ⚠️ Yes. Every chart is "Data From Surfer AI Tracker" (Surfer's paid product). Method: top 5% vs bottom 5% of cited (or named) listicles inside Surfer customer reports, compared on ~190 factors; footnotes say "within-report associations". No controlled test.
Thesis (3 bullets max)
Listicles still work: their share of AI citations did not move Jan–Sep 2026.
Two scoreboards: getting the page cited and getting the brand named want different, partly opposite, page features.
One page cannot win both: a long hub list for citations, several short "X vs Y" pages (you at #1) for mentions.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Studies | 238.6M citations in 8,677 reports, Jan–Sep 2026 (trend on the same 546 reports each month); 201,534 self-promo pages in 5,162 reports, Jul–Sep 2026, 190 factors per page | best 5% vs worst 5% of pages inside each report, once by citations and once by mentions; correlations across ~426,000 page-report pairs | Surfer | spoken ("quarter billion", 200,000) + deck method note | method now published; still no controlled test |
| Listicle share | about one third of AI citations go to listicles all year: own lists ~11%, third-party ~23%; flat Jan–Sep 2026 | same 546 reports in every month | Surfer | spoken + deck (slide 8, "six numbers") | descriptive |
| ⭐ Cited list → brand named | answers that cite your list name your brand 73% vs 57% (+16 pp) | same report, page, prompt, engine and month; 193,944 paired cells for own lists (1.63M for third-party lists); to 13 Oct 2026 | Surfer | t2-03 + deck method note | ✅ the best-designed figure in both talks (paired). Still observational: the engine may cite the list because it is already naming the brand |
| Competitors on your list | each competitor on your list gains +3.7 pp; on a third-party list you gain +6.3 pp when it is cited and each rival beside you +5.7 pp | paired test (above) | Surfer | spoken + deck (slides 10–11) | paired, observational |
| ⭐ Slot position | on someone else's list: brand named in 52% of answers at #1, 32% at #5, 13% from #10 down. On your own list: publisher named 38.4% when listed first vs 26.5% when not; reach unchanged (22.1% vs 20.0% of prompts cite the page) | not stated | Surfer | spoken + deck playbook (slide 48 for 38% vs 27%) | no base or engine split given |
| Brand persists | 11 weeks after the first citation, citation frequency is 26 and brand mentions 83 (first month = 100); 60% of pages are still cited at all | pages first cited Jan to mid-Jul 2026, followed 12 weeks | Surfer | spoken + deck (slide 14) | descriptive |
| ⭐ Citations cost you mentions (t2-01) | correlation with page cited / brand named: brands on the list +0.15 / −0.10; "vs" in title −0.05 / +0.11; "best" in title +0.05 / −0.11; mentions of 2026 +0.04 / −0.11; early query answer (LLM-graded) +0.14 / −0.06; search intent alignment (LLM-graded) +0.14 / −0.06; key takeaways summary (LLM-graded) +0.08 / −0.10; URL has query parameters −0.08 / +0.07 | 426,447 […] pairs, 201,53[4 pages], [5,]162 reports, […] 2026; within-report associations | Surfer | t2-01 | correlations, all ≤ 0.15 in size |
| Brands per list | your own list 9; third-party list 18 | 8,677 reports, 23[…] | Surfer | t2-02 | descriptive |
| Long lists | 47% of citations to third-party lists go to lists with 26+ brands; most-cited own lists compare a median of 11 brands vs 8 (the strongest of the 190 factors for citations, +0.32) | — | Surfer | spoken + deck (slides 21, 24) | no base for the 47% |
| Short lists | with 1–2 brands on the list the publisher is named in 50% of citing answers; with 8+ in 34% | — | Surfer | deck (slide 22) | no base |
| Factors that flip | 20 of 190 factors push citations and mentions in opposite directions | 201,534 pages | Surfer | deck (slide 20) | count only |
| "vs" wins the mention (t2-04) | best vs worst pages for mentions: "vs" in title 11% vs 4%; "best" in title 29% vs 43% (red bar hidden in the photo; t2-06 and the deck give 29%); year in title 22% vs 36%; number in title 26% vs 34% | 23,432 pages […], within-report associations | Surfer | t2-04 (blurred) + deck | winners-vs-losers. Deck adds: "vs" titles credit the publisher in 52.6% of answers, "top" titles in 31.4% |
| ⭐ Linked, visual, tight pages (t2-05) | effect size, most-named 5% vs least-named 5%: links per 100 words +0.22; share of words inside links +0.20; internal links +0.18; images per 1,000 words +0.17; share of short paragraphs +0.16; mentions of 2026 −0.15; AI-written score −0.15; key takeaways summary −0.15; average paragraph length −0.17 | 23,432 p[ages], self-promo, […] Sep 2026 | Surfer | t2-05 | effect sizes. Deck defines the scale: the gap between best and worst 5% in the same niche, where 0.3 means the better page wins about 65% of head-to-heads. Deck raw values: 11 internal links vs 7; 3 images vs 1; 2,350 vs 2,660 words |
| Title and pricing (t2-06) | most-named 5% vs least-named 5%: "best" in title 29% vs 43%; year in title 22% vs 36%; prices mentioned 1 vs 4 | […]432 pages, self-promo, Jul–Sep 2026, within-report associations | Surfer | t2-06 | winners-vs-losers |
| Name sticks 12 weeks (t2-07) | keepers vs losers: year in the title 41% vs 51%; explicit ranking 52% vs 62%; "you" per 1,000 words 14.6 vs 13.4; brands compared 6 vs 7 | 36,542 + 36[…] self-promo […] to 14 […] 2026, 12-week follow-up | Surfer | t2-07 | small gaps; "you" and brand-count gaps are trivial |
| Tables keep a page cited | the only structure factor that both wins and keeps citations: median 30 table cells on most-cited lists vs 0 on least-cited; pages still cited after 12 weeks have 27 cells vs 15; year in URL 11% vs 14% | 12-week follow-up | Surfer | spoken + deck (slides 32, 36–37) | small gaps on the keep side |
| AI-written | AI-flagged pages are cited more; human-like pages get the brand named more (C23 slide: cited 82% vs 71% flagged; named 63% vs 75%) | "a simple AI detector" (C23 Q&A) | Surfer | spoken + C23 t1-09 | ⚠️ AI detectors are unreliable; treat as weak |
| CTAs | most-cited pages carry no CTA phrases: median 0 vs 0.13 per 1,000 words (+0.15) | 201,534 pages | Surfer | spoken + deck | winners-vs-losers |
| Answer first | 96% of most-cited lists answer early vs 80% of least-cited; "who it is for" 95% vs 80% | 201,534 pages | Surfer | deck (slide 34) | LLM-graded rubric |
| Experts and sources | help listicle citations (not info content or landing pages); "zero connection" for brand naming. Deck: expert citations 78% vs 64%, relevant statistics 83% vs 72% on most- vs least-cited (+0.16 cited, −0.03 named) | 201,534 pages | Surfer | spoken + deck | LLM-graded rubric |
Asserted mechanisms (no evidence given in the talk)
A citation "opens the door" to the brand being named (t2-03 title). The data is paired but not causal.
"AI understands AI content better", so AI-written lists get cited more.
Ask for a better slot on a list that already cites you: worth more than a new low slot (from the 52% vs 13% figure).
Explicit rankings and years age a page; the name sticks longer without them. Small gaps (t2-07).
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Playbook 1, get the page cited (t2-08, t2-09: "Hub list for citations"):
"Best X tools" with 10+ options (third-party lists average 18 brands). WHITE
A comparison table; bold text, bullet lists, H2s; short words and paragraphs. WHITE
Answer first: who the product is for and what the page covers, right at the top. WHITE
Sources, statistics and expert quotes. WHITE
No CTAs; consider removing existing ones. WHITE (test first: may cost conversions)
No year in the URL, no "top" in the title (spoken). WHITE
Playbook 2, get your brand named (t2-08, t2-09: "X vs Y for mentions", several pages): 7. Short list (3–5 brands) with you at #1. WHITE if the ranking is honest and the page is clearly yours 8. Internal links to your product features and documentation, with screenshots. WHITE 9. Shorter page and paragraphs; no key takeaways or summary box; no "best 2026"; no explicit rank numbers. WHITE 10. Mention competitor prices rarely (winners: once; losers: four times); his own reading: show only your own price. WHITE 11. "Your own words, not a template"; first-hand experience. WHITE 12. Several "X vs Y" or "X vs Y vs Z" pages, not one. WHITE
Selling placements: 13. Build a long list (he imagined 50 tools at $100 a month each) because 47% of third-party list citations go to lists of 26+ brands; price each slot by position. GREY with clear paid-placement disclosure; BLACK if undisclosed (FTC endorsement rules).
Competitors on your list (Q&A, a friend's tactic): 14. Name each competitor once per section (one link), then call it "this tool", "them". GREY: lawful, built to deny rivals the mention; a test at most 15. Never lie about a competitor's features or prices: the only backfire he named is legal action. WHITE (rule)
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Surfer AI Tracker: source of every chart. No price given.
Nathan Gotch: shown as an example of a self-ranking listicle (a list ranking himself first) that wins AI visibility; slide not photographed.
"Rankability": named as the example of self-promo lists ("they rank themselves on the top of their own website").
Jabez Reuben ("Jabaz"): host of the day; Felix: audience question.
QR codes: free data form (deck slide 55: "your free AI Visibility Report"); his LinkedIn for the findings file. URLs not legible in the photos.
https://msu.ski/llm-mastery/: his page for this talk (slides, playbook, AI instructions, PDF). https://msu.ski/chiang-mai-seo-2026/ is his page for the earlier Chiang Mai SEO talk ("50M LLM answers"); not yet pulled into these notes.
Slide photos
Full text of each slide: ../resources/michal-suski/slide-text.md
t2-01-citations-cost-you-mentions.jpg — "Citations cost you mentions": eight factors, page cited vs brand named correlations (in the table above). Footnote partly hidden: "426,447 […] pairs, 201,53[…] […]162 report[s] […]26. Within-report associations."
t2-02-number-of-brands-on-the-list.jpg — your own list (self-promo) 9 brands; their list (third-party) 18. Footnote "8,677 reports, 23[…]".
t2-03-a-citation-opens-the-door.jpg — Step 1 Cited ("AI cites your list… That alone is just a link") → Step 2 Named: 57% → 73%, "answers that cite your list name your brand far more often", same prompt, same engine, same month, +16 pp. Footnote "193,944 paired […] –13 Oct 2026".
t2-04-vs-wins-the-mention-blurred.jpg — "'vs' wins the mention. 'Best' gets you cited instead": best vs worst pages for mentions: "vs" 11% vs 4%; "best" ? vs 43%; year in title 22% vs 36%; number in title 26% vs 34%. Footnote "23,432 pages […] associations". Blurred.
t2-05-linked-visual-tight-pages.jpg — "Linked, visual, tight pages get you named. Effect size, most-named 5% vs least-named 5%": nine factors (in the table above).
t2-06-title-x-vs-y-keep-pricing-off.jpg — "Title it 'X vs Y', keep pricing off": "best" 29% vs 43%; year 22% vs 36%; prices mentioned 1 vs 4. Footnote "[…]432 pag[es] […] self-promo […] Jul–Sep 2026, wit[hin-report] associations".
t2-07-no-year-no-ranking-12-week.jpg — "No year, no ranking. Keepers vs losers: the name sticks 12 weeks later": year 41% vs 51%; explicit ranking 52% vs 62%; "you" per 1,000 words 14.6 vs 13.4; brands compared 6 vs 7. Footnote "36,542 + 36[…] self-promo […] 14 […] 2026, 12-w[eek follow-]up".
t2-08-two-playbooks.jpg — Playbook 1 get the page cited (more brands on the list; tables, bold, lists, H2s; answer first, say who it's for; sources and statistics; no CTAs) · Playbook 2 get your brand named (you at #1, shorter list; internal links and screenshots; shorter page and paragraphs; "vs", not "best 2026", no prices; your own words, not a template).
t2-09-one-page-cant-win-both.jpg — "One page can't win both. A set can." One page: hub list for citations ("Best X tools", 10+ options; a comparison table; answer first, sources, no CTAs). Several pages: "X vs Y" for mentions (short, you at #1; linked to your product, with screenshots; written by you, not a template). Footnote partly hidden: "Our […] [recommen]di[ng] […] [bui]lt on both studies".
Q&A (question → answer)
How to include a competitor without getting it named (Felix) → name it once per section with one link, then "this tool", "them".
Can a listicle backfire (host) → anecdotes only; real risk is legal action if you lie about a competitor.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
"Getting cited lifts AI visibility by 16 percentage points": the slide measures brand naming in answers that cite the list (57% → 73%), paired by prompt, engine and month.
"First position ~52% citation probability": it is the chance of being named, not cited, and it applies to someone else's list (deck: 52% at #1, 32% at #5, 13% from #10 down).
"47% of cited third-party lists had 26+ brands": 47% of citations to third-party lists went to lists with 26+ brands.
"~$100/month per placement" is his hypothetical, not a market rate.
"Tables… the only sustained differentiator at 12 weeks": the deck confirms it (slides 36–37: 27 vs 15 table cells). The 12-week slide that was photographed is a different one, about the brand name sticking (year in title, explicit ranking).
"Tables are needed to kep page cited", "Dont put date in url", "Less content, less words", "Avoid prices for competitors", the competitor-name line, "Vs for mentions" and "Best category type for citations" are the note-taker's private notes, merged into the summary.
Omits that early answer and intent alignment correlate slightly negatively with brand naming (−0.06), which conflicts with his C23 answer that intent is needed for both.
Omits that all figures are within-report correlations from Surfer AI Tracker.
The competitor-pronoun tactic is credited to "a friend", not to the study.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
Footnote sample sizes partly hidden on t2-01, t2-02, t2-04, t2-06, t2-07. The deck method note settles the main ones: 201,534 pages in 5,162 reports (writing factors), 8,677 reports (listicle share), 193,944 paired cells (own lists). The full footnotes can be read from the saved PDF.
Whether 23,432 pages is the top-and-bottom 5% subset of the 201,534-page study.
Slot-position curve and the 11-week chart: no photo, but both are now in the deck (52% / 32% / 13%; 26 vs 83). Neither has a stated base or engine split.
The deck playbook gives "vs" in title as −0.04 cited / +0.07 named, while photo t2-01 shows −0.05 / +0.11 for the same factor. The two use different measures (effect size vs correlation), so they are not in conflict, but do not mix them.
His own caveats in the deck: these are associations within a niche, not proven causes; well-known brands get named more anyway; "run a set of pages" is his reading, not a measured result.
The talk he calls his first ("a session with Dutton… skiing") is garbled; it refers to the C23 talk.
"Rankability" as the self-promo example: speech-recognition spelling likely correct (Rankability is an SEO tool) but not checked.
AI Search Objectives, Answer Patterns and Measurement — Oliver Pechter (Co-Founder & CMO, HeyAmos)
Source: Granola https://notes.granola.ai/d/f18a86a8-0c43-415e-8396-847e9571695a · recorded 2026-11-15 (16:07 GMT+7; Granola 2026-11-15 01:07 PST), LLM Mastery session · transcript-verified 2026-11-16. Recording starts mid-talk (first words: "difficult to know where to execute…"); the opening is lost. Resources: 6 slide photos saved to ../resources/oliver-pechter/photos/ (6 of 6, all non-zero, all read). No handout. Vendor talk? ⚠️ Yes. HeyAmos (Singapore) sells AI-search analytics; closing offer on slide: 50% off any HeyAmos plan for 2 months, code LLMMASTERY, app.heyamos.com/signup, valid until 25 November. All three case studies are HeyAmos client or own-brand data. Speaker named only as "Oliver" by the host; surname and title from one web lookup (HeyAmos blog and LinkedIn: "Oliver Pechter, Co-Founder & CMO, HeyAmos").
Thesis (3 bullets max)
Start from the company's objective and translate it into one of three AI-search goals: high-consideration purchase → get recommended (no risk flags); household brand → perception; challenger → show up in more answers.
Find answer patterns at scale (thousands of answers), then build strategy on the pattern; run objectives → patterns → strategy → execution → measurement as a loop.
Measure with leading indicators (meaningful visibility and perception shifts tied to actions) and lagging ones (branded search and clicks, LLM referrals, self-reported attribution); there is no single source of truth. Add a PR / comms lens on top of the mechanics.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Investment firm: risk flags | engines flagged risk because they could not find license or auditor evidence; fix = readable license (PDF) and published facts; after the fix answers flagged fewer risks | >26,000 AI answers; prompts built from voice-of-customer data (slide text partly hidden: "…prompts from voice of c… …intent clu…"); example prompts: "Should I invest my money with [brand]", "Is [brand] a legitimate company?", "difference between [brand] and [competitor]", "risks associated with [brand product]"; period not given | HeyAmos | slide (photo 03) for sample and prompts; outcome spoken only | sample clear; the after-state has no numbers, period or control |
| Airline: selection criteria | mentions of criteria in answers: reputation 6,191 · service quality 5,170 · pricing 5,081 · quality 3,706 · reliability 2,539 · a sixth axis partly hidden ("…fort", likely comfort) | answers for a premium airline's prompts; count and period not given | HeyAmos | slide (photo 04) | clear on slide; base not given |
| Airline: awards page | one page listing all awards had citation density "miles ahead" of any other page; the home page was insignificant | same | HeyAmos | spoken (chart not photographed) | no numbers recorded |
| Single-article dominance | one article appears across 86% of prompts; one small YouTuber's video also covers many prompts | same airline set | HeyAmos | spoken | no base given |
| Tier-1 media | tier-1 outlets block, paywall or license; engines lean on tier-2/3 and trade press, pick a few sources and go deep, then a long tail | not stated | his observation | spoken | assertion |
| Supplement challenger positioning | attribute mentions: local production 168 · local 93 · convenience 64 · comprehensive 61 · no sweeteners 49 · Nordic focus 46 | answers for a Swedish supplement brand (Relivo, named on slide) vs incumbent AG1; period not given | HeyAmos | slide (photo 05) | clear on slide; base not given |
| AI Overview example | AIO describes Relivo as "a top Nordic-manufactured alternative to AG1", magnesium 188 mg vs 26 mg, zero sweeteners vs stevia, made in Scandinavia/Sweden under Swedish Food Agency monitoring vs AG1 made in New Zealand, priced ~40% less; cites Relivo's site | one AIO screenshot | HeyAmos | slide (photo 05) | one screenshot, one run |
| Speed of pickup | the local positioning was picked up "really, really quickly" because the position was unclaimed | no period given | HeyAmos | spoken | no numbers |
| Own brand, lagging indicators | HeyAmos AI visibility up → branded searches and clicks up; Claude share of LLM referrals rising; more customers self-report "found you on AI" | HeyAmos's own data; chart not photographed | HeyAmos | spoken | correlation by his own framing; no numbers recorded |
Asserted mechanisms (no evidence given in the talk)
For financial products, engines check institutional and regulator sites to verify legitimacy; when they cannot verify, they flag risk and the buyer is lost to a lawyer's opinion.
Engines quantify subjective qualities (reputation) through objective proxies: awards pages and editorial coverage.
In crowded markets the citation mix shifts to e-commerce and vendor sites, and positioning is the only way to win; for supplement claims engines check medical journals.
An unclaimed position ("greenfield") is picked up fast by LLMs.
Format of an awards or press page barely matters as long as it is written and clearly structured; LLMs read PDFs (e.g. sustainability reports) where the substance lives (Q&A).
Attribution is returning to the pre-digital TV model: correlate activity with business movement rather than track clicks.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Classify the client's objective: high-consideration → get recommended (trust, no risk flags); household → perception (e.g. family-friendly, support, cancellations); challenger → visibility. Pick the one that matters most. WHITE
Build prompts from voice-of-customer data and intent clusters; run them at scale (his example: >26,000 answers). WHITE
Read the citation mix by source type (institutional, editorial, e-commerce/vendor) and the selection criteria the engine uses (radar of attribute mentions). WHITE
For trust objectives: list what the engine says it cannot verify; publish the proof in readable form (license PDF, auditor, regulator), as a facts archive on the site. WHITE
For perception objectives: one page listing all awards; PR into tier-2/3 and trade press; find the few articles and videos that carry most prompts. WHITE
For challengers: claim an unoccupied position with two or three provable pillars (local manufacture for the Nordic climate, EU food-safety standards, key-ingredient differences). WHITE
Leading indicators: visibility moves larger than normal volatility, tied to a specific action; perception attributes appearing in answers; for trust, whether risk flags drop. WHITE
Lagging indicators: branded search volume and clicks, LLM referral trend and engine mix, self-reported attribution ("found you on AI"). WHITE
Run the loop at high cadence. WHITE
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
HeyAmos (app.heyamos.com/signup): AI-search analytics; 50% off any plan for 2 months with code LLMMASTERY until 25 November (slide). No list price given.
Relivo (client example) and AG1 / Athletic Greens (incumbent), both on slide 05.
Prosperity Media (C38) mentioned in passing as having worked on AG1 ("I think"); unverified aside.
Q&A questioner: "Jamie", runs a shop in the US.
Slide photos
Full text of each slide: ../resources/oliver-pechter/slide-text.md
01-objectives-loop.jpg — loop diagram: Objectives at the center; answer patterns → strategy → execution → measurement.
02-three-objective-buckets.jpg — high consideration purchases → "Get recommended by AI"; household brands → "AI Perception"; challenger brand → "Show up in more AI answers".
03-ai-recommendations-26000-answers.jpg — "Objective: AI Recommendations"; four trust prompts; "analysis of >26,000 AI answers"; bottom line partly hidden (prompts from voice-of-customer data, intent clusters).
04-selection-criteria-radar-airline.jpg — "Selection criteria: How does AI answer a subjective question based on objective parameters? How does it quantify quality and reputation?"; radar with mention counts (see claims table).
05-positioned-alternative-relivo-ag1.jpg — "Showing up as a clearly positioned alternative"; attribute radar (local production 168 … Nordic focus 46); Google AI Overview "Relivo vs. AG1" screenshot.
06-offer-50pct-code-llmmastery.jpg — offer slide: 50% off any HeyAmos plan for 2 months, code LLMMASTERY, app.heyamos.com/signup, valid until 25 November.
Q&A (question → answer)
Jamie (US shop owner): is there data on the best format for awards and press (one URL, separate press releases)? → He doesn't think it matters much if it is written and clearly structured; LLMs read PDFs such as sustainability reports; listing all awards clearly on one page does the job "99 times out of 100". Opinion, no data.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
Speaker is Oliver Pechter, Co-Founder & CMO of HeyAmos (one lookup); the summary gives only "Oliver".
The discount is specific: 50% off any plan for 2 months, code LLMMASTERY, until 25 November (slide 06).
The high-consideration goal on the slide is "Get recommended by AI"; the summary's "build AI trust to suppress risk flags" is the spoken explanation.
Omits the >26,000-answer base, the prompt examples, and the radar counts for the airline and supplement cases.
Omits that the supplement brand is Relivo and the incumbent AG1 (on the slide), and the AIO screenshot that shows the positioning.
Omits the Q&A on awards-page format.
Omits that the recording starts mid-talk.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
Base and period for the airline and supplement radars are not given; mention counts cannot be turned into rates.
No after-numbers for the investment firm; "fewer risk flags" is spoken only.
The sixth airline axis is hidden by a head (likely "comfort").
The 86% single-article figure is spoken only; the article is not named.
His own-brand chart (visibility vs branded searches and clicks) was not photographed.
Date: Granola timestamp converts to 2026-11-15 local; the assignment places it on the LLM Mastery day.
Parasite SEO Playbook — Ivana Flynn (iGaming SEO; owns DMCA Box; runs an "iGaming SEO boardroom"; built an unnamed parasite-placement platform)
Source: Granola https://notes.granola.ai/d/6276ad4d-36d4-4659-893d-3f3a7cb7ae40 · recorded 2026-11-12 · transcript-verified 2026-11-12 Vendor talk? Yes, partly. She pitched (a) her own all-in-one parasite-placement platform (name not caught; QR code on slide), (b) DMCA Box (DMCA takedown-recovery service, she says "I have a company called DMCA Box"), (c) her iGaming SEO boardroom community. She also sells links ("I do a lot of links with" clients).
Thesis (3 bullets max)
Parasite SEO = borrowing a stronger site's authority; six methods reviewed with 2026 verdicts and 2027 outlook.
2027 verdicts: do publisher partnerships, in-post placements, YouTube; maybe buy a site if you have a huge budget; try subdomains only in weak markets; skip Reddit (login-only change).
EU/EEA manual penalties for this tactic reportedly stopped on 30 Aug (her claim); manual penalties remain in US/UK/AU/CA.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Casino parasite placements for a client | 24,000 new clicks via affiliate links; deposits +11% | "within two weeks", 1 client | speaker/client | spoken (slide likely) | clear |
| Her test total spend | about 7,000 EUR (rounded; she said "6,000, whatever") | 30 days at the time (about 60 days when spoken); 3 sites x 2 placements = 6 placements | speaker | spoken, table on slide | clear on total, rounding admitted |
| Relevant gambling site, no extra work | about 1,000 EUR revenue | same test | speaker | spoken | clear; she does not know why it earned; internal links from others |
| Supported placement (links + traffic push) | "much more" than 1,000, no figure | same test | speaker | spoken | revenue figure not stated; she warns hybrid/RevShare deals and lucky player losses inflate it |
| Sports sites | one no revenue; "other sports one was making money" | same test | speaker | spoken | garbled/contradictory |
| Unrelated site | nothing at first; slow growth after adding articles + internal links | same test | speaker | spoken | clear |
| Earlier cheap placement | 90 USD placement, 90 links, no result (Australia casino post on irrelevant site) | one placement | speaker | spoken | clear |
| Reddit traffic lost / remaining | lost about 394 million; 770+ million remaining | period not stated | Ahrefs (per speaker) | spoken | clear |
| YouTube in SERPs | AU "bonuses in online casinos": 4/10 results; "betting bonus": 1/10; "no deposit bonuses": 3/10 | screenshot from "a few weeks back" | speaker | spoken + slides | clear |
| Reddit post cost | 15 USD/post, 10 USD/comment | vendor, name garbled | vendor price | spoken | price clear, vendor name garbled |
| Article cost | few hundred to a few thousand EUR; about 2,000 EUR "already amazing" | Q&A | speaker estimate | spoken | clear |
| Parasite site purchase | hundreds of thousands to millions; client budget 1M EUR | Q&A | speaker | spoken | clear |
| Subdomain DR inheritance | co.uk DR 91, us.com DR 92 | not dated | Ahrefs presumably (not named) | spoken | clear |
| Video schema abuse parasite | lasted 24-48 hours per test | her tests | speaker | spoken | clear |
Asserted mechanisms (no evidence given in the talk)
Stronger host sites survive negative-SEO attacks better.
Traffic push (bot or paid visits) helps rankings; over-pushing or identical behavior on every page triggers Google.
Entity relevance: a host site with any mention of casino/betting/licensing is enough; totally irrelevant host needs internal links built.
Reddit blocking Google crawling and going login-only because of a Google/Reddit falling out (her speculation).
Google favors its own product so YouTube ranks; AI Overviews include videos.
EU rule: DMA-style change meant no manual penalties from 30 Aug in EU, Iceland, Liechtenstein, Norway; she says "30 countries"; fines 10-20% for repeat infringement; algo penalties still possible. Not sourced in the talk.
Big operators will corner the market and raise prices.
Third-party mentions help AI citations (answer to last question).
Reddit device-fingerprints for about 100 days (spoken "a quarter"); stores IP, browser, OS, extensions, user agents.
Tactics and how-to steps (in order, with tools and prices)
Six parasite types as presented, with her 2026 / 2027 verdict:
Subdomains / co.uk-us.com-style borrowed domain authority. BLACK/GREY. Worked until recently, easy to spot; still OK in Malaysia, a bit in Thailand, and brand-protection sites. Not for tier-one markets; not 2027 focus.
Publisher partnerships. WHITE/GREY (host knows). Business proposal, revenue share, dedicated folder (gambling.com deals shown). Host keeps compliance control, can end the deal; reduced margins, no data access. 2027: yes.
In-post placements. BLACK-HAT/GREY. Procedure from her test:
Pick host sites: one gambling-relevant, one sports, one unrelated.
Buy 2 placements each; one placement left alone, one supported.
Support = buy backlinks (she used many PBNs, BLACK), plus traffic push (BLACK).
Track via affiliate links.
Placement cost examples: 90 USD cheap one; typical few hundred to 2,000+ EUR. Bulk "black hat supplier" placements possible but need an admin who understands dofollow affiliate links.
Traffic push options named: Fiverr, EZ Mob (cheap bots; "play with it").
Her own platform finds relevant posts, traffic, competitor link/internal link/traffic-push data, price, PBN and traffic push in one place.
2027: yes.
Reddit. BLACK-HAT (account farming, fake engagement). Build karma with memes/cute posts; buy aged accounts with karma (sellers named: "Social plug", Z2U, a Telegram seller garbled "red art"); accounts get suspended often. Use proper IP (IP Royal) and anti-detect browser (Multilogin, "works the best"); use a posting service (garbled; 15 USD post, 10 USD comment; private note says CrowdReply) that tells you which subreddits you can post in and tracks stickiness. Works for "best online casinos", "best sweepstake casinos", crypto casinos in 2026. 2027: no (login-only rollout).
YouTube. GREY/BLACK. Make AI videos, optimize title/description, link to offers in description; promotions possible except heavy gambling; for faster ranking add backlinks + traffic push. New accounts work; if banned, re-open with a new email (she says Google cannot link it; recovered a DMCA that way). 2027: yes, cheapest.
Buying existing websites (e.g., SheKicks, women's football in Scotland, bought for parasite; Esports Insider). GREY. Pros: backlink profile, brand, full control, resale, link selling. Cons: relevance mismatch, million-plus cost, inherited penalties, reputation damage. Failure cases: Gambling Insider traffic drop (she calls it manual penalty), Esports Insider not ranking for own brand, Teccopedia (spoken; likely Techopedia) three manual penalties. 2027: only with huge budget.
Tools, vendors, people and URLs named
Ahrefs (traffic loss figures); Fiverr (traffic push); EZ Mob (cheap traffic bots); IP Royal (IPs); Multilogin (anti-detect browser); Social plug, Z2U, Telegram seller "red art" (garbled), posting tool 15/10 USD (name garbled "isopink"; user's note: CrowdReply).
DMCA Box (her company; takedown/recovery); her all-in-one parasite platform (QR code, name not caught); iGaming SEO boardroom (community).
Hosts/examples: gambling.com deals, Medium (she says content gets removed fast), SheKicks, Esports Insider, Gambling Insider, Techopedia (Teccopedia), Game Reactor not mentioned here, Business Insider (Q&A, bought for several million).
GGL-licensed German casinos (publisher example).
Q&A (question -> answer)
Fastest way to deal with DMCA reports? -> Her DMCA Box process; submit simply, back within about 12 hours; DM her on LinkedIn for videos and an hour-long presentation.
Buy parasite links from bulk black-hat suppliers? -> Yes but negotiate; suppliers mislabel as nofollow, remove content, drop tables; find an admin who understands.
Which parasites work today? -> Those in the talk; schema-markup/video abuse lasts 24-48h, not worth the money. Buy website only with huge budget; try the rest.
YouTube with fresh accounts? -> Yes; optimize; add backlinks and traffic push to rank faster.
Best host niche for casino? -> Almost any with some casino/betting/licensing mention; unrelated needs internal links.
Smallest business doing 100k+/month? -> Not able to answer.
YouTube worth it in iGaming? -> Yes, competition not heavy yet; use new accounts if banned; Google not as smart as Reddit.
Parasite article cost on Business Insider-type sites? -> Whole site cost millions; placements few hundred to a few thousand EUR; 2,000 EUR is already great; six for 7,000 EUR still profitable (paid for her ticket).
Take more risk in EU? -> Yes; she predicted the rule change; big operators now testing with big budgets, prices will rise.
Third-party authority strategies for AI search? -> Yes; being everywhere on the web raises citation chances; authoritative sources best.
Corrections to the Granola summary
"Reddit (via Crowdreply and similar tools)": transcript never clearly names Crowdreply; vendor name is garbled; Crowdreply comes from the user's private note. Prices 15/10 USD are clear.
"YouTube appearing in 3-4 out of 10 SERP results": actual: 4/10, 1/10, 3/10 across three queries.
"Sports placement: no revenue yet": transcript is contradictory (one sports site made nothing, another sports one made money; garbled).
"6 placements (three niches, two with link/traffic push)": actual: three sites x two placements; one left alone, one supported; she used many PBNs; at 30 days then about 60.
"Submit a counter-notice": transcript says only to submit and be back in 12 hours; counter-notice is not stated.
"Bet365, William Hill": transcript garbled ("bets. And William"); do not treat Bet365 as verified.
"Multilogin + IP Royal": confirmed.
Summary omits: client results (24,000 clicks, +11% deposits in two weeks), subdomain DR 91/92, publisher-partnership examples, host-hat caveats (Medium removal), EZ Mob/Fiverr traffic push risks, Google email re-creation trick, video-schema abuse (24-48h), "30 countries" EU/EEA claim, million-euro budget, her product pitches (platform, DMCA Box, boardroom), SheKicks.
"Teccopedia (three manual penalties, millions lost)" is spoken as Teccopedia; probably Techopedia; unverified.
Summary says Reddit login-only "defeats the parasite model": her view, rollout claimed "right now".
Unclear / needs verification
Name of her platform; posting-service vendor name ("isopink", "red art", Z2U/"Social plug" spellings).
"Syrup poisoning" (spoken twice; probably SERP poisoning/site reputation abuse; unverified).
Reddit loss "394 million" period and unit (traffic visits per Ahrefs).
Revenue of the supported placement and which sports site made money.
EU rule basis (likely DMA; she gave no citation); "30 countries" vs the four jurisdictions listed.
Bet365/William Hill; Techopedia spelling; Gambling Insider "manual penalty" is inferred from a traffic drop.
LLM Strategy for Enterprise Brands: Crawl, Comprehend, Convert — Rahul Sengupta (Prosperity Media, "GEO + Content")
Source: Granola https://notes.granola.ai/d/6a8a192a-a43c-46d9-9b30-44658ce61f2c · recorded 2026-11-15 (11:47 GMT+7; Granola 2026-11-14 20:47 PST), LLM Mastery session (he refers back to the host Jabez's AI info page) · transcript-verified 2026-11-16 Resources: 10 slide photos saved to ../resources/rahul-sengupta/photos/ (10 of 10, all non-zero, all read). Slides and his "AI Accessibility Checker" are offered at https://rahulsengupta.digital/speaking/llm-mastery-chiang-mai/ (URL from the note-taker's private notes and the summary; not fetched). Vendor talk? ⚠️ Partly. Agency pitch for Prosperity Media's GEO service; shows its in-house tracker "GEOverview" and gives away a free checker. No price or offer on stage. Almost every number is spoken with no source; the slides carry sources for four of them.
Thesis (3 bullets max)
Enterprise AI search work fails on plumbing first (WAF, headless JavaScript, discovery, logs), then on entity confusion, then on sources; fix in that order: crawl → comprehend → convert.
Plan per buyer, per market, per engine: engine use differs by country, age and IT policy (Copilot in US enterprise, Doubao in China, telco bundles in India).
One run is not a baseline: run repeated prompts for four weeks, split branded from unbranded, and re-plan after every model change.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| ⭐ Repeat-run instability | <1% of repeated runs gave the same brand list for the same prompt | 12 prompts, 60–100 runs each, 2026 | source line partly hidden: "S… (R. Fishkin) and … Engine Journal" (reads as a Fishkin / SparkToro study reported in Search Engine Journal) | slide, photo 06 | clear on slide; original not read; measures identical full lists, a stricter test than C15's "top pick kept" (56.5%) |
| ⭐ Model change splits engines | one blog's citations: ChatGPT 0 (15 Jan) · 0 (1 Mar) · 0 (1 May) · 30 (1 Jul) · 0 (1 Sep) · 9 (10 Nov); Google AI Overviews 0 · 0 · 25 · 23 · 80 · 117 | one client blog (domain partly hidden, "…ali.com.au/blogs"), Jan–Nov 2026, citation links in Ahrefs' prompt set | Ahrefs (Site Explorer / Brand Radar prompt set), his reading | slide, photo 08; spoken "117 AI citations" | clear; one blog; Ahrefs' prompt set, not a locked client set; the model change is his attribution |
| Shopify agent files | 99% of Shopify stores ship a verified UCP manifest by default; custom builds 2.6% | not stated; "read 28 Aug 2026" | ucpchecker (source line partly hidden) | slide, photo 10 | clear on slide; source not read; his takeaway: platform files are table stakes, spend on product data and pages |
| Log retention | Cloudflare Log Explorer default retention 30 days; a Worker copies rows into D1 every 15 minutes | method | Cloudflare docs + a YouTube method video (20 Sep 2026, author name hidden) | slide, photo 09; spoken "seven days" | slide outranks audio: 30 days |
| AI share of traffic vs budget | AI = 1% of web traffic, 12% of budget "as of last year" | none | not named | spoken | unsourced |
| Enterprise stack | 73% of organizations run headless in some form; ~28% of recommended SEO fixes get implemented | none | not named | spoken | unsourced |
| Brand-free journeys | 60% of shoppers never mention a brand during the search journey | none | not named | spoken | unsourced; his reason to split branded and unbranded citations |
| Big brands skipped | brands with DR 40+ and no AI Overview mentions (count garbled) | "Asia's brand study" (garbled; possibly an Ahrefs study) | not clear | spoken | garbled |
| Engine use, Australia | 77% use ChatGPT, Gemini second; lower adoption in older age groups | none | not named | spoken | unsourced |
| Adobe EDS migration | promised 34–94% growth; sales fell 30%; ~$1M lost over a year; brand went defunct "three days ago" | one unnamed Australian brand | anecdote | spoken | anecdote, brand not named |
| Discovery failure | 0 of 1,806 URLs discovered on a custom headless build (no internal links; sitemap alone not enough) | one client | his agency | spoken | anecdote |
| Car insurance by state | strong in home state, zero presence in states B–E; improved after acquired subsidiaries were added to entity schema | one client; no numbers, period or control | his agency | spoken | anecdote; no before/after figures |
| Reddit correction | fix posted in the same Reddit thread picked up in LLM answers within 2–3 days | one SaaS client (API integration complaint) | his agency | spoken | anecdote |
| Awards site | "bestedwood.com" (audio) / "Bestinhood.com" (private note): 2 years old, 6,526 awards issued, "LLMs absolutely love them" | one site | his observation | spoken | spelling unverified; no citation counts shown |
| Agent shopping test | booking a Chiang Mai hotel, the agent ignored most of 3 merchant sites, even cheaper ones, because they blocked it | n=1 | speaker | spoken | anecdote |
| Credentials | banking share of voice: 58.4% of keywords in top 5; furniture blog "3 to 444" with 10 blogs ("346 for 78% of rankings", garbled); menswear won 43 of 60 Black Friday keywords, sales +30% | own clients, periods not given | speaker | spoken | self-reported; furniture figures garbled |
Asserted mechanisms (no evidence given in the talk)
WAF policy overrides robots.txt; a WAF block makes robots rules moot.
A 200 response can be a blank render; status codes alone are not proof of access.
All major LLM fetchers except Mistral skip JavaScript; Google "has started" rendering it. Spoken only.
Agents often request Markdown over HTML; Cloudflare offers free Markdown content negotiation.
LLMs confuse enterprise brands' history, geography and acquisitions; correct entity schema (sister brands, acquired companies, areas served) fixes state-level invisibility.
Wikipedia markup adds strong entity signal.
In regulated niches (Australian dental), engines lean on forums, YouTube and clinics because publishers cannot make claims.
AI picks up industry news fast and pulls rivals into it (Jetstar baggage story pulling in Virgin); old crises (Optus 2022 breach) keep surfacing until consensus content overrides them.
US enterprise staff are stuck on Copilot because IT has not approved other tools; that is an advantage for B2B brands that optimize for it.
India engine share follows telco bundles (Perplexity, then Gemini, then ChatGPT as free offers changed). Provider pairings spoken only.
Mentions and citations behave differently, and engines do not cite the same sources.
Shopify's default llms.txt is self-promotional and useless to agents; he also says "llms.txt doesn't work".
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Plan (12 weeks, photos 01–04, 07):
Before kick-off (pitch, public data only): AI visibility snapshot from Ahrefs Brand Radar; which engines buyers use by market; which sources AI cites in the category. WHITE
Signed to kick-off: draft the prompt set from buyer questions; category citation scan per engine; access list (Search Console, CDN logs, CMS). WHITE
Weeks 1–4: stakeholder discovery (brand, legal, service); market and engine mapping by market, language and age; prompt set from buyers (branded, category, comparison); tracker + Brand Radar setup (engines, competitors, markets); baseline runs begin, repeated, "not one screenshot". WHITE
Baseline KPIs over four weeks: mention rate, share of voice against 3–5 competitors, citation share, source map, sentiment, accuracy. Tag prompts by audience. Map to KPIs the marketing manager is already judged on. WHITE
Weeks 5–8: category citation analysis per engine; "truth notebook" signed off by the business; interrogate every engine as a buyer would; truth gaps and their sources (Steve Toth's Truth Alignment framework); truth gaps agreed by week 8. WHITE
Week 12: per-engine plan; re-plan when models change. WHITE
Crawl: 7. Check WAF rules before robots.txt. Do not trust 200s; compare JavaScript vs raw crawl in Screaming Frog. WHITE 8. Robots by use case: for a retailer, block training crawlers but allow user-triggered fetchers (so a model does not remember "lowest price ever"). WHITE (client decision) 9. Logs: Cloudflare Log Explorer filtered by verified bot category → Worker writes to D1 every 15 minutes → own dashboard (crawl volume, status codes, AI vs search bots). Fields: EdgeStartTimestamp, ClientRequestPath, ClientRequestUserAgent, VerifiedBotCategory, EdgeResponseStatus, OriginResponseStatus, CacheCacheStatus, RayID (dedupe). Ask enterprise IT for this view, not raw files. WHITE 10. Low-effort files: AI info page, UCP for e-commerce, agent sitemaps when URLs are only reachable via JavaScript; customize platform defaults. WHITE
Comprehend: 11. Prerendering without replatforming: Prerender.io or SEO4Ajax. WHITE 12. Fix discovery on headless builds with internal links, not sitemaps alone. WHITE 13. Serve Markdown to agents via Cloudflare negotiation. WHITE 14. Entity schema covering acquired brands, sister organizations and areas served; keep facts consistent across sources; Wikipedia where possible. WHITE
Convert: 15. Map who AI cites per market and engine (orthodontics: AU = association, Reddit, YouTube; SG = three local dentist sites; IN = YouTube, a dental chain, Healthline, medical publications). WHITE 16. Test a directory or mention before buying it: government childcare sites now block LLMs; JavaScript-heavy directories may not be read. WHITE 17. Correct negative Reddit threads in place, as the brand. WHITE (disclosed) 18. Award-mill pages ("if you want a quick black-hatty way, get these award pages"). BLACK by his own words 19. Report SEO and AI together; prove lifts against controls. WHITE
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Ahrefs Brand Radar: market-wide view, no setup (price line on slide too small to read reliably).
Profound: enterprise depth, bot analytics, up to 10 engines (slide).
Peec AI: your own prompts tracked daily; "from US$95 a month" (slide, small text).
Semrush AI Toolkit: inside a Semrush stack; US$99 per domain (slide).
Bing Webmaster Tools AI Performance (preview, Feb 2026): Copilot citation data, free, first-party (slide). He prefers Bing's query data to Google's.
FanoutFox (fanoutfox.com, free, by Suganthan Mohanadasan): ChatGPT's searches and sources (slide).
GEOverview: Prosperity Media's in-house tracker; client prompts, truth checks, Reddit (slide).
Screaming Frog (JS vs raw comparison crawl); Search Console; Ahrefs.
Cloudflare Log Explorer, Workers, D1; Cloudflare Markdown negotiation.
Prerender.io; SEO4Ajax (audio "SEO for Ajax"; private note "Seoajax").
AI Accessibility Checker: his tool, ~150 checks, built on Vercel; earlier version built for Omnicom Media Group was shut down. Free download (URL above).
Steve Toth: Truth Alignment framework (audio "Steve Todd").
Engines named: ChatGPT, Gemini, Copilot, Perplexity, Claude, Mistral, Doubao (audio "Daobao").
Award site: bestedwood.com / bestinhood.com (spelling unresolved).
Slide photos
Full text of each slide: ../resources/rahul-sengupta/slide-text.md
01-plan-by-buyer-category-engine.jpg — five planning steps: map buyers to engines (markets, languages, demographics) · learn your category (what AI cites) · baseline with GEO tools (Profound, Peec, Ahrefs, own tracker) · check what AI believes (Trust Alignment Framework) · plan per engine (re-plan when models change). Source: Prosperity Media GEO service method, 2026.
02-start-before-contract-kickoff.jpg — "Start before the contract does": pitch / signed-to-kick-off / week 1 columns; baseline lands by week four.
03-twelve-week-planning-timeline.jpg — 12-week Gantt; kick-off, baseline starts week 4, truth gaps agreed week 8, per-engine plan week 12.
04-weeks-1-4-understand-and-track.jpg — 1a–1e: stakeholder discovery, market and engine mapping, prompt set from buyers (branded, category, comparison), tracker + Brand Radar setup, baseline runs ("repeated runs, not one screenshot").
05-baseline-tools-paid-free-own.jpg — tool grid with prices (Peec from US$95/mo, Semrush US$99/domain, Profound up to 10 engines, Bing AI Performance free, FanoutFox free, GEOverview in-house); "how we combine them: one market-wide view, one prompt tracker daily, Bing for first-party data, four weeks before any verdict". Sources: vendor sites checked 12 Nov 2026.
06-one-run-is-not-a-baseline.jpg — "<1% of repeated runs gave the same brand list for the same prompt"; KPI list (mention rate, share of voice vs 3–5 competitors, citation share, source map, sentiment, accuracy); source 12 prompts, 60–100 runs each, partly hidden.
07-weeks-5-8-diagnose-truth-gaps.jpg — 2a–2e: category citation analysis, truth notebook signed off, interrogate every engine, truth gaps and sources, baseline settles (four weeks of repeated runs).
08-model-change-one-blog-two-engines.jpg — bar chart, ChatGPT vs Google AI Overviews citations for one blog, 15 Jan → 10 Nov (values in the claims table).
09-cloudflare-log-explorer-d1.jpg — Log Explorer → Worker → D1 every 15 min, past the 30-day limit; fields worth keeping; takeaway: ask IT for a Worker + Log Explorer view, not raw log files.
10-shopify-ucp-manifest-99pct.jpg — 99% of Shopify stores ship a verified UCP manifest by default, custom builds 2.6%; "treat platform files as [table stakes]; spend the effort on product data and pages" (one word hidden by a head). Source ucpchecker, read 28 Aug 2026.
Q&A (question → answer)
None. The talk ran out of time; the host sent questions to the hallway.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
Speaker surname is Sengupta (his site URL); the host's "Raffle Singh Gupta" is a mis-hearing.
"Steve Todd's Truth Alignment framework" is Steve Toth's.
"Log retention beyond the default 7 days" is wrong per the slide: Log Explorer keeps 30 days by default; the Worker keeps rows past that.
"Blog grew Jan–May, then fell off a cliff in September" is half right: ChatGPT citations fell 30 → 0 (Jul → Sep) while Google AI Overview citations rose 23 → 80 → 117 for the same blog. The "117" is AI Overviews on 10 Nov.
"Furniture blog grew from position 3 to 444" is a garble; the spoken numbers do not resolve.
"bestedwood.com … black-hat signal worth noting": the private note spells it "Bestinhood.com"; he presented it as a black-hat shortcut, not a signal.
"Revender.io" (private note) is Prerender.io; "Seoajax" is SEO4Ajax. The private-note lines are the note-taker's own.
Omits the 12-week plan, the pre-kick-off market map, the four-week baseline rule, the KPI list, the <1% repeat-run figure and its source, the tool prices, and the Shopify 99% UCP figure.
Omits that the "LLM Accessibility Checker" for Omnicom was shut down; the version given away is his current "AI Accessibility Checker".
Unclear / needs verification (mis-heard names, numbers you could not pin down)
Date: the assignment places this on the LLM Mastery day; Granola's timestamp converts to 2026-11-15 local, while C15 (LLM Mastery) converts to 11-14.
The <1% study: source line partly hidden ("S… (R. Fishkin) and … Engine Journal"). Find and read before quoting.
Blog domain on photo 08 partly hidden ("…ali.com.au/blogs").
"Asia's brand study" (DR 40+ brands with no AI Overview mentions), "Tomet from PKI", "Yasha" (childcare talk), "Incentra" (AU orthodontics source): speech-recognition spellings, unresolved.
India telco pairings (which telco bundled which engine) are spoken only and may be swapped.
Peec AI price and the Ahrefs Brand Radar price line on photo 05 are small text.
Whether Bing Webmaster Tools' AI Performance report is available in the Bing Webmaster API.
Award site spelling (bestedwood vs bestinhood).
Brand Visibility in AI Search: What Works — Robert Niechciał (co-founder, SensAI Academy; CTO & partner, Vestigio)
Source: Granola https://notes.granola.ai/d/98723310-e925-4b57-a75b-be428aafae10 · recorded 2026-11-14 (10:27 GMT+7), LLM Mastery 4.0 day · transcript-verified 2026-11-14 Resources: https://sensai.io/llmmastery (free; email form is optional) · saved to ../resources/robert-niechcial/: the speaker's own talk notes (brand-visibility-in-ai-search-notes.md, read in full) and the slides PDF (104 slides, saved; slide titles read from the page, PDF not read page by page). 7 slide photos from the Granola note saved to ../resources/robert-niechcial/photos/ and read 2026-11-16 (see Slide photos); none contradicts a figure below. Vendor talk? ⚠️ Yes. Sells the SensAI Academy course "Mission 01 · Agentic Semantic OS" (early bird opened the day of the talk, Season 1 starts 2026-12-01) and runs Vestigio OS, an AI-visibility monitoring product. Two of the three datasets are his own company's; the third (Senuto) is another SEO tool vendor. The handout labels its numbers as observations and correlations, not experiments.
Where the audio and the handout disagree, the handout is used and the difference is listed under Corrections. The audio is heavily garbled.
Thesis (3 bullets max)
One AI answer about a brand is a random draw. Measure a frozen set of buyer questions, many runs, every platform, and read the average.
AI recommends a brand when its passage is retrieved, then cited, then confirmed by other sources (Retrieved → Cited → Trusted).
Five moves: measure a portfolio · map the sources AI reads · speak the language of the question · be the easiest answer to extract · get others to confirm you.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Repeat-run stability | brand that was #1 is still #1 in 56.5% of repeats, lower in 16.5%, gone in 27% | 443 prompts × 6 platforms × 10 runs, 20 minutes apart | Senuto (M. Chmurkowski), vendor | handout + slide; garbled in audio | clear in handout; original study not read |
| One question over time | first-pick share 9.1% (Jun) → 29.2% (Aug) → 4.0% (Sep); all tracked questions averaged 6.1% → 6.4% → 3.7% | one electronics retailer, 6 platforms × 5 runs; ChatGPT model changed in between | Vestigio OS (his company) | handout + slide | clear; one client |
| Sentiment | 61.7% positive, 37.9% neutral, 0.5% negative | 1,361,459 brand ratings, 6 platforms | Senuto | handout + slide | clear |
| Mention share by platform | ChatGPT 3.4% · Copilot 4.3% · Gemini 6.8% · AI Mode 21.3% · Perplexity 28.9% · AI Overview 29.9% (median share of answers naming the brand) | 20 brands, ~698k answers, 90 days to 2026-11-11 | Vestigio OS | handout + slide | clear; his client mix, mostly Poland |
| Liked vs recommended | cosmetics brand rated +2.83 appears in 6% of answers; software leader rated +2.98 appears in 83% | two brands | Vestigio | handout + slide | two examples, not a test |
| Own site in citations | company websites are cited in 51–73% of answers about a brand; only 4–11% of answers rely on brand websites alone | 15 analyses of 8 brands, Poland | Vestigio (S. Parzych) | handout + slide | clear |
| Source concentration | 10,471 websites cited; 35 of them supplied 42% of citations | same, 954k citations | Vestigio | handout + slide | clear |
| Source mix by market | Poland retail/services: Trustpilot 35,477 · Opineo 17,150 · Ceneo 14,382 · GoWork 13,941 · Reddit 12,871 citations. USA software: tech editors in 67% of answers, comparison sites 52%, news 45%, customer reviews 7% | 954k citations (PL); 1,398 answers, 645 domains (US) | Vestigio | handout + slide | clear |
| Category filing | brand named in 97% of answers about its main product, 0% for its second product | 24 unbranded questions, 713 answers | Vestigio US software study | handout + slide | handout says "an observation on two questions, not a test" |
| ⭐ Answer first | pages whose first paragraph answers the question supply 18% of the AI answer vs 5% (about 3×) | n=492 pages | Senuto page-level study | handout + slide | correlation; the metric is share of the answer taken from the page, not citation probability |
| ⭐ What did not matter | no detectable effect on citations from schema markup, meta description, headings as questions, lists and tables, author box, domain strength (20+ factors) | same Senuto study | Senuto | handout + slide | correlation, one study, n=492; absence of a detected effect at that sample size |
| Rival chosen first | brand and rival mentioned 71% vs 72%; recommended first 20% vs 44%; 11 of the 14 rankings AI cites place the rival higher | one brand pair | Vestigio (S. Parzych) | handout + slide | one pair |
| Trust paper | share of correct answers: every source counts the same 15.6% · majority wins 38.4% · sources that confirm each other on specifics 77.1% | ClashEval, 1,299 questions, honest sources mixed with misleading ones | Jiang, Feng, Mehta, arXiv:2509.25184 v2 | handout + slide | ✅ paper, authors, title and method (Truthful Text Summarization, accepted at ICLR 2026) confirmed on arXiv; the three percentages were not checked in the paper body |
| Fact repetition | of 5 facts in a UK pool buying guide, 7 rival pages state them 2, 1, 0, 0, 0 times | 7 competitor pages | speaker demo | handout + slide | demo; counts repetition, not truth |
| Roofing case, blended | dashboard showed AI visibility +190.6%; June ChatGPT 44% blended = 27% on questions tracked since March + 62% on a set added in June | one client | Vestigio OS | handout + slide | clear; his point is that the blend is a sampling artifact |
| ⭐ Roofing case, fixed cohort | same 81 questions: ChatGPT 3.0% (Mar) → 21.1% (Apr) → 20.7 → 27.1 → 29.2 → 25.2 → 19.9 → 28.0 → 31.7% (Nov, partial); AI Mode 9.5% → 26.1% → 29.9 → 17.1 → 30.8 → 25.6 → 28.0 → 27.1 → 26.8% | fixed cohort since 2026-03-16; pages rewritten answer-first between March and April | Vestigio OS | handout + slide | one client, no control set; handout says "coincidence in time, not proof of cause" |
| Roofing case, citations and Google | client site = 6.6% of cited domains on its 242 questions (next competitor 4.9%); GSC clicks 125k vs 54k and average position 9.3 vs 16.3, last three months vs a year earlier | 30 days, 6 platforms; client's own question set | Vestigio OS + GSC | handout + slide | clear; own question set, not the market |
| Reranking demo | the passage that answers the question moves from #2 to #1 after reranking | 202 passages from 8 competitor pages; BAAI/bge-small-en-v1.5 + jina-reranker-v1-turbo-en | speaker | handout + slide | reproducible demo with open models; "a working model, not anyone's documented internals" |
Asserted mechanisms (no evidence given in the talk)
Engines shortlist about 100 passages with a cheap embedding model, then rerank. Presented as a working model; the handout says it is not documented internals.
"Cross-domain web entity ranking": AI treats the site, YouTube, Reddit, reviews and Wikipedia as one entity. Slide heading, no source given.
Inconsistent facts across sources make AI skip the brand (attributed on stage to "someone" at a conference).
Monitoring tools use logged-out accounts, so they see the cheapest models and skew results. Spoken only.
The real constraint for engines is GPU capacity, so the cheapest passage to read wins. Spoken only.
Sources confirming each other raise citation. The paper he cites proposes and tests a scoring mechanism; it is not a description of any production engine (the handout says so).
Cross-referencing your own blog posts to each other counts as confirmation. Spoken only, and it conflicts with the handout's "independent source" and "copies of the same text don't count".
"Good SEO is good GEO": AI search and Google rose together because most answers pull from a search index. One client, same period.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Move 1, measure:
Build 30–150 buyer questions from the roles of the buying situation (condition, cost, for whom, instead of what, from whom), across exploring, comparing, choosing, checking, buying. Most without the brand name. WHITE
Freeze the list. WHITE
Run each question 5 times on 6 platforms, weekly. WHITE
Record three numbers: presence (named at all), rating (−5 to +5), first pick (recommended first). Log the model version, the date and what changed on the site. WHITE
When questions are added, keep reporting the original cohort separately. WHITE
Move 2, map sources: 6. Export the pages AI cites for those questions; group by type (review sites, editors and rankings, forums, marketplaces, employer reviews). WHITE 7. Act by type: collect and answer reviews · brief editors, correct errors, supply test data · signed expert presence on forums, no ads · complete listings · bring in HR for employer reviews. WHITE 8. One version of the facts, quoted the same everywhere. WHITE
Move 3, language: 9. One defining sentence: "[Brand] is a [category] for [segment] that [attribute]". Ask each engine which category it files the brand under, per product line. WHITE 10. Lexical map of the product (other names, category, types, parts, alternatives) → headings. Semantic frame (who, for whom, condition, cost, instead of what) → the questions under them. Extend with People Also Ask and competitor pages; mark the questions no competitor answers. WHITE
Move 4, extract: 11. Rewrite first paragraphs as BLUF: answer, proof, context. Use only facts already on the page. WHITE 12. Delete sentences with no fact. WHITE 13. Make each section readable alone: the heading asks the question, sentence one answers it by name. WHITE
Move 5, confirm: 14. The rankings AI cites for the rival are the PR target list. WHITE (he also said "buy guest posts from them": GREY unless disclosed) 15. Take the three most specific facts and get one independent source to state each. WHITE
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Vestigio OS: his monitoring product (6 platforms × 5 runs). No price given.
SensAI Academy, Mission 01 · Agentic Semantic OS: his course; seven objectives; early bird 2026-11-14, Season 1 from 2026-12-01. No price on the page.
Senuto (Maciej Chmurkowski): repeat-run, sentiment and page-level citation studies; 1M+ answers, 141k brands.
Szymon Parzych (Vestigio): brand research, 73k answers and 954k citations.
Open models for the rerank demo: BAAI/bge-small-en-v1.5 (embedding), jina-reranker-v1-turbo-en (reranker). He said reranker models are available on OpenRouter; not verified.
Jiang, Feng, Mehta, "Incentive-Aligned Multi-Source LLM Summaries", https://arxiv.org/abs/2509.25184
J.R. Firth (1957): "You shall know a word by the company it keeps".
Jabez Reuben: LLM Mastery host; distributes the workshop materials.
Slide photos
Full text of each slide: ../resources/robert-niechcial/slide-text.md Saved in ../resources/robert-niechcial/photos/ (7, all readable except where the speaker blocks the screen):
01-move-1-measure-a-portfolio.jpg — "Move 1 of 5: Measure a portfolio, not a prompt. One platform, one question, one number: each of them misleads."
02-randomness-out-four-steps.jpg — "How we take the randomness out: four steps": 1 many questions (30–150 real buyer questions, not one) · 2 many runs ("each asked 5 ti[mes] on 6 AI platforms", partly hidden by the speaker) · 3 read every answer (is the brand there, how is it described, is it the first pick) · 4 average (three steady numbers per brand instead of one lucky answer). Footer line unreadable.
03-move-1-what-to-do.jpg — "Measure AI visibility like this": 1 freeze the questions (30–150 real buyer questions, then stop changing the list) · 2 ask them everywhere (6 AI platforms, 5 times each, every week) · 3 count three numbers (rating, presence, first pick) · 4 write down what changed (the AI model version, the date, what you changed on your side). Matches tactics 1–4 above.
04-move-3-defining-sentence.jpg — "Move 3 · Level 2 of 3 · One sentence, repeated everywhere": "[Brand] is a [category] for [segment] that [attribute]." Matches tactic 9.
05-move-3-word-map-swimming-pool.jpg — "Move 3 · Level 3 of 3 · First, the words around the product": map for "swimming pool": other names (garden pool, outdoor pool) · category (outdoor leisure equipment) · types ("st…-frame, … pool", partly hidden) · parts (pump, liner, cover, heater) · alternatives (hot tub, indoor pool). Matches tactic 10.
06-what-works-four-moves-partial.jpg — "What works" with moves 1–4 shown (build-in before move 5).
07-what-works-five-moves.jpg — "What works", all five moves; same wording as the Thesis.
Q&A (question → answer)
None recorded. The talk ran over and ended on the QR code; the host announced the added workshop slot.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
Speaker name is Niechciał, not "Niechial".
"51–73% of AI citations come from the brand's own website" is wrong. Company websites are cited in 51–73% of answers about a brand; 4–11% of answers rely on brand websites alone.
"Harvard/Google research… 77% vs 50% for isolated sources" is wrong twice. The paper is by Jiang, Feng and Mehta; the figures are 15.6% / 38.4% / 77.1% and measure correct answers in a test with deliberately misleading sources, not citation rate. The speaker himself said "50%" and "visibility grows to 77%" on stage; the handout and slides carry the correct numbers. The Harvard affiliation was spoken only and was not checked.
"Run 5–10 queries across many platforms" understates it: 30–150 questions, 5 runs each, 6 platforms, weekly.
"Rank (cited first?)" is "first pick": recommended first, not cited first.
Omits every limit the handout states: correlations not experiments; the reranking pipeline is a working model; the roofing result is a coincidence in time; the 97% / 0% is two questions.
Omits the "what did not matter" list (schema, meta description, headings as questions, lists and tables, author box, domain strength).
Omits the sampling point of the case study: the +190.6% dashboard number came from adding an easier question set.
Omits that the talk sells a course and a monitoring tool.
The private notes ("optimize external topical web for an entity", "go after existing citations", "build consensus with consistency") are the note-taker's own lines; the summary presents them as headings of the talk.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
On stage the 97% / 0% example was told as the roofing client adding a photovoltaic product. The handout attributes 97% / 0% to an anonymised US software brand. Treat the roofing/photovoltaic version as an anecdote without numbers.
Whether OpenRouter offers reranker models.
The Senuto studies were not read at source; n=492 and the 20+ factor list come from the handout.
The three paper percentages were not checked against the paper body.
"Mustafa" (a best-kebab analogy) and several brand names (Castorama, "Wonderland") are speech-recognition spellings.
Slides PDF saved but not read page by page. The 7 Granola photos were read 2026-11-16: they show only Move 1, Move 3 and the five-move summary, and agree with the handout. They carry no study figures, so the measured claims above still rest on the handout.
Skills for AI Agents (workshop) — Robert Niechciał (co-founder, SensAI Academy; CTO & partner, Vestigio)
Source: Granola https://notes.granola.ai/d/1c24a04e-4715-4eb5-a1a3-e67d86455479 · recorded 2026-11-14 (17:37 GMT+7), unscheduled closing slot of LLM Mastery 4.0 · transcript-verified 2026-11-14 Resources: ✅ materials in hand. Published at https://sensai.io/llmmastery#workshop, downloaded 2026-11-17 to ../resources/robert-niechcial/workshop/, all read 2026-11-17:
ai-search-workshop-slides.pdf: 66 pages, read through its text layer (pdftotext). Pages not viewed as images; the one image-only slide shows bluf-generator/SKILL.md, which is in the folder.
ai-search-workshop-walkthrough.md: the full explanation, read in full. Byte-identical to AI Search Workshop - LLM Mastery 14.11.2026.md inside the zip.
semantic-os-six-skills.zip: original archive, 100 entries, no LICENSE file. The extracted copy is at semantic-os-six-skills/Semantic-OS/: README.md, AGENTS.md, six .agents/skills/<name>/SKILL.md, bluf-generator/references/transformations.md, and 12 files in examples/garden-swimming-pool/. The duplicate per-agent skill copies and CLAUDE.md / GEMINI.md were removed from the extracted folder; the zip still holds them.
License: the README states MIT (exact text under Tools). No photo attachments on the Granola note (checked 2026-11-17). The morning talk's notes and slides are in ../resources/robert-niechcial/.
Vendor talk? ⚠️ Yes, same as the morning talk (SensAI Academy course, Vestigio OS). The skills themselves were given away.
Skill names, steps and output shapes below come from the published SKILL.md files and the walkthrough. The audio (heavily garbled) is used only for what he said in the room, and those items are marked (spoken).
Thesis (3 bullets max)
A skill is a short markdown file holding a method: what to look at, in what order, and the exact output shape. These six contain no code.
The materials say a plain chat "knew about as much as the skill". What the skill adds is shape: fixed sections, evidence tags, facts only from the source, and one row per item, so two runs can be compared and a team can review them. (Spoken framing was stronger: intelligence is a commodity, and the method encoded in skills is the only edge.)
Six skills cover Retrieved → Cited → Trusted. They measure page readiness, not AI visibility.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Fan-out, skill vs plain chat | skill: 13 sub-queries (5 CONFIRMED, 6 PREDICTED, 2 SERP-ONLY). Chat: 26 searches in 7 groups, no tags | one run each, 2026-11-14. Search data pasted by hand: 4 People Also Ask questions + 6 related searches from Google UK for the head term "garden swimming pool" | speaker (SensAI) | slide + walkthrough + 1-query-fanout*.md; "26" also spoken | demo, single run. The run itself notes the tags show overlap with a head-term SERP only, not demand for the full question |
| Frame, skill vs plain chat | skill: 15 of 15 roles filled, 8 High. Chat: 18 questions in 3 tiers | one run each | speaker | slide + walkthrough + 2-frame-semantics*.md; "18" also spoken | demo. Slide says when to buy and where to buy were missing from the chat list; the chat does list "Delivery and returns" (item 14) |
| Lexical, skill vs plain chat | skill: 5 synonyms, 8 narrower terms, 9 parts, 4 opposites. Chat: about 100 terms, with paddling pool listed as a pool type | one run each | speaker | slide + walkthrough + 3-lexical-expander*.md; "about 100" also spoken | demo |
| BLUF rewrite | source intro: 3 sentences, no facts. Rewrite: every value taken from the page; 1 [FACT NEEDED] (price range per frame type; the page lists only product prices of £159.99 to £475.99) | one intro, one run | speaker | slide + walkthrough + 4-bluf-generator*.md | demo |
| Chunk check | 12 sections: 7 answer first, 2 partial, 3 no; readiness 6/10 | one page, one run | speaker | slide + walkthrough + 5-chunk-optimizer.md | demo |
| ⭐ Score stability (his own limit) | two runs on the same page: 5/10 and 6/10; answer-first openings counted 1 of 9 vs 7 of 12 | one page, two runs | speaker | slide ("5/10 and 6/10") + walkthrough; spoken, garbled ("gave five") | clear. The second run's output is not in the folder |
| EAV claims vs other pages | 43 triples. Checked against 7 other ranking pages: 11 confirmed (2 of them partial), 32 alone, 0 conflict. Chat: 22 facts (6 confirmed, 4 partly, 12 not found) | one run. 3 of the 7 comparison pages (K3, K4, K5) were cut at 1,500 words; the comparison text (_consolidated.md) is not in the folder | speaker | slide + walkthrough + 6-eav-extractor*.md | demo. "Alone" means not in the text available, not absent from the live page. Most confirmations come from one page (Outdoor Toys) |
| Answer first "triples" citation | "probability of being cited" rises three times | no base given in the workshop. It restates the Senuto correlation from the morning talk (18% vs 5% of the answer taken from the page, n=492) | Senuto | spoken twice; not on any slide or in any file | rejected as wording. The materials' own AGENTS.md says never to describe an output as a measure of AI visibility or citation probability |
No outcome was measured. Neither the materials nor the audio contain a before/after visibility or citation result from using any skill. Every number is a single-run count on one test page, skill against plain chat. The README says: "The plain chat was not set up to fail. It got the same input and a normal request." The model and settings used for the plain chat are not stated.
Asserted mechanisms (no evidence given in the talk)
From the materials (several carry the speaker's own caveat):
AI search splits a question into sub-queries before it searches, so a page competes for the sub-queries. Own caveat: "No AI product publishes the ones it really runs."
Platform fan-out table in query-fanout/SKILL.md: ChatGPT "Bing + wide fan-out, prefers long articles" · Perplexity "Aggressive fan-out, cites specific fragments" · Gemini "Knowledge Graph + YouTube, structured data" · Claude "Own index, smaller fan-out". Labeled "Observed tendencies at the time of writing ... not documented guarantees". No source given.
Retrieval cuts pages into passages and judges each alone; about 200 to 500 words is "a common working assumption, not a known rule".
An answer-first passage is easier to match and quote. transformations.md labels this "working hypotheses from practice, not published ranking or citation factors".
AI tends to trust facts that independent sources repeat in detail. The walkthrough says this "comes from research on controlled data, not from a published rule of any search product. Treat it as a direction."
Covering frame roles "can improve the chance that a passage matches a sub-query (a planning heuristic, not a guarantee or a quota)".
Spoken only:
Intelligence is a commodity (he named Opus 5.5 as the example). Every competitor gets the same model the same day, so only domain expertise encoded in skills differentiates.
Each fan-out sub-query is a chance to appear; cover all of them to raise the odds. This conflicts with the materials ("Covering more roles does not automatically make a page better"; an empty role is "a gap to look at, not a rule").
Models have a reasoning gap (his term): they answer even without the information, so unanswered questions are open ground.
He said the skills verify what is true and what is hallucination. The materials say the opposite: the skills "do not check truth".
He said a skill removes hallucination in most cases. He still told the room to proofread every fact.
"Search purpose" (why they search and what would satisfy them) should be tracked beside search intent. Named as an idea, not defined.
BLUF lowers the machine's retrieval cost. He called user signals the most important factor, and said AI runs on knowledge, not opinions.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
How to run (materials): open the folder in Claude Code, type /<skill-name> and paste the input. No API keys, no Python, no .env. To reuse the skills, copy .agents/skills/ into the agent's skills folder (for Claude Code, .claude/skills/ or ~/.claude/skills/). No SERP tool ships with this edition; search data is pasted by hand. All six skills are WHITE.
1. query-fanout (Retrieved)
Job: simulate how AI search splits one question into sub-queries.
Input: one question in the customer's words, plus optional pasted SERP data (People Also Ask and related searches).
Method: (1) decompose three ways: Semantic (entity, attributes, relationships, time and place context), Intent (what the user really wants, hidden assumptions, likely follow-ups), Verification (fact-check, source and authority, comparison questions); (2) optional grounding against PAA and related searches, tagging each line [CONFIRMED] (in the SERP), [PREDICTED] (model only) or [SERP-ONLY] (in the SERP, missed by the model; a gap candidate only after checking the page does not already answer it); (3) with no SERP data, mark every line unknown.
Output: header line (question, entity, intent, complexity) · Sub-queries table (sub-query, purpose, source type, grounding) · Visualization tree · Implications for Content (what the page should contain per sub-query) · Content Gaps checklist. The skill targets 5 to 10 sub-queries; the example produced 13.
Spoken: the sub-query list is the prompt portfolio and the content plan; "measure the sub-queries, not the question you typed" (also a slide).
2. frame-semantics (Retrieved)
Job: list every kind of question an action or topic contains.
Input: a topic or verb phrase plus a perspective (buyer, seller or expert).
Method: fill 15 roles: Agent, Patient, Instrument, Location, Time, Cause, Purpose, Manner, Result, Condition, Beneficiary, Source, Cost, Alternative, Part. Turn each into a question with a priority (High, Medium or Low). Rules: perspective matters; prioritize by search intent and the page's job; roles combine (Cost + Instrument = how much and how to finance); frames nest (financing inside buying).
Output: Frame table (element, value, sub-query, priority) · Query Fanout Map (question tree, each linked to its role) · Suggested H2 Structure (H2, element, question type) · Related Frames (candidates for separate pages).
Pairing: fan-out starts from a question, the frame from the topic. In the example, the fan-out reached Cost, Condition, Alternative, Location and Source but not Time, Instrument or Part.
Spoken: perspective example (a UK homeowner asks different questions than an athlete); told the room to cover every role (see the conflict above).
3. lexical-expander (Retrieved)
Job: map the words around one keyword.
Input: one keyword plus context (market, language, what the site sells).
Method: five relations, each with a page job: Synonyms (match differently worded queries) · Hypernyms (broader category; intro context and heading hierarchy) · Hyponyms (narrower types; H2 sections) · Meronyms (parts; completeness, spec and accessory questions) · Antonyms (opposites; "X vs Y" sections). Rules: context matters; prioritize terms used in real queries; cover only the parts that matter to the page's job; review for domain accuracy ("related is not the same as synonym", e.g. paddling pool).
Output: tables and trees per relation, each with the sub-queries it reaches and suggested H2s · Query Fanout Coverage Map · Recommendations.
Spoken only: opposites are a good place for internal links to the next page; boundaries help avoid cannibalization; the map can feed a topical map. None of this is in the skill file.
4. bluf-generator (Cited)
Job: rewrite a passage so the answer comes first.
Input: the passage, ideally with the whole page pasted as the source of facts.
Method: (1) identify the question the text answers; (2) find the answer, usually buried lower down; (3) rewrite as answer, then evidence, then context, cutting intros, announcements and empty adjectives, and replacing vague words only with values the source supports; (4) return the result. Never invent a number; write [FACT NEEDED: ...] instead. The 50-word answer target is a heuristic, not a gate. references/transformations.md holds the full cut list and vague-to-precise list, plus "hierarchical BLUF" for texts over about 300 words.
Output: Analysis (question, where the answer was buried, missing data) · BLUF Transformation · Structure table (answer, evidence, context).
Spoken: the copywriter paid for 1,000 words when the topic needs 200; a New Year's Eve dress intro as a bad example; said a URL also works as input (the folder ships no page reader).
5. chunk-optimizer (Cited)
Job: check a whole article one section at a time.
Input: the article as markdown, without navigation and footer.
Method: five areas: heading structure (hierarchy; H2s answer sub-queries; descriptive headings) · answer first in each H2 · autonomy (names its subject; no "as mentioned" or "this") · term distribution (no section empty of key terms) · section length (soft check; about 200 to 500 words is a reference, never pass/fail).
Output: Summary · Heading Structure tree with ✅/⚠️/❌ · BLUF in Sections table · Autonomy table, quoting the phrase that breaks each section · Term Distribution bars · Section Length table · Chunk Readiness Score 1 to 10 · Recommendations ranked 🔴/🟡. Weak sections go back through bluf-generator.
Spoken: read one heading alone and ask whether it carries its own information; if not, rewrite or delete it.
6. eav-extractor (Trusted)
Job: list every fact a text states as entity / attribute / value, with the sentence it came from.
Input: any text.
Method: (1) identify entities; (2) extract attributes; (3) assign values and keep the conditions that change meaning (unit, date, market, plan); (4) keep only triples traceable to a passage, marking gaps [missing]. Attribute types: simple, complex, derived, key, multi-valued.
Output: Identified Entities · EAV Table (entity, attribute, value with conditions, type, quoted source passage) · Relationships Between Entities · Statistics (descriptive only).
Comparison step (not part of the skill): run it on other pages about the topic, then ask which facts appear with the same value in at least two sources, which appear only on your page, and which conflict. Confirmed = keep · Alone = "your best content and your weakest proof"; the outreach list · Conflict = fix or explain. The materials suggest two or three other pages; the example used seven.
Spoken only: if competitors state a claim your page lacks, add it to your page (WHITE if the claim is true). He also mentioned getting missing claims into guest posts (GREY unless disclosed).
First pass on one page (materials, 6 steps): fan out the main question → frame the topic and add the High rows the fan-out missed → map the words → chunk-check the page → BLUF the weak sections → extract facts from the page and from other pages, then mark the ones nobody else confirms. Spoken 7th step: confirm those facts on external pages.
Limits (materials):
They read pages and never see an AI answer, so visibility is measured separately, across many prompts and over time. (Spoken: reading AI answers is easy to orchestrate with agents but is not in these skills; he offered to help.)
Generated questions and terms are candidates, not proof of demand.
They do not check truth: eav-extractor reports what a text says.
Scores are judgment and move between runs.
Every [FACT NEEDED], every health, legal or money claim, and every final text needs a subject expert.
Monday list (materials, 4 items): fan out your five most important questions and track the sub-questions, not the five · build the frame for your main product and look at the High rows that are not about the product · rewrite the intro of your best-selling category answer first · list the facts on your key page and mark the ones no other site states. (Spoken version: find your five most important business, product and brand questions; the other three are the same.)
Running example: garden swimming pools
Case: a UK online shop selling above-ground and frame garden pools. The three planning skills run on the topic. The three page skills run on a public buying guide, https://www.aosom.co.uk/blog-how-to-choose-the-swimming-pool-for-garden.html ("a test page, not our client"). Every example is one saved run from 2026-11-14, with the plain-chat answer to the same input saved beside it.
Source intro, as published, opens: "Swimming pools make a fantastic addition to any garden, offering a perfect escape during the summer months."
| skill | plain chat gave | the skill run added |
| query-fanout | 26 searches in 7 groups plus general tips; noted that the PAA data "overlap[s] strongly" | a tag per line, a per-sub-query "page should contain" table, and a gap checklist with [FACT NEEDED] flags (own prices, warranty, verified planning source) |
| frame-semantics | 18 questions in 3 tiers, ordered by judgment | all 15 roles, each with a question and priority; draft H2s; 7 related frames (financing, installing, maintaining, safety, heating, pump, hot tub) |
| lexical-expander | about 100 terms grouped by where to use them | terms grouped by relation, each with a sub-query and suggested H2; paddling pool flagged "adjacent category ... not a true hyponym" |
| bluf-generator | answer first, but opened with "The best garden swimming pool for most households is a powder-coated steel frame pool", a verdict the page never states (the chat flagged this itself), and kept "This guide also covers..." | answer first using only page values; no announcement; missing price range flagged |
| chunk-optimizer | written review; also caught wrong image alt text and conflicting storage advice | a table for all 12 sections; quoted breaking phrases; flags that 7 of 12 sections never say which kind of pool; ranked fixes |
| eav-extractor | 22 facts as a summary | 43 rows, each with its quoted sentence and a verdict, plus reading notes on thin support and truncated pages |
Overall (materials): "Judgements still vary between runs. The shape does not."
Note: the BLUF rewrite reuses "3m x 3m round" from a size table that the chunk run calls flattened, with a round pool listed under an L x W column. "Facts only from the page" carries page errors forward; it does not check them.
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Semantic-OS workshop edition (SensAI): six skills, README, AGENTS.md, walkthrough, examples. Free download at https://sensai.io/llmmastery#workshop.
License, exact README text: under "Can I change the skills or share them?": "Yes. The license is MIT." The final section reads "## License" followed by "MIT". No copyright holder line, and no LICENSE file in the zip.
Agents (materials): Claude Code, Codex, Cursor, Gemini CLI, wired through links to .agents/skills/ (the zip holds copies instead). "The skills were tested in Claude Code."
Agents (spoken, garbled): Claude, Codex, Gemini, Copilot, plus names heard as "PI", "OpenCloud", "Hermes" and "dragbot". Copilot and those three are not in the materials.
NodesHub (nodeshub.io): API key for the Google-results tool in the full Semantic-OS system. Not shipped here. No price.
Jina AI Reader: optional key for the page-reader tool in the full system (20 vs 200 requests per minute). Not shipped here.
SensAI Academy, Mission 01 · Agentic Semantic OS: "the playbook, the rule catalogue, the planning and audit pipelines, and 30+ skills". Every SKILL.md ends with a "Go deeper" footer pointing to it. No price given.
Comparison pages in the EAV example: Bestway UK, Discount Leisure Products, Compass Pools, Outdoor Toys, My Pool Direct, The Wooden Pool Store, PriceRunner.
"Decision-class models", heard as "jazz Gemini decision" (spoken): said to make orchestrated results much better. Not in the materials. Unclear.
Jabez Reuben: LLM Mastery host. Handover as spoken: Niechciał said he would send the materials to Jabez, email them that evening to anyone who left an address in the room, and that Jabez would send them out after the weekend.
Slide photos
None on the Granola note. The published deck replaces them: ../resources/robert-niechcial/workshop/ai-search-workshop-slides.pdf (66 pages, text layer read). Every number on the slides matches the walkthrough and the example files.
Structure: what a skill is → repo layout → map (three steps, six skills) → running example → for each skill: what it is / how it works / run it / plain chat / with the skill / the difference / one-line takeaway → six runs, one pattern → first pass → limits → Monday → Join SensAI.
Takeaway slides: "Measure the sub-questions. Not the question you typed." · "The frame finds the questions nobody has typed yet." · "Write in the shopper's words before you write in your own." · "A chat makes the text prettier. The method makes it quotable." · "Let every section survive on its own." · "The "alone" column is your outreach list."
The "How it works" slide for eav-extractor presents the page comparison as part of the method ("Run it on other pages ... Compare the lists"). The walkthrough and README say the comparison is not part of the skill.
Q&A (question → answer)
None. A second voice says only "Yeah" once and "All right" at the end. He ran over time and sped up for the last skill.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
The heading says five skills; there are six (the slides, README and repo all list six).
"Retrieve, Seeded, Trusted" is Retrieved → Cited → Trusted.
Names, now confirmed from the files: "Query Format" = query-fanout; "BLUF Optimizer" = bluf-generator; "EAD Extractor" = eav-extractor.
Stage mapping is wrong. Per the README and slides, lexical-expander is Retrieved, bluf-generator and chunk-optimizer are Cited, and eav-extractor is Trusted.
Frame semantics has 15 roles, not the 8 the summary lists.
Lexical expander's classes are synonyms, hypernyms, hyponyms, meronyms and antonyms. "Boundaries" is not a class (it is a domain-accuracy rule). "Parts become body text", internal linking and topical maps are not in the skill; the last two were spoken.
"Opening with the answer triples citation probability" was spoken, but the materials never say it, and AGENTS.md forbids that framing.
EAV: the skill takes one text. The confirmed / alone / conflict comparison is a separate prompt, not "missing". "Missing competitor claims = add to your site" was spoken only.
Agent list: Copilot was spoken; the materials name Claude Code, Codex, Cursor and Gemini CLI.
Monday list: the summary's fifth item ("Confirm unclaimed facts on external pages") comes from his spoken first-pass recap. The materials' Monday list has four items, and the first is "fan out" the five questions.
Omits every stated limit, the MIT license, and that no result from using the skills was shown.
Where the materials contradict this file's earlier, audio-based version (2026-11-14):
Fan-out grounding uses only pasted PAA and related searches, not competitor pages. There is a third tag, [SERP-ONLY], and unknown when no data is given. The output also has a tree, an Implications table and a gaps checklist.
Frame: 15 roles, not 11 (adds Cause, Manner, Result, Part). Priority is High / Medium / Low. The output adds a question tree, draft H2s and related frames.
Lexical: five relations, not "synonyms, types, parts, opposites, boundaries". Internal-link targets and cannibalization are spoken only.
BLUF and chunk inputs are pasted text, not URLs. The folder ships no page reader; "paste URL" was spoken.
Chunk optimizer checks five areas (adds heading structure and section length) and gives a 1 to 10 score, not only a pass/partial/fail table.
EAV input is any single text, not "the client page and one other page". The comparison is an extra step; the example used seven pages.
Score stability: the numbers are 5/10 vs 6/10 (earlier: "number garbled").
"Plain chat: flat list with no validation": the chat file shows 26 searches in 7 groups, and the chat itself said the PAA data overlapped with its list. The slide's own "difference" table also says "flat list".
The earlier file said the repo was not linked from sensai.io/llmmastery (checked 2026-11-14). It is now published there (#workshop).
Unclear / needs verification (mis-heard names, numbers you could not pin down)
"Decision-class models" ("jazz Gemini decision"): not in the materials, still unresolved.
Spoken agent names "PI", "OpenCloud", "Hermes" and "dragbot" are speech-recognition spellings; not checked.
Whether the published folder differs from what was shown in the room. He said he built the repo about two hours before and the slides about an hour before. The zip entries are dated 2026-11-15 06:08 (time zone not stated), after the session.
The second chunk-optimizer run (5/10) and the EAV comparison text (_consolidated.md) are not in the folder, so those counts cannot be re-checked without fetching the pages again, and the pages change.
Which model ran the skills and which ran the plain chat is not stated.
The platform fan-out table in query-fanout gives no source.
Small internal inconsistencies: the README says the walkthrough explains each skill in "seven parts" while the walkthrough says eight; the README calls the chat fan-out a "flat list" while the file shows 7 groups.
License terms: stated only as "MIT", with no copyright holder named.
Scaling Social: 0 to 500,000 followers with AI (X and Instagram) — Sarvesh Srivastava (runs an SEO / local SEO agency; company not named on stage)
Source: Granola https://notes.granola.ai/d/93e8a6a9-f275-423d-9180-9a5f5e1f5b11 · recorded 2026-11-15 (14:33 GMT+7; Granola shows 11-14 23:33 PST) · transcript-verified 2026-11-16 (full transcript read, 20.4k chars, about 26 minutes incl. Q&A) Resources: 10 slide photos saved to ../resources/sarvesh-srivastava/photos/ (all viewed; photo 06 is motion-blurred and only partly readable, photo 03 is too blurred to read the file list, 09 and 10 are the same slide). Deck is 50 pages ("Page 20 of 50" on photo 02). Vendor talk? Partly. No product or course pitched; the talk advertises his agency's inbound model ("they come to you, you set the price"). The four prompts are given away on slides. All numbers are his own account stats.
Thesis (3 bullets max)
Test everything on X, where a failed post does not hurt the next one; scale the winners to every other channel.
Let AI do production: four chained prompts in Grok (Scout → Hook Forensics → Ghost Writer → Analyst) find outlier posts, extract the hook pattern, draft in your voice and score results; about 1 hour a day.
Convert views with the profile (who you help, what you do, a way into the funnel) and lead magnets; inbound clients arrive pre-sold and accept your price.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Follower growth | 0 → ~500,000 across Instagram, YouTube, X, LinkedIn, Facebook in ~18 months; Instagram ~280k; X ~62k; a third account 14k (likely LinkedIn, garbled "L") | his accounts | speaker, self-reported screenshots (not photographed) | spoken | self-reported; no photo |
| Views | 122M on X in the last year; 26M on Instagram (later "26 plus 25 million views in the last 30 days", garbled) | his accounts | speaker | spoken | the Instagram period is garbled: last year or last 30 days |
| X profile stats | "under 32 million impressions", 83,000 profile visits, 740,000 bookmarks, last year | X analytics screenshot | speaker | spoken (slide not photographed) | garbled; the 32M conflicts with 122M views |
| Newsletter | 7,000 "very active" readers | — | speaker | spoken | self-reported |
| Business result | his agency built "a multi billion dollar business" in two years from social alone | — | speaker | spoken | ⛔ almost certainly garbled; do not quote |
| Time cost | under 1 hour a day once optimized | his routine | speaker | spoken | self-reported |
| X audience income | "1 in 3" US X users earn $100k+ | "I was reading" | unsourced | spoken | unsourced |
| X time spent | users spend more time on X than other social platforms | "data from Similarweb" | Similarweb, relayed (slide not photographed) | spoken | not checked |
| X algorithm weights | link copy/share ×38; reply that the author engages with ("someone you follow back replies") ×138; report −55; delete −79; block −47 | his reading of the public X algorithm repo | speaker | spoken; the repo photo (03) is unreadable | ⚠️ unverified; transcript garbled around each figure |
| Hook examples | "things I know at 42 that I wish I knew at 22" ~7M views, 52,000 bookmarks (spoken "sales"); "how to do a hard reset on your life in 30 minutes" ~1.3M views, 23,000 bookmarks, 40,000 likes | other people's posts | speaker | spoken | garbled ("sales" for bookmarks) |
| Scout output | "I checked all 70 accounts this morning and 11 posts cleared 5× their account's median" | one Scout run | his Grok setup | slide (photo 06, partly readable) | motion-blurred; handles and per-post numbers not reliable |
| Profile examples | Dan Go: 565,000+ newsletter subscribers, ~1.2M followers; Marcos Ruiz: 28K followers | public X profiles | screenshot | slides (photos 01, 02) | readable |
Asserted mechanisms (no evidence given in the talk)
X scores each post on its own, so posting 10–30 times a day carries no penalty for failures.
Bookmarks, link copies and replies the author engages with count far more than likes; reports, blocks and deletes count against you (from the public repo, per him).
Hooks from other niches outperform because your audience has not seen the format.
A winning post can be reposted after about two weeks with a new hook; audiences do not remember.
Hooks do not carry across platforms; a thread must become a short guide elsewhere.
Instagram is the fastest-growing platform for a new account.
Inbound leads trust you before the call, close more easily and accept your price because SEO is a commodity.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
No prices stated.
Profile (photos 01, 02): state who you help, what you do for them, and one way into the funnel (strategy call, newsletter, lead magnet); add one human detail (his example: "Arsenal fan"). WHITE
Watchlist: 60–70 accounts in your niche and outside it. WHITE
Scout prompt (photo 05), in Grok: every morning at 8 AM scan the saved watchlist; per account compute the median views of its last 30 original posts; find posts from the last 48 hours at ≥5× that median; exclude replies and reposts; prioritize local SEO and agency growth; send the top 5 ranked by multiple of the account's median, not total views; per post give link and opening hook, views, median and multiple, why it is worth studying, an angle to adapt; "If nothing qualifies, say so. Don't lower the bar." (Spoken: every Monday at 8 AM; slide says every morning.) WHITE
Hook Forensics prompt (photo 07): 8:30 AM, read Scout's winners; name each hook's mechanism (curiosity, specificity, proof, contrarian claim, clear promise) and why it keeps people reading; turn each into a reusable pattern, not a rewrite; also map full-post structures (opening, main points, proof, ending) from the watchlist; keep a hook-and-format library, merge duplicates, count wins per pattern; send top 5 with mechanism, template, example link, angle for his local SEO audience. "Reuse the structure. Never copy the wording." WHITE
Ghost Writer prompt (photo 08): 9 AM, write 3 X posts for the local SEO audience; use this week's hook patterns and content focus, a different pattern per draft; match the saved voice guide (casing, line breaks, length, punctuation, emoji); borrow structure, "match my voice, not theirs"; each draft a different angle relevant to the services sold; "Use only real facts and results I've supplied. If a specific result is missing, ask me — never invent a number or case study."; send drafts with the pattern used and a ready-to-post link. WHITE
Analyst prompt (photos 09, 10): track every original post; refresh views, bookmarks, replies, likes through the day; compare with his 21-day median views, excluding posts under 24 hours old; keep snapshots; flag any post above 3× median; every Sunday review the last 7 days: strongest and weakest posts with links and scores, hooks/topics/formats to repeat, patterns to drop "grounded in the numbers"; "Separate what the data shows from what might explain it. Never invent missing metrics." WHITE
Posting stays manual: the bots need no access to the X account; he posts himself. WHITE
Scale winners elsewhere: reformat per platform (an X thread becomes a short guide); repost after ~2 weeks with a new hook. WHITE
Instagram production: AI script → HeyGen avatar from a 30-second talking-head clip → ElevenLabs cloned voice with audio tags for emotion → human editors finish. He says he has never recorded a video for the channel. GREY (undisclosed AI avatar presented as himself)
Comment-keyword lead magnet: ask viewers to comment a word; automation replies publicly and DMs the link; Instagram prompts non-followers to follow first; the link collects email. If buttons fail, send the link directly to a qualifying form. WHITE (tool not named)
Lead magnet first: pick the content topic, then have AI generate a matching lead magnet; make it more substantial for an expert audience. WHITE
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Grok / "Grok Bot" (xAI): runs all four prompts with native X access, no API setup; slide: "It scrapes X for you. Completely hands[-off]" (photo 04).
X algorithm repo on GitHub ("x-algorithm", public; folders labeled "Open-source X Recommendation Algorithm"; photo 03).
HeyGen (spoken "HN"): avatar video from a 30-second clip. ElevenLabs (spoken "11 labs"): voice cloning with audio tags.
Similarweb: source for the time-on-platform claim.
Dan Go (@CoachDanGo; dango.co/newsletter; hpfhq.com/r/x-bio) and Marcos Ruiz (@itsmarcosruiz; CEO, The Birdhouse, thebirdhouse.co): profile examples.
Slide photos
Full text of each slide: ../resources/sarvesh-srivastava/slide-text.md
01-x-profile-example-dan-go.jpg: Dan Go X profile. "Join 565,000+ subscribers getting high performance tips every Tuesday and Friday", dango.co/newsletter; bio "Health Performance Coach To Entrepreneurs | Tweets on Fat Loss and Optimiz[ing] The Body | On a Mission to Transform A Billion Lives…"; "Sign up for a strategy call → hpfhq.com/r/x-bio"; ~1.2M followers.
02-x-profile-example-marcos-ruiz-birdhouse.jpg: Marcos Ruiz (@itsmarcosruiz), "CEO @TheBirdhouse – We scale Personal Brands on X, LinkedIn, and more. Arsenal fan.", thebirdhouse.co, 788 following, 28K followers. Deck counter "Page 20 of 50".
03-x-algorithm-github-repo-blurred.jpg: GitHub repo "x-algorithm" (public). Too blurred to read folder names or any weight; it does not back the ×38 / ×138 figures.
04-grok-bot-magic-sauce-for-x.jpg: "Grok Bot is the magic sauce for X. It scrapes X for yo[u]. Completely hands[-off]" (speaker blocks the ends).
05-scout-prompt.jpg: full Scout prompt (step 3). Readable.
06-scout-output-example-motion-blurred.jpg: a Scout reply: "I checked all 70 accounts this morning and 11 posts cleared 5× their account's median…" then five posts with views, bookmarks and multiples. Motion-blurred; handles and numbers not used.
07-hook-forensics-prompt.jpg: full Hook Forensics prompt (step 4). Readable.
08-ghost-writer-prompt.jpg: full Ghost Writer prompt (step 5). Readable.
09-analyst-prompt.jpg, 10-analyst-prompt-duplicate.jpg: Analyst prompt (step 6); last line partly hidden ("Tell me what to repeat – not j[ust] wh[at got] views").
Q&A (question → answer)
Instagram "click the button below" never shows a button for me; workaround? → Automation sometimes fails; send the link directly and point people to a qualifying form first.
How do you rework content that should have performed but didn't? → Repost on the same platform after about two weeks with a new hook; reformat for each platform rather than cross-posting.
Do the bots need access to the X account? → No; they can post if given access, but he posts himself.
What comes first, the content or the lead magnet? → Decide the content first, then have AI generate a lead magnet for it; a non-expert audience needs a simpler magnet, an expert audience a deeper one.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
"Scout monitors 60–70 accounts weekly": the slide says every morning at 8 AM (spoken "every Monday"); the prompt also sets the 5× median, 48-hour, last-30-posts rules and the top-5 cut, none of which the summary carries.
"Highest multipliers: copying a link (38×), reply from someone you follow back (138×)": spoken only and garbled; the repo photo is unreadable. The summary presents them as fact.
"Avoid: deleted posts (−79×)": in the audio, −79 sits between report and block and its label is unclear.
"26M+ views in 30 days" on Instagram: the transcript gives 26M twice, once with "last year" context; the period is unclear.
The summary omits the guardrails in his own prompts: never invent a number or case study, never copy wording, never lower the bar, separate data from explanation.
It omits that he presents himself on Instagram only through an AI avatar, and the "multi-billion" business claim is garbled.
It omits that the bots do not post; he does.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
The X algorithm weights; check the repo before repeating any figure.
His agency's name and the real business figure ("multi billion" is not credible as spoken).
The third account's 14k (LinkedIn?) and the Instagram view period.
The comment-to-DM tool (not named).
Speaker name spelling taken from the Granola title; the host says "Sa…"/"Sabish".
From Rank to Recommend: the Recommendation Chain — speaker not named in the recording (former product marketing lead, Semrush; now freelance and at "RevenueCash", garbled)
Source: Granola https://notes.granola.ai/d/b396df99-3346-4884-ae31-1f4fc7854e72 · recorded 2026-11-14 (16:28 GMT+7; Granola 11-14 01:28 PST), LLM Mastery 4.0 day · transcript-verified 2026-11-16 Resources: no slide photos attached; slides offered by QR code (host said it was not on screen long enough). The speaker's introduction is at the end of the C32 recording: "led product marketing at Semrush, and now she's the senior data marketer at RevenueCash" (company garbled). One web search for her name did not settle it. Vendor talk? ⚠️ Partly. Two of the case studies were diagnosed with Semrush's paid brand-performance tool, and three (WordPress.com, Writesonic, Relay) are her own or Semrush's client work; she freelances and asked for contacts at the end. The survey and research figures are her own or co-authored, with no sample sizes stated.
Thesis (3 bullets max)
Search has moved from rank to recommend: AI does the comparing, buyers give it a full brief, so the brand that clearly fits the request is recommended, not the biggest one.
A recommendation needs four links: claim (clear positioning), proof (sources back it), perception (AI's picture is right and current), fit (proof for the specific use case). Diagnose which link breaks before doing generic GEO work.
Do the positioning homework first, then lead with it on the homepage and every profile, answer AI's negative perceptions with verifiable facts, and go deep on fewer topics.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Buyer briefs | 61% of B2B buyers describe their exact situation in the prompt (constraints, budgets, required features) | "a couple of pretty big surveys" earlier in 2026; no n, no method | speaker | spoken | low: no sample |
| What stands out | 53% of B2B buyers: a vendor stands out when it matches their use case; 7% would choose because they recognize the name; 20% of consumers: a brand stands out because it appears first | same surveys | speaker | spoken | low: no sample |
| WorkLaunch (Prague coworking; spelling uncertain) | 5 months after the fix: sentiment score 82 positive; Google AI Overview visibility doubled; 20× more traffic from ChatGPT | one client; base traffic not given | Semrush brand-performance tool + client | spoken | low: no base; ratio on an unknown base |
| rtCamp | AI sentiment score to 100% "in a couple of months"; "pretty significant increase" in organic leads from AI search | one client; no numbers for leads | Semrush tool | spoken | low |
| Relay (teacher-education school) | entered "best masters in teaching" lists after repositioning | one client; no count | speaker | spoken | anecdote |
| ⭐ Verifiable facts on homepages | probability of a brand mention rose from 5% to 30% as verifiable facts on the homepage rose "from 15 to 16" (garbled; likely 1→16 or 0→15); homepage is the page agents request most | research by "Andy Krista Dina" (likely Andy Crestodina), "recently published, or maybe about to" | third party (Orbit Media, if Crestodina) | spoken | low until the study is read; correlation |
| Depth beats breadth | brands present in fewer core topics got more mentions than brands spread thin | research with Kevin Indig; no n | speaker + Kevin Indig | spoken | low until read |
| Topic ownership | 85% of ChatGPT topics have no clear owner | same; "owner" not defined | speaker + Kevin Indig | spoken | low |
| ChatGPT searches per question | ~24 web searches on average for a typical comparison question, in a reasoning mode ("speaking mode" in audio) | research with Kevin Indig; no n | speaker + Kevin Indig | spoken | low until read |
Asserted mechanisms (no evidence given in the talk)
AI recommends the brand it can clearly match to the buyer's stated constraints, then verify across the web.
Inconsistent positioning across the brand's own site, listicles and reviews makes AI treat a product as a mixed tool recommended for nothing (Writesonic: content generator → SEO tool → GEO tool).
Too few third-party mentions make AI bypass a clearly positioned niche brand (Invoicefly).
Stale negative perceptions (from old Reddit threads and reviews) keep a brand out even when the facts changed (WordPress.com, WorkLaunch).
Consistency matters more than content volume.
ChatGPT brand claiming (launched days before the talk) does not raise visibility by itself; it is another surface to keep accurate.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Diagnose:
Run three prompt types per brand: "what is X", "best X for Y", "X vs competitor". WHITE
Build a "Golden Thread" document: brand, product, audience, the verifiable facts you want surfaced, and the category prompts to track. WHITE
Measure share of voice and sentiment against competitors, what AI praises and criticizes, and which sources shape the answers. WHITE
Label the break: claim, proof, perception or fit. WHITE Act:
Write the positioning: what you do, for whom, why you are credible (Relay: from "practice-based certification tied to charter schools" to "nationally accredited graduate school that defines how educators learn by doing across public school systems"). WHITE
Lead with it on the homepage, product and solution pages, Google Business Profile, with verifiable facts (ratings, credentials, client count, years, specific offers). WHITE
Correct outdated facts (pricing, features) on the site and everywhere else, including ChatGPT's brand profile. WHITE
Answer perceptions with content: tackle the negatives, repeat the positives; rewrite pages with missing facts and build FAQ blocks from real prompts (WorkLaunch rewrote ~90 pages). WHITE
Own the niche: a page for every audience served, original data on a regular schedule (Semrush published proprietary data at least monthly), executives sharing expertise. WHITE
External: ask customers for reviews that cover the attributes you want highlighted; reply to negative reviews with verifiable facts. GREY (steering review content is close to the no-review-gating line; fine if the request names topics, not wording, and is sent to every customer)
Find the listicles and directories AI already cites; ask them to correct errors and add missing information; pitch corrections backed by data. WHITE
Put the positioning into coverage, partner content and communities (a branded subreddit, Quora). WHITE if disclosed
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Semrush brand performance tool: shows positive and negative brand factors in how AI perceives a brand. No price.
ChatGPT brand claiming / "ChatGPT for business": verified profile, product feeds, mention data, a product agent for US businesses; no prompt data; mentions = references to the website, not the brand name; leans to e-commerce now. She called it a mix of Google Business Profile and Search Console.
Kevin Indig: co-author of the depth-vs-breadth, topic-ownership and 24-searches research.
"Andy Krista Dina" (likely Andy Crestodina): homepage verifiable-facts research.
Case brands (spellings uncertain where noted): WorkLaunch / "Work lounge" (Prague coworking), "Summary AI" (mobile AI note-taker), Writesonic, Invoicefly, WordPress.com (her 10-month fractional engagement), rtCamp (WordPress agency; launched a "trust center"), Relay (US teacher-education graduate school), WeWork (comparison example).
Slide photos
None attached to the Granola note.
Q&A (question → answer)
None. The host noted the QR code was not on screen long enough and suggested republishing all QR codes later.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
The summary gives the survey percentages (61%, 53%, 7%, 20%) as facts; no sample size, population or method was given.
"Verifiable facts lift brand mention probability from 5% to 30%" drops that it is about homepages, that it is someone else's study (likely Andy Crestodina's, "recently published, or maybe about to"), and that the fact counts are garbled.
"ChatGPT runs ~24 web searches" drops the mode qualifier (a reasoning mode) and the co-author.
Omits that the WorkLaunch and rtCamp diagnoses used Semrush's own paid tool, and that WordPress.com was her own fractional client.
Omits that rtCamp's lead increase has no number and Relay's result has no count.
Omits the speaker's identity line (from the previous recording) and her freelance pitch.
Brand names are uneven: "WorkLaunch" is also "Work lounge" in the audio; "RT Camp" is rtCamp.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
Speaker's name: not said in either recording. Introduced as former product marketing lead at Semrush, now at "RevenueCash" (likely garbled). One web search did not settle it.
The fact-count range "15 to 16" for the 5% → 30% result.
The surveys, the Kevin Indig co-studies and the Crestodina study: none read.
Whether ChatGPT brand claiming launched in the days before 2026-11-14 as described.
An Autonomous AI-Avatar Video Engine for AI Overviews (title not captured; "slop or not" is his framing) — Stewart Vickers, "SEO Jesus" (link-building agency owner; YouTube channel "Stewart Vickers AI")
Source: Granola https://notes.granola.ai/d/619fab5b-c144-47a6-8b1a-e277cb04e6d3 · recorded 2026-11-14 (12:02 GMT+7; Granola shows 2026-11-13 21:02 PST); last slot before lunch, immediately before Alan CladX's LLM Mastery-branded talk (C27), so most likely the LLM Mastery 4.0 day despite the "CMSEO" note title · transcript-verified 2026-11-16 Resources: 8 slide photos saved to ../resources/seo-jesus/photos/ (all 8 read; one partly blocked by a phone, re-shot in the next photo). He says the full workflow and skill are on his Skool community page (QR code; URL not captured). Vendor talk? ⚠️ Partly. He gives the pipeline away on the slides but the talk ends on a QR code to join his Skool community, where the "whole skill" is posted. Same speaker as C20 (PBN pitch). No sales numbers; view counts are his own.
Thesis (3 bullets max)
Avatar-only AI videos mostly flop (most get 19–27 views) and even when they reach people they don't build trust or sales; successful AI channels are dropping avatars.
The useful version is a hands-off engine that makes screen-recording + B-roll videos with a cloned voice and only seconds of avatar, aimed at Google AI Overviews rather than virality.
Only make a video where Google already shows YouTube in the AI Overview for that query; then write the title, first line and description as the answer Google already gives.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Output | ~170 videos uploaded since July 2026; peak 15 a day | his AI channel | self | spoken | self-reported |
| Views | most videos 19–27 views; ~10% "take off"; best example 1,400 views | same channel | self | spoken | no distribution shown |
| Cost per video | $12 and ~2 hours each at first; ~$4 after switching B-roll from Google Veo to Kling 2.5; later "$8", then "$5–10" | his runs | self | spoken; slide 02 gives unit costs (HeyGen lip-sync "about $3.50"; Veo "$0.12 a second, Kling cheaper"; Fish Audio "pennies per video") | spoken figures conflict; slide unit costs clear |
| YouTube API quota | ~1,600 of the 10,000 daily YouTube Data API quota units per upload | per video | self | slide 04 | clear; 1,600 units is the standard upload cost (general knowledge, not looked up) |
| Speech rate | 2.8 words a second, measured from his own voice | his voice | self | slide 05 | clear |
| AI-avatar channel research | very few successful AI-avatar channels; many successful AI channels removed their avatars | scraping study; no counts | self | spoken | no numbers |
| YouTube in AI Overviews by niche | YouTube cited in AIO for roofing, welding, HVAC, how-to and (UK) iGaming queries; none for local "plumber in [town]", legal, accounting, dental | "thousands of searches" via DataForSEO; no counts per niche | self | spoken | direction only |
| Vanity Short | "Stewart Vickers SEO Jesus is the sexiest SEO in the world" Short ranked #2 within 24 hours | one self-named query | self | spoken | one example, no competition |
| ⭐ Invented-term video in Google's AI answer | video "How To Rank In AI Search in 2026 (The A-S-S Method)", 8:53, channel "Stewart Vickers AI", shown inside a Google AI answer "2 hours ago" next to Neil Patel, Henry Purchase and Ahrefs sources | one screenshot; the exact query is not visible | self | slide 08 | real screenshot; one query, one moment, persistence unknown; the term was invented the night before, so there was no competing source for it |
| Other AIO "tests" | "best AI visibility source" (an older video) and a joke query heard as "horse special rating 2026" also appeared in AI Overviews | none | self | spoken | anecdotes |
Asserted mechanisms (no evidence given in the talk)
YouTube overtook Reddit as an AI Overview source in "early September" because Google owns it.
If YouTube is not already cited in the AI Overview for a query, a new video will probably not be cited either.
Watch time is decided in the first minute; opening on voice + B-roll or screen share instead of an avatar face improves it.
The video description works like a parasite page: Google reads it, so it should be a long-form article mirroring the AI Overview's structure.
Syndicating the script to ~400 podcast sites spreads "semantic triples" across the web as corroborating evidence.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Pre-check:
Pull thousands of target queries through DataForSEO and keep only those where the AI Overview already cites YouTube. WHITE Eight-stage engine (slide 01):
Research: reads only the source pages it is given ("no sources, no video"). WHITE
Script: title written first; the hook pays it off inside 30 seconds. Title = search phrase word for word; first sentence = the answer, "same claims, same names, same order as the answer Google already gives"; headline answer by 2:00, strongest proof before 3:00; 2.8 words a second; [SCREEN] [BROLL] [ON-SCREEN TEXT] markers become the shot list; "every claim gets a receipt": a line that can't be shown on a real page is rewritten or cut. WHITE
Recording: Playwright + Chromium films each source page with a humanized cursor, through an Oxylabs static ISP proxy so pages "see a person, not a server". GREY (proxy to evade bot walls)
Voice and avatar: cloned voice (Fish Audio) reads the whole script; HeyGen v3 audio-driven lip-sync only for the seconds he is on screen (~$3.50). GREY (synthetic presenter; he sets YouTube's synthetic-media flag on upload)
B-roll: generated physical scenes cached by concept (Google Veo 3.1 at $0.12/second, or Kling 2.5 via fal.ai; stock footage as fallback); text cards rendered as HTML. WHITE
Render: shots placed where the words are spoken (OpenAI Whisper word timestamps). WHITE
Checks that "fail closed" (slide 06): black/frozen frames, duration contract, text cards under a quarter of runtime; loudness normalized to −14 LUFS with peaks capped; final audio transcribed and checked against a pronunciation list and a blocklist; sampled frames sent to a vision model for CAPTCHAs, blank pages, brand-safety terms, visible IPs; too few real pages on screen is a hard fail; the upload step re-runs every check. WHITE
Publish: YouTube Data API v3 (upload, custom thumbnail from real face crops, own caption track, synthetic-media flag; pinned comments and title tests stay manual); YouTube Analytics API daily scorecard (search vs browse traffic, retention) feeds the next script; Transistor turns each video into a podcast episode page with the full transcript; RocketIndexer pings it for same-day crawling; Slack gets run reports and failures; Skool posts are staged for a human; LinkedIn, Meta and X posting exist but are switched off. WHITE for one transcript page; GREY for scaled syndication + paid indexing Description (slide 07, "the part Google actually reads"):
Title: search phrase word for word, then year and method. Line one: the answer in one or two sentences, every entity named before any pronoun. TL;DR + steps: one definition per line, then Step 1, Step 2, each a sentence that stands alone. Chapters: one per step, so Google has a timestamp to cite. FAQ: three or four questions phrased the way people type them into an assistant. Three surfaces: the video, its own uploaded captions, and a podcast page carrying the full transcript. WHITE Running cost control:
Run Claude Code CLI as claude -p on two $200/month Max subscriptions with the API key "deliberately empty" instead of paying API rates (~$3,000/month). GREY (check the subscription terms for unattended automated use before copying)
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Claude Code CLI on Claude Max ($200/month each, two seats): research, script, shot list, packaging, frame review.
Playwright + Chromium: screen recordings with a humanized cursor; renders HTML text cards.
Oxylabs ISP proxy: static residential IP for the recording browser.
Fish Audio: voice clone; "best by a long way" in his comparison against ElevenLabs; cheaper.
OpenAI Whisper: word timestamps; transcript QA; "about [n] cents" on the final mix (number blurred on slide 02).
HeyGen v3: audio-driven lip-sync, ~$3.50 a video.
Google Veo 3.1 ($0.12/second) and Kling 2.5 (cheaper) via fal.ai (one API key and balance for several video models); stock as fallback.
OpenAI gpt-image + FFmpeg: thumbnails from real face crops; text composited; OCR-checked.
YouTube Data API v3; YouTube Analytics API.
Transistor (podcast host; "~400 podcast websites"); RocketIndexer (indexing pings); Slack.
DataForSEO: AI Overview source check at scale. Ahrefs: his older manual method (video-carousel filter).
Synthesia and "HeyGen" one-shot avatar videos: tried and rejected as unconvincing.
People: Matt Diggity (joke), an attendee named "Milan" (impressed by the B-roll), the SEO Domains Mastery Summit in Bulgaria (where the "ASS metric" joke was invented).
Slide photos
Full text of each slide: ../resources/seo-jesus/slide-text.md
01-eight-stages-pipeline.jpg: "Eight stages, each one saves its work": Research · Script · Recording · Voice and avatar · B-roll · Render · Checks · Publish. Lower row partly blocked by audience phones (stage 7 and 8 text partly unreadable).
02-what-makes-the-video-apis.jpg: "Every API in the workflow, part one / What makes the video": Claude Code CLI (claude -p on the subscription, API key empty), Playwright + Chromium, Oxylabs ISP proxy, Fish Audio, OpenAI Whisper (cost blurred), HeyGen v3 (~$3.50), Google Veo 3.1 / fal.ai Kling 2.5 (Veo $0.12 a second), OpenAI gpt-image + FFmpeg. Bottom edge partly blocked.
03-what-publishes-apis.jpg: first shot of "part two / What publishes"; left half blocked by a phone. Superseded by 04.
04-what-publishes-apis-readable.jpg: readable: YouTube Data API v3 (~1,600 of 10,000 daily quota units per video; can't pin comments or run title tests), YouTube Analytics API (daily scorecard: search vs browse, retention), Transistor + RocketIndexer (podcast episode page with full transcript, pinged same day), Slack (reports; Skool posts staged for a human; LinkedIn, Meta, X switched off).
05-script-rules-answer-first.jpg: "The script rules that matter for being cited / Answer first. Proof by three minutes": title first, first sentence = the answer, headline answer by 2:00, 2.8 words a second, markers drive the shots, every claim gets a receipt.
06-quality-checks-fails-closed.jpg: "Before anything uploads / It checks itself, and fails closed": Picture, Sound (−14 LUFS), Words (pronunciation list, blocklist), Frames (vision model), Receipts (hard fail), Upload re-checks.
07-description-is-a-quotable-page.jpg: "The part Google actually reads / The description is a quotable page": Title, Line one, TL;DR + steps, Chapters, FAQ, Three surfaces.
08-ai-overview-ass-method-video-cited.jpg: screenshot of a Google AI answer ("3. Build Multi-Platform Trust…") embedding his video "How To Rank In AI Search in 2026 (The A-S-S Method)", 8:53, "2 hours ago", YouTube · Stewart Vickers AI; side panel shows Henry Purchase and Neil Patel YouTube videos and an Ahrefs article. Whether it is an AI Overview or AI Mode is not visible.
Q&A (question → answer)
None. He ran out of time ("I'll get to the chase"); the host moved to lunch announcements.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
Speaker name: "Stuart Vickers" in the summary; the slide shows "Stewart Vickers AI".
"Reduced to ~$4–5 per video" smooths over conflicting spoken figures ($12 → ~$4, then "$8", then "$5–10"); the slide gives unit costs, not a total.
"Avatar used sparingly and overlaid on the voice track (not generated directly)": the slide says the cloned voice reads the whole script and HeyGen lip-sync is rendered only for the seconds he is on screen.
Tech stack omits HeyGen, Google Veo, YouTube Analytics API and the fail-closed QA list (slides 02, 04, 06).
"Photograph the workflow slides and save to Dropbox" under Next Steps is the speaker telling the audience to photograph his slides, not an agreed action.
"Ranked in AI Overviews the next day" for the ASS method: the screenshot shows the video in a Google AI answer two hours after upload; the term was invented that night, so there was no competition.
Omits that he sets YouTube's synthetic-media flag and keeps title tests and pinned comments manual.
The private-notes bullets (don't show the avatar first, check AI Overviews, Oxylabs, Fish Audio, fal.ai, YouTube API) are the note-taker's; they match the talk.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
Total cost per video (three different spoken figures).
The query behind the slide 08 screenshot, and whether the video stayed in the answer.
"Horse special rating 2026" (garbled joke query).
Whisper cost on slide 02 is blurred.
Whether running claude -p unattended on Max subscriptions is within Anthropic's terms: not checked.
Agreement with prior evidence: the earlier measurement that AI-avatar video earned zero AI citations still stands. His own channel data agrees: avatar videos mostly flop and don't convert, and successful channels are dropping avatars. The one apparent counter-example (slide 08) is a mostly screen-recorded video, on a term he invented that night, in one screenshot. It does not show avatar video earning citations on queries with competition.
Link Building Is Dead, Long Live the Resurrection Network — Stewart Vickers, "SEO Jesus" (link-building agency owner, 5 years; runs the "Resurrection Network")
Source: Granola https://notes.granola.ai/d/384f5b74-0df7-4741-a768-117777f18588 · recorded 2026-11-13 (13:01 GMT+7; Granola shows 2026-11-12 22:01 PST), CMSEO 2026 · transcript-verified 2026-11-16 Resources: no slide photos attached to the Granola note (0 saved). Booking URL from the QR code, as written in the note-taker's private notes: https://seojesus.com/resurrection-network/ (UTM-tagged; not opened). Vendor talk? ⚠️ Yes. The talk is a pitch for his expired-domain network (placements via portal, API and MCP), "clickbomb" amplification, consulting, and a "5,000-domain iGaming SEO SOP playbook"; it ends on "scan the QR code and book a call". No client results shown.
Same speaker as C26 (2026-11-14): both talks open with the Bali swing photo and the "second sexiest SEO after Matt Diggity" joke, and the C26 slide shows his YouTube channel as "Stewart Vickers AI". The audio here says "Stuart Vic…". Spelling follows the slide.
The recording appears to start after his introduction (first words are mid-argument). No Q&A ("come and find me").
Thesis (3 bullets max)
On-page and technical SEO are now solved by AI tooling; backlinks (and brand mentions for AI search) are the last real battleground, "back to 2008".
Guest-post outreach can't be automated (every placement is an edge case) and its metrics are gamed (DR inflation, spoofed traffic, link farms), so the webmaster holds the margin.
Own the links instead: buy expired domains for their underlying editorial links, publish on them agentically, and boost each placement with bought "viral" traffic.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Guest-post price drift | ~$30–50 per link before the Sept 2023 Helpful Content Update; a "$100 special deal" quote now | his outreach; dates of quotes not given | self | spoken | anecdote |
| Gamed traffic metric | a site showing 1,400 monthly traffic worth $56 | one site | self (Ahrefs) | spoken | one example |
| Keyword-tool spoofing | he pushed "6,000 searches a month" into Ahrefs for a vanity query about himself | one query | self | spoken | anecdote; method not described |
| Expired-domain value | an Indonesian expired domain bought for "a couple hundred dollars", DR 20, carrying 7 Ahrefs "best links" he values at "thousands" | one domain | self | spoken | one example; the valuation is his |
| Clickbomb decay | viral-traffic ranking boost ~20–30% weaker after Google patches "in the last few months" | none | self | spoken | unbased |
| Auction tracking | 5,000 expired domains traced; individual operators spent ~$500k on domains | his tracking agent; mostly iGaming | self | spoken | self-reported |
Asserted mechanisms (no evidence given in the talk)
AI search visibility is built the same way as 2008 rankings: mass links and mentions ("corroboration").
The value of an expired domain is its individual editorial links (Ahrefs "best links": dofollow, in-content, from real domains with DR and traffic), not its brandability or DR.
Link power is diluted across every outbound link a link farm sells.
Viral traffic now works mainly by "powering up" placed links rather than ranking pages directly.
CTR and autosuggest manipulation inflate brand search volumes in keyword tools, which then attract more content about the brand.
"Indonesian expired domains are powerful" (he declined to say why on the recording).
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Watch domain auctions and the SERPs where canonical-abuse / expired-domain plays rank (iGaming), weekly; record which domain types win. GREY as research, BLACK as the play it feeds
Score candidate domains on: Ahrefs "best links" count, LLM citations of the domain, harmonic centrality from Common Crawl, current keyword traffic. Ignore DR and brandability. GREY (the scoring is neutral; the purpose is a PBN)
Buy (Claude finds candidates; ~$200 a domain in his example). BLACK
Publish guest posts on the network agentically: write, place, index, add to the homepage blogroll. BLACK
Sell access through a portal, an API and an MCP server ("place five backlinks a week on this site"); proof returned via API; network domains hidden but "findable if you're smart". BLACK
Optional: send a blast of viral traffic to each placed post; to launch a site fast, place 10–20 posts and click-bomb them all; register 10 exact-match domains through the Namecheap API by voice note. BLACK
In iGaming, keep spare domains to redirect power after DMCA, negative SEO or regulator takedowns. BLACK
What he says to stop doing:
Do not buy on "DR 30+, traffic 1,000+" rules; check what the traffic is (keyword value, branded spoofing) and how many sites the host already links to. WHITE (this is a vetting rule)
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Resurrection Network (seojesus.com/resurrection-network): his expired-domain placement network; portal, API and MCP access. No price given.
"5,000-domain iGaming SEO SOP playbook" and strategy consulting: sold via the QR booking page.
Ahrefs "Best links" filter: his main domain-scoring filter.
Common Crawl harmonic centrality: domain authority signal he uses.
Claude (Code): domain finding and the publishing workflow; Namecheap API for registration.
"Grokbot": named as a tool that builds a "perfect SEO website in an hour" on Cloudflare / Vercel (speech-recognition spelling; not identified).
"Fable 5.2": named as the model generation where agents finally handle outreach edge cases (as heard).
Matt Diggity: the "sexiest SEO" joke.
"Batman News": a former site cited as a public canonical-abuse case.
Peter Drucker: misattributed quote (the "when a measure becomes a target" line is Goodhart's law).
Slide photos
None attached to the Granola note. He mentions a missing slide mid-talk ("I'm missing the slide, I think").
Q&A (question → answer)
None. He ended with "I'm too burnt out to do back and forth" and invited people to find him.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
Speaker name missing; the summary calls him only "SEO Jesus". Name from C26's slide: Stewart Vickers.
"YouTube videos ranking well in AI Overviews, cited as proof the fundamentals hold" overstates a joke in his bio (the Bali swing video).
Presents the Resurrection Network neutrally; omits that it is a PBN by his own words ("yes, we're talking about PBNs, but a fancy high-quality PBN") and that the talk is a sales pitch.
"Full agentic workflow" and "API + MCP layer" are described, but no results, client counts or ranking data were shown.
The booking URL in the summary comes from the note-taker's private notes (the QR), not from the audio.
Omits his Goodhart's-law point on DR and traffic, which is the one reusable vetting idea.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
Spelling "Stewart" (C26 slide) vs "Stuart" (audio, Granola). No web lookup done.
"Grokbot" and "Fable 5.2" as named tools or models.
The 20–30% clickbomb decline has no base.
Whether the recording missed an opening section (it starts mid-sentence).
SEO tactics for 2026 (15 tips) — Leo "Peuthevin" (spelling garbled in transcript), founder of Linky Vista and Astrak
Source: Granola https://notes.granola.ai/d/37d407ba-36cd-4892-bc01-5b4d555ba4ed · recorded 2026-11-10 · transcript-verified 2026-11-12 Vendor talk? Yes. Speaker says he founded Linky Vista (backlink marketplace) and Astrak (SEO + AIO agency). He also sells backlinks (admitted in Q&A). 10+ years in gambling affiliate SEO, claims about 1M EUR spent on backlinks, lives in Chiang Mai. Self-described "more in the black hat area". Slides carry white-hat / black-hat labels; tips 4, 12, 13 are labeled BLACK HAT, tip 15 WHITE HAT. A slide footnote credits "Romain Pirotte" for micro-task costs (name as seen on slide photo).
Thesis (3 bullets max)
Backlinks still produce the biggest organic gains; buy on Ahrefs traffic value + top-3 keyword count, and on topical relevance measured from SERP data, not DR.
For AI citations, the main lever is placement in many niche, low-competition listicles, plus EMDs, Trustpilot and Maps reviews, old forums, LinkedIn articles and YouTube.
Claude Code is the operations layer: briefs micro-workers, buys links (API or browser), and logs/analyzes tests at scale.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| besthrsoftware.io (new EMD, built with Claude Code) earned AI citations | 190 citations | "few prompts", 90 days, site did not exist in March/April | speaker's own agency (tracker not named) | spoken | transcript clear on 190 and 90 days; prompt set size not stated |
| 6 cheap listicles for "best SEO agency for industrial companies" | cost 300 EUR total; at least one lead | no period given | speaker | spoken | partly garbled: sentence about AI mention rate reads "zero for 95%..." (unintelligible); "wine plans / one leads at least" garbled, read as at least one lead |
| Listicle inclusion odds | 1 listicle = low chance; 4+ = high chance | "some studies", unnamed | third-party unnamed | spoken | clear but source unnamed |
| Link Finder example site | 200+ keywords matching client targets, best price per keyword | 1 example (a site on the client's HR software niche) | Link Finder (his own marketplace tool) | spoken | clear |
| Programmatic pages for CBD wholesale client | 500 pages, 6 languages, 10-20 leads/month | no period, 1 client, old established site | speaker/client | spoken | clear |
| Claude Code bought 4 listicles | about 150 EUR, 5 seconds, 12 EUR credits | 1 case | speaker's team | spoken | clear |
| YouTube video example | 1,500 views; video dates from 2025 | 1 video | speaker | spoken | clear; "650 different cities coming from YouTube" is garbled (likely 650 citations from YouTube in a study; unverified) |
| Emirates scam numbers in Google AI Overview | 2 victims lost a bit over US$1,000 each | 1 story | secondhand, unnamed | spoken | clear, source not named |
| Expired GMB domains, pest control | 90+ domains, about 10 USD each (registrar fee) | one search on GMB Premium | speaker | spoken | clear |
| Micro-worker quality | about 50% do it correctly; send to 100 workers | speaker experience | speaker | spoken | clear |
| Amazon MTurk closed | 2026-09-30 | n/a | n/a | slide says Sept 30, 2026; speaker says "one month ago" | clear |
| Subdomain+canonical trick stopped working | "about a month" before talk | gambling SERPs | speaker | spoken | clear |
| New-site publishing pace | 1-2/day then 2-3/day | advice, not measured | speaker | spoken | clear |
Asserted mechanisms (no evidence given in the talk)
DR is a faked metric because sellers pump it (Fiverr "raise DR to 74 for 100 bucks"); traffic value is "not perfect" but includes keyword competitiveness.
Top-3 keyword count signals a site that ranks decently across many keywords.
GBP-linked expired domains get a ranking boost in local and "even in other areas" since 2024 (no data).
Subdomain + canonical to root works "nobody really knows why", also with hreflang and AMP (slide: canonical root->subdomain, hreflang subdomain as alternate, AMP subdomain as AMP). Needs a mobile-heavy market for AMP.
AI picks which sources to open from title, meta description, URL and domain, so exact-match domains are favored.
AI Trustpilot lookups dig into review text for specific attributes (delivery speed etc.).
Ask Maps (Gemini) recommends dishes/services based on phrases repeated in reviews.
AI weights forum content above freshness (a 2014 forum page still appears in answers).
LinkedIn articles are trusted by AI; YouTube is a major AI source.
Old, brand-searched sites can publish programmatic pages aggressively; new sites cannot.
Rented sub-folders/bought media explain current gambling rankings (inferred from design and menu signals, not proven).
Tactics and how-to steps (in order, with tools and prices)
Tip numbers: 1-4, 8-9, 12-13, 15 are stated or on slides. 5, 6, 10, 11, 14 are inferred by order (see Unclear).
Tip 1, Buy links on traffic value, not DR. WHITE. Use Ahrefs traffic value (spoken as "iHref"/"eye traff") plus count of top-3 keywords.
Tip 2, Topical relevance process. WHITE.
Connect Claude Code to Search Console and the client site; pull about 500 target keywords.
Use DataForSEO API to scrape top 30 results for those 500 keywords.
Rank sites by how many of the keywords they appear for.
Check which of those sites are on backlink marketplaces via Link Finder API; pick best price per keyword (not cheapest, not priciest).
Tip 3, Expired domains with an active Google Business Profile via GMB Premium (GMBPremium.com). GREY. About 10 USD per domain (registrar fee). Claim the GBP after purchase. Use for pest control-type lead-gen rank-and-rent. Q&A bypasses (see Q&A) are BLACK.
Tip 4, Expired authority domain + subdomain with content + canonical from root to subdomain (also hreflang, AMP variants). BLACK-HAT. Speaker says it worked all year in gambling and stopped about a month ago.
Tip 5 (inferred), Gambling: what works now = bought or rented media (Game Reactor DK bought by affiliate; ghanaweb.com rented subfolder). BLACK/GREY. Test: gambling on homepage suggests full buy; weird sub-menu and old design suggests rented folder.
Tip 6 (inferred), Listicles. GREY (paid placements). Get into 4+ listicles; target low-competition niche variants ("best SEO agency for industrial companies", company-size angle) because AI fan-out carries user context. Combine with step 2 to find sites; buy placements at once.
Tip 7, EMD: best[category]software.io type site, built with Claude Code. WHITE/GREY. Evidence: besthrsoftware.io example.
Tip 8, Trustpilot. Review gating (email, 1-3 stars to support, 4-5 to Trustpilot) is illegal in some jurisdictions (speaker). Buying reviews: GREY/BLACK (fake reviews). Speaker says doable and he did it, vendors scam often, go slow, test many, do not test on your own profile or a competitor's. Private note says about 20 EUR each (not in transcript).
Tip 9, Google Maps reviews. Ask for reviews that read like sales pitches naming the signature dish/advantage and keywords. WHITE. Buying reviews: BLACK-HAT (speaker advises against, did it as research, killed some of his own listings).
Tip 10 (inferred), Relaunch expired forums; use AI to simulate posting cadence and natural time gaps. BLACK-HAT (fake activity).
Tip 11 (inferred), Monthly check of what AI says about your business: phone, email, pricing, positioning; fix with fresh posts; legal removal (DMCA-type) for scam impersonation. WHITE.
Tip 12, LinkedIn articles at scale via micro-workers. BLACK-HAT (account farming/astroturf).
Build a task sheet with article variants (e.g., top 5 iGaming SEO agencies).
Workers log into their own LinkedIn and publish as an article.
Expect about 50% correct; send to 100 workers.
Platforms (slide): Microworkers (millions of workers), Hitworkers (tasks from Claude Code), Clickworker (big German crowd).
Tip 13, YouTube. BLACK-HAT. (1) Buy old Gmail / YouTube channels for "a few dollars" (slide); (2) make AI videos with Claude Code + Opus 5.5 (slide), ElevenLabs voice-over; (3) workers for CTR and watch time.
Tip 14 (inferred), Programmatic SEO. WHITE/GREY. Old, brand-searched site: aggressive OK. New site: 1-2 pages/day, then 2-3/day.
Tip 15, Claude Code briefs, buys, watches. WHITE per slide (slide says Brief = micro-worker tasks, Buy = links by API or in-browser, Watch = every test). Browser mode lets Claude Code operate a marketplace UI.
Tools, vendors, people and URLs named
Ahrefs (traffic value; spoken "iHref"); DataForSEO API (SERP scrape); Link Finder (marketplace API; speaker's own); Linky Vista (speaker's backlink marketplace); Astrak (his agency); GMB Premium / GMBPremium.com (expired domains with GBP, about 10 USD each).
Claude Code (SEO ops, browser mode); Opus 5.5 (slide); ElevenLabs (voice-over; spoken "11 maps").
Trustpilot; Google Maps "Ask Maps" (Gemini); Fiverr (DR gig example).
Microworkers, Hitworkers, Clickworker, Amazon MTurk (closed 2026-09-30).
Examples: besthrsoftware.io, bestcbdshop... (regulated domain, garbled; ranks "best CBD shop" in France), Game Reactor (DK), ghanaweb.com.
Earlier speaker "Michael" referenced (topic overlap on DR); Romain Pirotte (slide credit). "SEO JS" credited with a Claude Code insight (garbled name).
Speaker LinkedIn shown on final slide; not read out.
Slide photos
Full text of each slide: ../resources/seo-tactics-2026/slide-text.md
01-tip15-white-hat-claude-code-briefs-buys-watches.jpg: "Claude Code briefs, buys and watches." White hat, tip 15/15. Three cards: Brief (micro-worker tasks), Buy (links, by API or in-browser), Watch (every test). Readable.
02-tip13-black-hat-old-channels-ai-videos-workers.jpg: "How: old channels, AI videos, workers." Black hat, tip 13/15. Three steps: old channels (a few dollars), AI videos (Claude Code + Opus 5.5), workers (CTR, watch time). Footnote credits micro-task costs to Romain Pirotte; its first word is hidden by the speaker. Partly hidden.
03-tip12-black-hat-where-to-find-micro-workers.jpg: "Where to find micro-workers." Black hat, tip 12/15. Microworkers (millions of workers), Hitworkers (tasks from Claude Code), Clickworker (big crowd, German); Amazon MTurk was the original and closed on Sept 30, 2026. Readable (two letters of the bottom line hidden by the speaker).
04-tip04-black-hat-canonical-hreflang-amp-subdomain.jpg: "hreflang and AMP send the same signal." Black hat, tip 04/15. canonical: root to subdomain; hreflang: subdomain as alternate; AMP: subdomain as AMP. Readable.
Q&A (question -> answer)
Other niches for expired domains besides gaming media? -> Sports, video games, board games media work; closer to gambling is best.
Verifying GBPs with virtual addresses? -> Many ways: short looping AI-generated verification videos (early days), strong or natural-behavior accounts skip verification, high-level Local Guide account in same area is the easiest. BLACK-HAT.
Rank GLP-1/ozempic reselling site (US gray area)? -> No known site; will experiment; compares to CBD niche; DM him.
Top 3 tactics for ROI / scale? -> Listicles (about 90% of his AI work) found via the tip 2 process. Local lead-gen is hard after the latest local update; free/expired GMB profiles are doable; can claim a GBP on an EMD if a Workspace account is tied to the domain (claimed without verification). No scalable local process.
Secret-sauce supplier request -> will share via DM; says current tactics last about 2 months.
Top 3 automations for 1000 sites? -> Questions the premise; content is now free, backlinks cost money and automation there underdelivers; technical already fine; dislikes site networks; sell listicle positions; social discoverability would be the big unlock but hard to automate.
Biggest organic traffic increase? -> Buying backlinks (admits he sells them); content is solved with Surfer/writer APIs.
Correct wrong AI info? -> Check cited sources; scam sources via legal/DMCA tools (needs legal team); stale info via fresh posts on fresh platforms.
Highest-paying niche for black hat? -> iGaming; crypto second; non-regulated iGaming "more money but fully legal so do not do it" (garbled/sarcastic).
Corrections to the Granola summary
20 EUR per Trustpilot review is NOT in the transcript; it comes from the user's private notes. Speaker gave no price.
Summary says Tip 13 example "generating strong AI citations": transcript only says a 1,500-view, 2025 video is an example; the 650 figure is garbled.
Summary "6 listicles cost about 300 EUR, already generating leads": speaker said at least one lead; AI-mention metric garbled.
"Hitworkers (tasks from Claude Code)" and "Clickworker (large German crowd)" come from the slide; transcript is garbled around them.
Summary calls MTurk closing "September 30, 2026" (slide); speaker said "one month ago". Both consistent.
Summary treats Opus 5.5 as spoken; it is on slide 13 (transcript: "Glutecon and Office 5 5", garbled).
Summary leaves out: speaker identity (Leo, Linky Vista/Astrak, vendor conflict), that he sells backlinks, review-gating illegality warning, tip-5 gambling bought/rented-media section, the Q&A (GBP verification bypass, EMD+Workspace GBP claim, local-is-hard), Emirates victims figure, AMP caveat (mobile market).
Summary says tip numbers only for 4, 13, 15; others reconstructed here.
Summary frames tip 15 as plain how-to; slide labels it WHITE HAT, whereas tips 4, 12, 13 are BLACK HAT.
Summary says Google Maps reviews "can get listings killed"; speaker said it killed some of his own listings.
Unclear / needs verification
Speaker surname spelling ("Peuthevin"); company names Linky Vista, Astrak (heard once each).
Which tip number is listicles (5 or 6), gambling-now section, forums (10), AI monitoring (11), programmatic (14): inferred from "tip number seven" EMD, "8", "9", "12", "13", "15".
Listicle study (4+ listicles) not named.
"650 ... from YouTube" figure; "zero for 95%" AI-mention line.
Whether besthrsoftware.io prompt tracker was Ahrefs/other; "few prompts" is small.
Exact bestcbdshop domain (regulated domain) is garbled.
Who "Michael" is (earlier speaker).
SEO Testing Panel — Kyle Roof (Page Optimizer Pro), Kasra Dash (Mastermind organizer), David Quaid; moderator heard as "Neil"
Source: Granola https://notes.granola.ai/d/fd788f36-a753-479f-9fc7-011d021abf6c · recorded 2026-11-12 23:13 PST = 2026-11-13 14:13 GMT+7, Chiang Mai SEO main stage · transcript-verified 2026-11-16 (full transcript read, 59,917 chars) Resources: none. No photos attached to the Granola note; no handout or deck. Vendor talk? ⚠️ Partly. Kyle Roof's one dataset comes from his own tool (Page Optimizer Pro) and its own score. Kasra Dash runs events and buys mention placements from Giga Links (he names them). David Quaid runs a small agency. No product was pitched from the stage; the host plugged next year's tickets.
Speaker labels in the transcript are stable for the panel: B = Kyle Roof ("Kel"/"Kyle"; lives in Chiang Mai; Page Optimizer Pro), C = Kasra Dash (addressed as "Kasra"/"Kosra"; organizes the Mastermind; met his wife at Chiang Mai SEO), D = David Quaid (named by Kasra; "Dennis Quaid" name collision; Microsoft UK and Ireland contract; King of AEO entrant), A = moderator. Attribution below follows those labels.
Thesis (3 bullets max)
A good test isolates one variable, is repeated, is retested over time, and tests the reverse direction too (Roof, Kasra, Quaid each gave one of these).
Links still work; what sits around the link (the placement's text, relevance, brand mentions) now matters as much as the link itself.
LLMs are force multipliers for people who already know SEO; used alone for diagnostics or strategy they mislead.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| First-run LLM content quality (Roof) | average tool score ~40; "pages get moving around 80"; >60% lack the keyword in title or H1; needed length ~2,000 words vs ~1,500 delivered; "about half" missing schema; all missing contextual terms | 11,000 pages on their first run through Page Optimizer Pro, this year | Kyle Roof, his own tool and score | spoken | vendor tool metric; assumes the pages are AI-written ("at least one in two"), not verified |
| Paid search → organic (Quaid) | ~180,000 search impressions a day; site ranked organically for terms worth "1 million clicks a week" within ~60 days | one Malaysian campaign asking people to search brand + generic term | David Quaid | spoken | one case, no control; part of the sentence is garbled ("popular background tool") |
| Arguing with AI from logged-in accounts (Kasra) | cited "within 24, 48 hours" | none given | Kasra Dash | spoken | no sample, engine or prompt count |
| Rater Hub visits (Kasra, from his 2023 talk) | ~90% of sites showing Rater Hub visits in GA tanked | not given | Kasra Dash | spoken | recalled, no base |
| About Us page traffic (Quaid) | 4 About Us visits in the last month at ~500,000 visits/month | KEMP (former company), 12 months of data | David Quaid | spoken | anecdote; the KEMP rebrand ($1M, 19 people, sold for $52.4M) is self-reported |
| Agency capacity (Quaid) | could take 5–6× the clients with the same team because of AI | his agency | David Quaid | spoken | estimate |
| Knowledge panels in progress (Kasra) | "about 70" | his agency | Kasra Dash | spoken | count only |
Asserted mechanisms (no evidence given in the talk)
Citations in AI answers work like "high-powered guest posts" (Roof).
Google measures site popularity by branded search volume; a brand searched 5,000 times beats one searched 1,000 times (Kasra, referencing a Google leak).
LLMs and Bing lean toward low-competition indexes, so sites with no backlinks get cited (Quaid).
ChatGPT, Bing, Yandex, Baidu have been reverse-engineering Google for years; PageRank "won't get any better", context and relevance decide (Quaid).
Google rewards "visual semantics": the page format users want (a 50-word calculator page outranking long articles) (Kasra).
"Natural link profile" is a security blanket; the real use is catching bad actors (Quaid, Roof).
Google will not make value judgments on expertise; EEAT signals matter only to prove a real business and a real person (Roof); Quaid goes further: EEAT is a safety blanket except for YMYL sites likely to see a quality rater.
When Google tests a new SERP feature it reads schema first (Roof).
LLMs keep sending traffic back through SEO because they use search to find answers (Quaid).
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
What a good test looks like:
Build near-identical pages, remove every variable but one, see if it is a ranking factor, then pit factors against each other; repeat the test (Roof). WHITE
Retest old beliefs; some things that worked 12 months ago no longer do, and the reverse (Kasra). WHITE
Test the corollary: if adding X helps, check whether removing it hurts; one direction only is confirmation bias (Quaid). WHITE
Named tests of the year: 4. Logged-in accounts argue with ChatGPT for a brand, giving a reason (a case study) rather than an assertion (Kasra). BLACK/GREY (he calls it that himself; coordinated fake-user steering) 5. Ad campaign asking people to search brand + generic term to lift organic ranking (Quaid). GREY 6. Audit first-run LLM drafts for keyword in title/H1, length vs competitors, schema and contextual terms before publishing (Roof). WHITE
Links and anchors: 7. Write real content for the placement itself; no content tool optimizes guest-post or PBN text (Kasra; he invites SaaS builders to make one). WHITE for the content; the PBN use is BLACK 8. Build relevance through the story, e.g. a gardening company's head of SEO attended the conference, so a gardening site links to it (Kasra). GREY if the placement is paid 9. Anchors: new domain heavy on brand, then 1–2 exact-match links to a page sitting around position 5, plus internal links from the homepage (Kasra). Use the full page title as anchor to get a partial match plus context (Roof). Quaid still uses exact match, sparingly. GREY (exact-match on paid links) 10. Tier 2 links only to get spammy links indexed; Kasra now buys unlinked brand mentions from Giga Links for "consensus". GREY
Core update recovery (Kasra, then Roof): 11. Check GA4 for Rater Hub referral visits. WHITE 12. Ahrefs Keywords Explorer → dropped keyword → page history chart, to see competitor on-page or link changes. WHITE 13. GSC site-wide: the page that dropped may not be the page that was hit. WHITE 14. Benchmarks per page type: term counts, page sizes, page types ranking before vs after (e.g. long articles replaced by category pages). If on-page looks the same, look off-page. WHITE 15. Compare the visual format of what now ranks (calculators, forms) with yours. WHITE 16. Hold more than one domain as a hedge against penalties or an accidental noindex (Quaid; the moderator does the same across affiliate sites). WHITE for own projects 17. On a hit domain: 301 to a new URL with a new slug (Roof says the same slug carried the problem back after ~3 months); the moderator canonicalized one broad domain to several narrower ones. GREY
Measuring AI visibility: 18. Tools: Peec AI (heard "PETE"/"Peak") and "Radar Kit" (Kasra); Microsoft Clarity for its ChatGPT/Copilot referral data (Quaid); multiple brand prompts across the spectrum (Roof). WHITE 19. Train sales staff to ask "how did you hear about us?" on calls, not only on forms (Kasra). WHITE
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Page Optimizer Pro: Roof's tool; score where ~80 is the threshold. No price.
Peec AI (speech-recognition "PETE"/"Peak"), Radar Kit: AI visibility tracking (Kasra). Spelling of Radar Kit unverified.
Microsoft Clarity: Copilot/ChatGPT data (Quaid).
Ahrefs Keywords Explorer page history: core-update diagnosis.
Giga Links: Kasra buys unlinked brand mentions there.
James Dooley: named twice (YMYL example; ran 27,000 searches a day to fix a name panel); "JB's talk" (a client knocked out of #1 by adding too much information, garbled).
Barry Schwartz (heard "Baron Schwartz"): Quaid quoted his disavow statements back at a Googler on Reddit.
King of AEO competition: Quaid says Bing refuses to index his entry site.
No URLs, no prices.
Q&A (question → answer)
How important are author and team profiles? → Quaid: outside YMYL, a safety blanket; test without them. Kasra: they help conversion and trust, not SEO. Quaid agreed (the 4-visit About Us figure).
Tier 2 link building? → Kasra: only to index spammy links; he now buys mentions without links.
Lightning round, most expensive belief: "AI can do your SEO" (Roof) · "you need expensive backlinks; PBNs are enough" (Kasra) · over-producing pages nobody reads, ship a minimum viable page (Quaid).
Where not to use AI: final client communication (Roof) · auto LinkedIn replies (Kasra) · diagnostics you cannot check yourself (Quaid).
Agree/disagree "tracking AI visibility reliably is possible" and "AI takes more SEO jobs than it creates": no audible answers; Roof added a prediction (below).
Schema worth it? → Quaid: only where a feature requires it (job postings), maybe aggregated reviews; not optimization. Kasra: does not move #5 to #1 but glues knowledge panels together, especially with a common name. Roof: keep it so you do not miss new SERP features.
Monday action: compare your SOPs against every idea from the conference (Roof) · buy a test domain (Quaid) · act on one thing (Kasra).
Disagreements worth keeping:
Authority vs relevance: Roof would take one irrelevant ESPN link over five flower-site links; Quaid says relevance wins and EMDs do better in AI; Kasra builds relevance through the placement's story.
Schema: Quaid says it does nothing for knowledge panels in his case; Kasra says knowledge panel work is impossible without it.
EEAT: Roof (real business, real person) vs Quaid (mostly theatre outside YMYL) vs Kasra (CRO value).
Predictions (labelled):
PREDICTION (Roof): AI will remove junior SEO roles and leave a management and skills gap in ~20 years.
PREDICTION (Kasra): agencies move from selling tasks (five guest posts a month) to selling knowledge.
After-panel conversation: HAR file analysis (separate from the panel)
Hallway, after the break (~54:00–66:00). Speaker labels K and F both appear to carry one person; the note-taker calls that person Brie and confirms the surname as Moreau. Remarks below are hers unless stated; labels are not reliable enough to split further.
HAR analysis shows engines retrieving text from all over the page, not mostly the top 10% as another talk ("Tom X"'s, name garbled) claimed. A high-authority source (a US government page) may be used even when the fact sits at the bottom.
Next: a time series of what the APK files and the Chrome build carry ("5.6 to 6", garbled), expecting more data collection over time; going further into a decompiler.
Mobile vs web HAR: the mobile capture was pulling health-app data (blood pressure, steps, sleep score). Which app was not said. Unverified.
She is looking at buying Chrome extensions as a data source. Legal position unresolved: research use vs commercial resale, user opt-in, GDPR, terms of service; "selling this to a bank" was mentioned as a use case.
The note-taker described a public HAR parser he adapted for AI Overview and Gemini; she questioned whether that is allowed under ChatGPT's terms of service.
Link vetting by "Max" (surname not given): compare a site's PageRank with its harmonic centrality; sites whose PageRank runs ~15× ahead of their harmonic centrality are flagged as buying links that inflate DR. Two domains were named and are garbled ("pre tax USA", "tax act"). The "should be 0:0" remark about the expected relationship is garbled.
The journey view (question → whether the brand is cited or only named) was the note-taker's point of interest; she said she would contact Steve (Toth) in a couple of weeks for a call.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
The summary names no panelist. Panel: Kyle Roof, Kasra Dash, David Quaid; moderator heard as "Neil".
"Nearly all missing schema" is wrong: Roof said about half; all were missing contextual terms.
"Branded search volume (e.g. from job post campaigns)": Kasra described publishing ~500 job posts in a week to inflate branded search, introduced as "one thing I'm definitely not doing, wink wink". That is fake job posts, not a campaign type.
"AI visibility tracking: not yet reliably possible at scale" was the moderator's agree/disagree statement; no panelist answer is audible.
"Multiple domains recommended as a hedge" omits the reason: Quaid's team once noindexed his whole site, and Bing will not index his contest site.
The 24–48 hour "AI citation manipulation" result has no sample; the summary presents it as a finding.
HAR section: "a participant asked for the slide deck" was the note-taker. The health-data finding is attributed in the summary to "mobile data" without saying it is unverified and the app is not named.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
Moderator's name ("Neil"/"Niels").
"Radar Kit" spelling; "PETE"/"Peak" assumed to be Peec AI.
Quaid's Malaysia campaign: what was advertised and what "1 million click a week search rates" means.
"JB's talk" and the decibel example: garbled.
The two domains in Max's PageRank vs harmonic centrality example; Max's surname; the expected relationship ("0:0").
"Tom X" talk on top-10% retrieval: speaker not identified.
Which mobile app exposed health data, and whether that is HAR evidence or a permission prompt.
SEO vs GEO Panel — Kasra Dash (moderating and answering), Dennis Yu, David Quaid
Source: Granola https://notes.granola.ai/d/f195128c-f253-4589-b6ce-dffbbc879031 · recorded 2026-11-15 01:25 PST = 2026-11-15 16:25 GMT+7, LLM Mastery 4.0 (closing panel) · transcript-verified 2026-11-16 (full transcript read, 43,623 chars) Resources: none. No photos attached; no deck. Vendor talk? ⚠️ Partly. Dennis Yu sells knowledge-panel help and equity-for-growth deals (same pitch as his C9 talk); Kasra Dash offered "$50 free in Giga Links" for the last question; David Quaid runs an agency. No numbers were shown on screen.
Speaker labels: A = Kasra Dash (runs the panel and answers; KGMID score story, James Dooley videos, UK construction clients, OpenClaw bill). C = Dennis Yu (KGMID scoring of speakers, Anthony Hill, 3% equity, Wikidata). B = mostly David Quaid (KEMP, King of AEO, "Dennis Quaid" name problem, blog-to-forum schema, EMDs). ⚠️ Labels B and C swap in places: the opening "former search engine engineer… 30 years ago" is labelled B but fits Dennis Yu, and one answer (~4:40–5:11) starts under B and continues under C. Where a remark could belong to either, it says "a panelist".
Thesis (3 bullets max)
Entity first: knowledge panels, KGMIDs, Wikidata and association with better-known people decide what Google and AI say about you (Dennis Yu).
SEO vs GEO: the work largely overlaps, but clients are moving PPC budget into "GEO", so sell it under that name (Kasra) — vs "good GEO is good SEO" (Quaid, Yu).
Underlying proof outlasts tricks as models get better; revenue is the only metric to optimize.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Speaker knowledge panels | 6 of 26 LLM Mastery speakers have a knowledge panel; 2 have claimed it (Quaid, Kasra) | 26 speakers, checked before the panel | Dennis Yu | spoken | clear; he says the Knowledge Graph API can confirm it |
| KGMID confidence | Kasra's result score 1 → 19 since Chiang Mai SEO | one person | Dennis Yu | spoken | one case; the score is the Knowledge Graph Search API resultScore, which is not a ranking measure |
| Wikidata submissions | ~40% of the items he submitted for speakers rejected ("normal") | all speakers | Dennis Yu | spoken | count not given |
| AI Overview presence | 70% of the time Google showed an AI Overview for his lawyer queries | his own test | Dennis Yu | spoken | no query count |
| Search-volume push | James Dooley ran ~27,000 searches in one day with Quaid's middle initial; Google then split his panel in two | one case | David Quaid | spoken | anecdote |
| Agent cost | OpenClaw API bill ~$4,500 in 3 days on a Mac Mini setup | one person | Kasra Dash | spoken | anecdote |
| Local equity deals | landscaper +$1M/year; Dennis holds 3% | one client (repeat of C9) | Dennis Yu | spoken | self-reported |
Asserted mechanisms (no evidence given in the talk)
Search and AI both resolve to a database of entities (KGMID), attributes and edges; AI Overviews are "dynamic knowledge panels" (Dennis Yu).
You can already claim a business in ChatGPT (Dennis Yu; no source).
Being shown in other people's knowledge panels ("people also search for") brings more clients than self-promotion (Dennis Yu, Kasra).
Changing blog schema to forum schema gets posts into forum results (Quaid, "works very well").
GEO needs things SEO never did: accreditations, company registry numbers (Companies House), Trustpilot reviews, for "is X trusted?" queries (Kasra).
Black hat in GEO is exploiting the engines' inconsistencies (Dennis Yu).
Deep-research content on link placements gets cited positively by LLMs; cheap 500-word filler does not (Kasra).
Decision engines: buyers paste competing quotes into ChatGPT or Claude and let it choose; insurance cover vs years trading decides (Kasra, UK construction tenders).
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Knowledge panel, fast (Dennis Yu):
Start a podcast; interview respected people in your field. WHITE
Cut 30-second clips to YouTube. WHITE
Turn the conversations into a book; publish on Amazon; run $1/day Amazon ads "until you're a bestseller". GREY (buying the bestseller label)
Claim your Google profile; tie every item to Wikidata objects (not Wikipedia); claim the Wikidata items. WHITE when items are accurate and notable; he created items for every speaker as a "gift", which is GREY on notability
Common name: add disambiguation text and the KGMID in schema (Kasra). WHITE
Run an ad asking people to search your name (Quaid; the same idea as his C21 Malaysia campaign). GREY
Co-create content with people who already have panels to get into their "people also search for" (Kasra: 6,500 videos with James Dooley; a video ranked for Tim Soulo's name). WHITE
Other tactics named: 8. Switch blog posts' schema to forum schema to rank in forum results (Quaid). BLACK (mislabels page type; against Google's structured-data rules) 9. Deep-research content for every bought link instead of 500 words (Kasra). GREY (paid links); the content part is WHITE 10. Reputation case: Dennis researched a copyright-claim lawyer with several LLMs, published a critical post across several sites, then checked what each LLM now says about him. BLACK/GREY (adversarial content about an individual) 11. New site, three moves (Quaid): branded domain plus exact- and partial-match domains; video first; mirror real-life activity online. GREY (EMD network) 12. New brand (Dennis Yu): partner with a respected person who lacks a personal brand; interviews → YouTube → book → YouTube ads for lead gen; cross-equity. WHITE 13. Testing (Kasra): a pool of test sites not linked to main sites; nonsense-keyword tests across ~10 sites; retest what others claim. Quaid: test the corollary. Dennis: agents read your own analytics history for what drives revenue; spend $25–$100 to trial vendor tools and split-test them. WHITE 14. Revenue: find the one thing already making money and do more of it (Dennis Yu, "99:1, not 80:20"); quarterly one-week timesheet with a dollar value per activity, then hand low-value work to AI or hires (Kasra); comparison content about competitors to catch people already looking (Quaid). WHITE
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Google Knowledge Graph API (resultScore), Wikidata: entity checks and fixes.
OpenClaw: agent setup on a Mac Mini; ~$4,500 API spend in 3 days.
Perplexity: used for "brutal honest feedback"; a follow-up instruction emailed that feedback to people, ending a client relationship (a panelist; label B, likely Quaid).
Giga Links: $50 credit offered to the audience.
People: James Dooley; Tim Soulo (heard "Tim Su", Ahrefs); Neil Patel; Rand Fishkin; Mari Smith; Anthony Hill (landscaper); Jeff Hughes (Sterling Lawyers, 17 cities, buying competitors); Justin Mills (reputation case); Marco Sipola, George Poladichuk, Tommy Mello (Dennis's published case studies; spellings unverified); Jabez (host).
King of AEO contest: Quaid ranks #1–2 on Google but Dooley beats him in the AI Overview.
Q&A (question → answer)
Agencies in 12 months? → A panelist (label B/C split): strategy over deliverables, more than 60% of work strategy-led; SEO and digital PR merging is the strongest combination. Kasra: output per client has to rise.
Buy competitors? → Quaid: buy news sites; ad revenue is gone. Dennis: Jeff Hughes buys rival law firms from their own earnings.
One new thing learned? → Quaid: blog-to-forum schema. Dennis: GEO black hat = exploiting inconsistencies. Kasra: people who acted are now winning.
Has client demand changed? → Quaid: his old employer rehired him after failing at GEO; CMOs now see good GEO as good SEO. Kasra: UK companies are moving budget from PPC to GEO.
Entity association? → Yes (Dennis, Kasra), with examples above.
Biggest AI opportunity? → Kasra: automate repeat tasks; invest in old-owner businesses. Dennis: boring local businesses on retainer → rev share → equity. Quaid: dictation for writing and admin.
AI mistakes? → OpenClaw bill (Kasra); feedback email (a panelist); LinkedIn auto-reply congratulating someone on a death (Kasra); an LLM invented a biography (skiing in Argentina, painter) for a reputation client because it was given only a goal, no constraints (Dennis).
How do new brands get big fast? → Kasra: big competitors move slowly. Quaid: build fast, test many, get acquired. Dennis: compete where rivals are weak.
Disagreements worth keeping:
SEO vs GEO: Kasra says different and should be sold as GEO; Quaid and Dennis say the same. Quaid's own King of AEO result (ranks top on Google, loses in the AI Overview) cuts against "same".
Will people change behavior? Quaid: technology is ahead of people's willingness to adapt. Dennis: it does not matter, Google pushes AI into the results anyway.
Predictions (labelled):
PREDICTION (Kasra): by 2027 brand association beats keyword ranking ("best CRM for SEOs"); long tail matters less in zero-click; knowledge panels and brand building fill the gap.
PREDICTION (Dennis Yu): within a year models close the hallucination gap; proof (real photos, credentials, experience) beats technical tricks; agents will book travel and buy on that proof.
PREDICTION (Quaid): land grab in news sites; SEO domain owners become "property developers".
PREDICTION (a panelist): within 12 months more than 60% of agency work is strategy.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
The summary names nobody. Panelists: Kasra Dash, Dennis Yu, David Quaid.
"One speaker went from 1 to 19": it is Kasra's score, measured by Dennis Yu.
The KGMID tactic list in the summary is spoken content; the matching private-note lines are the note-taker's shorthand of it, not extra advice.
"Reputation management via AI hallucinated a fake biography" omits the lesson's source (Dennis, for Justin Mills) and omits Dennis's other reputation case: critical content about a lawyer pushed across several sites.
"Acquisition play: buy struggling news sites or competitor agencies cheaply": news sites were Quaid's idea; agency buying was Kasra's question; Dennis's example was a law firm buying rivals.
"Entry via retainer, then rev share, then equity" is Dennis's C9 model repeated.
The summary misses the speaker-label swap between B and C.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
Which panelist gave the 60% strategy figure and the introduction (labels swap).
"You can claim your business in ChatGPT": no source.
Names of Dennis's case studies (Marco Sipola, George Poladichuk) and "Black Cat Day" (likely the Black Hat day of the conference).
Whether the forum-schema result was measured.
Why High-Quality Websites Are Invisible to AI (Common Crawl, CCBot, harmonic centrality) — Stephen Burns (Common Crawl; founder, StephenBurns.ai)
Source: Granola https://notes.granola.ai/d/05632883-d6ef-4557-a403-33d5503654fe · recorded 2026-11-14 (16:00 GMT+7; Granola 11-14 01:00 PST), LLM Mastery 4.0 day · transcript-verified 2026-11-16 Resources: no slide photos attached. Audit tool https://audit.stephenburns.ai (from the note-taker's notes and the QR on stage; not run). Game at game.commoncrawl.org (audio "game.com commoncrawl.org"; not opened). He offered a PDF "SEO's guide to Common Crawl" to LinkedIn connections, the week after the talk. Vendor talk? Partly. Speaks from inside Common Crawl ("we launched", "we publish the archive", "here's ours from inside Common Crawl"); the role title was not said on stage (the note-taker's notes record him as Common Crawl's Web Intelligence Lead). Pitches a free audit tool that he says creates "a new deliverable category" for agencies; no price.
Thesis (3 bullets max)
Being crawled, being trained on and being retrieved are three separate stages; SEO happens at the crawl, and you can vanish at any stage (blocked, JavaScript shell, thin template, deduplicated).
CCBot sets each site's page budget by harmonic centrality (closeness to the web's core), not PageRank; a famous site can be far from the core, and a perfect score cannot get past a blocked door.
About a third of high-quality sites are blocked from AI crawlers by CDN defaults nobody chose; audit three gates (access, corpus presence, rendering) as a new deliverable.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Archive size | 12 PB, every crawl since 2008; ~400 TB and 2.1B pages per monthly crawl | Common Crawl | Common Crawl (his employer) | spoken | high for an insider figure; not checked |
| Model reliance | at least 64% of 47 language models built on Common Crawl | 47 models | Mozilla (report not named) | spoken | medium: matches a known Mozilla Foundation study; not re-read |
| Team | 20 people | — | speaker | spoken | — |
| ⭐ AI-crawler blocking | ~35% of high-quality sites block AI crawlers, "usually by accident" (CDN defaults) | "from inside Common Crawl"; definition of "high-quality" not given | Common Crawl | spoken | medium: insider number, no method stated |
| Fetch denials | 5–10% of all fetch attempts denied by robots.txt or 403; 429s and empty JavaScript shells on top | CCBot fetch logs | Common Crawl | spoken | medium: insider number |
| Silent blocking growing | "silent blockers are growing" | 10,000-domain study, author not named | not named | spoken | low |
| One-link seeding | his new domain (launched 07-26) missed the August crawl; after linking it from his commoncrawl.org profile page it was in the very next crawl | n=1, his own site, linked from his employer's domain | speaker | spoken | anecdote; source domain is unusually central |
| Recovery lag | a Melbourne SEO's client disappeared from Bing Chat; CCBot was blocked by the firewall; 4 months after the fix it came back | one client | "Ash Nala Walla" (garbled) | spoken | anecdote |
| Training lag | crawl → training "months to a year" | — | speaker | spoken | assertion |
| Language | ChatGPT searches in English even when asked in another language | 10M prompts | "PKI" (garbled; possibly Peec AI) | spoken | low until the study is found |
| English folder test | English folder: +122% ChatGPT citations, +52% Copilot, +28% Google AI impressions; ChatGPT-User fetched English 3 of 4 times | his clients; no base, period or control | "Peter Sereris", Belgium (garbled) | spoken | low: vendor test, no base |
| ⭐ Hyatt audit | hyatt.com HC rank 2,028 of 130M domains; robots.txt request returns 429; 0 of a 500-URL sample captured with a 200; no homepage capture in 12 monthly snapshots (Nov 2025 → Oct 2026, rechecked "this week"); live fetch also 429; 13 crawler user agents probed, 0 served | one domain | speaker's audit tool + CC index | spoken (slides not photographed) | medium: specific and checkable; not reproduced |
| Cloudflare change | July 1: AI crawlers split into search, agent and training; since September 15 agent and training blocked by default on pages with ads | — | Cloudflare (as reported by him) | spoken | medium: checkable in Cloudflare docs; not checked |
| Wheel vs chain | wheel solved the puzzle in 32 s, chain in 53 s | 1948 MIT experiment | Bavelas / Leavitt | spoken | history, illustrative |
Asserted mechanisms (no evidence given in the talk)
Harmonic centrality sets each site's CCBot page budget; site size decides how much of the site that budget covers (his 2,500-page example is illustrative, not a real budget).
Labs extract, filter and deduplicate before training, so thin template copy and duplicates vanish; the fix is "extractable, distinctive, corroborated pages", not more pages.
If the model never learned the brand, retrieval cannot save it. Spoken only; no test.
Multi-purpose bots are judged by Cloudflare's strictest rule, so a training block can also block search by accident.
A robots.txt that looks friendly no longer means access; blocking has moved to the edge.
Blocking CCBot blocks "the whole AI ecosystem" (the Hyatt edge rule served 0 of 13 user agents).
English is "the gateway into the model"; non-English sites compete for a small slice.
Common Crawl honors nofollow, so a nofollow link may not help discovery.
CCBot also discovers sites through sitemaps.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Five checks (his audit; free, "about a minute"):
Can CCBot get in? Fetch robots.txt as CCBot; a 429 or 403 at the edge means closed, whatever the rules say. WHITE
Is the domain in the Common Crawl index? Sample URLs (he uses 500) and count captures with status 200; check the homepage across the last 12 monthly crawls. WHITE
When was it last seen? WHITE
Harmonic centrality score/rank. WHITE
Rendering: how many real words are stored in the captured HTML (AI crawlers behave like early Googlebot; no JavaScript). WHITE Then:
Probe the live site with the main AI crawler user agents (he uses 13) and record which are served. WHITE
Check Cloudflare (or other CDN) AI-crawler settings, especially the training and agent categories, on banks, hospitals, government and ad-carrying pages. WHITE
For a new or low-centrality domain: publish something real on GitHub, WordPress.com, Substack or Hugging Face and link to the site; then check whether the next crawl captures it (followed links only). WHITE
Publish in English alongside the local language (not instead); keep the English version current, because it becomes the source of truth. WHITE
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
audit.stephenburns.ai: checks the three gates against Common Crawl's own archives; verdict plus to-do list; free.
game.commoncrawl.org: "CCBot, the Great Crawl", a game launched the day before the talk.
Common Crawl Foundation: nonprofit founded 2007 by Gil Elbaz (audio "Gil Elvad"; Applied Semantics, bought by Google 2003, became AdSense). Sebastian Nagel: switched CC to harmonic centrality in 2017 against spam.
Harmonic centrality lineage: Bavelas and Leavitt, MIT 1948 (audio "Bevelis and Levitt") → Marchiori and Latora, 2000 (audio "Marquori and La Torre") → Boldi and Vigna, Milan, 2013 axioms paper (audio "Bolvi and Vigna").
Cloudflare AI crawler categories (search / agent / training).
Mozilla study of 47 models; "PKI" 10M-prompt study; "Peter Sereris" (Belgium); "Ash Nala Walla" (Melbourne): all names garbled except Mozilla.
High-centrality hosts to test: GitHub, WordPress.com, Substack, Hugging Face.
Children's Hospital Los Angeles: example of a Cloudflare default blocking AI crawlers (absent from ChatGPT answers about pediatric cancer care; no prompt data shown).
Hyatt (hyatt.com): live audit walkthrough.
Slide photos
None attached to the Granola note.
Q&A (question → answer)
None. Show of hands at the start: most had heard of Common Crawl; some had audited CCBot access this year; few could explain harmonic centrality to a client.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
Names: Gil Elbaz (not "Gil Elvad"); Bavelas/Leavitt; Marchiori/Latora; Boldi/Vigna. "Peter Sereris" and "PKI" are speech-recognition spellings and should not be quoted as written.
"64%+ of 47 language models studied were trained on it" is Mozilla's figure, not Common Crawl's.
Omits that he speaks as a Common Crawl insider ("here's ours from inside Common Crawl"), which makes the 35% and 5–10% figures internal numbers rather than a third-party study.
Omits his caveat that Common Crawl honors nofollow, so the one-link test should be checked after publishing, and that his own example link came from commoncrawl.org itself.
Omits the crawl-to-training lag (months to a year; "until then you only exist in retrieval") and the Melbourne four-month recovery case.
Omits the point that multi-purpose bots are judged by the strictest Cloudflare rule.
"Run the AI visibility audit for key clients", "Audit CCBot access", "Test a high-centrality inbound link" are Granola's next steps; the talk offered the tool, not a plan.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
The Cloudflare dates (July 1 split; September 15 default block on pages with ads): year and exact scope not stated; check Cloudflare's changelog before telling a client.
The 10,000-domain silent-blocking study: author not named.
The English-folder test and the "ChatGPT searches in English" study: authors garbled; find the sources before quoting.
"Entity hiking. The industry skips it." garbled (possibly "entity hygiene").
Counterweight from the note-taker's notes: James Dooley's Common Crawl test (200 sites, all bots blocked except CCBot, invented terms, 10 weeks) returned nothing in models. Burns's talk does not claim CC presence produces recall on any timescale shorter than a training cycle.
Hyatt figures not reproduced; the hc-rank skill can check the 2,028 rank.
The new GTM: how to get replies to outbound campaigns (timing, offer, copy) — Thibault Garcia (founder, Reachly; done-for-you cold email and LinkedIn outreach agency)
Source: Granola https://notes.granola.ai/d/9671e9eb-089e-41d3-87e5-08de45237230 · recorded 2026-11-14 (14:29 GMT+7; Granola shows 11-13 23:29 PST) · transcript-verified 2026-11-16 (full transcript read, 23.9k chars, about 25 minutes incl. Q&A) Resources: 7 slide photos saved to ../resources/thibault-garcia/photos/ (all read). Deck is about 32 slides (page counter "/32" visible). He offered to share the slides after the talk; not in hand. Vendor talk? ⚠️ Yes. Runs an outbound agency (says about 1M emails a month across clients and his own campaigns; "first Clay-certified agency in Asia Pacific"). Agency name comes from the slides ("Reachly" logo, "you@reachly.co" in the example email); spoken as "richly". All results are his agency's own campaigns.
Thesis (3 bullets max)
AI made research, list-building and personalization nearly free, so everyone sends the same AI-written email; the edge is now judgment on who, when, the offer and the copy.
Three levers: timing (a signal gives a reason to reach out now), offer (something worth a reply; never "a call"), copy (sounds like a person).
Optimize for the reply, not the meeting; replies are the top of the funnel.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| ⭐ AEO-agency case: one line changed | positive replies 7% → 34% | "positive reply rate from the people that were replying" (share of replies, not of sends); slide footnote partly hidden: "Positive replies as a sh[are]... same list, same ... we on[ly changed]..."; send volume, period and number of replies not given | his agency, for a client (an "AEO agency") | slides (photos 05, 06) + spoken | slide clear on 7% and 34%; denominator is replies, base size unknown |
| Same case, two winning lines | Version A: "we searched for best accounting software for SMEs and you didn't appear in ChatGPT nor on the 1st page of Google. If my team put together a checklist on how your team could achieve this within 45 days, could I send it over?" Second line: "if we put together a checklist on how you could appear in ChatGPT for 'best accounting software' in 45 days, could I send it over?" | both photos show 34% and are labeled "Version A"; spoken as versions A and B | his agency | slides (photos 05, 06) | the label conflict is unresolved; spoken "25 days", slides say 45 days (slide wins) |
| ⭐ Honest math, email | 5,000 unique leads → 10,000 emails (2-step) → ~200 replies (2% reply rate) → ~60 positive (30% of replies) → ~20 meetings | "typical", no campaign, period or sector named | his agency, rule of thumb | slide (photo 07) | clear on slide; illustrative, not a campaign result |
| Honest math, LinkedIn | 5,000 leads → 5,000 connection requests → ~1,400 accepted → ~350 replies → ~105 positive → ~30 meetings | same | same | slide (photo 07); rate labels partly hidden by the speaker | clear numbers; the rate labels are partly blocked |
| Positive reply frequency, email | one positive reply per 300–600 sends | "depending on offer, social proof, authority, USP" | speaker | spoken | ⚠️ conflicts with his own slide: ~60 positive per 10,000 sends is one per ~167 sends |
| Meetings from LinkedIn | spoken "about 20 meetings for every 5,000" | — | speaker | spoken | ⚠️ the slide shows ~30 for LinkedIn and ~20 for email; the audio is garbled here |
| Test volume needed | 5,000–20,000 sends before judging an A/B test; 1,000 or 3,000 is not enough | his rule | speaker | spoken | rule of thumb |
| List-offer email | "a list of 200 fintech companies that match your ICP, with the opener to use for each" = replied; templated partnership email = ignored | example, no rates | his agency | slide (photo 03); spoken "215" | slide wins (200) |
| Video-production client | "free video at no charge" offer did worse than "can I send samples of our work in fintech?" (used as email 2) | no numbers | his agency | spoken | qualitative |
| Volume | about 1M emails/month | his agency + clients | speaker | spoken | self-reported |
| LinkedIn restrictions | never restricted in 8 years of automated outreach after passport KYC | his own account | speaker | spoken (Q&A) | anecdote |
Asserted mechanisms (no evidence given in the talk)
Buyers see identical AI emails because everyone uses the same tools, data and lines.
A signal raises relevance but does not make a company a fit.
Offers that are "too good to be true" (a free video) are tuned out; a smaller, specific offer can win. He says always test.
Infrastructure errors (domains, mailboxes) send everything to spam regardless of copy. Not covered in the talk.
Paying for LinkedIn Sales Navigator raises the weekly invite limit, and LinkedIn is less likely to ban paying users. He says "I like to believe".
Passport KYC on a LinkedIn account prevents a permanent ban.
Prospects Google the sender; a thin or missing profile loses them. He says "no data behind this".
People on LinkedIn want to connect with founders, not SDRs.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
No prices stated.
Signals (slide photo 01): new in the seat (under 90 days; rebuilding tools, team, process) · just raised (new budget, pressure to show growth) · hiring for the role (the pain is public) · added a tool you fit · opening a new market · champion left (follow them to the new company). Track with AI tools (not named on stage). WHITE
Offer (slide photo 02, "Offers worth a reply. None is 'a call.'"): free audit (where they stand vs peers) · teardown (3 things you'd change) · interview/podcast (insights on what peers say) · benchmark (their numbers vs the market) · relevant resource (the exact playbook for their case) · warm intro. WHITE
Email copy (photo 03): a reason to reply, not a reason to book. Short, specific, useful before you ever talk. Offer to send the thing; do not send the finished thing plus a meeting ask ("A finished thing, plus a meeting ask" is the 7% version). WHITE
LinkedIn copy (photo 04): one idea, one real question, no pitch (example: "is your sales team using Claude for prospecting by any chance?"). Mobile-length. WHITE as copy; LinkedIn automation is GREY (platform terms)
AI-visibility angle: name the buyer's search ("best accounting software for SMEs"), say they are absent from ChatGPT and Google page 1, offer a checklist "within 45 days", ask permission to send. WHITE if the absence was actually checked; GREY if the 45-day line reads as a promise
On a "yes, please": some US/UK clients have an SDR phone the lead at once, referencing the founder's email, and try to book a meeting; if not, they send the checklist anyway. WHITE (calling rules vary by country)
Test: always A/B; judge only after 5,000–20,000 sends. WHITE
Have one real offer that is easy to say yes to; measure it. WHITE
Stack (slide not photographed; audio garbled): a domain and mailbox infrastructure reseller (name garbled, "I know"), Supabase (keep the data in-house), a lead-data scraper ("ARC", garbled), "Smartly" for sending (likely Smartlead), Clay. WHITE
Job-post trigger (Q&A): scrape LinkedIn Jobs / Google Jobs weekly for roles you can replace (e.g., "SEO manager"), email: "I see you're hiring for this; we can do it for you without the hire." WHITE (scraping terms aside)
Sender: always the founder or CEO; keep a real public profile. GREY if using rented accounts or avatar personas (he mentions these exist and work but lose people who check)
Sound human: fifth-grade reading level; ask "would I say this to this prospect in an elevator?" WHITE
LinkedIn account safety: KYC the account with a passport before automating. GREY (keeps automation going against platform terms)
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Reachly (his agency; slide logo, reachly.co in the sample email). No price.
Clay: list building and enrichment; his agency is Clay-certified.
LinkedIn Sales Navigator: higher invite limits.
Supabase: their own data store.
"Smartly" (likely Smartlead): sending tool. ASR.
Domain/mailbox reseller and "ARC" scraper: names garbled.
Claude, ChatGPT: named in example copy.
Attendees: Christian (semantic content business); Felix (runs an AI-visibility startup). First names only.
Slide photos
Full text of each slide: ../resources/thibault-garcia/slide-text.md
01-lever1-timing-signals.jpg: "Lever 1 · Timing. Signals: a reason to reach out now." Six signals (new role under 90 days, funding, hiring, tech added, expansion, champion left). Readable; the speaker blocks part of one card.
02-lever2-offers-worth-a-reply.jpg: "Lever 2 · Offer. Offers worth a reply. None is 'a call.'" Six offers with one-line definitions. Readable.
03-lever3-email-copy-ignored-vs-replied.jpg: "On email: a reason to reply, not a reason to book." Ignored: "Jordan · Growthly, Partnership opportunity for Acme… Open to a quick 15-minute [call] this week?" Replied: "You · Reachly, Acme's list: If I put together a list of 200 fintech companies that match your ICP, with the opener to use for each, could I send it over?" Caption: "Short, specific, useful before you ever talk."
04-lever3-linkedin-copy-ignored-vs-replied.jpg: "On LinkedIn: sound like a person, not a prompt." Ignored pitch vs replied "Hi Sarah, is your sales team using Claude for prospecting by any chance?" Caption: "One idea, one real question, no pitch."
05-case-study-aeo-agency-7-to-34pct-google-chatgpt-line.jpg: "Case study 1 · AEO agency. One line. 7% → 34% positive replies." What they sent (7%): "I'm Mike from Acme, a leading SEO agency in the USA. We put together an SEO audit for you and wanted to book a meeting to show you the results." What we changed it to (34%): the ChatGPT + Google page-1 line with a 45-day checklist. Footnote partly hidden: "Positive replies as a sh[are]… same list, same… we on[ly]…".
06-case-study-aeo-agency-7-to-34pct-chatgpt-45-days-line.jpg: same slide, other variant: "if we put together a checklist on how you could appear in ChatGPT for 'best accounting software' in 45 days, could I send it over?" Caption: "Offer to send it. Let them say yes." Both photos are labeled "Version A" and 34%.
07-honest-math-5000-leads-linkedin-vs-email.jpg: "The honest math. 5,000 unique leads, down two channels." LinkedIn (1 request each): 5,000 / 5,000 / ~1,400 / ~350 / ~105 / ~30 meetings. Email (2 emails each): 5,000 / 10,000 / ~200 replies (2%) / ~60 positive (30% of replies) / ~20 meetings. Footer partly hidden: "Same leads, same des[tination]… fewer touches, warmer… more infrast[ructure]".
Q&A (question → answer)
Does LinkedIn plan level (Sales Navigator) affect delivery? → Not much; it raises the weekly invite limit and, he believes, lowers ban risk. KYC the account with a passport first.
(Christian) Pitching companies that post a job you could fulfill? → Yes, it works: scrape job boards weekly for the role keyword and offer to do the work without the hire.
(Felix, AI-visibility startup) Founder or head of BD as sender? → Founder/CEO, with a real personal brand; prospects Google the sender, and LinkedIn users want founders, not SDRs.
Follow-up: prospects think my manual messages are AI → Simplify: fifth-grade level, elevator test; say "rank on ChatGPT" rather than "AI" because most people only know ChatGPT.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
"I built a list of 215 leads": the slide says 200 fintech companies, and the copy is an offer ("If I put together… could I send it over?"), not "I built".
"Appear in ChatGPT in 25 days": the slides say 45 days.
"7% to 34% positive reply rate" is right, but the summary omits that the denominator is replies (positive share of replies), not sends; so 34% is not comparable to a reply rate.
The summary omits the "honest math" slide entirely (2% reply rate, 30% positive, ~20 meetings per 5,000 email leads; ~30 meetings per 5,000 LinkedIn leads), and that his spoken "one positive per 300–600 sends" conflicts with it.
It omits the video-production case (the free offer lost to "samples of our work").
It omits the SDR call-on-yes step and the "too good to be true" warning.
It omits his conflict: he sells done-for-you outbound.
Speaker's company: the summary gives none; the slides show Reachly.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
Which of the two 34% lines is Version B; both photos say "Version A".
Size of the 7% → 34% test (sends, replies, period) and whether "same list" means the same people were emailed twice.
Stack names: the mailbox reseller ("I know"), "ARC", "Smartly". The stack slide was not photographed.
"First Clay-certified agency in Asia Pacific" and "1M emails a month": self-reported.
Legal side (UK/EU cold email, calling rules, LinkedIn automation terms) not discussed.
Content Distribution: from one book to 660 pieces — Victoria Olsina (independent Web3/crypto SEO consultant; company name not stated)
Source: Granola https://notes.granola.ai/d/5620b11c-f222-4a53-9ffb-d2778490f2f1 · recorded 2026-11-09 (3:00 PM GMT+7) · transcript-verified 2026-11-12 Vendor talk? Partly. She sells her book (free with newsletter signup, paid on Kindle and Google Books with bonus custom GPTs), and says her anti-AI-slop prompt, slides and the repurposing lines are "on sale" on her website. She is a consultant, not a tool vendor. Speaker is named by the MC at the start only as "Victoria Olsina"; the surname is also in the book title, notes and file title.
Transcript caveats: audio is rough (speech-to-text garbles tool names and several numbers). Transcript ends in the middle of the first Q&A answer (only one question captured). A pre-recorded promo video (a different voice, labeled Speaker C) plays mid-talk.
Thesis (3 bullets max)
A big content asset (book, report, whitepaper) should be the SOURCE, not the destination: repeat the same claim about who you are across many independent platforms, because LLMs trust repeated corroboration, not one source.
Run it as a system: Claude = brain, skills = instructions/brand voice, MCP connectors = hands that publish; one input (book) → 60 blog posts → five more lines of formats (660 pieces total).
After becoming the top recommendation, publish that fact so LLMs keep repeating it.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Appears in AI recommendation for "Web3 SEO consultant" | "very high chance"; no rate | Single prompt example; she said ask Google or "any" AI | Speaker, anecdote | Spoken | Clear (qualitative only) |
| Share of leads from AI | "2%" | Said as "the 2% that I got from this experiment is that all of my leads, the main source of leads right now is AI search" — internally contradictory (2% vs main source); base and period not stated | Speaker | Spoken | GARBLED. Summary says "2% of leads come directly from AI search"; transcript could mean main source. Do not cite either way without the slide |
| Organic traffic | +37% | Metric name garbled ("my organization 37%"); likely organic sessions; period and baseline not stated | Speaker (tool not named) | Spoken | Garbled label, number clear |
| Organic video sessions | +44% | Not defined, no period | Speaker | Spoken | Number clear |
| Organic social sessions | +344% | Not defined, no period | Speaker | Spoken | Number clear |
| LinkedIn engagement | +72% | No period, no base | Speaker | Spoken | Number clear |
| LinkedIn impressions | +30% | No period, no base | Speaker | Spoken | Number clear |
| Book effort | Planned 2 days, took about 2 months; 137 pages | Her own project | Speaker | Spoken | Clear |
| Content output | 60 blog posts → "150 [garbled]" social posts + 120 long-form + 120 carousels + 240 videos = "660" | Her own count | Speaker | Spoken | Arithmetic check: 60+120+120+120+240 = 660, so "150" is probably 120 (garbled). With 150 the total would be 690 |
| Channels that gave most visibility | Blog and LinkedIn | B2B crypto clients only | Speaker | Spoken | Clear; she says she can only answer for her B2B crypto clients |
| Blog-from-video system worked | "Half of my most popular blog posts in traffic" came from the earlier YouTube→blog automation | Her own site, earlier system | Speaker | Spoken | Clear; no numbers |
| LinkedIn articles rank better than LinkedIn posts | Not quantified | Her own experience; "I think" they rank better due to headers/semantics | Speaker | Spoken | Hedged |
| Promo video: only 28% of brands earn both mentions and citations | 28% | Pre-recorded promo for the book; source, sample, period not stated | Unknown (book promo) | Spoken in promo video | Clear on number, no provenance |
| Promo video: a brand went from 154 to 6,000 visitors after doing "first 30 [seconds?] reinforcement" | 154 → 6,000 | Not stated which brand, period, or metric | Unknown | Spoken in promo video | Garbled phrase around it; number clear |
| YouTube has "the highest correlation" with OpenAI and Google AI Overviews | n/a | Attributed to a previous speaker she calls "Ruben" | Ruben's talk (not this one) | Spoken | Not hers; check Ruben's source |
Asserted mechanisms (no evidence given in the talk)
LLMs do not trust one source; they trust what "the Internet" repeats independently across platforms; hence distribution = reinforcement.
Publishing "I am the top recommendation" content feeds back into LLM answers (self-referential loop).
Being the only person to write a book at the intersection (SEO + AI search + crypto) makes LLMs recommend you.
Reddit, YouTube and Wikipedia build the "story repeated" layer; X does not (promo video).
Mentions predict visibility; citations alone do not (promo video).
JavaScript-only sites show crawlers nothing; Web3 sites split content across app, docs and blog subdomains (promo video).
Alternating human and animation scenes hides the "AI avatar" look; a long avatar shot makes the AI obvious.
ChatGPT desktop extension is "much better for browser tasks" than Claude desktop and the Claude Chrome extension.
AI slop comes from bad prompting, not from AI itself; a brand-voice skill with real facts fixes it.
"70% of all SEOs are on the autistic spectrum" (aside, no source).
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
A. Write the book (WHITE)
Drop all sources into one project (Claude or ChatGPT project); set goals, format, length, audience.
Build the outline; have a second LLM review the outline.
Create a "sketch" in her voice with a skill that strips AI markers (e.g., no generic "in the ever-changing world of..." openers).
Write chapter by chapter (137 pages is too long to do in one pass).
Second-LLM review again; add a hook or funny line per chapter.
Read it yourself without AI and amend. B. Launch (WHITE)
Free version behind newsletter signup on a landing page; paid version on Kindle and Google Books with bonuses (custom GPTs); press release; channel promotion on own media; webinar (Luma event, recorded); then pitch conferences and podcasts. C. Six repurposing lines (all powered by blog posts, except line 1)
Line 1: YouTube video → seven formats (blog, Medium, LinkedIn article, newsletter, etc.) via a Make.com automation built years ago. (WHITE)
Line 2: book → 60 blog posts, one pillar per chapter plus cluster posts; skills: keyword research (DataForSEO MCP), SEO content assistant (content briefs via NeuronWriter), AI SEO blog writer, thumbnail generator, publisher to WordPress (REST API, Claude Chrome extension, or desktop app); schedule 1/day = 60 days. (WHITE)
Line 3: RSS feed → spreadsheet log → brand-context skill → LinkedIn post + X post; Make.com automation; Blotato publishes to social channels; log back to spreadsheet. (WHITE)
Line 4: long-form LinkedIn articles and Medium articles; publish through ChatGPT desktop extension. (WHITE)
Line 5: each blog post → 9-image carousel via Gamma for LinkedIn and Instagram; slides end by pointing to her book. (WHITE)
Line 6: blog → script → AI avatar + motion graphics, 90-second reel, 10 scenes alternating human/animation, spreadsheet tracks scenes; published to YouTube, LinkedIn, X video, Instagram; per-platform captions; skill took longest to build (anti-filler-words); scheduling by Blotato. (GREY: AI avatar of herself, deliberately masked with animation so viewers do not realize it is AI.)
Unique captions per platform, not copy-paste. (WHITE) D. Reinforcement loop
Once top recommendation is reached, publish blog posts and LinkedIn articles stating it so LLMs keep referencing it. (GREY: self-referential claim; works only while true.)
Prospect trick: ask the AI live in front of a client for "3 SEO consultants". (GREY/WHITE: sales demo, depends on honesty about prompt variability.)
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Claude / ChatGPT: projects, skills, drafting; ChatGPT desktop extension for browser publishing.
Make.com: automations for video-to-blog and RSS-to-social; "old one" tweaked.
DataForSEO MCP: keyword research.
NeuronWriter (transcribed "Neuro Writer"/"your writer"): content briefs.
WordPress REST API: publishing; her site is WordPress.
Blotato (transcribed "Potato"): multi-channel social publishing to LinkedIn, Instagram, TikTok, X.
Gamma: carousels.
AI avatar/video tool: transcript garbled ("Cajun", "agent"); summary says Captions.ai; speaker says it clones her image/voice and has an AI agent that produces video. Unverified.
Luma: webinar event page.
Kindle and Google Books: paid book versions.
Ruben: previous speaker on listicles and outside-platform reinforcement; surname not given.
URLs from notes (not spoken): victoriaolsina.com, linktr.ee/victoriaolsina.
Prices: none stated.
Q&A (question → answer)
Which channel gives the best leads per piece of content (B2B vs consumer)? → All her clients are B2B crypto; blog and LinkedIn give the most visibility; the answer is cut off mid-sentence. No other Q&A in the transcript.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
"2% of leads now come directly from AI search": the transcript says 2% but also says AI search is the MAIN source of leads; contradictory. Needs slide check.
Summary lists "37% increase in organic sessions": the spoken metric is garbled; sessions inferred.
Summary says "Captions.ai" for the avatar tool: transcript has "Cajun"/"agent". Summary-only name.
Summary says "660 pieces": correct; the 150 social figure in the transcript is garbled (120 makes the sum).
Summary line 1 "YouTube video → 7 formats via Make.com" is roughly right but that automation is an earlier, years-old system that fed the original idea; lines 2-6 are the new build. Line 2 is the book → blog step.
Omitted: the book's launch also had a paid Kindle/Google Books version with custom GPT bonuses, a Luma webinar, press release, and conference/podcast pitching (summary has most of this).
Omitted: promo video stats (28% mentions and citations; 154 → 6,000 visitors; Reddit/YouTube/Wikipedia vs X) which are not her measurements.
Omitted: she says YouTube has the highest correlation with ChatGPT and Google AI Overviews, quoting an earlier speaker.
Omitted: ChatGPT desktop is better than Claude for browser tasks (summary mentions it).
Omitted: alternating human/animation scenes to disguise the avatar.
Summary "once you achieve top recommendation status, publish that fact": correct.
Only one Q&A question exists in the transcript; the summary has no Q&A section, which is consistent.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
AI-lead share (2% vs "main source").
"150" social posts (probably 120).
"Cajun"/"agent" = the avatar tool; "80 to create" (skill build time or cost; garbled, unit unknown).
"first 30 second reinforcement" in the promo video (probably "first 30 days"? unverified).
Whether the 37%/44%/344%/72%/30% figures are year-over-year or since launch; no period given.
"Atasd/ADD" spelling aside: she says she has ADHD (transcript spells it unreliably).
"Binos" (a project tool, probably garbled "ChatGPT").
Baselines for every percentage lift: none stated.
Local Maps for LLMs: GBP and Website Factors for HVAC and Plumbing — Yash Singh (20-year-old US home-services local SEO)
Source: Granola https://notes.granola.ai/d/5d5a2c39-bf28-4850-a328-a85c26940ac6 · recorded 2026-11-15 (11:29 GMT+7), LLM Mastery 4.0, second day · transcript-verified 2026-11-16 Resources: 6 slide photos saved to ../resources/yash-singh/photos/ (6 of 6 attachments; 5 fully readable, the chart on photo 04 too small to read). No deck. Speaker name confirmed by the note-taker 2026-11-16 (the audio has Yash Singh). Vendor talk? Practitioner/agency. Works for US HVAC and plumbing companies; YouTube channel (4,000 subscribers per the host), former local SEO tester inside IMG Courses (Kyle Roof's platform). No product sold. Every number is from his own client grids; no sample sizes beyond "7 of 9 matchups".
Despite the title, the talk is almost entirely classic Google Business Profile and local website SEO. The only LLM link is the opening assertion that AI Mode and ChatGPT draw on Google Maps (and Yelp).
Thesis (3 bullets max)
Most local-service leads still come through the Google Business Profile, and AI Mode and ChatGPT read Maps data, so map rankings feed AI visibility.
Map rank = proximity, prominence, relevance (photo 01). The cheapest wins are the website page linked from the GBP, GBP on-page fields, review recency, and a visible address.
Diagnose drops by reverse-engineering who took the spot and what they changed (photo 04).
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| Review recency beats total | business with more reviews in the last 90 days ranked better in 7 of 9 matchups | 9 HVAC matchups; period and grid not given | his agency | spoken | low; small, no method |
| Reviews alone | competitor went from 8 to 42 reviews, the only change, +7.9 average rank positions (grid average, out of 20) | one competitor plumbing listing ("White Bull plumbing" in audio) | his agency | spoken | anecdote; "only change" not verifiable |
| Page linked from the GBP | average rank 15.5 → 9.53; 12.9 → 9.76; competitor 17.98 → 14.6 after optimizing the homepage / linked URL (competitor created a dedicated HVAC page) | three listings; period not given | his agency | spoken | anecdote |
| Website + GBP on-page only | 16.64 → 12.616 (sic); 4.33 → 3.88 | two listings | his agency | spoken | anecdote |
| Hiding the address | map grid rankings fell when the address was hidden and recovered when it was shown again | Sterling Sky study (Joy Hawkins; see C18) | Sterling Sky | spoken; grids shown, not photographed | medium; the study itself not read |
| Ranking-factor order | primary category · proximity · keywords in business name · physical address in city of search · open at time of search · high ratings (above 4.7 "pretty good") · address shown (not a service-area business) · additional categories · quantity of native reviews · map pin placement | Whitespark 2026 Local Search Ranking Factors (spoken); photo 01 shows a BrightLocal diagram instead | Whitespark survey (expert opinion) | spoken; photo 01 | the list order is attributed, not his data |
| Open hours | "open at time of search" and ratings were weak in 2024–2025, stronger in 2026 | none | his reading of the survey | spoken | low |
Asserted mechanisms (no evidence given in the talk)
AI Mode and ChatGPT use Google Maps (and Yelp) heavily, so map rank drives LLM visibility. Title claim; no test shown.
Marking a business open 24 hours gives "a lot of edge" if an AI receptionist covers calls.
HEIC photos from iPhones carry rich EXIF data that helps optimization; "Google reads the [image] with vision AI". Not shown; Google is widely reported to strip EXIF on upload.
Facts on the page (license number, years in business, certifications) "impact rankings in AI". Spoken only.
Flat keyword-rich URLs beat nested URLs. Observation, no data.
A single Chamber of Commerce link "can help you get a really good ranking" in Maps.
Scaled location pages are "penalized very hard" in local.
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
GBP:
Keyword in the business name only via the legal name or a state DBA filing (US). GREY (WHITE only when the business genuinely trades under that name)
Pick primary and secondary categories with Pleper's GBP category helper (share of competitors per category; HVAC contractor vs air conditioning service both 15.6% in his example). WHITE
Seasonal businesses: switch the primary category by season. GREY (category churn can trigger re-verification or suspension)
Benchmark review count, monthly review velocity and average rating against the top 3 competitors. WHITE
Ask customers to mention the service and city in their reviews; hand out a business card with a review QR code (made in Canva). WHITE if not scripted or incentivized
Show the address; do not run as a service-area business. WHITE only for a real, staffed location
Fill every field: services and descriptions, products, categories, socials, posts (he automates posting from Dropbox). WHITE
Media: ask clients for original iPhone photos and videos (HEIC), add keywords to file names and text. WHITE (EXIF benefit asserted)
Mark 24/7 hours if calls are covered 24/7. GREY unless the business truly operates 24/7 (GBP hours must be real)
Website (photo 02): 10. Meta title, description, H1, H2s. WHITE 11. Put "near me", "near you" and "nearby" in FAQs, H2s or the meta title (he concedes it is keyword stuffing). GREY 12. Keyword-rich internal anchor text from the homepage to each service page. WHITE-to-GREY 13. NAP (name and phone) in the footer. WHITE 14. Add equipment brand names (Goodman, Mitsubishi) and brand partnerships. WHITE if true 15. Embed reviews on the site. WHITE 16. Add facts: license number, years of experience, certifications; a menu (photo 02 "Menu (imp.)"). WHITE 17. Optimize the page the GBP links to (often the homepage). WHITE 18. Content tools: Cora, Page Optimizer Pro, or scrape top competitors for entities, topics, n-grams, semantic triples and categories. WHITE 19. Consolidate tier-2/3 service pages that get no traffic; flat keyword-rich URLs. WHITE
Citations and links (photo 03): 20. Citations and data aggregators (BrightLocal, Yext and others; he also buys a citation "gig"). WHITE for real listings 21. Chamber of Commerce; foundational social profiles; directories (BBB, Yelp, MapQuest); guest posts; brand partnerships (Goodman). WHITE 22. Cloud stacks; "YT citation, BatchGeo, map embed — gather all entities and start embedding all of those" across Web 2.0 properties. GREY/BLACK (manufactured link and embed networks) 23. Local resource pages, then outreach to local influencers. WHITE
Diagnosis (photo 04): 24. Connect heatmap software (he uses Local Dominator) + Pleper + DataForSEO + Ahrefs/Semrush in a Claude skill with historical data; for each drop, list who took the spot and what they changed (new listing, category added, pin moved, website changed, reviews). WHITE
Bonus tips: 25. CTR manipulation: an "undetectable" Android phone system, Facebook ads at $2–3/day sending clicks to the GBP URL, and named CTR vendors. BLACK 26. Buy aged GBPs, or rent a location for 3–4 months and leave. BLACK (fake or temporary addresses break GBP guidelines) 27. Separate profiles per service line (HVAC vs plumbing). GREY/BLACK unless they are genuinely separate businesses or locations 28. Check the client sits inside the city boundary. WHITE 29. Do not mass-produce location pages. WHITE 30. Local Services Ads for every eligible client (photo 05): complete every field, answer within 5 seconds, cover calls 24/7 (AI answering service such as Avoca), at least 10 photos a week, get reviews and reply quickly. WHITE
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
Whitespark 2026 Local Search Ranking Factors: source of the factor list (spoken). Photo 01's diagram is BrightLocal's "Google's Local Ranking Factors".
Pleper ("Pleba/Plebber/Pieper" in audio; "Pleper" on photos 04 and 06): GBP category helper; historical listing data.
GMB Everywhere, Local Dominator (heatmaps; or "own vibecoded through an API"), Hey Clicky: photo 06 tool list.
DataForSEO ("Dfs"), Ahrefs, Semrush: competitor data in his diagnosis skill (photo 04).
Cora, Page Optimizer Pro: on-page analysis.
BrightLocal, Yext: citations; another aggregator name garbled ("lean stack").
BatchGeo: map embeds (photo 03).
Canva: review QR cards. Dropbox: post automation.
Avoca: AI answering service (photo 05).
IMG Courses / Kyle Roof ("Kyle Roo" in audio): platform where he was a local SEO tester.
Joy Hawkins / Sterling Sky: source of the address-hiding study (C18).
A named CTR vendor (audio: "Chris Palmer"; likely mis-heard; not used).
Slide photos
Full text of each slide: ../resources/yash-singh/slide-text.md
01-gbp-ranking-three-things.jpg: "Whole GBP ranking is around 3 things: Proximity, Prominence, Relevance" with a BrightLocal Venn diagram; lower boxes partly hidden ("…listings / citations", "…-page signals", "…personalization"; "Reviews", "Behavioral").
02-what-to-optimize-website.jpg: "What to optimize:" meta title/desc/H1/H2s · "near me", "near you", "nearby" in FAQs, H2s or meta title (right edge cut off) · keyword-rich anchors to service pages · NAP in the footer · brand names (ex – Goodman hvac…) and partnership · review embed · facts: license number, years of experience, certifications · Menu (imp.). Image of AC / Air Duct / Air Handler service tiles.
03-other-link-building-methods.jpg: "Other Link Building Methods We Use": Chamber of Commerce · foundational link (social media) · directories (BBB, Yelp, MapQuest, etc.) · Cloud Stacks · Guest Posts · Brand Partnership (Goodman etc.) · "Make YT citation, Batchgeo, map embed and gather all entities and start embedding all of those." · last line blocked ("Loca… …ces – then re…t", local resources then outreach).
04-reverse-engineering-decline.jpg: "Reverse-engineering — Know: why & what. Connect a heatmap software + Pleper + Dfs + Ahrefs/Semrush/DFS." Chart "AC, furnace and plumbing, week by week" (Plumbing, AC, Furnace panels) and a keyword table labelled "Decline". Chart numbers too small to read; not used.
05-turn-on-lsa.jpg: "Turn on LSA for all the clients": every business info, answer within 5 seconds, cover calls 24/7 (AI answering service like Avoca), at least 10 photos a week, get reviews and reply quickly.
06-tools-list.jpg: "And some tools to make your life easier": Pleper · GMB Everywhere · Local Dominator or own vibecoded through an API · Hey Clicky.
Q&A (question → answer)
None recorded. He offered questions after the talk; the host closed.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
Omits the black-hat bonus tips entirely: CTR manipulation (Android phone farm, $2–3/day Facebook clicks to the GBP, CTR vendors) and buying GBPs or renting locations for 3–4 months. The summary's "Separate GBP profiles per service" softens the "buy multiple GBPs" passage.
"Flippa (for historical competitor data in Claude)" is Pleper (photo 04).
"Foundation links … (e.g., ACCA, MapQuest for HVAC)": the slide says BBB, Yelp, MapQuest.
"Map embed placement" as a ranking factor is most likely "proper placement of the map pin" (Whitespark factor); garbled in the audio.
"Top GBP factors (WhiteSpark 2026…)": photo 01 shows a BrightLocal diagram; the list itself is spoken.
"Physical address showing on GBP" and "Address visibility" are two separate items in his list (physical address in city of search; address shown vs service-area business).
"Mark 24/7 if possible for edge": he tied it to having an AI receptionist; the summary omits that hours must be real.
"Respond within 5 seconds" applies to Local Services Ads lead calls (photo 05), not to GBP generally.
"Avoid bulk AI-generated location pages": he said scaled location pages in general, AI or not.
"Pieper GMB tool" and "Add Review embedded to site" in the private notes are the note-taker's lines.
Speaker background (20 years old … IMG Courses) is the host's introduction plus his own.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
"Document Pro was one of my SEO clients" (possibly Page Optimizer Pro) and "featured in a book, casual SEO": garbled.
"16.64 → 12.616" is as heard; likely 12.61 or 12.66.
"White Bull plumbing", "lean stack", "Chris Palmer": speech-recognition spellings.
The photo 04 chart values.
Whether AI Mode / ChatGPT local answers actually track map rank was asserted, not tested.
Become the Answer — Zhivko Stoyanov (GIGALinks.com / SEO.BO; same group as C11's SEO Domains + Giga Links)
Source: Granola https://notes.granola.ai/d/0057381e-c04c-4dd2-a34c-e2c0cd9d3f56 · recorded 2026-11-15 (12:14 GMT+7; Granola 2026-11-14 21:14 PST), LLM Mastery session · transcript-verified 2026-11-16 Resources: 6 slide photos saved to ../resources/zhivko-stoyanov/photos/ (6 of 6, all non-zero; 5 readable, 1 too blurred to read). No handout. Private note: https://seo.bo/ Vendor talk? ⚠️ Yes, an open pitch. Sells GIGALinks.com (guest posts and "citations across the web", self-serve network or managed "we write it and choose where it's published") and SEO.BO (white-label SEO agency). Spoken close also pushes a 200,000-domain marketplace for building your own PBN (audio "ACL domain", most likely SEO Domains, the C11 company). The speaker said at the start he had not slept for four days and had swapped his planned PBN talk for this one.
Thesis (3 bullets max)
An LLM repeats what "the crowd" (other websites) says; control the rumor and you control the answer. Being in the answer matters, position in it does not.
"Poison the training data": a paper shows 250 documents can compromise a model of any size, but competitors are pouring too, so you must keep feeding the same story without stopping.
Sell it to clients as a story, not an ad (the "Jenny the baker" parable); his network is the story carrier.
Measured claims
| claim | number | base / sample / period | who measured | spoken or on slide | confidence |
| 250-document poisoning | "250 poisoned documents similarly compromise models across all model and dataset sizes, despite the largest models training on more than 20 times more clean data" | pretraining experiments, models 600M–13B parameters, 6B–260B tokens; the attack is an injected backdoor | Souly, Rando, Chapman, Davies et al. (UK AI Security Institute, Anthropic, Alan Turing Institute, OATML Oxford, ETH Zurich), arXiv, 8 Oct 2025 | slide, photo 01 (abstract with that sentence highlighted); spoken as "a paper from Anthropic" | the paper is real and the sentence is on the slide; it measures backdoor triggers in models trained from scratch, not brand recommendations in deployed, search-grounded assistants. His use of it is an extrapolation |
| Four client cases | cybersecurity firm, residential proxies, a physician/surgeon, a crypto gambling platform: all "absent" from AI answers before, present after | no prompt counts, no run counts, no engines named per case, no post volume per case, no period ("I can't tell you how much time"), no control | GIGALinks (vendor) | before/after screenshots on stage; none photographed by the note-taker | self-reported screenshots; nothing measurable recorded |
| Case positions | residential proxies: #6 in one answer; physician: #2, "next to the top-rated surgeon in the country"; Bitcoin gambling: #3 for "what is a good platform for bitcoin gambling", and present for another prompt on another model | single prompts, single runs as shown | vendor | spoken | single screenshots; repeat-run variance (C15, C38: <1% identical lists) makes one run uninformative |
| Volume needed | casinos: "won't do with a hundred posts", probably 500 or 1,000; some clients post about ten a week (audio garbled) | none | speaker | spoken | rule of thumb |
| Prices | none stated in this talk; "register now" for free credits | — | — | spoken | C11 gave $40 per post and 6,000 credits for $25,000 |
Asserted mechanisms (no evidence given in the talk)
LLMs are "gradient descent matrix multiplications", not Boolean retrieval, so being cited works differently from ranking. Stated, not shown.
Whatever story is fed consistently across enough sites becomes the answer; "as long as you are seen everywhere, it doesn't matter what you are saying".
Competitors' content overwrites yours as soon as you stop posting.
Position in the answer does not matter because users ask a follow-up question that narrows the list. Conflicts with C15's first-pick data (rival recommended first 44% vs 20% at equal mention rates).
Engines are learning to exclude manipulation, but "if you poison every source of data, they cannot improve it".
A PBN "makes one source sound like thousands" (photo 04).
Tactics and how-to steps (the actual procedure, in order, with tools and prices named)
Map the parable to the web (photos 03–04): square = internet; princess = brand; balcony = the SEO position the rumor points to (SEO.BO); herald = guest post with a link; stage = authoritative site; rumors = citations / mentions across the web; whisper = PBN; the person beside you = the AI. GREY (paid guest posts, no disclosure stated) / BLACK (PBN)
"You don't climb to the balcony, you build the square that points at it": (1) place the voice (guest posts from authoritative sites), (2) spread the rumor (a network of citations until it is consensus), (3) hold the balcony. BLACK as described (manufactured consensus)
Feed one consistent narrative everywhere, never contradict it; vary formats (lists, comparisons, client testimonials, stories). The consistency and format variety are WHITE on owned and earned channels; at network scale it is BLACK
Seed the story on Reddit, Facebook "or whatever you can think about", continuously. BLACK (astroturfing; platform rules)
Check answers by location, account state (logged out, free, each paid tier) and every model available. WHITE
Use GIGALinks self-serve (push your own content) or managed service; resell via SEO.BO white label so the agency stays invisible to its client. GREY / BLACK; white-label resale of undisclosed placements is a client-trust issue
Build your own PBN from the 200,000-domain marketplace. BLACK
He also said: do proper SEO as well, and do not rely on his product or any competitor's alone. WHITE
Tools, vendors, people and URLs named (with what each was said to do, and price if given)
GIGALinks.com (slide; audio "Gigarinx", "Gigarins", "data links"): heralds, stages, rumors and the whisper (PBN); self-serve network or managed service. No price given here (C11: $40/post; $25,000 for 6,000 credits).
SEO.BO (slide; private note https://seo.bo/; audio "CLO"): white-label SEO agency, "the SEO position the square points to".
Domain marketplace, 200,000 domains (audio "ACL domain"): most likely SEO Domains, run by C11's speaker. Not confirmed on any slide.
Souly et al., "Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples", arXiv, 8 Oct 2025 (ID partly hidden on the slide, ends "…92v1").
Slide photos
Full text of each slide: ../resources/zhivko-stoyanov/slide-text.md
01-poisoning-paper-250-documents.jpg — title page and abstract of the Souly et al. paper; authors and affiliations (UK AI Security Institute, Anthropic, Alan Turing Institute, OATML Oxford, ETH Zurich); highlighted: 250 poisoned documents compromise models across sizes; abstract text mentions backdoors, 600M–13B parameters, 6B–260B tokens. Right edge shows a cut-off "25…" title slide.
02-not-the-only-poison-master.jpg — illustration; "You are not the only poison master. Everyone's pouring. Only the strongest survives the current."
03-gigalinks-seo-bo-square-map.jpg — GIGALinks.com → heralds (guest post with a link), stages (authoritative site), rumors (citations across the web), the whisper (PBN, carries the name to everyone); SEO.BO → balconies (the SEO position the square points to). "The voice, the stage, and the position — every lever, one square."
04-analogy-and-the-play-mapping.jpg — "Swap the words, and the parable becomes a playbook"; full mapping table; three steps (place the voice, spread the rumor, hold the balcony); "PBN makes one source sound like thousands".
05-bakery-story-mapping-gigalinks.jpg — Jeny and her bakery = the brand; Leo = GIGALinks; Willowbridge = the internet; noticeboards = citations on sites in the GIGALinks network; "Leo doing more of the work" = Managed Service ("we write it and choose where it's published"); the town's readers = the AI.
06-blurred-unreadable.jpg — motion-blurred; appears to be the same bakery mapping slide; unreadable, not used.
Q&A (question → answer)
None recorded.
Corrections to the Granola summary (what the summary got wrong, garbled, or left out that matters)
"Gigarins" is GIGALinks.com (slide 03). The summary never names it correctly.
"CLO white-label SEO agency" is SEO.BO (slide 03, private note).
"ACL domain marketplace (200,000 domains)": audio garble; most likely SEO Domains (C11). Not on a slide.
"Anthropic paper: 250 documents of consistent, flowing information can shift model outputs" overstates it. The paper (multi-institution, Anthropic one of five) shows 250 poisoned documents can implant a backdoor during pretraining of models up to 13B parameters. It says nothing about steering brand recommendations in retrieval-grounded assistants.
The "Next steps" item ("Register now to claim free credits; evaluate the ACL domain marketplace as a PBN starting point") is the vendor's closing pitch, not an action the note-taker agreed to.
Omits the residential-proxies case (#6) and that none of the four cases had numbers, periods, prompt counts or controls.
Omits that he said not to rely on his product alone and to keep doing proper SEO.
Omits that he swapped his planned PBN talk at the last minute and said he was unwell.
Unclear / needs verification (mis-heard names, numbers you could not pin down)
Speaker name and company come from the Granola title and the slides; no slide photo shows his name.
The domain marketplace name ("ACL domain") and its 200,000-domain count are spoken only.
arXiv ID of the paper partly hidden ("…92v1"); not looked up.
Case-study screenshots were not photographed; the residential-proxy client name ("J Flash") is a speech-recognition spelling.
"Ten posts a week" is a garble ("a tender post a week").
Date: Granola timestamp converts to 2026-11-15 local; the assignment places it on the LLM Mastery day.