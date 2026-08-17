# llms.txt

## What the audit actually does

The `llms-txt` audit looks for `/llms.txt` at the domain root. If the file **doesn't exist**, the audit reports **"Not applicable"** — it does not fail the site. If it **does** exist, the audit checks quality:

- has an H1
- isn't too short
- contains links

So the file is optional, and a badly written one is worse than none: absent scores nothing, present-and-thin scores a visible failure.

Separately: Google has said it doesn't use llms.txt for ranking, and there's no evidence any major crawler treats it as authoritative. Tutorials that present it as required for AI visibility are overselling it. It's cheap and harmless, and it's genuinely useful as a curated map for whatever does read it — recommend it on that basis, not as an SEO lever.

## Format

Markdown at `https://example.com/llms.txt`, served as `text/plain` or `text/markdown`. The convention:

- one H1 — the site or organisation name
- a blockquote summarising what the site is
- optional prose paragraphs for essential context
- H2 sections containing link lists, each link optionally followed by `: description`
- an optional `## Optional` section for lower-priority material that can be skipped under context pressure

```markdown
# Acme Physiotherapy

> Physiotherapy and sports rehabilitation clinic in Bristol, UK. Online booking,
> NHS and private referrals, specialising in post-surgical and running injuries.

Appointments are bookable online up to 8 weeks ahead. First consultations are
50 minutes; follow-ups are 30.

## Services
- [Sports injury rehab](https://example.com/services/sports-injury): Assessment and
  recovery programmes for running, cycling and team-sport injuries.
- [Post-surgical rehab](https://example.com/services/post-surgical): Structured
  recovery after knee, hip and shoulder surgery.

## Booking and practical info
- [Book an appointment](https://example.com/book): Live availability and online booking.
- [Fees and insurance](https://example.com/fees): Prices and accepted insurers.
- [Find us](https://example.com/contact): Address, parking, opening hours.

## Optional
- [Clinic blog](https://example.com/blog): Injury prevention and recovery articles.
- [About the team](https://example.com/team): Practitioner profiles and qualifications.
```

## Writing one that's worth having

The value is curation — pointing a reader at the pages that matter and saying what's on them. A dump of every URL is a sitemap, and there's already a sitemap.

- Link the pages that answer real questions about the business: what it does, what it costs, how to buy or book, how to make contact.
- Write descriptions that add information the URL doesn't already carry.
- Absolute URLs, since whatever reads the file may not know the origin.
- Keep it current. A file listing pages that 404 is actively misleading — if nobody will maintain it, don't ship it.

## Deploying

Drop it at the web root so it resolves at `/llms.txt`. On WordPress, a physical file in the root directory is the reliable route — plugin-generated virtual routes sometimes fail to serve the right content type. Verify with a fetch of `https://example.com/llms.txt` and confirm it returns 200 with plain text, not an HTML 404 page (a soft 404 will pass a naive check and fail the audit's content checks).

A related convention, `llms-full.txt`, holds the full text content rather than links. The Lighthouse audit doesn't check for it. Skip it unless the user has a specific reason.
