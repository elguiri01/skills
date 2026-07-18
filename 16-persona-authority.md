# Skill 16: Digital Persona Authority & Reputation

How to build the off-site reputation of each site's digital persona — the named
author identity behind the content — so that Google, other sites, and real
readers recognise it as a credible, consistent voice in its niche. Skill 06
covers on-page E-E-A-T signals; this skill covers the persona's presence
*beyond* the site: author identity, social footprint, video, community
participation, and the citations that tie them together.

Written 2026-07-18. Each affiliate site has a persona
(`affiliate_sites.persona_name`), an email (`persona_emails`), and social
handles (`youtube_url`, `facebook_url`, `twitter_url`, `pinterest_url`,
`tumblr_url`). Skill 08 runs one umbrella video channel with a consistent
AI presenter.

## The line this skill will not cross (read first)

These are Your-Money-or-Your-Life sites: real people make career and education
decisions based on them. A persona is a legitimate device — a consistent branded
byline, like a magazine's house author or a pen name. Building its reputation
honestly is fine and effective. Fabricating trust is not, and on YMYL topics it
is both an ethics failure and a ranking risk (Google demotes fake E-E-A-T and
issues manual actions for it). Hard rules:

- **No fabricated credentials.** Do not claim the persona holds a specific
  license, degree, certification, or job title it cannot back up. "Writes about
  radiography careers after researching the field" is honest; "Licensed
  Radiologic Technologist, ARRT #12345" is a fabricated verifiable claim — never
  do that.
- **No impersonation of real people.** The persona is a distinct identity, not a
  real person's name, face, or likeness. AI-generated photos are acceptable as
  clearly-a-brand-avatar; a real person's photo or identity is not.
- **No manufactured professional-network profiles.** Generic YMYL advice says
  "link the author's LinkedIn." For a persona that means creating a fake
  professional profile with an invented work history on a real network — that is
  fabricated credentials plus impersonation of the platform's real-identity
  norms. `sameAs` links to the persona's own site/social/video profiles are
  fine; a fabricated LinkedIn is not.
- **No fake reviews, testimonials, or ratings** — on-site or off (Google, Trust-
  pilot, Reddit, etc.). This is fraud and a schema/review-spam violation.
- **No sock-puppet spam.** Community participation (Reddit, Quora, forums) must
  be genuinely helpful and disclosed-where-required, not manufactured upvotes,
  fake threads, or drive-by link drops.
- **Real expertise comes from real sources.** Authority is built by citing the
  actual data we hold (BLS wages, JRCERT outcomes, licensing-board rules) and
  quoting or linking real practitioners — not by the persona pretending to be
  one.
- **No invented review panel.** Generic advice says "identify the industry
  experts or career counsellors who review your directory." If no such people
  exist, do not name them. Our honest "editorial oversight" is the documented
  process — sourced from public data, fact-checked (verify_facts), links
  verified (url_checks), dated — not a fabricated panel of reviewers.

If a tactic only works because a reader is deceived about who is talking or what
they know, it is out of scope. Everything below builds authority the honest way,
which is also the way that lasts.

## What our sites are — and are not (this governs everything)

Our sites are **affiliate listing/directory sites**: we compile and compare
programs and publish genuinely-useful data about them, and we link out to the
real providers (and earn on the referral). **We are not the school.** We do not
offer courses, employ instructors, grant certifications, accredit anything, or
enrol students.

This single fact decides which E-E-A-T tactic is honest and which is fraud.
Generic YMYL advice (written for actual training providers) says to show
instructor credentials, put accreditation in the footer, embed student reviews,
and publish alumni case studies. Applied to us, every one of those is a
fabrication — inventing instructors we don't employ, accreditation we don't
hold, students we don't have. Do not do it.

The honest, and equally rankable, translation of each:

| Generic "you are the school" advice | Our honest version (a listings site) |
|---|---|
| Show your instructors' licenses | Cite the **real** accreditors and licensing boards (JRCERT, state boards) and link to them; be the site that explains them accurately |
| Accreditation in the footer | Be transparent that we are an independent listings/comparison resource; link to the programs' actual accreditation |
| Embed student reviews (Trustpilot etc.) | Never fabricate reviews. Surface only real third-party data; if we show ratings, they must be genuine |
| Alumni case studies | Publish **real outcome data** (BLS salaries, JRCERT completion/placement rates) attributed to its source, not invented graduate stories |
| "Enrol Now" course pages | Program pages built from real listing data, with the CTA linking to the **actual provider** to enrol — we present and compare, we don't enrol |

Course-page structure and Course/FAQ schema (H1 job title, cost/duration,
syllabus, prerequisites) still apply — as the shape of a **listing** page about
programs, sourced from real data, pointing to the provider. Those mechanics live
in Skill 15 (schema) and Skill 09 (page structure), not here. Course schema must
name the **real provider**, never imply we are it.

## What a persona is, here

One persona per site (or per niche), consistent everywhere:
- **A name and a face:** the `persona_name`, plus a consistent AI-generated
  avatar used identically on the author page, social profiles, and video. Same
  name, same face, same bio voice, everywhere.
- **An honest bio:** what this person does (researches and writes about the
  niche), what informs the work (the data sources, years following the field),
  and a genuine point of view. No invented licensure.
- **A home base:** the on-site author page (see below) that every off-site
  profile links back to. This is the entity Google ties the reputation to.
- **Contact + social:** the persona email and the social handles already in
  `affiliate_sites`.

## The on-site anchor: the author page

Everything off-site points here, so get it right first (this overlaps Skill 06):
- A dedicated `/author/<persona>/` or `/about/<persona>/` page with the avatar,
  the honest bio, the niche focus, and links out to the persona's social/video
  profiles (`sameAs` in Person schema).
- `Person` schema on the author page and `author` on each Article linking to it,
  so Google connects byline → author entity → external profiles.
- Real specifics that demonstrate helpfulness: the methodology behind the site's
  data (how the scores/comparisons are built — Skill 07), which sources are
  used, when data was last updated. Specific and true beats credentialed and
  fake.

## Site-level trust signals (honest translations of the Google plan)

