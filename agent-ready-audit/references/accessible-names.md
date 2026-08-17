# Accessible names and a clean accessibility tree

The `agent-accessibility-tree` audit is the one that decides whether an agent can operate the page at all. It runs a subset of the standard Lighthouse accessibility audits — the ones that affect machine interaction — grouped into three concerns:

- **Names and labels** — every interactive element has a programmatic name
- **Tree integrity** — roles are valid and parent/child role relationships are legal
- **Visibility** — nothing is interactive while hidden from the accessibility tree, and nothing is exposed that shouldn't be

An agent builds its model of the page from this tree. If a control has no name, the agent has nothing to reason about — it can't decide the button is the one it wants, so it either stalls or picks something else.

## The patterns that break it

### Icon-only buttons

The single most common failure. Visually unambiguous, programmatically empty.

```html
<!-- broken: name is the empty string -->
<button class="cart"><svg>…</svg></button>

<!-- fixed -->
<button class="cart" aria-label="View cart">
  <svg aria-hidden="true" focusable="false">…</svg>
</button>
```

Note `aria-hidden` on the SVG: the icon itself carries no meaning once the button is named, and leaving it exposed adds noise. If the icon is inline SVG with a `<title>`, that title can serve as the name instead — but only one mechanism should provide it.

Same fix applies to hamburger menus, close buttons, carousel arrows, social icons, and search magnifiers. Mobile layouts are dense with these, which is why a site can pass on desktop and fail on mobile.

### `<div>` and `<span>` acting as controls

```html
<!-- broken: a click handler on a generic element. Not in the tree as a control. -->
<div class="btn" onclick="checkout()">Checkout</div>

<!-- fixed: use the real element -->
<button type="button" onclick="checkout()">Checkout</button>
```

Prefer the native element over patching a `<div>` with `role="button"` + `tabindex="0"` + key handlers. The native version gets keyboard behaviour, focus, and the correct role for free, and there's less to get wrong. Reach for the ARIA version only when you genuinely cannot change the element.

### Links whose name is the URL, an image, or nothing

```html
<!-- broken -->
<a href="/pricing"><img src="pricing.png"></a>
<a href="/pricing">Click here</a>

<!-- fixed -->
<a href="/pricing"><img src="pricing.png" alt="Pricing plans"></a>
<a href="/pricing">See pricing plans</a>
```

"Click here", "Read more", and "Learn more" repeated down a page give an agent a set of identical, indistinguishable targets. Make the link text describe the destination. Where the design demands short text, `aria-label` on the link can carry the fuller name.

### Form fields with no associated label

Placeholder text is not a label — it disappears on input and isn't a reliable name.

```html
<!-- broken -->
<input type="email" placeholder="Your email">

<!-- fixed -->
<label for="email">Email address</label>
<input type="email" id="email" name="email" autocomplete="email">
```

Add `autocomplete` and a sensible `name` while you're there. Agents filling forms use them, and they cost nothing.

If the design has no room for a visible label, `aria-label` on the input works, but a visible label is better for humans too.

### Invalid role nesting

Certain roles require particular children — `role="list"` must contain `role="listitem"`, tab and menu patterns have similar rules. Breaking this is a common cause of a failed tree audit even when every element is individually named. It usually comes from a component library wrapping list items in an extra `<div>`.

```html
<!-- broken: the wrapper div breaks the list/listitem relationship -->
<ul role="list">
  <div class="row"><li>Item</li></div>
</ul>

<!-- fixed: move the wrapper inside the li, or drop it -->
<ul role="list">
  <li class="row">Item</li>
</ul>
```

### Interactive content hidden from the tree

```html
<!-- broken: focusable but invisible to agents and screen readers -->
<button aria-hidden="true">Submit</button>

<!-- also broken: an off-screen menu that stays focusable when closed -->
<nav style="left: -9999px"><a href="/about">About</a></nav>
```

If something is closed or off-screen, remove it from the tree properly — `display: none`, `visibility: hidden`, `hidden`, or `inert` on the container. Half-hidden interactive content produces agents that click things the user can't see.

## Finding the failures

Lighthouse names the offending elements under each failed audit — start there rather than auditing the page by hand.

To check independently, read the page's accessibility tree and look for nodes with an interactive role (`button`, `link`, `textbox`, `checkbox`, `combobox`) whose name is empty. In DevTools that's the Accessibility pane on a selected element; from a browser tool it's whatever exposes the a11y tree. A quick in-page sweep:

```js
[...document.querySelectorAll('button, a, input, select, textarea, [role="button"], [role="link"]')]
  .filter(el => !(el.ariaLabel || el.textContent.trim() || el.getAttribute('title') ||
                  (el.labels && el.labels.length) || el.getAttribute('aria-labelledby')))
```

That's a heuristic — it won't resolve `aria-labelledby` targets or computed names perfectly — but it surfaces the obvious cases fast on a page you can't run Lighthouse against.

## Verifying

Re-run the audit. Beyond that, the honest test is behavioural: tab through the page and confirm every stop announces something meaningful, and that the tab order matches the visual order. If a human using only the keyboard and a screen reader can complete the site's main task, an agent generally can too.
