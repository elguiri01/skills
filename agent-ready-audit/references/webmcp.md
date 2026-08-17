# WebMCP

## What it is

WebMCP is a proposed standard that lets a page expose explicit **tools** to an AI agent — "search products", "book appointment", "check order status" — instead of forcing the agent to infer them by looking at the UI and clicking around.

The difference is reliability. Without it, an agent trying to book an appointment reads the page, guesses which form is the booking form, guesses which field is the date, and hopes. With it, the site declares a `book_appointment` tool with a typed schema, and the agent calls it. Fewer steps, no guessing, and the site controls what agents are allowed to do.

## The three audits

- `webmcp-registered-tools` — lists tools registered on the page, declarative or imperative
- `webmcp-form-coverage` — flags forms with no declarative WebMCP annotation
- `webmcp-schema-validity` — checks annotations match the expected schema

All three report **"Not applicable"** on a site that hasn't adopted WebMCP. They don't fail it. Reading them additionally requires registering for the **WebMCP origin trial** — without that, Chrome doesn't expose the CDP domain Lighthouse queries, so the audits stay N/A even on a site that has implemented it.

## When it's worth doing

Worth it when agents completing transactions is a real commercial channel: e-commerce checkout and search, booking and reservations, quote and lead forms, account/order lookup. Also worth it when the site's core interaction is genuinely hard to drive through the DOM — multi-step wizards, custom date pickers, canvas-based UI.

Not worth it yet for content sites, brochureware, or anything where the agent's job ends at reading a page. The spec is still moving, browser support is behind an origin trial, and time spent here before accessible names and layout stability are sorted is time spent on the wrong thing. Say so plainly if the user wants to start here.

## Declarative: annotating an existing form

The lowest-effort adoption path — mark up a form you already have.

```html
<form tool-name="search_products"
      tool-description="Search the product catalogue by keyword, category and price range">
  <input name="q" tool-param-description="Search keywords, e.g. 'waterproof jacket'">
  <select name="category" tool-param-description="Product category">
    <option value="outerwear">Outerwear</option>
    <option value="footwear">Footwear</option>
  </select>
  <input type="number" name="max_price" tool-param-description="Maximum price in GBP">
  <button type="submit">Search</button>
</form>
```

The form keeps working normally for humans — the annotations only add a machine-readable description of what it does and what each field means. Write the descriptions for a reader who cannot see the page: state units, formats, and allowed values, because that's what stops an agent submitting `max_price: "cheap"`.

## Imperative: registering a tool in JavaScript

For actions that aren't a form, or that need logic:

```js
navigator.modelContext.registerTool({
  name: 'check_order_status',
  description: 'Look up the current status of an order by order number and postcode',
  inputSchema: {
    type: 'object',
    properties: {
      orderNumber: { type: 'string', description: 'Order number, e.g. ACM-10432' },
      postcode:    { type: 'string', description: 'Delivery postcode used on the order' }
    },
    required: ['orderNumber', 'postcode']
  },
  async execute({ orderNumber, postcode }) {
    const res = await fetch(`/api/orders/${orderNumber}?postcode=${postcode}`);
    return { content: [{ type: 'text', text: await res.text() }] };
  }
});
```

Register tools only on pages where they make sense, and only ones the current user is entitled to call — the tool runs with whatever session the page has. Treat every argument as untrusted input, exactly as you would a form post, and keep destructive actions (cancel, delete, pay) out of the tool surface unless there's a deliberate confirmation step. The API surface is still changing; check the current WebMCP explainer before implementing rather than copying this verbatim.

## Verifying

Run the audit with the origin trial token in place and confirm the tools appear under `webmcp-registered-tools`, and that `webmcp-schema-validity` passes. If tools are missing, they were probably registered after Lighthouse finished observing — register them early in page lifecycle, not behind a user interaction.
