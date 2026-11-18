---
name: agency-economics
description: Pricing and structuring client work so it makes money, and choosing between a retainer, profit share and equity. Use when quoting a client, setting a minimum price, deciding whether a client or service line is worth keeping, pricing AI-assisted work, considering a results-based or equity deal, or thinking about what makes the business worth more. Covers the six revenue buckets, the three causes of a fulfilment overrun, utilisation arithmetic and the hourly-rate formulas, per-deliverable pricing, the price reset that lost no clients, how to charge for agent work, phantom equity and profit share, and what an acquirer pays for. From Jacob Kettner, Dennis Yu and Thomas Smale, CMSEO, November 2026. Complements cfo-agent, which governs our own spend.
---

# Agency economics

`cfo-agent` gives a spend rule for the portfolio. This is the other side: what
client work has to earn. Three sources, each self-reported and unaudited:
Jacob Kettner's own agency books, Dennis Yu's client stories, and Thomas
Smale's view from brokering business sales.

Scale warning. Kettner's model is for an agency of about thirty people. Galena
Hall is Adrian and agents. The formulas still apply to one person; the
utilisation floors are, if anything, harsher.

## Six buckets

Every revenue dollar goes into one of six. His targets at about $300K a month:

| bucket | target |
|---|---|
| Fulfilment (doing the work) | 35% |
| Overhead | 25% |
| Profit | 20% |
| Sales | 10% |
| Account management | 7% |
| Marketing | 3% |

A smaller agency runs nearer 50% fulfilment, 30% everything else, 20% profit.
Profit is what is left after the other five, so it is set first and defended.

His own result: 12% margin on $3.2M last year, 21% on $2.7M in nine months
this year, after applying this.

His thesis on why margins erode: pricing was set for the smaller business.
Each non-revenue hire, and each raise for long tenure, adds cost the old price
never covered. **Price for the cost structure you are growing into.**

For us the equivalent non-revenue costs are subscriptions, API spend, data
purchases and Adrian's own unbilled hours on client admin.

## An overrun has exactly three causes

When fulfilment costs more than its target share, it is one of these, and the
numbers say which:

| cause | signature | fix |
|---|---|---|
| Pricing | Cost share high while utilisation is healthy | Raise the price |
| Capacity | Utilisation under the minimum | Sell more of that service, or stop offering it |
| Scope creep | Delivered far above what was budgeted | Per-client limits on billable time |

His January by service line, as cost against the revenue each line generates:
SEO 33%, paid media 53%, web development 198%, hosting 205%. Two lines were
losing money on every job and the blended figure hid it. **Look per service,
never blended.** His over-delivery case: a team 50% billable with 83% of its
time going into client work.

"You can't delegate what you can't measure." His prerequisite is recording
every deliverable per client, in hours, words, links or fixed cost. A
spreadsheet is enough.

## Utilisation and the hourly rate

Maximum realistic billable share of a person's time: 75%. His formulas:

- **Minimum acceptable utilisation** = max billable % − (max billable % ÷ team
  size). Two people 37.5%, three 50%, four 56%. For one person it is zero,
  which is the formula's way of saying a solo operator has no cover at all.
- **Required rate** = total team cost ÷ (target fulfilment % × total hours ×
  minimum utilisation).
- **Break-even utilisation** = total team cost ÷ (target fulfilment % × hourly
  rate × total hours).

His worked example, with an assumed employee cost of $5,500 a month and 143
billable-eligible hours: $5,500 ÷ 0.35 ÷ 143 = about $110 an hour if every
hour were sold; $200 at 55% utilisation; $290 at 37.5%.

The point of the arithmetic: the rate that covers a person is roughly **double**
the naive cost-plus figure, because nobody sells every hour. Adrian's own rate
should be worked the same way, using what his time would cost to replace.

Spare hours given to client work are hard to take back. Put them into internal
projects.

## Price by deliverable

A contract is quantities times unit prices. Each month, re-plan the bundle so
the budgeted value still equals the contract value within 5%. Mark non-billable
work so it uses capacity without inflating revenue.

His sample unit prices, from a toolkit that calls them samples: local profile
post $45; blog or page content $0.45 a word; press release $250; citation $12;
link $250; technical hour $200; "GEO" hour $200; design $120 an hour. Useful
as a sanity range for a quote, not as our rate card.

His toolkit (four workbooks and a file of formulas and prompts, given away) is
referenced in `conference-intel-2026-11/source-extract.md` from line 1060. The
workbooks were not audited for formula errors, and two of its defaults disagree
with the figures used on stage. Rebuild rather than trust.

