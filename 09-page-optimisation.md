# Skill 09 — Page Optimisation Process

## Strategic context

Our competitors are frequently the colleges offering ed2go's white-label courses —
the same institutions we generate leads for. They rank through brand authority.
We cannot win on brand. We win by:

- Solving problems potential students actually have
- Answering questions competitors don't answer (or answer poorly)
- Offering unique insight into issues students face: cost of living vs salary,
  program quality signals, honest comparisons, licensing complexity
- Publishing data nobody else has assembled (JRCERT accreditation data,
  proprietary scoring, salary vs living wage by state)

Every optimisation decision should be evaluated against: does this help a
working adult make a better decision about their career training?

---

## The optimisation pipeline

Pages are optimised in priority order based on GSC data:
- Converting page type (state pages, article pages — NOT glossary/reference)
- High impression volume (>5,000 impressions/90 days)
- Position 8-25 (close enough to move, not already on page 1)
- High revenue site (Tier 1 sites first)

**Human review is mandatory before any content is pushed to WordPress.**
The orchestrator generates and queues. Adrian approves and publishes.

---

## What to optimise — in order

### 1. Update stale statistics

**Salary data**
- Source: BLS Occupational Employment and Wage Statistics (OEWS)
- Update annually — BLS releases new data each spring
- Do NOT just replace the number. Update the context:
  - State median vs national median
  - Percentile breakdown (10th, 25th, 75th, 90th)
  - Regional breakdown within state (major metros vs rural)
  - Cost-of-living adjustment using MIT Living Wage Calculator
- Flag data with the year: "According to 2024 BLS data..."
- Never delete existing salary commentary — rewrite it with updated figures

**Employment trends**
- Job growth projections from BLS Occupational Outlook Handbook
- Update the employment figures, projected growth percentage, annual openings
- Note if trend has improved or worsened since last update

**Licensing requirements**
- State licensing boards change requirements periodically
- Verify current requirements from the state licensing board directly
- Flag with "as of [year]" dates

### 2. Rebuild TablePress tables as responsive HTML

TablePress tables are often not mobile-responsive and load slowly.
Replace with clean HTML tables using inline styles or a simple CSS class.

**Responsive table pattern:**
```html
<div style="overflow-x: auto;">
  <table style="width:100%; border-collapse:collapse; font-size:0.95em;">
    <thead style="background:#f5f5f5;">
      <tr>
        <th style="padding:8px; text-align:left; border-bottom:2px solid #ddd;">Location</th>
        <th style="padding:8px; text-align:right; border-bottom:2px solid #ddd;">Median Salary</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:8px; border-bottom:1px solid #eee;">Colorado</td>
        <td style="padding:8px; text-align:right; border-bottom:1px solid #eee;">$77,830</td>
      </tr>
    </tbody>
  </table>
</div>
```

Rules:
- Preserve all existing data — just change the markup
- Add a mobile-friendly horizontal scroll wrapper
- Keep column headers descriptive
- Source and date footnote below every table

### 3. Update, rewrite and enrich college listings

This is the highest-value optimisation. Our JRCERT-sourced listings are our
primary competitive moat.

**For each program listing, include:**
- Institution name, address, phone
- Program type (certificate/associate/bachelor)
- Program length in months
- Tuition (resident and non-resident)
- Completion rate (from JRCERT)
- Credential exam pass rate (5-year, from JRCERT)
- Job placement rate (5-year, from JRCERT)
- Number of recognised clinical settings
- Our proprietary score (see scoring system, Skill 07)
- Direct link to program website
- "Last verified" date

**Add the Top 5 Schools section**
Using the proprietary scoring system (Skill 07), calculate scores for all
programs in the state and display the top 5 prominently with brief commentary.

Format:
```
## Top 5 Radiology Tech Programs in [State] (Our Rating)

### 1. [School Name] — Score: 87/100
[City, State] | [Program type] | [Length] months | $[tuition]/yr
Pass rate: X% | Placement: X% | Completion: X%
Our take: [2-3 sentences on why this program scores well — specific,
not generic. What makes it stand out: clinical network, pass rate
consistency, affordable tuition relative to state average, etc.]

### 2. [School Name] — Score: 82/100
...
```

**Do not delete existing program descriptions.** Enrich them. If there is
existing human-written commentary about a school, preserve it and add the
structured data below it.

