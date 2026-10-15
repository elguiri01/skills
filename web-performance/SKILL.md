---
name: web-performance
description: Measure and improve page speed without fooling yourself or the client. The control discipline, why two instruments disagree, what Lighthouse scores and what it merely diagnoses, how to read LCP candidates, and the safety rules for any change that removes or defers an asset. Written from the Lisclare engagement, September and October 2026, where the site went from 20.9 s to 3.5 s LCP and three of the changes that felt like wins moved nothing.
---

# Web performance: measuring honestly, changing safely

**How this relates to Skill 18.** Skill 18 owns the portfolio loop: the
`perf_audit.py` cron, the `perf_audits` history, the fix playbook and the
WordPress mechanics for sites we run. This skill owns the part that is not
automatable: how to know whether a change worked, and how to remove an asset
without breaking something nobody notices for three weeks.

## Our own sites and a client's site are different jobs

Most of this skill applies to both. These differences decide how you work,
and getting them the wrong way round is how a client engagement goes wrong.

| | Our sites | A client's site |
| --- | --- | --- |
| **Who decides** | We do. Ship it | The client. Even a change we are certain about |
| **What "done" means** | The number moved | The number moved **on the instrument the contract names** |
| **Blast radius of a mistake** | Our traffic | Their customers, and our standing |
| **Reversibility** | Nice to have | Mandatory, in one action, written into the artefact |
| **Visible changes** | Our call | A separate, slower gate than invisible ones |
| **Measurement** | Automated, historical, trusted | Re-proved per change, because they may ask |
| **The platform** | Known, ours | Theirs. Assume nothing. Audit before changing |

**On our own sites, measure to improve. On a client's, measure to be able to
say so.** The cron history is sufficient evidence for us. For a client, every
number needs its instrument named beside it, because they will run the tool
themselves and get a different answer, and the first time that happens
unexplained you have lost the argument.

**Split client changes by visibility, not by risk.** On the Lisclare
engagement seven performance changes shipped to live in an afternoon because
none of them altered what a visitor sees. One was held back because it
changed the typeface, and it needed the managing director.

That split is right, and it has a failure mode worth naming: **the invisible
changes are the ones you can ship, so they become the ones you work on, and
the visible one quietly becomes the backlog.** On that engagement the held
change turned out to be worth **six seconds of LCP, more than the other seven
together**, and it sat on staging for ten days logged as cosmetic because
nobody had priced it.

So: **price the changes you cannot ship, as carefully as the ones you can.**
Put the number in front of the person who can approve it. "Replace the
typeface" is a design decision they will defer. "This is 9.9 seconds against
3.5" is a business one they will not.

**Never let an unshippable change go unmeasured just because it is
unshippable.** Build it on staging, measure it, and hold the number.

Two halves, and the first one matters more. Most performance work fails not
because the change was wrong but because nobody could tell whether it
worked. Get the measurement discipline right and the changes follow.

Read `~/skills/12-agent-operations.md` first. Nothing reaches a live site
without the account holder. Short plain sentences, no em-dashes.

---

# Part one: measurement

## The rule that would have saved the most time

**A single run cannot resolve a small difference.** Use five runs and a
median, or an on/off control in the same session. Nothing else counts.

On the Lisclare staging host, TTFB measured anywhere between 1.7 s and
6.8 s depending on the minute. Three separate times I nearly reported a
result from one reading:

- `/slings/` read 7,820 ms after a change and looked like a regression.
  Three repeats gave 5,880, 5,680 and 5,672. The first was a cold render
  straight after a cache purge. The page had improved.
- A homepage LCP of 5.6 s was treated as the "before" for a later
  comparison. The same page had read 5.9 and 6.3 within two hours.
- A deferral looked like it cost 256 ms on one page while saving 1,000 ms on
  another. Both directions in one pair of runs is the signature of noise.

**The control to prefer is the same change toggled on and off in one
session**, not before-and-after across days. Staging state drifts: fonts,
snippets and caches all change under you.

## Two instruments will disagree, and that is not a fault

PageSpeed Insights uses *simulated* throttling: it loads the page fast and
models a slow connection afterwards. A Playwright harness with
`Network.emulateNetworkConditions` uses *applied* throttling. They are not
interchangeable and they will differ by seconds.

Worked example. On the same page on the same afternoon: the harness reported
LCP 1,948 ms, PSI reported 9.1 s. Neither was lying.

Three consequences:

1. **Use the instrument the contract names.** If the statement of work says
   "PageSpeed / Lighthouse", that is the number that decides whether you met
   the target, whatever your own tooling says.
