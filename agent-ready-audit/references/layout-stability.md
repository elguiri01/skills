# Layout stability for agents

The audit reports **Cumulative Layout Shift** (CLS). Same metric as Core Web Vitals, but the failure mode it predicts for agents is different from the one it predicts for humans.

A human watching content jump is annoyed. An agent works in a locate-then-act cycle: it reads the page, decides "the Add to basket button is at these coordinates", then clicks. If a banner, image, or late-loading ad pushes the layout down in the gap between those two steps, the click lands on whatever moved into that spot. The result is an agent that appears to work in testing and then does the wrong thing in production — hard to reproduce, easy to prevent.

Google's thresholds: **good ≤ 0.1**, needs improvement 0.1–0.25, poor > 0.25. Aim for ≤ 0.1.

## Causes, in the order they're usually worth fixing

### Images and video without dimensions

The browser can't reserve space until the file arrives, so everything below jumps when it does.

```html
<!-- broken -->
<img src="hero.jpg">

<!-- fixed: intrinsic dimensions let the browser reserve the box -->
<img src="hero.jpg" width="1200" height="630" alt="…">
```

Set the real intrinsic dimensions; CSS can still resize it (`width: 100%; height: auto`). For responsive art direction, `aspect-ratio` on the container achieves the same reservation.

### Ads, embeds, and iframes

Third-party slots that size themselves after load are the biggest single source of shift on content sites. Reserve the space:

```css
.ad-slot { min-height: 250px; }        /* the slot's known height */
.video-embed { aspect-ratio: 16 / 9; }
```

If the slot may collapse to nothing when unfilled, still reserve it — a permanently empty box is better than a moving page. If ad sizes vary, reserve the largest common size.

### Web fonts swapping

A fallback font with different metrics reflows text when the web font loads.

```css
@font-face {
  font-family: 'Brand';
  src: url('brand.woff2') format('woff2');
  font-display: optional;          /* or swap, with metric overrides below */
  size-adjust: 105%;               /* tune so fallback metrics match */
  ascent-override: 90%;
}
```

`font-display: optional` eliminates the shift outright at the cost of occasionally not using the web font on a slow first load. Where the brand font is non-negotiable, `swap` plus metric overrides (`size-adjust`, `ascent-override`, `descent-override`) tuned against the fallback gets most of the way there. Preload the font file either way.

### Content injected above existing content

Cookie banners, promo bars, "you have items in your basket" notices, A/B test variants. Anything inserted at the top after first paint pushes the whole page down — exactly the shift that misdirects a click.

Fixes, best first:
- Render it server-side so it's present in the first paint.
- Overlay it (`position: fixed`) instead of inserting it into flow.
- If it must be injected into flow, reserve its height from the start.

### Animating layout properties

Animating `height`, `width`, `top`, `margin` moves everything around them. Animate `transform` and `opacity` instead — they're composited and don't affect layout.

```css
/* broken */ .panel { transition: height .3s; }
/* fixed  */ .panel { transition: transform .3s; }
```

## Measuring

The audit reports the number, but not always which element moved. To find culprits:

- **DevTools → Performance**: record a page load, look for Layout Shift entries in the timeline; each names the element.
- **In-page observer**, useful when driving the page with browser tools:

```js
new PerformanceObserver(list => {
  for (const e of list.getEntries()) {
    if (!e.hadRecentInput) console.log(e.value, e.sources.map(s => s.node));
  }
}).observe({type: 'layout-shift', buffered: true});
```

Lab measurement understates real CLS — it misses shifts triggered by scrolling and by slow third parties on real connections. If field data (CrUX, RUM) is available, trust it over the Lighthouse number, and throttle the connection when testing locally.
