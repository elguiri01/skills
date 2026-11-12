---
name: entity-markup-and-wikidata
description: Decide which entities a site should mark up, which it should mention, and which belong in Wikidata. Covers the sameAs / additionalType distinction that merges products if you get it backwards, the notability test that decides whether an item is a contribution or a deletion request, and a read-only triage script. Written from the Lisclare engagement, September to November 2026, where two Wikidata items were created and eight categories are still unanchored.
---

# Entities: what to mark up, what to mention, what to add to Wikidata

Three jobs get run together and confused. Separate them before starting.

1. **Markup.** Declaring, in structured data, which known thing a page is
   about. Costs an hour, breaks nothing if done right, merges your whole
   catalogue into two entities if done wrong.
2. **Mention.** Naming the entities a topic is made of in the prose, so the
   page reads as belonging to its field. This is content work with an entity
   list behind it, not markup.
3. **Contribute.** Adding a missing concept to Wikidata. Legitimate for a
   category, a deletion request for a brand, and the one of the three that
   involves a third party's project and their rules.

Only job 1 is fully in your control. Job 3 is a public-good edit whose benefit
to the client is indirect, and it must be described that way.

Read `information-gain` before job 2 and `11-content-style` before any of it
reaches a page. On a client engagement nothing is published as fact without
sign-off, which includes a standard number, a device code and a notified body.

## The distinction that does the damage

`sameAs` asserts identity. Everything else asserts a relationship. Four
properties, and using the wrong one is not a style choice.

| Property | Says | Use on |
| --- | --- | --- |
| `sameAs` | this node **is** that entity | the concept node only |
| `additionalType` | this thing is **of that type** | individual products |
| `about` | this **page** is about that entity | category and guidance pages |
| untyped `mentions` | this page **refers to** this thing | products named in prose |

Worked through on Lisclare: the concept "profiling bed" genuinely **is**
Q141544523, so a `Thing` node carries `sameAs` to it. An individual Allura is
not the concept, so the product page carries `additionalType` instead. The
category page is not the concept either, so it carries `about`, pointing at the
`Thing` that does.

**Getting this backwards would have merged 57 products into two entities.**
That is the whole reason the distinction is the first section of this skill.

Two further rules learned the same way:

**Never mark up what the page does not say.** Markup describes the page. A
claim that appears only in JSON-LD is a claim nobody signed off and no reader
can check.

**Which items share a page is a fact about the site, never a fact about the
product.** Three Lisclare product URLs are referenced under more than one name
because ranges share a page. Pointing them at one `@id` would have merged three
distinct beds into one entity named "Acute Hospital Beds". `@id` references are
tidier and were rejected for exactly this. The same fault, in a different
costume, once made a page claim the client supplied one product where they
supply four.

**One definition, byte-identical, everywhere.** JSON-LD merges nodes by `@id`,
so the same definition repeated across pages reinforces one entity, while a
second slightly different definition under the same `@id` fragments it. That is
why the node is generated from one module and copied verbatim, not hand written
per template. On Lisclare the live category-page node compares equal to the node
on 29 guidance pages, and that equality is the property that matters.

## Job 1: build the inventory from documents, not from a keyword tool

The entity list comes from what the client can evidence. On Lisclare that was
33 extracted sling PDFs and three Declarations of Conformity, which is where
the GMDN term, the EMDN code and the ISO standard came from. A keyword tool
tells you what people type. It does not tell you what the thing is.

For each concept record: the term practitioners use, the regional variant, the
competing senses, the hard identifiers, the governing standard, and the parent
classes it belongs under. That record is the input to everything downstream,
including the script below.

**A product category is not an entity.** This is the most common modelling
error and it is invisible until someone tries to anchor a category page.
"Small Manual Handling Aids" is a merchandising bucket holding slide sheets,
transfer boards and handling belts, which are three different devices with
three different senses. Eleven Lisclare categories resolve to more concepts
than categories. Anchor the concept, then point the category page at whichever
concept it is actually about, or at several.

**Watch for a category borrowing another's entity.** Lisclare's children's beds
page points at the profiling-bed entity because nothing better existed. A cot
or an enclosed safety bed is not a profiling bed. That is consistent rather
than correct, and consistent-rather-than-correct is worth writing down the day
you do it, because otherwise it reads as settled six weeks later.

