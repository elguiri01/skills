---
name: client-content-review
description: Take a client's review of draft content and turn it into applied changes without losing anything, inventing anything, or putting your own working into their copy. Capture verbatim, separate fact corrections from preferences, apply, then show a Was/Now diff. Written from Stephen Hall's review of the Lisclare sling and bed pages, September 2026, which caught a compatibility claim that was wrong.
---

# Handling a client's review of draft content

The review is the gate the whole process exists for. A subject-matter expert
reading your drafts will find things no amount of document research can:
this one caught a product compatibility claim that would have told buyers a
sling fits a hoist it does not fit.

Read `~/skills/12-agent-operations.md` first. Nothing is published as fact
without the client's sign-off. Short plain sentences, no em-dashes.

## 1. Capture it verbatim before you touch anything

Put the review in the repo word for word, with the date and the author, in
`context/client-review/`. Not a summary. You will reread it four times and
every time you will find a qualifier you had flattened.

Reviews arrive in pieces. Record which sections are done and which are
still coming, so nobody treats a partial review as a sign-off.

## 2. Separate the three kinds of comment

**Factual corrections.** The client says something you published is wrong.
These are not negotiable and they are the reason the gate exists.

**Additions.** New facts you did not hold. Record them like any other fact,
with the client's statement as the source.

**Preferences.** Wording, emphasis, naming. Use their words exactly. If they
write a product name in lower case, use lower case. It is their product.

Write them into a numbered action list with the file and line for each, then
work the list. On this engagement: four corrections, nine wording changes,
three beds of new data, five questions back.

## 3. Check every correction against your own data first

Not to argue. To find out what broke.

Every bed figure the client supplied was **already in our specs file**. The
page builder had picked base heights over low variants and treated a range
page as a product. So the research was right and the generator was wrong,
which is a completely different fix from "go and get better facts".

**If a client correction is already in your data, you have a build bug, and
it is probably not the only instance.** Look for siblings before moving on.

## 4. Ask, do not guess, and check before you accept a guess

Five questions went back. The client answered three immediately and the
remaining two were the ones that genuinely blocked work.

When the account holder suggested assuming the client had simply overlooked
a product, checking took four minutes and showed he had not: he was answering
a question about one specific page, and the product belonged to a different
clinical category. **Acting on the assumption would have published a product
on a list it does not belong on, and attributed the decision to him.**

Ask questions that offer concrete options rather than open ones. "Is it A or
B? We will use your wording" gets answered. "What should we call this?" does
not.

Phrase a safety-relevant question to invite exceptions. "Is every one of
these X, or are there exceptions?" is better than "are these all X?", because
a cheerful yes to the second costs you if it is wrong.

## 5. Keep your own working out of their copy

The two faults the account holder caught, both mine, both the same shape.

Keyword research had established that a term the client uses in the trade is
dominated in search by a completely different consumer product. True, useful,
and it stopped us targeting the wrong term. Then it appeared on the page:

> but "floor bed" typed into a search engine overwhelmingly returns toddlers'
> Montessori beds and cot mattresses. That is a different product.

A clinician reading about low beds has no use for that. **The research was
right. The place I put it was wrong.**

The same applies to disambiguation. Separating your entity from the consumer
products that share its words is real work, but it is work for machines.
**Put the full list in the structured data and show the reader the two things
they might plausibly confuse it with.** Keep the two strings separate in code
so nobody collapses them later.

Sweep for the pattern before you ship: "in a search engine", "searches a
month", "keyword", "mostly means", "typed into".

## 6. Do not let a structural decision leak into a claim

The worst sequence on this engagement, and all of it mine.

Some products had their own page and some shared one with their range. I
modelled that as two tables. Then:

- the summary counted only the first table, so a page claimed the client
  supplied **one** product where they supply four;
- the source citations were built from the first table, so **three of the
  four products lost their provenance** on a project whose entire claim is
  that every figure traces to a named client document;
- and I wrote a sentence explaining the two-table split to readers who had
  not asked.

Four separate corrections from the account holder, all tracing to one
unnecessary structure. The instruction that fixed it was: *"You know there
are four. So put four in the table. For a link, link the three that live on
the other page to that page. You don't have to explain the navigation."*

**Which items have their own page is a fact about the site. It is not a fact
about the product, and it must never drive a count, a list or a citation.**
When a structure starts needing explanation, delete the structure.

## 7. Provenance has to survive refactors

If the deliverable's value is traceability, add a check that the citation
list still covers every item on the page. Losing three of four citations was
invisible in the rendered page and obvious the moment it was set against what
it replaced.

Related: do not sort a citation list. Documents recorded against an item
belong together, and alphabetising a flattened set splits them apart.

## 8. Send a Was / Now diff, not a changelog

Generate it from the repository, diffing the **visible text** between the
commit before the review and the current state. Strip markup, drop table
cells and one-word labels, and group by page.

Head each section with the client's own comment, so they check your change
against their point rather than working out which is which. Name the ones
that needed no text change, so they do not think you missed them.

`tools/client_review_diff.py` in this repo is the implementation. It is about
forty lines.

The diff earns its keep twice over. It is the clearest thing to send a
reviewer, and it is the best self-check you have: three of the four faults in
section 6 were invisible in the page and obvious in the diff. **Run it before
anything goes to the client, not only when they ask.**

## 9. Close the loop in their language

When the client answers a question, reply with the specific answer, not a
restatement. Asked which products needed codes, the answer was 25 across
three ranges, with the two that cannot have codes excluded and the reason
given. Not "the ones that are made in both fittings".

Pull the number from the data at the moment of writing. The tracker said 25,
the data said 27, and the difference was two items that do not attach at all.
Sending 27 would have had somebody hunting for codes that cannot exist.