2. **Never mix instruments in a before-and-after.** A "before" from one and
   an "after" from the other is not a measurement.
3. **Say which instrument produced every number you report.** In a client
   report, a figure without its instrument is close to meaningless.

**Simulated throttling also models RTT for the TCP and TLS handshake, and
applied throttling on a datacentre host does not.** That is why preconnect
could not be shown to work from a droplet sitting a few milliseconds from
Cloudflare: DNS, TCP and TLS cost 25 to 50 ms there and about 450 ms on a
real phone. Some changes cannot be measured where you are standing. Say so
rather than reporting "no effect".

## What Lighthouse scores, and what it only diagnoses

The performance score is computed from **FCP, LCP, TBT, CLS and Speed
Index**. Nothing else. Everything in the "Diagnostics" and "Insights"
sections is advice, not arithmetic.

This predicts, in advance, which changes will move the number:

| Change | Moves the score? | Why |
| --- | --- | --- |
| Font `font-display` and preload | No | The font was not the LCP element and not render-blocking |
| Preconnect to a third-party origin | No | The resources were async and off the critical path |
| Deferring 538 DOM nodes | Barely | DOM size is a diagnostic; it showed up only through TBT |
| Right-sizing the LCP image | Yes | It is the LCP element |
| Stopping a repaint of the LCP element | Yes, hugely | It decides which paint the metric records |

**Predict before you measure, and say the prediction out loud.** Three times
on this engagement I told the client in advance that a change would not move
the score, and was right each time. That is worth more to a client than a
surprise, and it stops you claiming a noise-level movement as a win.

A change can be real and worth shipping while moving no score. An icon font
that arrived 2,775 ms earlier was a genuine improvement for a visitor and
zero points on PSI. Ship it, record it, do not count it toward a target.

## Read the LCP candidates, not just the LCP

LCP is the *last* candidate before interaction, and a repaint of something
already on screen can take it.

The worked example is the one worth remembering. A hero image painted twice:

| Candidate | At | Size |
| --- | --- | --- |
| Hero, painted from CSS | 3,916 ms | 216,450 |
| Hero, repainted by the carousel | 9,380 ms | 216,687 |

Same image. The second was **237 pixels larger, one tenth of one percent**,
and that was enough to make it the reported LCP. The visitor saw the hero at
3.9 seconds; the tool reported 9.7. Fixing it took the live homepage from
9,008 ms to 2,652 ms and was the single largest win of the engagement.

So: **log every candidate with its timestamp, size and the element that
painted it.** A tool that reports one number hides this entirely. When a
carousel, slideshow or lazy-loaded hero is involved, assume a repaint until
you have checked.

## Split the pre-paint window before optimising anything in it

Before attacking "render-blocking resources", find out what share of the time
they actually own. On the Lisclare homepage:

| | ms | share |
| --- | --- | --- |
| Waiting for the server | 1,915 | **49%** |
| HTML download, 36 KB gzipped | 174 | 4% |
| All 36 stylesheets, in parallel | ~1,000 | |
| First paint | 3,876 | |

PSI priced the render-blocking set at 1,460 ms and recommended attacking it.
But the 30 stylesheets were requested within 60 ms of each other over HTTP/2
and finished within a second. **Nothing about them was serial**, and no
amount of combining or inlining could recover the 1.9 seconds in front of
them. The real lever was the cache.

**Measure TTFB, HTML transfer, the stylesheet window and the remainder
separately.** The headline recommendation in a performance tool is about the
largest *category*, not the largest *cause*.

## Check where a script actually loads before blaming it

Head or body decides whether a script can affect paint at all. A 20.9 KB file
loaded in the body cannot delay FCP or LCP, so restoring it costs nothing on
those metrics no matter what the timings look like on a noisy run.

This is a structural answer and it beats a statistical one. Reach for it
first.

## Images: the box, not the file

Compare the image's intrinsic size against the box it paints into, at the
device pixel ratio the test harness uses.

- A 1920 x 1080 file in a 391 x 220 box ships **2.1 million pixels to paint
  0.3 million**, six times more than needed, and took 4.4 seconds to arrive.
- A 16:9 image in a **portrait** box is the trap. `cover` scales until the
  height fits, so a 371 x 586 box renders the image 1,042 px wide and
  **crops 64% of it off-screen**. You pay for the whole width and show a
  third of it.
- `background-position: 50% 50%` then keeps the *middle*. On a landscape
  photograph of a person that frequently crops the person out. Check what the
  mobile crop actually shows, with a screenshot, before optimising its size.
