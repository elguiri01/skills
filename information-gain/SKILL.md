# Information gain: why a page is allowed to exist

Skill 11 governs how a sentence reads. This governs whether the page should
have been written. A page can pass Skill 11 completely — grade-7, no banned
vocabulary, no em-dashes, humanized — and still be the exact thing that gets a
site removed. Read this before Skill 11, because it decides whether there is a
page to style.

## The test

> Could a competitor publish a near-identical version of this page tomorrow,
> using the same prompt, the same method and the same public inputs?

If yes, the page has no reason to exist. It does not matter that it reads well,
that it is accurate, or that it is better than what currently ranks. A thing
anyone with the same software and the same inputs can reproduce is a copy that
happened to be published first.

Apply it per page, before writing, not after.

## Why the failure is slow, and why that matters

Lily Ray tracked 220+ sites and found a consistent shape: organic pages climb
for 6–12 months, traffic peaks 3–6 months after the content peaks, then falls
away. Glenn Gabe calls the chart Mount AI. In her set, 54% lost 30%+ of peak
traffic, 39% lost half, 22% lost three quarters, and many ended below where
they started.

**Read the provenance before quoting any of that.** These are third-party
estimates — Ahrefs organic traffic and page counts, cross-checked against
Sistrix so the pattern had to hold in two independent data sets — not Search
Console. That cross-check is worth more than it first looks: Sistrix's
Visibility Index is derived from ranking positions rather than modelled
clickstream traffic, so two methods built on different assumptions agree. Two
traffic estimators agreeing would share the same modelling flaws; these do not.

The sites were *not* randomly sampled: they were pulled from the customer-story
pages of a dozen-plus AI content platforms, so the set is selected for sites
vendors chose to advertise. No causation is claimed, and no vendor or domain is
named. It is a strong pattern and a weak statistic. Use it to generate a
hypothesis about our own sites; never quote the percentages to a client as if
they were a controlled study. Our own standing rule applies: compare against a
control, because the +707% that turned out to be seasonality is what happens
when we do not.

The delay is the trap, and it is the part worth internalising. If scaled
template content failed immediately, it would be a cheap lesson — publish,
nothing ranks, stop. Instead it works long enough to believe in, long enough to
scale, long enough to build an operation on and sell to a client. By the time
it reverses, everything is sitting on top of it.

**The delay is not Google deliberating about your pages.** The footprint forms
on everyone else's sites. One site running a template looks like a site that
publishes a lot. Ten thousand sites running the same template through the same
prompt is a signature, and once the pattern is obvious it becomes cheap to act
on — and everyone running it gets caught together, including whoever ran the
best version of it. This is why "but ours is better written" is not a defence.

The mechanism is not new. The September 2023 helpful content update and the
March 2024 core update both targeted content produced at scale to rank, and the
scaled content abuse policy that shipped alongside says authorship is
irrelevant: human, AI, or a mix. Sites publishing original human-written copy
were hit when it carried so much SEO structure that no person had a reason to
write or read it. The packaging changed; the pattern did not.

## The eight templates, and the four we run

Ray found eight templates recurring on the declining sites. Most sites in
trouble ran three or four; the worst hit ran all eight.

| template | do we run it |
|---|---|
| Programmatic location/language pages, one per city or country | **yes, at scale** |
| "What is X" glossary pages, one term each | yes, in places |
| "Best X for Y" listicles | **yes** (`listicle-agent`) |
| FAQ farms, one question per URL | yes, in places |
| Comparison pages at scale, A vs B | rarely |
| Self-promotional listicles placing yourself at #1 | no |
| Competitor-alternative pages, one per named rival | no |
| Off-topic content at scale for keyword volume | no |

None of these is listed because it fails to rank. Every one of them works —
that is precisely why enough people built them for the shape to become
detectable. Ranking is not evidence that a page is safe.

**This is the second independent source telling us the same thing.**
`grow-search-visibility` already rejects "near-duplicate query permutations"
and scaled low-value publishing, and CLAUDE.md already records the obvious
reading: a portfolio of 62 sites running state pages off a shared template is
the shape being described. Our `/es/` sections — one template translated across
a section — are named in the study explicitly. Two sources arriving
independently at our architecture is not something to argue with.

## What actually separates our state pages from a plumber's city spam

The study's worst case is a local service business spinning "plumber in
Sugarland" across a 50-mile radius. That fails for a specific reason, and it is
not page count: **the page claims something untrue.** It tells a reader there
is a plumbing business in Sugarland when there is no address, no coverage and
no completed jobs there. Google knows where the business is, because the owner
said so on the Google Business Profile. The page is a claim with nothing
behind it.

Our state pages are not that claim. A page about vet tech programmes in
Washington makes no assertion that we are in Washington; it asserts things
about Washington's programmes, licensure and wages, and those can be true,
sourced and checked. The architecture is defensible in a way the plumber's is
not.

That is the defence against *deception*. It is not a defence against
*reproducibility*, and that is the one we keep failing.