## Job 1b: the identifier ladder

Strongest first. The top of this ladder beats any amount of prose.

1. **Hard device nomenclature.** GMDN and EMDN terms are globally recognised
   and a machine reading them cannot mistake the sense. On Lisclare, GMDN 37480
   and EMDN V0805038002 appear on all three Declarations of Conformity, so they
   are true across the catalogue. This was the strongest asset on the site and
   it was on one page.
2. **The governing standard.** ISO 10535:2021 for hoists and slings,
   IEC 60601-2-52 for medical beds. Cite the number, and check whether the
   client's own documents cite the UK adoption instead (BS EN ...), because
   those are different strings for the same thing.
3. **A knowledge-graph QID**, once one exists and genuinely matches.
4. **The manufacturer's page for that exact product**, for `sameAs` on a
   product. Only where it resolves to the exact variant. A URL that looks right
   and is the wrong variant asserts a false identity, and loop-versus-clip
   variants are precisely where that happens. Fetch every one and check the
   product name on the target.
5. **Company registration**, for the organisation node. Lisclare is NI031180 at
   Companies House. Dull, verifiable, and it is the only unambiguous identifier
   a small supplier has.

Where there is no property for an identifier, keep it in your own markup. There
is no GMDN or EMDN property on Wikidata, so those codes live in the page schema
and come out of the Wikidata item. See the correction below.

## Job 2: deciding what to mention

The useful method is co-citation. Ask the engines the queries that matter, and
record which entities they name in the answer: standards, manufacturers,
regulators, device classes, professional bodies. That set is what the engine
treats as the topic's furniture. Entities in that set which your pages never
name are the gap.

This is the `listicle-agent` method pointed at entities rather than brands, and
the same warning applies: the consensus has to be real. Do not add a mention
because a competitor has it, and never claim a relationship, an accreditation
or a framework place the client does not hold.

Two constraints from `client-content-review` that belong here:

**Put the full disambiguation list in structured data and show the reader the
two things they might plausibly confuse.** A clinician reading about low beds
has no use for a list of six excluded senses. A machine does. Keep the two
strings separate in code so nobody collapses them later.

**Keep the search research out of the copy.** "X typed into a search engine
mostly returns Y" is true, useful, and belongs in the internal note. It has
appeared in client copy on this account and had to be removed.

## Job 3: Wikidata

### The notability test, and it is not Wikipedia's

Read against the policy page itself, re-checked 12 November 2026. An item is
acceptable if it meets at least one of three criteria. The first is a valid
sitelink to a Wikimedia project page. The third is a structural need. The one
that applies to a category concept is the second, quoted exactly:

> It refers to an instance of a clearly identifiable conceptual or material
> entity that can be described using serious and publicly available
> references.

That bar is lower than Wikipedia's and it is still a bar. Two caveats worth
knowing before quoting it at anyone: the page says the guidelines are
"intentionally left a bit vague", and a notability reform RfC was open when
this was checked. Re-read the policy rather than trusting this paragraph.

**The category qualifies. The brand does not, and the reason matters.**
"Patient lift sling" has a GMDN term, an EMDN code and ISO 10535:2021 behind
it, and the graph had nothing: searching Wikidata for "sling" returned a Clairo
album and then a weapon, and "patient sling" returned nothing at all. Filling
that is a contribution.

An item for a house brand like MySling fails criterion 2, because there are no
serious, publicly available, independent references about it. **Be precise
about the grounds.** Wikidata:Notability contains no clause about promotion,
advertising, self-promotion or conflict of interest, so "it reads as
self-promotion" is not the policy argument and should not be presented as one.
The brand item fails on references. The conflict-of-interest obligation is a
separate thing and comes from the Terms of Use, below. Either way the item gets
deleted and **losing that argument taints the account that also made the useful
edit.** Do not attempt it.

The same answer applies to the client company. A supplier with a Companies
House number and no independent coverage does not get an item, and asking for
one costs more than it returns.

### Procedure

1. Run the triage first. Half of what looks missing is already there under a
   name you did not search.
2. Use an account with a history. A new account whose first act is creating an
   item in a client's category attracts scrutiny, and deserves to.