## The price reset

Legacy clients at about $1,000 a month were moved to a $2,000 minimum with a
$200 a month lifetime discount, so $1,800. By his recollection none left, two
pushed back and one was re-scoped at the old price. Then 3% every year,
stated in advance.

Take from that: a minimum; a grandfathered discount that makes the rise feel
like a favour; a small automatic annual increase so there is never a large
one.

## Charging for agent work

The live question for a business that is mostly agents. His three options:

1. Treat model spend as overhead, already inside the hourly rate.
2. Treat it as a direct cost and divide by the fulfilment target, so $35 of
   tokens is priced at $100.
3. Charge "agent runtime" at its own rate. He is experimenting with $200 an
   hour for a person and $20 for an agent.

Our position should be the second or a fixed price per deliverable. The client
is buying an outcome and a standard, not hours, and pricing by the hour gives
away the gain from doing it faster. Dennis Yu's estimate that 5% of work needs
a frontier model and 95% can run on small or local ones is the cost side of
the same point, and it is what `multi-llm-router` already implements.

Kettner on headcount: nobody was fired; people who left were not replaced.
Smale: do not add headcount where an agent can do the work, because cutting
later is hard.

## Results-based pricing

Valid as risk reversal when there is no proof to show yet. It has to cost the
client **more** than a retainer would, because we carry the risk. And it cannot
be a guarantee of a ranking or a citation; tie it to something countable in the
client's own system, such as enquiries.

## Profit share and equity

Yu's argument: a retainer undervalues work whose effect lasts. Trace it
through: ranking, calls, revenue, profit, then profit times a multiple is the
value of the company. Work billed at $5,000 a month can move a valuation by
millions.

Structures he named, as described on stage and not as legal advice:

| structure | what it is |
|---|---|
| Equity | Shares in the client's business |
| Phantom equity | A contract entitling us to a percentage of proceeds on a sale or change of control. No shares issued. His version required still being engaged on the day |
| Profit share | A percentage of profit, paid periodically |
| Partner or super-affiliate | Paid per result through the client's own programme |
| Advisory equity | He mentioned "a percent or two" (the audio is unclear) |

His worked client: a landscaper on $3,500 a month who moved to an aligned
arrangement and, he says, added $1M in revenue the next year. Who holds what
in that deal is not clear from the talk, and nothing is audited.

When it fits:

- An owner-run business with a sale in view and books we can see.
- Profit share before equity. It pays sooner and needs less law.
- "Revenue is vanity, profit is real": never a share of revenue.
- A lawyer drafts it. Tax follows.
- It replaces part of a retainer, not all of it. The retainer covers cost;
  the share is the upside.

It does not fit a client who will not share numbers, which
`client-value-reporting` treats as a trust stage to work through first.

His prediction for where this is heading, shared by others on the panel:
boring local businesses, moving from retainer to revenue share to equity. Those
are the businesses the directory strategy reaches.

## What an acquirer pays for

Smale has brokered more of these sales than anyone else who spoke.

- **What moves price:** year-on-year growth; recurring revenue; existing
  customers paying more over time (net revenue retention above 100%); profit.
  AI has not changed the list.
- **What to do about it:** add a recurring element whatever the model; build
  ways for customers to pay more as they use more; stay profitable while
  growing; drop high-hassle, low-paying customers.
- **Most undervalued:** agencies. **Most overvalued:** businesses that rely
  only on free organic traffic with no moat.
- **What he would build in 2026:** an AI-native agency with recurring
  contracts, selling to businesses, in a category where the spending is not
  optional. Reputation first.
- **What he would avoid buying:** anything 100% reliant on organic search.
- E-commerce multiples he quoted: 4 to 8 times profit above $500K profit.
- His market-size figures are unsourced and were partly produced with an AI
  assistant from internal data. Do not quote them.

Asked directly by someone with a working site portfolio whether to scale that
or build software, he said double down on what works, and that diversifying
had been his own mistake. So this is not an instruction to abandon the sites.
It is a description of what would make them, and the business around them,
worth more: recurring revenue and a moat. The specific moves are in
`conference-intel-2026-11/plays.md`.

Two rules from Yu's panel that cost nothing:

- Find the one thing already making money and do more of it. "99 to 1, not 80
  to 20."
- Once a quarter, keep a timesheet for a week and put a dollar value on each
  activity.

## What this skill will not do

Give legal, tax or valuation advice, or state a market rate. Every figure is
one operator's own account of their own business.
