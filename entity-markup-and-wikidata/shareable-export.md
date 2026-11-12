# Entities: what to mark up, what to mention, what to add to Wikidata

A method note, written from one engagement for a UK supplier of patient
handling equipment, September to November 2026. Two Wikidata items were created
in the course of it and a reconciliation pass was run over twelve concepts.
Every number here was measured rather than estimated.

**Redacted export, 12 November 2026.** This is the external copy of an internal
skill. The client, their catalogue and our file layout are removed. Nothing
else is: the measurements and the corrections are the whole value and they are
intact.

## Three jobs that get confused

Separate them before starting.

1. **Markup.** Declaring, in structured data, which known thing a page is
   about. Costs an hour, breaks nothing if done right, merges your whole
   catalogue into two entities if done wrong.
2. **Mention.** Naming the entities a topic is made of in the prose, so the
   page reads as belonging to its field. Content work with an entity list
   behind it, not markup.
3. **Contribute.** Adding a missing concept to Wikidata. Legitimate for a
   category, a deletion request for a brand, and the only one of the three
   that involves a third party's project and their rules.

Only job 1 is fully in your control. Job 3 is a public-good edit whose benefit
to any single site is indirect, and it should be described that way to whoever
is paying for it.

## The distinction that does the damage

`sameAs` asserts identity. Everything else asserts a relationship. Using the
wrong one is not a style choice.

| Property | Says | Use on |
| --- | --- | --- |
| `sameAs` | this node **is** that entity | the concept node only |
| `additionalType` | this thing is **of that type** | individual products |
| `about` | this **page** is about that entity | category and guidance pages |
| untyped `mentions` | this page **refers to** this thing | products named in prose |

Worked through: the concept "profiling bed" genuinely **is** Q141544523, so a
`Thing` node carries `sameAs` to it. An individual bed is not the concept, so
the product page carries `additionalType`. The category page is not the concept
either, so it carries `about`, pointing at the `Thing` that does.

**Getting this backwards would have merged 57 products into two entities.**

Two further rules learned the same way.

**Never mark up what the page does not say.** Markup describes the page. A
claim that lives only in JSON-LD is a claim nobody signed off and no reader can
check.

**Which items share a page is a fact about the site, never a fact about the
product.** Three product URLs were each referenced under more than one name,
because some ranges share a page. Pointing them at one `@id` would have merged
three distinct products into one entity named after whichever page they shared.
`@id` references are tidier, and were rejected for exactly this. The same fault
in a different costume once made a page claim the supplier offered one product
where they offered four.

**One definition, byte-identical, everywhere.** JSON-LD merges nodes by `@id`,
so the same definition repeated across pages reinforces one entity, while a
second slightly different definition under the same `@id` fragments it. Generate
the node from one module rather than hand-writing it per template. On this site
the live category-page node compares equal to the node on 29 guidance pages,
and that equality is the property that matters.

## Build the inventory from documents, not from a keyword tool

The entity list comes from what can be evidenced. Here that was 33 extracted
product PDFs and three Declarations of Conformity, which is where the device
nomenclature and the governing standard came from. A keyword tool tells you
what people type. It does not tell you what the thing is.

For each concept record the term practitioners use, the regional variant, the
competing senses, the hard identifiers, the governing standard, and the parent
classes it belongs under.

**A product category is not an entity.** This is the most common modelling
error and it stays invisible until someone tries to anchor a category page. A
merchandising bucket like "small manual handling aids" holds slide sheets,
transfer boards and handling belts, which are three devices with three senses
needing three anchors. On this site the categories resolved to more concepts
than there were categories.

**Watch for one category borrowing another's entity.** Where no item exists,
a page tends to get pointed at the nearest thing that does. That is consistent
rather than correct, and it is worth writing down the day you do it, because
otherwise it reads as settled six weeks later.

## The identifier ladder

Strongest first. The top of this ladder beats any amount of prose.

1. **Hard device nomenclature.** GMDN and EMDN terms are globally recognised
   and a machine reading them cannot mistake the sense. Here, GMDN 37480 and
   EMDN V0805038002 appeared on all three Declarations of Conformity, so they
   were true across the catalogue. This was the strongest asset on the site and
   it was on one page.
2. **The governing standard.** ISO 10535:2021 for hoists and slings,
   IEC 60601-2-52 for medical beds. Cite the number, and check whether the
   client's own documents cite the national adoption instead (BS EN ...),
   because those are different strings for the same thing.