**Handle missing programs:**
- Cross-reference JRCERT database against existing page listings
- Add any programs currently accredited that are not on the page
- Flag any programs that appear on the page but are no longer in the
  JRCERT database (may have lost accreditation — note as "accreditation
  status unknown, verify before applying")

### 4. Add UGC capture

**Salary submission widget**
Simple form on state pages: "Working as a [job title] in [state]? Share
your salary anonymously."
Fields: years experience, employer type (hospital/clinic/imaging centre),
city, annual salary, certified (Y/N).
Display aggregated results once 5+ submissions received.
Powers "Reader-reported salaries" section — original data, strongly citable.

**Program Q&A section**
Allow visitors to submit questions. Site persona answers.
Common questions to seed initially:
- "How long does it take to find a job after graduating?"
- "Is the [specific school] program worth it?"
- "Can I work while completing the program?"

**Implementation:** Simple WordPress custom post type or comment-based
system. Moderated before display.

### 5. Schema markup

Add/update these schema types on every state page:

**FAQPage schema**
Wrap existing Q&A content in FAQPage JSON-LD. This creates FAQ rich
snippets in search results, which can significantly improve CTR.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How long does it take to become a radiology tech in Colorado?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Most JRCERT-accredited programs in Colorado take 21-64 months..."
    }
  }]
}
```

**ItemList schema for program listings**
Wrap the school listings in ItemList schema so Google can display them
as structured data.

**BreadcrumbList schema**
Ensures correct breadcrumb display in search results.

**Add FAQ sections where missing**
Pages without explicit Q&A sections should have one added targeting
the long-tail queries the page receives (visible in GSC keywords data).

### 6. Page speed optimisation

**Image optimisation**
- Convert PNG/JPG images to WebP format
- Add explicit width and height attributes to prevent layout shift
- Lazy load images below the fold

**Reduce render-blocking**
- Check for unnecessary plugins loading CSS/JS on this page type
- Disable TablePress on pages where we've replaced tables with HTML

**Core Web Vitals targets:**
- LCP (Largest Contentful Paint): < 2.5 seconds
- CLS (Cumulative Layout Shift): < 0.1
- FID/INP: < 200ms

Measure with PageSpeed Insights before and after each optimisation.

### 7. A/B test: esyoh search box position

**Hypothesis:** Users who see the esyoh search widget above the fold
convert at a higher rate than users who scroll past text to find it.

**Mobile problem:** On mobile, the search box is typically below the fold.
Users see only text. This may explain lower mobile conversion rates.

**Test variants:**

Variant A (control): Current layout — search box in its current position
Variant B: Move esyoh search widget to immediately after the H1,
           before any introductory text
Variant C: Add a sticky mobile CTA bar that appears after 3 seconds:
           "Find [program] programs near you →" linking to the widget

**Measurement:**
- Primary metric: esyoh widget clicks / page sessions
- Secondary: time on page, scroll depth
- Run for minimum 4 weeks before concluding

**Internal page navigation**
Add a sticky "On This Page" nav (visible in the Colorado page sidebar
on desktop) that works on mobile too. Jump links to:
- Salary Data
- Licensing Requirements
- Top Schools (our ranked list)
- All Accredited Programs
- FAQs

This improves engagement signals and helps users complete their task.

---

## What NOT to do

- **Never delete human-written content.** Rewrite stale sections,
  but preserve original insights and local knowledge.
- **Never overwrite Gutenberg block structure** unless replacing with
  equivalent or better structure.
- **Never push content without human review.**
- **Never add generic AI content** that could appear on any state's page.
  Every sentence should contain something state-specific.
- **Never invent statistics.** Use real sources, cite them, date them.
- **Never remove existing shortcodes** (esyoh widgets, lead forms) —
  these are the revenue mechanism.

---

## Implementation workflow

```
1. FETCH current page content via WordPress REST API
2. AUDIT — identify what needs updating:
   - Flag stale salary figures (year check)
   - Compare program listings against JRCERT database
   - Check for TablePress tables
   - Check for existing FAQ section
   - Check for schema markup
3. GENERATE updates (Claude API):
   - Updated salary tables with current BLS data
   - Enriched program listings with JRCERT data + scoring
   - New FAQ section from GSC keyword data
   - Schema JSON-LD blocks
4. DIFF — show Adrian exactly what would change
5. APPROVE — Adrian reviews and approves specific changes
6. PUSH — targeted updates via WordPress REST API
   - Update specific blocks only
   - Preserve all shortcodes and Gutenberg structure
7. VERIFY — fetch page and confirm changes rendered correctly
8. MEASURE — note pre/post position in GSC (check in 30/60/90 days)
```

---

## Related skills
- Skill 06 — E-E-A-T and Content Authority
- Skill 07 — School Listings and Proprietary Scoring System
- Skill 08 — AI Video Production
- Skill 05 — Orchestrator Operations

---

## Additions 2026-07-09

### Language version safety
Some sites carry Spanish translations at /es/ paths sharing slugs with the
English pages. Any tool resolving a page by slug MUST verify the full URL
path matches the target exactly. Pushing English content onto a Spanish
translation page (or vice versa) is a critical failure. review_expansions.py
enforces exact-path matching; any push tool must do the same before writing.

### Ad placement position rules (extends "never remove shortcodes")
1. Always fetch page content with context=edit (raw editor content) so
   shortcodes are visible as authored. Rendered content hides them and
   makes accidental deletion likely.
2. Before any merge, inventory every ad placement and revenue shortcode
   with its position relative to surrounding headings. review_expansions.py
   produces this inventory.
3. Placements stay in broadly the same position in the reading flow.
   New sections are inserted around them, never displacing them to the
   bottom or consolidating them.
4. Post-merge check: count and relative order of placements must be
   identical before and after. Mismatch rejects the merge.

### JRCERT data gating
Do not queue a content_expansion job for a state whose JRCERT data has not
been scraped:
    SELECT COUNT(*) FROM jrcert_programs WHERE state = ?
Zero rows means the job waits. A state page expansion generated without
JRCERT listings is incomplete and must not be pushed. This rule exists
because 28 jobs were queued on 2026-06-26 while the JRCERT scrape was
mid-run, producing content with no program data.

### Style compliance (Skill 11)
All generated content must comply with Skill 11. The Skill 11 prompt
injection block is mandatory in every content-generation job prompt:
no em-dashes, no "not X, it's Y" constructions, current date injected,
no templated intros, no invented facts, banned vocabulary list enforced.

### Workflow updates
- Step 4 (DIFF) is implemented: cd ~/orchestrator && python3
  review_expansions.py, then serve ~/orchestrator/review/ on port 8080.
  Triage from index columns: dashes, stale dates, JRCERT coverage,
  heading overlaps, duplicate paragraphs.
- Step 6 (PUSH): save as a draft revision first, never straight to the
  live page. Compare draft preview against live before publishing.
