---
name: ai-crawl-access
description: Whether AI crawlers can actually reach, store and read a site. Use when a site or client is absent from AI answers and nothing explains it, before any AI visibility work on a new client, when changing Cloudflare or firewall settings, and as the first section of a paid AI visibility audit. Covers the three stages (crawled, trained on, retrieved), CDN and firewall defaults that block crawlers silently, the Common Crawl presence check and harmonic centrality, OpenAI's three crawlers and what blocking each does, server-log verification, the JavaScript check, and our own measured position. Pairs with agent-ready-audit, which covers whether an agent can act on a page once it has it.
---

# AI crawl access

`agent-ready-audit` asks whether an agent can use the page. This asks the
question before that one: did the page arrive.

Stephen Burns, who works on Common Crawl, puts it as three separate stages and
a site can vanish at any of them:

1. **Crawled.** The request was allowed and returned real content.
2. **Trained on.** The capture survived extraction, filtering and
   deduplication.
3. **Retrieved.** A live search-backed assistant fetched it at answer time.

Blocking, a JavaScript shell, thin template copy and duplication each kill a
page at a different stage, and none of them shows up in Search Console.

## Our measured position, 2026-11-18

Two readings, and the first one was wrong. It is kept here because the way it
was wrong is the lesson.

**The spoofed probe.** `cf_ai_control.py --probe` wears a crawler's user agent
from the droplet. It reported 10 of 111 zones returning 403 to GPTBot,
ClaudeBot and PerplexityBot, and prints "these cannot be cited by
ChatGPT/Claude/Perplexity no matter what they publish". That sentence is not
supported by its own data.

**What verified crawlers actually received** (Cloudflare analytics, seven days,
bots identified by Cloudflare from published IP ranges, via
`verify_from_analytics()` in the same script):

| zone | verified AI-bot requests | reading |
|---|---|---|
| careerspy.org | 403: 3,731; 200: 1,631 | **Really blocking, by category** |
| lifecoachtraining.us.com | 200: 1,142; 403: 2 | Open |
| pilatesdigest.com | 200: 1,199; 403: 52; 400: 85 | Open, minor refusals |
| wetrainlifecoaches.com | 301: 168 | Redirecting, not blocking |
| galenahall.co.uk and four Spanish local sites | 5 to 15 requests, all 200 | Open on what little traffic there is |
| puertasgarajesanse.es | none | No evidence either way |
| radiologyed.org, electricalschool.org (controls) | no 403s | Open |

So one zone, not ten. And OpenAI's own fetcher (`ai_fetch_probe.py`) loaded
careerspy.org and quoted figures from it.

**careerspy.org by crawler**, which is the useful part:

| category | crawler | status |
|---|---|---|
| AI Crawler (training) | meta-externalagent | 403 x 3,546 |
| AI Crawler (training) | GPTBot | 403 x 110 |
| AI Crawler (training) | GoogleOther | 403 x 47 |
| AI Crawler (training) | ClaudeBot | 403 x 42, 202 x 6 |
| AI Assistant | ChatGPT-User | 200 x 122 |
| AI Search | Amzn-SearchBot, Applebot, Bravebot and others | 200 |

Training crawlers are refused; search and assistant fetchers are served. That
is exactly the category split Burns described, seen on our own zone. The
consequence: careerspy.org can be retrieved and cited in a live answer today,
and is being kept out of training data. Whether to change that is a real
choice (see "Which crawler does what"). For a site whose whole purpose is to be
the cited source, allowing training is the consistent answer.

Rules this leaves:

- **Never report a block from a spoofed user agent.** Use verified-bot
  analytics. A zone with no AI-bot visits is "unknown", not "open" and not
  "blocked".
- **Report by category.** "Blocked" and "open" are both wrong for a zone that
  serves search bots and refuses training bots.
- **CCBot was not seen on any of these zones in the week**, so nothing here
  says whether Common Crawl is getting in.
- The toggle is in the Cloudflare dashboard (Security, Bots, the AI bots
  setting). Our API token cannot read or write bot settings: `--audit` returns
  403 for every zone. It is a security setting and Adrian's to change.

## Why it is worth an hour

Common Crawl's own figures, as given on stage (insider numbers, method not
stated):

- About 35% of high-quality sites block AI crawlers, usually by accident.
- 5 to 10% of all fetch attempts are refused by robots.txt or a 403, with
  rate-limit responses and empty JavaScript shells on top.
- At least 64% of 47 language models studied were built on Common Crawl (a
  Mozilla figure).

His worked example: hyatt.com ranks 2,028th of 130 million domains for
closeness to the web's core, and Common Crawl has zero usable captures of it.
The robots.txt request itself is rate-limited, none of a 500-URL sample
returned a 200, there is no homepage capture in twelve monthly crawls, and of
13 AI crawler user agents probed live, none was served.

And the recovery lag: one client vanished from Bing Chat because a firewall
blocked CCBot, and came back four months after the fix. Blocked now is absent
for a long time.

**The Cloudflare claim to verify before repeating it.** He said that since 1
July AI crawlers are split into search, agent and training categories, and that
since 15 September agent and training crawlers are blocked by default on pages
carrying ads. No year or scope was given. Our sites carry ads. Check
Cloudflare's own changelog before telling a client this, and check what our
own zones do rather than what the announcement says.

