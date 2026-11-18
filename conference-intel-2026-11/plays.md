# Revenue plays from the conference, ranked

Every value here is a projection. Where the inputs are weak the size is given
as High, Medium or Low, never as a figure. Anything public-facing or paid goes
through the Skill 12 gate.

Ranking is by expected return against cost to test, for this business as it is:
62 affiliate sites, a handful of brand clients, LoadLander and the freight kit,
a YouTube channel, the tool sites.

## Do first: cheap, and the evidence is good enough

### 1. Decide what careerspy.org lets in

Checked properly on 2026-11-18 (Cloudflare analytics for verified bots, seven
days): careerspy.org refuses training crawlers and serves search and assistant
fetchers. GPTBot 110, ClaudeBot 42, GoogleOther 47 and Meta's crawler 3,546
requests all got 403; ChatGPT-User got 200 on 122. So the site can be cited in
a live answer and is being kept out of training data.

An earlier spoofed-user-agent probe said ten zones were closed. Nine are not.
The detail is in `ai-crawl-access/`.

The change is one dashboard setting on one zone, and it is Adrian's to make.
Size: Low. It removes a reason for the channel's site being unknown to models;
it does not by itself earn anything. Cost: two minutes.

### 2. Answer-first rewrite on a matched test set

The cheapest on-page change with two independent vendor datasets behind it:
29% of cited passages come from a page's first 50 words (Surfer); pages whose
first paragraph answers the question supply 18% of the answer against 5%
(Senuto). Uses facts already on the page, so the fact gate is easy.

Run it as a test, not a rollout: 20 to 30 pages on one earning site, a matched
set left alone, read at 28 and 90 days on Bing clicks, Google clicks and AI
citations. Size: Medium. Cost: DeepSeek tokens and one approval batch. Method
in `answer-ready-pages/`.

### 3. Sell sponsored slots on our own best-of pages

Three speakers arrived here independently. Leo, asked what he would do with
1,000 sites: "sell listicle positions". Suski sketched a long list with slots
priced by position. Joy Hawkins reports best-of list sites with "wild" traffic
growth and one that quadrupled its prices. Surfer's slot data gives the price
logic: named 52% of the time at number one, 32% at five, 13% from ten down.

We already own the inventory and the disclosure habit (esyoh units carry
"Sponsored listings"). A labelled, position-priced sponsored slot on a
programme or tool list is the same thing sold directly. It also answers the
automechanicschools problem, where pages monetise with no advertiser on them.
Size: Medium to High, depending on whether schools buy direct. Cost: one pilot
page, a rate card, and outreach that Adrian approves. Disclosure is not
optional (FTC).

### 4. The AI visibility audit as a paid deliverable

Four talks describe pieces of one product that agencies are already selling:
the access audit (Burns: can crawlers reach it, is it in Common Crawl, does it
render without JavaScript), the Door Audit (Takas: inclusion rate and
gatekeepers), the perception diagnosis (Kiekbusch: absent, mis-framed,
out-ranked, wrong axis), and the goal reset (the reporting talk).

We have most of the tooling already: `cf_ai_control.py`, `agent_ready.py`,
`perf_audit.py`, `query_battery.py`, `backlink_profile.py`. Packaged, that is a
fixed-price audit for brand clients and the natural first sale after the
directory foot-in-the-door. Kasra Dash says UK companies are moving PPC budget
into "GEO" and buying it under that name. Size: Medium. Cost: assembling a
report template; no new data spend beyond DataForSEO pennies.

## Do next: needs a decision or a build

### 5. LoadLander: build the post-click system the HighLevel talk describes

Jeremy Burgos (HighLevel) laid out exactly what a GHL sub-account product
should do after a reply or a click: first message inside five minutes on the
channel the lead used, opening with a qualifying question; AI voicemail capture
when nobody answers; follow-ups mapped to the nine places a lead goes quiet.
His opening story is the pitch: the client blamed call tracking and nobody was
answering the phone.

Brokers who buy the freight kit generate replies. What they lack is the part
after. That is LoadLander's reason to cost $99 a month, and it is a feature
list rather than a research project. See `outbound-replies/`. Size: High
relative to the product, because it is the retention mechanism. Cost: GHL
workflow build.

