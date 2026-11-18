# Black-hat ledger

Black Hat Day and several main-stage talks taught manipulation on purpose.
This file records what was shown, so that we can recognise it, defend a client
against it, and say plainly what we will not do. It is a ledger, not a
playbook: procedures are named, not reproduced. The detail is in
`source-extract.md` for anyone who needs to identify an attack.

The house position is in CLAUDE.md under "Links we acquire": acquiring links
and dead domains is a commercial judgement and permitted, priced per site.
What is refused is refused because it deceives a reader, impersonates someone,
uses a person or a system without consent, or attacks a third party. Google's
rules are not the test.

## What was demonstrated, and how solid it is

| technique | who | evidence | our position |
|---|---|---|---|
| A crawler-only directory, hidden from people and redirecting them away | Alan CladX | Slide only, no result | Refused: cloaking plus a sneaky redirect. Also visible in robots.txt to any competitor |
| Links or hidden frames that fire a prompt from a visitor's own AI session | Alan CladX | Claimed to "train" the model; nothing shown | Refused: uses visitors' accounts without consent |
| Adding a false job to a LinkedIn profile so AI repeats it | Alan CladX | Screenshot of Gemini listing him as a Google founder | Refused. **Defensive value is high**, see below |
| Filing a privacy removal request to erase a person from AI answers | Alan CladX | Spoken, names garbled | Refused: abuse of a privacy process against a third party |
| Seeding claims from countries with thin source coverage | Alan CladX | Three single responses a year old | Refused, and unproven |
| Parasite pages on high-authority hosts | Floate, Flynn | One page, one day; one client | Site reputation abuse when done on someone else's offer. A disclosed publisher partnership is the legitimate form |
| Networks of rebuilt aged domains that mention a brand without linking | Floate, Kalin, Stoyanov, Vickers | No results shown by any of the four sellers | Push tier at most, recorded, against a control. See `link-and-domain-vetting/` |
| Bought pop traffic dressed as social to move rankings | Floate, Vickers, Flynn | Floate: under 2% touches Google. Vickers: effect down 20 to 30% after patches | Refused: fake engagement |
| Refusal-removed models for content the main models decline | Floate, Kiekbusch | None | Refused. If a frontier model declines the brief, the brief is the problem |
| "AI lawyers" emailing owners, hosts and registrars until a page comes down | Floate | None | Refused: harassment by automation, and close to negative SEO |
| Mass PDFs in shadow libraries to enter training data | Floate, Moeller | "Basically guaranteed" two model generations later, no base | Refused, and uncheckable |
| Invented award with invented judges | Floate, Sengupta | Ranked in two days, still ranking six months after he confessed | Refused: fabricated record |
| Invented reviewers on an owned review site | Kiekbusch | Cited by ChatGPT within days; taken down after about 33 hours | Refused: FTC, and no publishing under invented identities |
| Aged social accounts run by agents; seeded Reddit threads | Moeller, Flynn, Stoyanov | Moeller's comments were deleted | Refused: astroturfing |
| Micro-workers publishing article variants on their own LinkedIn accounts | Leo | None | Refused |
| Bought reviews, review gating, verification bypasses, rented GBPs | Leo, Singh | Leo: killed some of his own listings | Refused. Official APIs only |
| Blog schema relabelled as forum schema | Quaid | Unmeasured | Refused: mislabels the page |
| Competitor pages built to be mistaken for the competitor's support site | Quaid | Anecdote | Refused: brand confusion, and a legal risk |
| 500 fake job posts to inflate branded search | Kasra Dash | None | Refused |

Two things stand out when the table is read down the evidence column. First,
almost none of it came with a result. The sellers of networks showed
screenshots or nothing. Second, the tactics that did show a result were short:
33 hours, 24 to 48 hours, "about two months", "stopped working a month ago".
Leo's own summary of his field is that tactics last about two months.

## What is worth taking from the black-hat talks

- **Update forensics as a method** (Floate). Snapshot SERPs before, during and
  after an update, pair winners with losers, score attribute families, add
  placebo attributes and report placebo-adjusted confidence. The placebo step
  is the good idea: an analysis that "finds" an effect for a made-up attribute
  is finding noise. `rewrite_control.py` could carry a placebo column.
- **Freshness is several signals that have to agree** (Floate): visible date,
  metadata, schema. Changing only the schema date is one vote of several.
  Refresh when the content changed; never move a date alone.
- **Evergreen URLs** for anything seasonal: no year in the slug.
- **A platform's own search can be studied** by reading what it weights (he
  did Skool). Fine on any platform we are allowed to list on.
- **Vetting rules.** The sellers describe precisely how their competitors'
  inventory is faked. That is the most useful output of the day and it is in
  `link-and-domain-vetting/`.

## Defending a brand client

These talks are also a threat model. For a client with a recognisable name:

1. **Monitor what the engines say about named people.** AI answers about
   individuals lean heavily on LinkedIn. A false role on someone else's
   profile, or on a look-alike profile, can surface in an answer within a week
   or two and fades about as fast once removed. Check founders and
   spokespeople monthly. `perception-engineering/` carries the prompt set.
2. **Watch for invented comparison and award sites** naming the client. They
   get cited fast on ChatGPT in particular. The response is the Tummy Shield
   pattern: publish verifiable evidence and get independent sources to repeat
   it, rather than chasing the page.
3. **Know that erasure exists.** If a client or founder vanishes from one
   engine's answers, a privacy removal filed by someone else is a possible
   cause alongside the ordinary ones.
4. **Keep server logs.** Spoofed AI crawlers probe for exposed configuration
   files. Verify bot IPs against published ranges (`ai-crawl-access/`).
5. **Assume robots.txt is read by competitors.** Anything clever in it is
   public.

## The honest summary

Charles Floate's own reading of the rules is that buying any third-party
mention is a link scheme, so "everybody is a black hat now". That is a
salesman's framing and it flattens a real difference. Paying a publisher for a
labelled placement is marketing. Inventing a person, a review or an award is
fraud on the reader, and it stays fraud whether or not Google notices.