- The fix for a portrait box is a **portrait crop, not a downscale**.
  Reducing height makes the upscale worse.
- Lighthouse's mobile profile renders at DPR 1.75. A box of 371 x 586 CSS
  pixels needs roughly 649 x 1,025 real ones.

Check whether the smaller sizes already exist before generating any. On this
site WordPress had generated them years earlier and nothing used them:
17.9 MB of hero imagery became 3.8 MB, 79% saved, with files already on disk.

## Never quote a proxy as the real metric

A long-task probe is not TBT. On one page the probe said 2,645 ms and
Lighthouse said 90 ms. The probe is useful for A/B against itself in one
session and must never appear in a report as a TBT figure.

Name any home-made metric so it cannot be mistaken for the standard one.

---

# Part two: changing safely

## The rule: never assert a fact about the site in a comment

The worst bug of this engagement was one line:

```php
// WP Popups: there are no published popups on this site at all.
$drop[] = '/plugins/wp-popups-lite/';
```

That was false when written. Six popups had been published five months
earlier, set to show on every page, carrying 19 PDF links per product page.
Dropping the plugin's script left the markup and the triggers in the page
with nothing to open them. **For three weeks, clicking "Downloads" on any
product page did nothing.** The documents stayed in the HTML, so the search
engine could still see them; only the customer could not.

It was found by the client, by accident.

The surrounding clauses in the same file all tested the page before dropping
anything. The one that asserted was the one that was wrong.

**Every clause that removes an asset must answer "will the thing that uses
this render on this page", not "does this post mention it".**

## Why content searching is the wrong test

On any site with a template layer, most of what renders comes from templates
the post knows nothing about: headers, footers, single-post templates,
popups. Searching the current post's content and page-builder data cannot see
any of it.

The audit of four dequeue clauses on this engagement:

| Clause | Verdict |
| --- | --- |
| Popups | Broken. Asserted instead of testing |
| Events calendar | Correct. Used framework conditionals, not string matching |
| Form plugin | **Inert, and safe only because inert** |
| Membership plugin | Correct. Whitelisted four named pages |

The form clause is the one to study. The condition was false on every product
page, so it asked for the form assets to be dropped. They loaded anyway,
because the plugin enqueues at render time, after the dequeue runs. **It was
saved by a timing accident.** The product enquiry form lives in a template
the check cannot see, so anyone who "fixed" the timing without fixing the
scope would break the form on 121 pages at once, while believing they had
made the site faster.

Dead code that looks like live code is worse than no code. Either scope it
properly or delete it. If you leave it, write the trap into the file in
capitals.

**The pattern to copy** is the membership one: name the pages that need the
asset, never touch a logged-in user, and treat a content search as belt and
braces rather than as the test.

## Before shipping any removal

1. Enumerate what uses the thing, from the database, not from memory. Post
   types, templates, shortcodes, popups.
2. Test a page that should keep it and a page that should lose it.
3. Exercise the feature, do not just count assets. A form can render its
   fields with no JavaScript and fail on submit.
4. Record what the saving actually was. The popup drop bought 20.9 KB of
   non-critical-path JavaScript and cost three weeks of broken document
   access. **That trade was bad on its own terms, before the premise turned
   out to be false.**

## Rollback has to be one action

Every change on this engagement was a snippet that could be deactivated, or
an option that could be set back. Two needed a paired undo and both said so
in their own body: moving a library to the footer also required moving the
inline scripts that call it, and the undo is both.

Write the rollback into the artefact, not into your notes.

## A smoke test is cheaper than a rollback

One script, five representative pages, run before and after every change:
console errors, page errors, the navigation opens, the hero painted, search
returns results, forms render their fields, the mobile menu opens.

It caught nothing most days and that is the point. When it did fire, it fired
immediately rather than three weeks later.

**Keep the assertions honest when the implementation changes.** After the
hero fix, the smoke test reported `hero: blank`, because it checked the slide
that the fix deliberately blanks. That is a false alarm, and a false alarm
you have to explain twice is a test nobody trusts. Fix the test.

---

## What to carry into any engagement

- Five runs or a control. Never one.
- Name the instrument beside every number.
- Predict whether a change will move the score, in advance, in writing.
- Log LCP candidates, not LCP.
- Split the pre-paint window before optimising inside it.
- Compare the image to its box, at the right pixel ratio.
- Never assert a fact about the site in a comment. Test the page.
- A removal is not finished until you have exercised the feature it touches.
- On a client's site, price the changes you cannot ship. The one needing
  their approval is not automatically the small one.