## The audit

All of it is read-only. His free tool at audit.stephenburns.ai runs most of
these in about a minute; the note-taker did not run it and neither have we.

1. **Edge before rules.** Fetch robots.txt as the crawler. A 403 or 429 at the
   edge means closed, whatever the file says. A firewall rule outranks
   robots.txt.
2. **The CDN's AI settings**, especially training and agent categories and any
   rule tied to ad-carrying pages. A bot that does several jobs is held to the
   strictest rule, so a training block can also shut out search.
3. **Corpus presence.** Sample URLs (he uses 500) against the Common Crawl
   index. Count captures that returned 200. Check the homepage across the last
   twelve monthly crawls, and when the domain was last seen.
4. **Harmonic centrality** score and rank. This, not PageRank, sets how many
   pages CCBot will take from a site.
5. **Rendering.** Count the real words in the stored HTML. AI crawlers behave
   like early Googlebot: no JavaScript. Crawl once rendered and once raw and
   compare. Only Google among the major fetchers is reported to render.
6. **Live probe** with the main AI user agents, from somewhere that is not a
   fingerprinted datacentre IP if possible.
7. **Do not trust a 200.** It can be a blank render or a challenge page.

For our stack, steps 1, 2 and 6 are `cf_ai_control.py` (verified-bot analytics,
not the spoofed probe), step 5 is
`perf_audit.py` and `agent_ready.py`, and steps 3 and 4 are not built. Common
Crawl's index is a public API; a small `cc_presence.py` would close the gap and
is the one new script this skill argues for.

## Which crawler does what

From Marc Moeller's slide, consistent with OpenAI's published roles:

| crawler | job | if blocked |
|---|---|---|
| OAI-SearchBot | Builds ChatGPT's search index | The site leaves ChatGPT search answers |
| GPTBot | Collects for training | No effect on ChatGPT search |
| ChatGPT-User | Fetches when a person asks | robots.txt may not apply |
| CCBot | Common Crawl, used widely for training | Absent from much of the training supply |

So "block the AI bots" is not one decision. A retailer may sensibly block
training crawlers and allow user-triggered fetchers, so that a model does not
memorise a price that has since changed. That is a client's decision to make
knowingly. For our own sites, which want to be the cited source, the answer is
to allow all four.

His observation of fetch behaviour: the bot opens one page, then two or three
pages linked from it. Internal links from the page that gets fetched decide
what else is read.

## Logs

The only ground truth on who came.

- **Verify the bot.** Check the IP against the operator's published ranges.
  Spoofed AI crawlers exist and probe for exposed configuration files; confirm
  none is reachable.
- **What to keep** (Cloudflare field names): timestamp, request path, user
  agent, verified bot category, edge status, origin status, cache status, ray
  ID for de-duplication.
- **Retention.** Cloudflare Log Explorer keeps 30 days by default. Sengupta's
  pattern is a Worker writing to D1 every 15 minutes and a small dashboard of
  crawl volume, status codes and AI against search bots. `twin_performance.py`
  already counts verified AI-bot requests on twin pages; the same source
  generalises.
- **For a client**, ask IT for that view rather than raw files.

## Getting into Common Crawl

For a new or peripheral domain. Only followed links count; nofollow is
honoured.

- Publish something real on a host that sits near the web's core (GitHub,
  WordPress.com, Substack, Hugging Face) and link to the site. His own domain
  missed one monthly crawl and was in the next after a single link from a
  central profile page. One case, and an unusually central source.
- Keep the sitemap current; CCBot uses it for discovery.
- Then check the next crawl. Crawl to training takes months to a year.

For the tool sites this is nearly free: each has, or could have, a public
repository.

## The counterweight

James Dooley's test, recorded in the same notes: 200 sites, every bot blocked
except CCBot, invented terms, ten weeks. Nothing came back in any model. Being
in Common Crawl is necessary for training-time recall and is nowhere near
sufficient, and it does not act on the timescale of a campaign. Burns does not
claim otherwise.

So the order of value is: (1) not blocked at the edge, which affects live
retrieval today; (2) readable without JavaScript; (3) present in the corpus.
Fix in that order.

## Other access notes from the set

- **Markdown for agents.** Sengupta recommends Cloudflare's content
  negotiation to serve Markdown to agents that ask for it, free. This is our
  Skill 19 by another route. Nobody measured it. `twin_performance.py` is the
  evidence.
- **Prerendering** (Prerender.io, SEO4Ajax) fixes a headless build without
  replatforming. On one custom headless site, 0 of 1,806 URLs were discovered:
  no internal links, and a sitemap alone was not enough.
- **Platform agent files.** 99% of Shopify stores ship a commerce-protocol
  manifest by default against 2.6% of custom builds. Table stakes where the
  platform does it. Spend on the product data instead.
- **An English version alongside a local-language site** is claimed to raise
  ChatGPT citations sharply. Low confidence, cheap to test on one Spanish site.

## What this skill will not claim

That unblocking produces citations. It removes a reason for having none.