### 6. An exact-match tool site as the front door for LoadLander

David Quaid's best-evidenced story is freeloadbalancer.com: an exact-match
domain offering a free version of the product, styled as part of the brand
family, live since 2015, which he says produced 160 leads in week one and
about 50 a month for a decade, with three such domains supplying a quarter of
the company's leads. Grade C, self-reported, but it is one of the few cases in
the set with a ten-year tail.

We already build exactly this shape in `~/tool-sites`. A free, useful freight
tool on an exact-match domain (a lane-rate or margin calculator, a carrier
packet checklist), openly branded LoadLander, is the same play. The versions
he also described, styled as an independent third party or as a competitor's
support page, are refused. Size: Medium. Cost: one tool-site build.

### 7. The outbound opener that already tests well

Thibault Garcia's one measured case: changing a single line took positive
replies from 7% to 34% of replies. The losing line offered a finished audit
and asked for a meeting. The winning line named the buyer's own search, said
they were absent from ChatGPT and page one, and asked permission to send a
checklist. It maps directly onto agency prospecting from the directory, with
two edits: check the absence for real before saying it, and drop "within 45
days", which is a promise. See `outbound-replies/`. Size: Medium. Cost:
nothing beyond the sending already planned.

### 8. Profit share or phantom equity for local clients

Dennis Yu's model: a landscaper who started on $3,500 a month and moved to
aligned equity. Phantom equity is a contractual share of proceeds on a sale
with no shares issued. It suits exactly the clients the directory strategy
finds, where a retainer undervalues work that lasts. It needs a lawyer and a
client whose books Adrian can see. See `agency-economics/`. Size: High per
client, slow. Cost: legal drafting once.

## Watch: interesting, not ours yet

### 9. Licensing operational data to AI labs

Real market, wrong fit. Buyers want about 30 desk staff, two years of email,
Slack, Drive, CRM and call recordings, and they quote $100K to $500K (Dom
Wells, who brokers these deals and is paid when they close). Galena Hall does
not have the headcount. Two things are worth keeping:

- **Referral.** Typical commission is about 6%, some 10%, some a flat $10K to
  $20K. A brand client with 30+ staff is a referral worth a five-figure fee.
  Ask the question during onboarding.
- **Due diligence.** If Adrian buys a site or business again, ask what
  operational data comes with it.

Buyer names in the notes are speech-recognition spellings. Verify any of them
on their own sites before contact, and expect unanswered GDPR and employee
consent questions.

### 10. ChatGPT business profiles

Mentioned in four sessions as newly launched: a verified brand profile with
product feeds and mention data, described as a cross between Google Business
Profile and Search Console, US businesses first. Nobody had results and one
speaker said claiming does not raise visibility by itself. Claim it for
Lisclare and LoadLander when it is available to them. It is free and it is the
kind of thing that is worth having early.

### 11. Quiz rebuilt as a game with the offer on the result screen

A "which trade fits you" game on a vocational site, with the school listings on
the result screen. Zero conversion evidence was shown. The useful habit is the
speaker's test budget: about $50 of ads per prototype. Low priority.

### 12. Chinese exporters as agency clients

A real gap (few local SEO agencies for a very large number of exporters) from
someone who sells the introductions. Needs in-person presence and a local
middleman. Not now.

## The strategic one

Thomas Smale has sold more online businesses than anyone else in the room.
What he said about valuation applies to the whole portfolio:

- What drives price is growth, recurring revenue with existing customers
  paying more over time, and profit. AI has not changed that.
- The most overvalued thing to buy is a business that depends entirely on free
  organic traffic with no moat. The most undervalued is an agency.
- ChatGPT went from nothing to his firm's top lead source in twelve months
  while organic fell.
- Asked directly by someone with a working site portfolio, he said to double
  down on what works, and that diversifying was his own mistake.

Read together: keep the sites, and convert what they are good at into
recurring revenue. Sponsored slots sold monthly (play 3), LoadLander (5, 6),
audits that become retainers (4) and profit share (8) are all the same move.
A second site network is not.