3. **A knowledge-graph QID**, once one exists and genuinely matches.
4. **The manufacturer's page for that exact product**, for `sameAs` on a
   product, and only where it resolves to the exact variant. A URL that looks
   right and is the wrong variant asserts a false identity. Variant pairs that
   differ by one fitting are precisely where that happens. Fetch every one and
   check the product name on the target.
5. **Company registration.** Dull, verifiable, and often the only unambiguous
   identifier a small supplier has.

Where no property exists for an identifier, keep it in your own markup. There
is no GMDN or EMDN property on Wikidata, so those codes live in the page schema
and stay out of the Wikidata item. See the corrections below.

## Deciding what to mention

The useful method is co-citation. Ask the engines the queries that matter and
record which entities they name: standards, manufacturers, regulators, device
classes, professional bodies. That set is the topic's furniture. Entities in it
that your pages never name are the gap.

The same warning applies as to any consensus-following method: the consensus
has to be real. Do not add a mention because a competitor has it, and never
claim a relationship, an accreditation or a framework place the client does not
hold.

Two constraints that belong here.

**Put the full disambiguation list in structured data and show the reader only
the two things they might plausibly confuse.** A clinician reading about low
beds has no use for six excluded senses. A machine does. Keep the two strings
separate in code so nobody collapses them later.

**Keep the search research out of the copy.** "X typed into a search engine
mostly returns Y" is true, useful, and belongs in the internal note. It reached
client copy once on this engagement and had to be removed.

## Wikidata

### The notability test, and it is not Wikipedia's

Read against the policy page, re-checked 12 November 2026. An item is
acceptable if it meets at least one of three criteria. The first is a valid
sitelink to a Wikimedia project page. The third is a structural need. The one
that applies to a category concept is the second, quoted exactly:

> It refers to an instance of a clearly identifiable conceptual or material
> entity that can be described using serious and publicly available
> references.

That bar is lower than Wikipedia's and it is still a bar. Two caveats before
quoting it at anyone: the page says the guidelines are "intentionally left a
bit vague", and a notability reform RfC was open when this was checked.
Re-read the policy rather than trusting this paragraph.

**The category qualifies. A house brand does not, and the grounds matter.**
"Patient lift sling" has a GMDN term, an EMDN code and ISO 10535:2021 behind
it, and the graph had nothing: searching Wikidata for "sling" returned a Clairo
album and then a weapon, and "patient sling" returned nothing at all. Filling
that is a contribution.

An item for a house brand fails criterion 2, because there are no serious,
publicly available, independent references about it. **Be precise about why.**
Wikidata:Notability contains no clause about promotion, advertising,
self-promotion or conflict of interest, so "it reads as self-promotion" is not
the policy argument and should not be presented as one. The brand item fails on
references. The conflict-of-interest obligation is separate and comes from the
Terms of Use. Either way the item gets deleted, and losing that argument taints
the account that also made the useful edit. Do not attempt it.

### Procedure

1. Run the triage first. Half of what looks missing is already there under a
   name you did not search. Measured below.
2. Use an account with a history. A new account whose first act is creating an
   item in a client's category attracts scrutiny, and deserves to.
3. **Declare the connection. Two rules apply and the narrower one governs.**

   Section 4 of the Terms of Use, "Paid Contributions Without Disclosure",
   requires disclosure of "each and any employer, client, intended beneficiary
   and affiliation" for any contribution for which you receive or expect
   compensation, on your user page, on the talk page, or in the edit summary.

   **Wikidata's own policy is narrower on both counts** and it is a policy, not
   a guideline: `Wikidata:Disclosure of paid editing`, shortcut WD:PAID, banner
   "This page documents a Wikidata policy", read 2026-11-12. It requires "the
   name of every organization (regardless of legal status) and individual that
   pays the user money for contributing to Wikidata", and it names **one**
   channel: "This disclosure can either happen via plain-text or with the
   `{{PaidContributions}}` template on the user page." No talk page, no edit
   summary. It does not call itself an alternative policy under section 4; it
   says it "affirms that we expect users of Wikidata to follow the Wikimedia
   policy on paid editing". Treat it as additive, which means: user page.

   **There is no benefit test and no promotional test.** Neither rule asks
   whether the client gains from the edit, or whether the content reads as
   neutral. The trigger is payment for the contribution. A generic category
   item with no brand in it, created inside a paid engagement, is still a paid
   contribution. The neutrality of the item is a defence against deletion, not
   against the disclosure rule.

   What non-disclosure actually risks, since this is usually overstated:
   WD:PAID does not name it as a violation in itself. Enforcement runs warning
   then block, and the block wording is aimed at an editor who "is disruptive".
   A clean item from an undisclosed account is a long way from that. The honest
   summary is that the obligation is real and the exposure is small, and those
   are two separate facts that get collapsed into one in both directions.
