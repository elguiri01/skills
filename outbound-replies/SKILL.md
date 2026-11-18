---
name: outbound-replies
description: Cold email and LinkedIn that gets a reply, and what has to happen in the five minutes after one. Use when writing outreach copy for agency prospecting, the freight prospecting kit or any LoadLander template, when deciding what LoadLander should do after a lead responds, and when reading outbound results. Covers timing signals, offers that are not "a call", the one measured copy test, the honest reply arithmetic, how many sends a test needs, the post-click system (speed to lead, voicemail capture, where leads go quiet), and what our own rules change. From Thibault Garcia (Reachly) and Jeremy Burgos (HighLevel), CMSEO and LLM Mastery, November 2026.
---

# Outbound replies

Two talks, two halves of one system. Garcia runs done-for-you cold outreach at
about a million emails a month and covers getting the reply. Burgos works at
HighLevel and covers what happens after. LoadLander is a HighLevel sub-account
product that sends cold email for freight brokers, so both halves are product
requirements as much as advice.

Every outreach message to a real person is public-facing and goes through the
Skill 12 gate. The freight kit's own decisions (`~/clients/freight-kit/DECISIONS.md`)
take precedence over anything here: US only, CAN-SPAM compliant, no guarantees,
no earnings claims, sending from LoadLander on a subdomain per buyer.

## The premise

AI made research and personalisation free, so every prospect now receives the
same well-researched email. What is left to compete on is **timing, offer and
copy**. Optimise for the reply, not the meeting.

## Timing: send on a signal

| signal | why it works |
|---|---|
| New in the role, under 90 days | Looking for early wins and new suppliers |
| Just raised money | Budget and a mandate to spend it |
| Hiring for the role you replace | The need is advertised |
| Added a tool you fit alongside | Stack is in motion |
| Opening a new market | Everything is unsettled |
| Your champion left | Follow them to the new company |

The job-post trigger is the most mechanical: scrape job listings weekly for
roles you can do instead, and write "I see you're hiring for this; we can do it
without the hire."

For freight, the equivalents are a shipper opening a new facility or lane, a
new logistics manager, a hiring post for a transport coordinator, a carrier
failure in the news. The kit's four targeting types (near me, lane, freight
type, equipment type) say who. A signal says when.

## Offer: never "a call"

Six that ask less than a meeting: a free audit against peers; a teardown, three
things you would change; an interview or podcast invitation; a benchmark; the
exact playbook for their case; a warm introduction.

Have one real offer that is easy to say yes to. An offer that sounds too good
is tuned out: for a video client, "a free video at no charge" did worse than
"can I send samples of our work in fintech?".

## Copy: the one measured test

One line changed, for an agency selling AI search work, on what he says was
the same list.

**Lost (7% of replies were positive):**

> I'm Mike from Acme, a leading SEO agency in the USA. We put together an SEO
> audit for you and wanted to book a meeting to show you the results.

**Won (34%):**

> We searched for best accounting software for SMEs and you didn't appear in
> ChatGPT nor on the 1st page of Google. If my team put together a checklist on
> how your team could achieve this within 45 days, could I send it over?

Read the provenance. The denominator is replies, not sends: the share of
replies that were positive. No volume, period or reply count was given, and it
is not clear whether the same people were mailed twice. One campaign.

What the winner does, which transfers:

- Opens with something specific and checkable about them, not about us.
- Offers a thing and **asks permission to send it**. A finished thing plus a
  meeting request is the losing version.
- Is short, and readable at a fifth-grade level. Say "rank on ChatGPT", not
  "AI visibility".

Two edits before we use it:

1. **Check it first.** The line is honest only if we ran the search and they
   were absent. Given how much answers vary between runs
   (`ai-answer-measurement`), "you didn't appear" needs several runs behind it,
   and "when we checked" is the accurate wording.
2. **Drop "within 45 days".** It reads as a promise of a ranking, and we never
   guarantee one.

A version for agency prospecting from the directory:

> We asked ChatGPT and Google for [the thing they sell] in [town] a few times
> this week and [business] didn't come up. I've written down the three things
> the businesses that did come up have in common. Want me to send it?

A version for a broker using the kit, where the specific fact is about the
shipper's freight and the offer is something a logistics manager can use:

> Saw [company] is opening the [place] facility in [month]. I've got current
> spot and contract ranges for [lane] out of there from the last 30 days. Want
> me to send them over?

