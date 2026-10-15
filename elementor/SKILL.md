---
name: elementor
description: Traps and facts specific to Elementor and Elementor Pro, found the hard way on a 121-product WordPress site. Where the real data lives, what is cached and where, why render-time enqueueing defeats wp_enqueue_scripts, how dynamic tags hide the thing you are looking for, and the heading, width and font behaviours that waste an afternoon each.
---

# Elementor: what bites, and where the data really is

Platform-specific companion to `web-performance` and `category-cluster`.
Everything here was measured on a live Elementor Pro site, September and
October 2026. Nothing here is general web knowledge; it is all Elementor
behaving in a way that looks like a bug in your own code.

**Client site or ours?** On a client's site, assume someone has hand-built pages that look templated. Element ids differ per post, templates carry what pages appear to, and a layout copied six times is six separate sets of data. Audit across the whole post type before you write a rule that depends on one.

## Caches, and the one that is not where you expect

**`_elementor_element_cache` post meta.** Edit `_elementor_data` directly and
the front end will keep serving the old markup. Delete the cache rows after
any direct edit:

```
wp db query "DELETE FROM wp_postmeta WHERE meta_key='_elementor_element_cache'"
```

**`elementor_pro_theme_builder_conditions` option.** This is the one that
costs you a morning. A custom-code block's location lives in post meta
*and* in this option, and **the option is what is read at render time**.
Change `_elementor_location` alone and nothing moves.

The option also holds every header, footer, archive and single condition on
the site, so it cannot simply be deleted to force a rebuild. Edit the one
entry surgically and back the whole option up first.

**After any Elementor CSS change:** `wp elementor flush-css`.

## Elementor enqueues at render time, not at wp_enqueue_scripts

This defeats a whole class of optimisation.

`wp_enqueue_scripts` runs before the body renders. Elementor, Elementor Pro
and several plugins that render through Elementor widgets enqueue their
assets **while rendering**, which is afterwards. A dequeue hooked at
`wp_enqueue_scripts`, even at priority 999, never sees them.

Observed consequences:

- A snippet that dequeued a form plugin's assets on pages with no form had no
  effect on pages that did have one, because the form enqueued later. The
  clause was inert, and that inertness was the only thing stopping it
  breaking 121 product pages. See `web-performance`, part two.
- A snippet that self-hosted Google Fonts never caught Elementor's fonts for
  the same reason. The fix was the filter below, not better timing.

**To stop Elementor printing Google Fonts:**

```php
add_filter( 'elementor/frontend/print_google_fonts', '__return_false' );
```

Before using it, check whether anything actually renders in those families.
On this site the two Google Fonts requests existed because the Elementor kit
carried its factory typography defaults, which nothing used. One real font
file did download, and only because the theme's body stack named Roboto and
the browser found a webfont declared by that name instead of using the copy
already on the device.

## Dynamic tags hide the thing you are searching for

A container whose background is the featured image does **not** store the
image URL. It stores an empty `background_image` and a dynamic tag:

```json
"background_image": {"url": "", "id": "", "source": "library"},
"__dynamic__": {"background_image": "[elementor-tag id=\"fe4aa24\" name=\"post-featured-image\" settings=\"%7B%7D\"]"}
```

So searching `_elementor_data` for the image URL finds nothing, and the
element looks like it has no background. **Search for the tag name.**

This is also how to find a hero element whose id differs on every page.
Walking each post's `_elementor_data` for a container whose
`__dynamic__.background_image` contains `post-featured-image` identified the
hero on **121 of 121 products, exactly one each, none ambiguous**. Verify
that against the whole set with a read-only script before you build on it,
and cache the result in post meta so the JSON is parsed once per post rather
than once per request.

## Element ids are per-post, not per-template

Pages built by copying a layout carry **different element ids for the same
visual component**. On this site the product hero was `3312fc2` on one
product, `4a446bc6` on another, `5b85965` on a third.

So a CSS override keyed to an element id works on exactly one page. If you
need to target a component across a post type, resolve the id per post from
`_elementor_data` and emit the rule per page. Do not assume a shared
template, and do not conclude from one sample that there is one.

## Theme Builder templates are invisible to post-level checks

A check that reads the current post's content and `_elementor_data` cannot
see the header, the footer, the single template, the archive template or any
popup. On an Elementor site that is most of what renders.

**"Does this post mention X" cannot answer "will X render here".** This is
the single most dangerous assumption in the file.

Find what templates actually contain by querying `_elementor_data` across
`post_type='elementor_library'`, not by reading pages.

## Widgets, headings and the outline

**A heading widget with `header_size` unset defaults to `h2`.** Put one in a
loop template used by a navigation dropdown and every item becomes a heading
on every page. On this site that produced about 93 headings per page from the
menu alone: 109 headings on a product page, of which 93 were navigation. On
the slings category page the first ten headings a crawler met were bed
product names.

Setting the tag is cosmetic in appearance because typography is set per
widget, so this is cheap to fix and easy to miss.

## Containers take their width from a custom property

An Elementor container's width comes from its own `--width` custom property,
not from `width` or `max-width`. Overriding `max-width` alone does nothing.
Set both:

```css
.elementor-element-xxxxxxx { --width: 98% !important; max-width: 98% !important; }
```

## Mega menu and off-canvas

**Padding targets.** The item padding is on `.e-n-menu-title`. Applying it to
`.e-n-menu-title-container`, which is 0, makes items *wider* rather than
narrower. Measured: 642 px became 786 px when applied to the wrong one.

**Testing dropdowns.** Elementor mega menus and nav dropdowns cannot be
reliably driven by a headless hover. Target `.e-n-menu-item` and
`.e-n-menu-dropdown-icon` directly, and confirm anything important in a real
browser.

**Off-canvas menus are a second full copy of the navigation.** On this site
the header held three menus carrying 245 links to 136 destinations, so 109
were duplicates, and one category page appeared six times in the header of
every page. The header was **232 KB, 50% of the page and 62% of its DOM, and
byte-for-byte identical at 412 px and 1440 px**.

A media query cannot fix that: `display:none` still ships the bytes and still
builds the nodes, and nodes are what cost. The nodes are also what Elementor
walks with `getComputedStyle`, 2,233 times per load on this page, which is
the "forced reflow" a performance tool reports as unattributed.

Deferring the duplicate into a `<template>` and injecting it on first
interaction or on idle cut 477 nodes from the header at parse, a 31% drop,
with no change to what a crawler sees because the primary menu was untouched.
Fire `elementorFrontend.elementsHandler.runReadyTrigger(el)` after injecting
so widget handlers bind as they would have on load.

## Experiments

List them from the plugin rather than guessing at option names:

```php
$m = \Elementor\Plugin::$instance->experiments;
foreach ( $m->get_features() as $k => $f ) { /* is_feature_active( $k ) */ }
```

Names change between versions and old advice rots. In 4.2.4 there is no
CSS-loading experiment at all, so any guidance telling you to enable
"Improved CSS Loading" is out of date.

## Swiper background slideshows

Elementor's background slideshow is Swiper. Expect **loop clones**: four
images produced twelve slide elements. Only the active slide is a visible
paint candidate.

The important consequence is in `web-performance`: a slideshow repaints the
same hero image the CSS already painted, seconds later, and takes the LCP
with it. If you paint a hero from CSS to beat the JavaScript, blank the
slides that would repaint *that same image* rather than blanking the
container once any slide exists.