**Accurate salary and school data is necessary. It is not sufficient, and the
difference is assembly.** A page that omits what a programme costs, what the
job pays, or which schools are accredited has failed the reader outright, so
accuracy is not optional and never a thing to trade away. But accuracy alone
does not answer the reproducibility test, and the line between the two is not
"public versus private" — it is **restating versus assembling**.

- **Restating one public table is reproducible.** Correctly quoted BLS OEWS
  wages are available to every competitor on the same terms. The item129 and
  item152 corrections on electricalschool — "stale wage prose restated from
  BLS OEWS May 2025" — were necessary and right to ship, but they buy
  *accuracy*, not a reason to exist. Repairing a defect and building a
  differentiator are different jobs; finishing the first does not advance the
  second.
- **A maintained multi-source join is a moat, even though every input is
  public.** Nobody else holds ARRT pass rate, completion rate, job placement
  rate, resident tuition, programme length and accreditation status for 742
  radiography programmes in one comparable table. JRCERT publishes those
  figures one programme at a time across 742 separate pages; the assembly, the
  normalisation and the upkeep are the work, and a competitor would need months
  to match it and would then have to maintain it. That is not reproducible
  tomorrow with the same prompt.

**radiologyed is the proof, and the revenue agrees.** It carries that table
live on its state pages (47 programmes on Texas, 44 on Florida), and it earns
$10,122 per 90 days — more than the next three sites combined. The one site in
the portfolio with a genuine assembled moat is the one that makes the money.
Treat that as the model to replicate rather than an accident.

Where the automechanicschools city page quoted state-level projections as
though they described the city, it crossed from reproducible into the
plumber's error: a claim with nothing behind it. The fix was to make the page
carry something true of the city, not to delete it. That instinct was right and
it generalises.

## What we have that nobody can reproduce

A local service business generates new information daily — what the pipe looked
like behind the wall, what the job cost in that neighbourhood last month, which
failure keeps appearing in houses built in the 90s, which inspection the city
always flags — and almost none of it reaches the internet. That is the
advantage B2B SaaS lacks, which is why those companies end up writing about
baby names: there is no information left to gain about their own product.

We are closer to the local business than to the SaaS company, and we have
barely used it. What is genuinely ours:

- **`vt_licensure_claims`** — per-state licensure verified against primary code,
  not board summaries. Washington's six routes in WAC 246-935-060, where the
  Department of Health's own page omits the apprenticeship route. No competitor
  publishes that correctly because almost nobody reads the code. Non-reproducible
  without doing the same work.
- **`avma_cvtea`** — 216 CVTEA programmes across 49 states, joined against IPEDS
  so a page can show which programmes are *not* accredited. That join is the
  thing a student actually needs and nobody publishes.
- **`lead_buyer_footprint`** — 590 campuses of 543 lead-buying brands, 88 with
  vet programmes across 32 states. Nobody outside this operation has it.
- **`sp_listings`** — maintained official programme names and real college
  programme URLs. Maintained research, not a scrape.
- **Our own GSC and `esyoh_leads`** — what people actually ask *our* pages, and
  which pages produce leads at what value. pharmacistschools' CVS page turning
  58 clicks into 11 leads is a fact that exists nowhere else.

A competitor can copy any prompt we write. They cannot copy our Search Console,
our lead data, our licensure research or our accreditation join.

## Building moats on purpose

The question to carry into every content decision is not "is this accurate"
but **"what is on this page that could only have come from us, and how do we
get more of it?"** Ranked by what it costs us:

**1. Crossing two or more public sources to produce a figure that exists in
neither.** The cheapest moat of all and the most overlooked, because every
input is free. The gain is not in either source; it is in the cross. Nobody
else did the join, so nobody else has the number.

`careerspy-net-price` is the worked example and already calls itself the
portfolio's moat: IPEDS SFA publishes a net price band, the federal SAI Guide
publishes a formula, and crossing them yields a computed Pell grant and net
price shown beside the published band — a figure neither source contains.
Likewise merit aid assembled out of each school's own Common Data Set
section H2A, and Georgia HOPE rates crossed against per-school cost.

The same move is available everywhere and mostly unused:

- **BLS OEWS wage crossed with IPEDS net price** gives cost-to-earn: what the
  programme costs against what the job pays in that state, and how long it
  takes to pay back. Neither source publishes it. This is the single most
  useful number a prospective student could be given, and we hold both halves
  for every vertical already.
- **CVTEA accreditation crossed with IPEDS completions** shows which programmes
  in a state are *not* accredited — the thing a student most needs and nobody
  publishes.
- **BLS projections crossed with programme capacity** (we hold `total_capacity`
  for 724 of 742 radiography programmes) indicates whether a state is training
  more people than the roles it expects.

Rules that keep a crossed figure honest: show both inputs and their years,
state the method, never present a derived number as though a source published
it, and carry the source's own caveats through (the net price cohort caveat is
the standing example). A cross that cannot be explained in a sentence is a
guess wearing a decimal point.