Both are drafts for Adrian, not templates to ship.

### Structure

- Two emails per lead. The "samples" style offer works well as the second.
- Sender is a real person, the founder or owner, with a public profile.
  Prospects look the sender up. Rented accounts and invented personas are
  refused.
- On a yes, send the thing promised. Some of his clients also phone at once,
  referencing the email.

### LinkedIn

One idea, one real question, no pitch, short enough for a phone: "is your
sales team using Claude for prospecting by any chance?". The kit's decision
stands: LinkedIn is done by hand, and automation is at the buyer's own risk.

## The honest arithmetic

His slide, labelled illustrative rather than a campaign:

| channel | leads | sent | replies | positive | meetings |
|---|---|---|---|---|---|
| Email, two steps | 5,000 | 10,000 emails | about 200 (2%) | about 60 | about 20 |
| LinkedIn | 5,000 | 5,000 requests, about 1,400 accepted | about 350 | about 105 | about 30 |

His spoken figures disagree with the slide (he said one positive reply per 300
to 600 sends; the slide implies one per about 167), so hold these loosely.

What this means for a kit buyer on Apollo's free plan, which the decisions file
puts at 250 emails a day, two active sequences and enough credits for the
25-shipper recipe three times a month: at about 2% replies, 75 shippers a
month is one or two replies. The kit's promise has to be the method and the
quality of the list, which is what the decisions already say. **Do not let any
copy imply a number of loads.**

## How many sends a test needs

His rule: judge an A/B only after 5,000 to 20,000 sends. One thousand or three
thousand is not enough. At a 2% reply rate that is arithmetic, not caution.

Consequences:

- A single broker will never have the volume to test copy. **LoadLander can.**
  Aggregated across accounts, it can learn which openers earn replies in
  freight and ship the winners as defaults. That is "our own aggregated
  behaviour" from the moat ladder in `information-gain`, and it is a reason to
  stay subscribed that a PDF cannot offer. It needs the buyers' consent in the
  terms.
- For our own prospecting, do not rewrite copy on fifty sends.

## Infrastructure

Not covered in his talk beyond one sentence: get the sending setup wrong and
everything goes to spam whatever the copy says. The kit's decision to send from
a subdomain per buyer is the standard protection for the main domain. The open
risks are in the kit's `sources.md`. This skill adds nothing to them.

## After the reply: the part that is LoadLander

Burgos's opening story: a client blamed the call tracking, and nobody was
answering the phone. His five moves (segment, map, plan, fix, compare) applied
after the click:

1. **Segment leads by source.** Cold email, ads, referral, search. They behave
   differently.
2. **Map where they drop.** He lists nine places a lead goes quiet. Example:
   "I need to think about it" gets a follow-up next day with a reason to
   decide.
3. **First message inside five minutes, on the channel the lead used**, and
   open with a quick qualifying question, not "book here". He cites leads being
   about seven times more likely to qualify when contacted within the hour;
   unsourced, and the direction is not in doubt.
4. **When nobody answers, capture the voicemail** with an automated assistant
   and say that it is automated where the law requires.
5. **Hand to a human** when the conversation needs one.
6. **Change one thing and measure** against a comparable group left alone.
7. **Test the phone yourself, out of hours.**

For a freight broker the same list reads: a shipper replies at 6pm asking for
a rate; the broker is driving; by morning the shipper has three other quotes.
An instant reply that asks the two questions needed to quote (lane, date,
equipment) and tells the broker, is the product.

His unsourced open rates (SMS over 90%, email around 20%) are the usual case
for texting a lead who gave a number. US texting rules on consent apply to
that and are stricter than CAN-SPAM is for email. Check before building it.

## What the talks did not cover and we must

- **Law.** Neither speaker discussed it. CAN-SPAM for US business email: a
  true sender and subject, a postal address, a working opt-out honoured
  promptly. Other countries are different and stricter; the kit is US only for
  that reason.
- **LinkedIn's terms** on automation.
- **Deliverability** set-up.

## Refused or changed

- A stated result in a stated time ("in 45 days").
- A claim of absence we did not check.
- Rented or invented senders.
- Any earnings or load-count claim, in copy or in ads.

## What this skill will not claim

That the 7% to 34% result will repeat. It is one campaign with an unusual
denominator. Its structure (specific, checkable, permission-seeking) is
consistent with everything else known about cold outreach, and that is the
part to keep.