4. Write the item as a document first, with every Q-number and P-number fetched
   from the API and confirmed by label. Guessing a Q-number is inventing an
   identity.
5. Label in plain English, regional term in the `en-GB` label. Do not duplicate
   the English label into `en-GB`: that field exists so the regional term can
   be primary. "Hoist sling" is the British term and the highest-volume query
   in its category at 1,300 UK searches a month, so it is the en-GB label
   rather than an alias.
6. Description: no leading capital, no full stop. Aliases one per line.
7. Statements: `P279` subclass of for a class, never `P31` instance of. `P1889`
   different from for each competing sense, which is the work that makes the
   item worth creating. `P8956` compatible with for a device that works
   alongside another, because a sling is not a lift and `part of` is arguable.
8. One reference is enough. Unreferenced subclass claims are normal.
9. No sitelink unless an article genuinely exists.
10. **A human creates it, under a declared account.** Not an agent, not a
    script, not a shared credential.

### Never, in an item

No brand, no manufacturer, no supplier, no product names, no client. A category
item has to read as a category item.

Do not fix a neighbouring item while you are there. There was a thin,
badly-modelled item adjacent to this work. A merge request is the right fix and
it is not yours to start from an account with a declared commercial interest in
the neighbourhood.

## The triage script

Read-only against the public API. It creates, edits and proposes nothing, and
holds no credentials.

Input is a list of concepts, each with the term, its synonyms, and the parent
QIDs you expect the right item to sit under. **Parents are required and
deliberately have no default.** A label match is not an identity: "sling"
matches a Clairo album, "chair" returns chairperson before the furniture, and
"mattress" returns an episode of Glee. Naming the expected parents is what
turns a string match into a class check, and refusing to default them is what
stops the script adopting a wrong QID quietly.

Three verdicts. `MATCH` with a QID to use. `REVIEW` where the name matches but
the class does not, and a person has to read it. `ABSENT` where nothing carries
the term.

The second output is the one that pays for it. For every term it lists the
senses Wikidata currently returns. For an `ABSENT` term that list is both the
`P1889` different-from statements a new item needs and the input to the "not
this" sentence on the page. Both jobs want the same list.

**Put controls in the input.** Two concepts you know are anchored must come
back `MATCH`, or the script is not reading the graph and every other row is
noise.

**It is slow, and not for the reason it looks.** Measured 12 November 2026: the
Action API returns HTTP 429 Too Many Requests to an unauthenticated client well
before you would expect, and the backoff is what costs the minutes. Twelve
concepts took 625 seconds. Three consequences:

- **Never run two copies at once.** They throttle each other, and the second
  makes the first slower. This was found by firing a latency probe at the API
  while the script was working, getting a 429 on the probe, and realising the
  probe was part of the problem.
- Cost scales with search phrases, which is two languages times one plus the
  synonyms. Trim the synonym list to terms you would defend.
- At scale, the Query Service answers a class check in one request and a
  logged-in client gets a higher limit. Neither is worth building for ten
  concepts.

The Wikimedia User-Agent policy asks automated clients to identify themselves
and offer a contact. Use a generic client name or a role address. Never put a
personal email address in it.

## Corrections register

Every one of these was asserted confidently and was wrong. This is the most
useful part of the note.

**A nomenclature is not a source.** I recommended `P248 stated in` and
`P1343 described by source` pointing at the GMDN item, to get GMDN 37480 onto
the sling item. That item is `instance of` nomenclature, a system of names.
P248 is defined as referring to an information document and P1343 to a work. A
naming system is neither, so both fail the value-type constraint and Wikidata
flags them. **There is no correct way to record a GMDN or EMDN code on
Wikidata:** no property exists, the nomenclature item is the wrong type to be a
source, and GMDN term pages sit behind registration so there is no public URL.
The codes stay in the page schema. Reference the standard instead, as a
three-part web reference: `P854` reference URL, `P1476` title, `P813`
retrieved.