For a directory, E-E-A-T shifts from "prove teaching expertise" (we don't teach)
to **proving editorial integrity, vetting rigour, and neutrality**. That is the
authority we can honestly claim, and it is genuinely additive — some of it is
also legally required. These map to the flags already tracked in
`affiliate_sites` (`has_about`, `has_contact`, `has_disclaimer`, `has_tos`,
`has_privacy`); populate them truthfully.

**Editorial integrity (a directory's version of expertise):**
- **A published vetting/methodology page.** Explain exactly how listings are
  compiled, screened, and scored, and where the data comes from (College
  Navigator, JRCERT, BLS). This is the directory equivalent of an author's
  credentials — it proves rigour instead of claiming a license. Describe the
  real process only (Skill 07's methodology); do not dress it up with reviewers
  who don't exist (see guardrails).
- **Data freshness, shown.** Display a "Last reviewed / updated on [date]" label
  on listing and program pages, and actually keep the data current. The system
  already tracks freshness (`seo_last_updated`, `sp_pages`, `url_checks`
  timestamps); surface it. Ties to Skill 11's no-stale-dates rule.
- **Balanced assessment, not just positives.** Present honest pros *and* cons of
  programs from the data (cost vs regional salary, completion/placement rates,
  licensing caveats). All-positive listings read as promotional to both raters
  and users; balanced editorial judgement is a trust signal and is honest,
  because it comes from real data, not invented reviews.

**Trust and disclosure:**

- **Commercial disclosure, accurate to our actual model (required).** State
  plainly how the site makes money — we earn referral commissions when a user
  enrols through our links. Disclose it truthfully and specifically: if listing
  or ranking is ever influenced by a commercial relationship, say so; if listings
  are compiled from public data independent of payment, say that. The US FTC
  requires disclosure, and Google reads it as honesty, not weakness. Never
  describe the model as more neutral than it is. `has_disclaimer`.
- **Honest About Us.** Say what the site actually is: an independent resource
  that compiles and compares programs using public data, and how that data is
  assembled (the methodology — Skill 07). This is the site's institutional
  E-E-A-T. Do **not** invent a corporate history, a founding team, or a campus.
- **Reachable Contact.** A real, monitored support channel — the persona email
  works (SendGrid). Do **not** fabricate a physical corporate address or phone we
  don't have; a genuine contact email satisfies the trust signal, an invented
  address is a fabrication that can be checked and fails.
- **Privacy policy and Terms.** Real and accurate. `has_privacy`, `has_tos`.
- **Real outcome data, sourced and dated, never exaggerated.** This is the honest
  version of "student outcomes" and it is our strongest asset: BLS salary
  percentiles, JRCERT completion/exam/placement rates, cost-of-living-adjusted
  figures (Skills 07/10) — attributed to the source (e.g. "BLS May 2025 OEWS")
  and to the program, never presented as "our graduates". No invented case
  studies, no rounded-up placement rates.
- **Reviews: real third-party only.** If a page shows ratings or feedback, it
  must be genuine and from an independent source. Never fabricate reviews or
  `AggregateRating` schema (repeat of the guardrail because generic advice keeps
  pushing it).

## Building off-site presence

The goal is a consistent, verifiable footprint that corroborates the author
entity. Anything published here is public-facing and gated on Adrian (Skill 12).

1. **Social profiles (consistency over volume).** Claim the handles in
   `affiliate_sites` with the same name, avatar, and bio, each linking to the
   author page. A few consistent, real profiles beat many empty ones. Post
   genuinely useful niche content (a salary stat, a licensing change, a program
   tip) on a sustainable cadence — not automated spam.
2. **The umbrella video channel (Skill 08).** The single AI presenter answering
   niche queries is the strongest external author signal we have: it puts the
   persona's face and voice on YouTube (the #2 search engine) with each video
   linking to the relevant site and author page. Prioritise videos for the
   converting queries (state/salary/how-to-become), not glossary terms.
3. **Community participation, genuinely.** Where the niche lives (Reddit, Quora,
   specialist forums), the persona can answer real questions with real value,
   citing our data. This builds recognition and referral traffic (a stated
   revenue channel). Rules: follow each platform's self-promotion and
   AI-disclosure policies, add value first, link only when it genuinely helps.
   No manufactured threads or vote manipulation.
4. **Earned citations and links.** The durable E-E-A-T signal is other sites
   referencing the persona or the site's unique data. The lever we control is
   *being citable*: publish the proprietary, genuinely-useful data (Skill 07/10
   — JRCERT outcomes, cost-of-living-adjusted salary, the proprietary score)
   that journalists, bloggers, and school pages want to cite. Outreach to real
   sites is legitimate; buying links or fake guest posts is the deceptive path
   (and link-selling on *our* pages is a separate, gated revenue line — Skill 12).

## Measuring it

- **Referral traffic** to the site from social/video/community (GSC + analytics).
- **Author-entity recognition:** the author page and profiles indexed and
  surfacing for the persona's name.
- **Video performance:** views and click-through to the site (Skill 08).
- **Citations:** referring domains that mention the persona or the data.
- Ultimately, the same north star as everything else: revenue on the site
  (Skill 13), since authority is a means to ranking and traffic, not an end.

## What the agent can do vs what needs a human

- **Agent (autonomous):** draft author bios and pages, draft social/community
  posts and video scripts, identify which queries deserve video (from GSC),
  assemble citable data assets, plan the persona's presence. All drafting and
  planning is upstream of publication.
- **Human (gated, Skill 12):** anything that goes public under the persona —
  publishing the author page, posting to social/YouTube/communities, sending
  outreach to real people, claiming a handle. The publication gate is the
  human-eyes rule; the persona posting to the world is exactly that.

## Related skills

- Skill 06 — E-E-A-T and Content Authority (on-page signals)
- Skill 08 — AI Video Production (the persona's video presence)
- Skill 07 / 10 — the proprietary, citable data that earns authority
- Skill 12 — Agent Operations (nothing public-facing ships un-gated)
- Skill 15 — Technical SEO (Person/Article schema wiring)