3. **Declare the connection, because the Terms of Use require it.** Section 4
   of the Wikimedia Foundation Terms of Use, "Paid Contributions Without
   Disclosure", requires you to disclose "each and any employer, client,
   intended beneficiary and affiliation" for any contribution for which you
   receive or expect compensation. It accepts a statement on your user page, on
   the talk page accompanying the contribution, or in the edit summary. A user
   page statement is the right one here, because it covers every edit without
   cluttering any of them.

   Two things to check rather than assume. The Terms of Use let a project adopt
   an alternative disclosure policy that supplements or replaces section 4, and
   **Wikidata has its own "Disclosure of paid editing" policy page**, which has
   not been read as part of writing this skill. Read it before contributing: it
   is the operative rule if it is that alternative policy. Second, agency work
   for a client is compensated contribution whether or not anyone invoiced for
   the edit itself, so the obligation applies to us.
4. Write the item as a document first, with every Q-number and P-number fetched
   from the API and confirmed by label. `slings/wikidata/patient-lift-sling-item.md`
   in the Lisclare repo is the worked example, down to the QuickStatements
   paste.
5. Label in plain English, regional term in the `en-GB` label. Do not duplicate
   the English label into `en-GB`: that field exists so the regional term can
   be primary. "Hoist sling" is the British term and the highest-volume query
   in its category, so it is the en-GB label rather than an alias.
6. Description: no leading capital, no full stop. Aliases one per line.
7. Statements: `P279` subclass of for a class, never `P31` instance of.
   `P1889` different from for each competing sense, which is the work that
   makes the item worth creating. `P8956` compatible with for a device that
   works alongside another, because a sling is not a lift and `part of` is
   arguable.
8. One reference is enough. Unreferenced subclass claims are normal on
   Wikidata.
9. No sitelink unless an article genuinely exists.
10. **A human creates it, under a declared account.** Not an agent, not a
    script, not a shared credential.

### Never, in an item

No brand, no manufacturer, no supplier, no product names, no client. A category
item has to read as a category item. On this engagement that also means no
country of manufacture, which is a client constraint rather than a Wikidata
one, and it holds in every surface including this one.

Do not fix a neighbouring item while you are there. There is a thin
"Medical bed" item next to Lisclare's work whose modelling is wrong. A merge
request is the right fix and it is not ours to start from an account with a
declared commercial interest in the neighbourhood.

## The script

`reconcile.py`, in this directory. Read-only against the public API. It writes
nothing to Wikidata and holds no credentials.

```
python3 reconcile.py entities.json --json out.json
python3 reconcile.py --term "gantry hoist" --parents Q1419194,Q6554101
```

Input is a list of concepts, each with the term, its synonyms, and the parent
QIDs you expect the right item to sit under. **Parents are required and
deliberately have no default.** A label match is not an identity: "sling"
matches a Clairo album, "chair" returns chairperson before the furniture, and
"mattress" returns an episode of Glee. Naming the expected parents is what
turns a string match into a class check, and refusing to default them is what
stops the script adopting a wrong QID quietly.

Three verdicts: `MATCH` with a QID to use, `REVIEW` where the name matches but
the class does not and a person has to read it, `ABSENT` where nothing carries
the term.

The second output is the one that pays for it. For every term it lists the
senses Wikidata currently returns. For an `ABSENT` term that list is exactly
the `P1889` different-from statements a new item needs, and the input to the
"not this" sentence on the page. Both jobs want the same list and nobody wants
to assemble it twice.

Put the controls in the input file. Two concepts you know are anchored must
come back `MATCH`, or the script is not reading the graph and every other row
is noise.

**Courtesy.** Serial requests with a pause, one backoff retry, honours a 429.
The Wikimedia User-Agent policy asks automated clients to identify themselves
and offer a contact. The `CONTACT` string is a generic client name on purpose.
Never put a personal email address in it. If a contact is wanted, use a role
address the owner has agreed to.

## Corrections register

Every one of these was asserted confidently and was wrong. They are the most
useful part of this skill.

**A nomenclature is not a source.** I recommended `P248 stated in` and `P1343
described by source` pointing at the GMDN item, to get GMDN 37480 onto the
sling item. Q5570492 is `instance of` nomenclature, a system of names. P248 is
defined as referring to an information document and P1343 to a work. A naming
system is neither, so both fail the value-type constraint and Wikidata flags
them. There is no correct way to record a GMDN or EMDN code on Wikidata: no
property exists, the nomenclature item is the wrong type to be a source, and
GMDN term pages sit behind registration so there is no public URL. The codes
stay in the page schema. Reference the standard instead, as a three-part web
reference: `P854` reference URL, `P1476` title, `P813` retrieved.