**`P854` is a reference property, not a claim.** It was sitting as a top-level
statement and had to be deleted once it existed inside the reference.

**Check the sense of a value, not just that an item exists.** I nearly added
`P366 has use` pointing at an item called "patient transfer". It is described as
interfacility or intrahospital transfer, meaning moving a patient between
wards. Wrong sense, and a factual error of exactly the kind the item exists to
prevent.

**`MedicalDevice` has no `purpose` and no `indication`.** Neither property
exists anywhere in schema.org. I stated the opposite twice.
`MedicalDevicePurpose` is a real enumeration whose members are Diagnostic and
Therapeutic, but no property accepts it, so it is orphaned and reachable only
through `additionalType`. Verified against the current vocabulary file, not
from memory. **Check a property exists in the current vocabulary before using
it.**

**Valid markup is not a rich result.** The product schema here is valid and
passes validation. A Google merchant rich result needs `offers.price`, or
`review`, or `aggregateRating`, and this business publishes none of those
because it takes enquiries rather than selling online. The value of the markup
is entity resolution and AI retrieval. Saying otherwise sells a star rating
that cannot appear.

**Google validates every `Product` node on a page, however deeply nested.** The
guidance pages named the products they discussed as full `Product` nodes inside
`mentions`, which produced 138 invalid items, 12 on one page. The fix was to
drop `"@type": "Product"` and keep name, url and brand. An untyped node is a
plain reference with nothing to validate against, and the label, the link and
the manufacturer all survive for entity resolution.

**A client correction that is already in your data is a build bug.** When the
expert's correction matches the spec file you already hold, the research was
right and the generator was wrong. That is a completely different fix from
going to get better facts. Look for siblings before moving on.

## Measured outcome

**Two items created**, both category items with no brand in them:

- **Q141451358** patient lift sling, 14 September 2026. En-GB label "hoist
  sling". Different from the arm sling, the baby sling, the weapon sling and
  surgical mesh.
- **Q141544523** profiling bed, 23 September 2026. Six aliases, four subclass
  statements, different from the domestic bed and the infant bed, compatible
  with the cot side.

Both are carried by one disambiguation module per cluster, which feeds every
page generator, so one definition reaches all of them.

**The audit that started it, 14 September 2026.** The four cluster pages used
the bare ambiguous word between 99 and 179 times each, against 1 to 6 uses of
the qualified phrase. Two of four titles did not contain the qualifier. No page
carried a single `sameAs`. The only disambiguation anywhere was one line in
`llms.txt`, which nothing is committed to reading. The pages had been written
for a reader who already knew what we meant.

Where the anchoring was thinnest was not where anyone looked: all 29 static
guidance pages carried the `Thing` node, and the category pages carried nothing
at all. Those are the head pages of each silo and the most linked pages in the
cluster.

**The reconciliation pass, 12 November 2026.** Twelve concepts, including the
two above as controls. Both controls returned `MATCH`, so the tool was reading
the graph correctly.

| | concepts |
| --- | --- |
| MATCH, an item already existed | 7 |
| REVIEW | 0 |
| ABSENT, a real gap | 5 |

**Five concepts already had items nobody was using.** The plan had assumed
lookup-or-create across the board. Half the work turned out to be wiring rather
than creating, and the only reason that was known before starting was running
the triage first.

One honest limit on the competing-senses output. For two of the absent
concepts, what came back was scientific papers and patents rather than
confusable concepts. Those make poor `different from` candidates. The output is
only useful when the rival sense is something a person could actually mean.

## Honest limits

**No measured ranking or citation effect.** Two items were created in September
2026 and wired into the pages. Nothing here has been shown to move a ranking,
earn an AI citation or produce a knowledge panel, and no such claim should be
made to a client. The argument for the work is narrower and it is sound: the
sense of an ambiguous term now resolves to a node in the graph, so `sameAs` is
a relation that can be stated honestly instead of a gap. Never guarantee a
ranking, an index, a citation or revenue.

**A Wikidata item helps the whole category, competitors included.** That is
what makes it a contribution rather than a promotion, and it is also why the
benefit to one client is indirect. Worth an hour. Not worth a campaign.

**Wikidata is not a ranking factor** and no amount of it substitutes for the
page being worth citing.

**The item can be deleted.** It is a third party's project and a contribution
can be reverted or merged by anyone. Do not build a deliverable whose value
depends on an edit you do not control.