**2. Assembled public data, kept current.** The same inputs, many sources, one
comparable table. The radiologyed JRCERT table is the worked example and it
generalises directly: CVTEA for vet tech (216 programmes, where we already hold
accreditation status, probation and deficiencies), and the equivalent
programmatic accreditor for every other vertical. A sortable, maintained,
programme-level outcomes table is the highest-value thing we can build without
talking to anyone. **Build this on any site that earns.**

**3. Our own aggregated behaviour.** We know which programmes people actually
enquire about, from which states, and what those enquiries are worth. Properly
aggregated and anonymised, "the most-requested vet tech programme in
Washington" is a real statistic that exists nowhere else and costs nothing to
produce. Never publish anything traceable to an individual enquirer, and never
contact a lead we have sold.

**4. Surveys of our own readers.** pharmacistschools alone draws 602k
impressions in 180 days. A short on-page survey — what surprised you about the
cost, did you finish, where are you applying — produces a proprietary dataset
that compounds every month and that no competitor can obtain at any price.
Cheap to run, and the output is quotable, citable and genuinely useful.

**5. Expert interviews.** This is where the real authority is, and we are
already holding the contact list: **`jrcert_programs` carries the programme
director's name for 741 of 742 programmes and an email address for 741 of
them** — professional contacts published by JRCERT itself. Ten interviews per
vertical with programme directors would give every state page something no
template can produce, and the outreach doubles as E-E-A-T (Skill 06), persona
authority (Skill 16) and a legitimate route to editorial links. `sp_listings`
and `avma_cvtea_programs.institution_url` give the same route for other
verticals.

**6. Student quotes.** The most valuable and the most dangerous. Real students
describing what a programme cost, how long the waitlist was, or what the
clinical rotation was actually like is exactly the "information that exists and
never reaches the internet" the whole method turns on.

**The hard rules, which are not negotiable:**

- **Never fabricate a quote, a student, a reviewer or an interview.** CLAUDE.md
  already forbids publishing under a real person's name without consent; an
  invented student on a page where someone is deciding where to spend tuition
  money is the worst thing this operation could publish, and it would be
  indefensible if found. There is no volume argument that beats this.
- Real people, named only with consent, and we keep the consent.
- Material quoted from a public forum is **attributed and linked**, never
  passed off as ours and never lightly reworded to look original. Reddit and
  programme forums are a legitimate source of what students actually ask; they
  are a source to cite, not a well to drain.
- A quote that cannot be sourced does not get published. Same standard as the
  licensure work, for the same reason.

**Creativity is required here, not optional.** The eight templates exist
because they are the obvious thing to do, and the obvious thing is by
definition what everyone else is also doing. Anything reachable by a prompt
alone is reachable by every competitor's prompt. The moat is always something
we went and got.

## What the AI is for

The tools in that study were one prompt in, one page out. That architecture is
why every page they produced was reproducible by the next person with the same
subscription. The model should collect and assemble, not originate.

**Give the model:** site architecture and category mapping, the brief, titles,
H1s, internal linking plans, schema, turning verified notes into clean copy,
and researching what already ranks so we do not repeat it. This is real work
that takes days by hand, and none of it is the part that makes a page worth
indexing.

**Do not let the model be the source of** the claim that makes the page worth
publishing. Every factual declaration traces to a named source, read by us, on
a recorded date. The licensure work is the standing example of why: the failure
mode is a confident paragraph citing a code section that says something else.

## The gate

Before any page is published, on our sites or a client's:

1. Could a competitor reproduce this tomorrow with the same prompt and the same
   public inputs? If yes, stop.
2. What is on this page that could only have come from us? Name it. If nothing,
   stop.
3. Does this page exist because a reader needs it, or because a search engine or
   an LLM might cite it? The second alone is not a reason.
4. Does every factual claim trace to a source we read, with a date?

Adding a near-identical page is the option that must be justified, not the
default. Effort goes into making existing pages independently worth citing.
The sites that came through 2023–24 best went narrow rather than wide: fewer
pages, tighter topics, real experience on the page.

## Client work

Everything above applies, plus:

- **Never sell scaled template publishing**, and never price work by page count.
  It works long enough to invoice for and fails after the engagement, which is
  the worst possible shape for a reputation.
- **Never guarantee** a ranking, an index, a citation, traffic or revenue.
  Unchanged from CLAUDE.md, and it binds hardest here.
- A client service business has the same untapped first-party data as any local
  operator: job history, pricing, permits, recurring failures, photos, named
  technicians. Extracting it is the billable work. `client-content-review` is
  the mechanism for capturing it from a subject-matter expert verbatim.
- If a client asks for the thing in the eight-template table, say what it does
  and over what period, then offer the narrow version.

## One claim in the source not to repeat

The video closes by saying Anthropic announced it will watermark Claude's
output, and implies an SEO consequence. **Unverified — do not put it in client
material or act on it until checked.** Verify against Anthropic's own
documentation before it goes anywhere near a deliverable, and treat any
"AI detection" claim with the same suspicion: Google's own position is that
authorship is irrelevant, so a detector would not change what the gate above
asks.