**`P854` is a reference property, not a claim.** It was sitting as a top-level
statement and had to be deleted once it existed inside the reference.

**Check the sense of a value, not just that an item exists.** I nearly added
`P366 has use` pointing at an item called "patient transfer". It is described as
interfacility or intrahospital transfer, meaning moving a patient between
wards. Wrong sense. That would have been a factual error of exactly the kind
the item exists to prevent.

**`MedicalDevice` has no `purpose` and no `indication`.** Neither property
exists anywhere in schema.org. I stated the opposite twice.
`MedicalDevicePurpose` is a real enumeration whose members are Diagnostic and
Therapeutic, but no property accepts it, so it is orphaned and reachable only
through `additionalType`. Verified against `schemaorg-current-https.jsonld`,
not from memory. **Check a property exists in the current vocabulary file
before using it.**

**Valid markup is not a rich result.** The Lisclare product schema is valid and
will pass validation. A Google merchant rich result needs `offers.price`, or
`review`, or `aggregateRating`, and the client publishes none of those because
the business takes enquiries. The value of the markup is entity resolution and
AI retrieval. Saying otherwise sells a star rating that cannot appear.

**Google validates every `Product` node on a page, however deeply nested.** The
guidance pages named the products they discussed as full `Product` nodes inside
`mentions`, which made 138 invalid items, 12 on one page. The fix was to drop
`"@type": "Product"` and keep name, url and brand. An untyped node is a plain
reference with nothing to validate against, and the label, link and
manufacturer all survive for entity resolution.

**A correction already in your data is a build bug.** When the client's
correction turns out to match the spec file you already hold, the research was
right and the generator was wrong. Look for siblings before moving on.

## Honest limits

**No measured ranking or citation effect.** Two items were created in September
2026 and wired into the cluster. Nothing here has been shown to move a ranking,
earn an AI citation or produce a knowledge panel, and no such claim should be
made to a client. The argument for the work is narrower and it is sound: the
sense of an ambiguous term now resolves to a node in the graph, so `sameAs` is
a relation that can be stated honestly instead of a gap. Hold it to the
standard the portfolio already holds: never guarantee a ranking, an index, a
citation or revenue.

**A Wikidata item helps the whole category, competitors included.** That is
what makes it a legitimate contribution rather than a promotion, and it is also
the reason the benefit to one client is indirect. Worth an hour. Not worth a
campaign.

**Wikidata is not a ranking factor** and no amount of it substitutes for the
page being worth citing. The same correction `agent-ready-audit` makes about
llms.txt applies here.

**The item can be deleted.** It is a third party's project and a contribution
can be reverted or merged by anyone. Do not build a deliverable whose value
depends on an edit you do not control.

## Measured position on Lisclare, 12 November 2026

Two items created, both for this engagement, both category items with no brand
in them:

- **Q141451358** patient lift sling, 14 September 2026. En-GB label "hoist
  sling". Different from the arm sling, the baby sling, the weapon sling and
  surgical mesh.
- **Q141544523** profiling bed, 23 September 2026. Six aliases, four subclass
  statements, different from the domestic bed and the infant bed, compatible
  with the cot side.

Both are carried by `slings/disambiguation.py` and `beds/disambiguation.py`,
which feed every page generator in each cluster, so one definition reaches all
of them.

The audit that started it, 14 September 2026: the four sling cluster pages used
the bare word "sling" between 99 and 179 times each, against 1 to 6 uses of
"hoist sling". Two of four titles did not contain "hoist". No page carried a
single `sameAs`. The only disambiguation anywhere was one line in `llms.txt`,
which nothing is committed to reading. **The pages had been written for a
reader who already knew what we meant.**

Where the anchoring was thinnest was not where anyone looked: all 29 static
guidance pages carried the `Thing` node, and the three WordPress category pages
carried nothing at all. Those are the head pages of each silo and the most
linked pages in the cluster.

**Eight categories remain unanchored**, not nine. The scope note in
`deliverables/month-3/entity-linking-scope.md` says nine and counts a category
that is out of scope. Those eight resolve to ten concepts, because a category
is not an entity.
