# Skill 07 — School Listings, Proprietary Scoring and Data Strategy

## Purpose
Build genuinely differentiated school listing pages and data-driven content that cannot be replicated by competitors or AI overviews. The competitive moat is not scraped data — it is synthesised, scored and interpreted data that requires methodology decisions only a human expert can make.

## Strategic context

### Why listings matter
The original competitive advantage of the affiliate portfolio was publishing complete school listings for every state and program — sourced from College Navigator (US Department of Education). This was:
- More comprehensive than competitors who listed only sponsored schools
- From an authoritative primary source
- Not easily replicated without knowing the source and building a scraper

### Why the old approach broke down
- seopirate.ninja made listings rigid — developer-dependent for any changes
- Shortcode approach `[sp-listings]` created fragile dependency
- Data wasn't enriched or interpreted — just displayed
- No proprietary scoring or synthesis

### The new approach
Replace raw listings with a **scored, enriched, interpreted** school data layer that:
- Pulls from multiple authoritative sources
- Applies a proprietary scoring methodology
- Adds cost-of-living adjusted salary interpretation
- Creates content that is genuinely impossible to replicate

---

## Data sources

### Primary — School data
**College Navigator (nces.ed.gov/collegenavigator)**
The authoritative US Department of Education database. Contains:
- All accredited programs by CIP code and institution
- Completion rates
- Tuition and fees (in-state/out-of-state, full-time/part-time)
- Program length
- Institution type (public/private/for-profit)
- Accreditation status
- Financial aid availability
- Retention rates

**API access:** College Scorecard API (collegescorecard.ed.gov/data) provides machine-readable access to most College Navigator data. Free, no rate limiting for reasonable use.

**IPEDS (Integrated Postsecondary Education Data System)**
Deeper institutional data — graduation rates by demographic, default rates, earnings after graduation (where available).

### Primary — Employment and salary data
**BLS Occupational Employment and Wage Statistics (OEWS)**
- National and state-level median wages by occupation (SOC code)
- Employment levels and projections
- Updated annually
- Available via API or bulk download

**BLS Occupational Outlook Handbook**
- 10-year job growth projections by occupation
- Typical entry requirements
- Work environment descriptions

**O*NET (onetonline.org)**
- Detailed task and skill requirements by occupation
- Technology skills required
- Related occupations

### Secondary — Cost of living adjustment
**MIT Living Wage Calculator (livingwage.mit.edu)**
- Living wage by county and family size
- Poverty wage and minimum wage comparison
- Updated annually

**BLS Consumer Price Index by metro area**
Used to adjust salary data for local purchasing power.

**Missouri Economic Research and Information Center (MERIC)**
Quarterly cost of living index by state — simpler than county-level data, useful for state pages.

### Tertiary — Program quality signals
**Accreditation body pass rates** (where published)
- NCLEX pass rates for nursing programs (published by state boards)
- NBCOT pass rates for OT programs
- NPTAE pass rates for PT assistant programs
- Many programs publish these on their websites or state licensing boards

**Default rates** (College Scorecard)
High student loan default rates signal programs that don't deliver employment outcomes.

**Earnings after attendance** (College Scorecard)
Federal data on median earnings 1, 5 and 10 years after attending, by institution.

---

## The proprietary scoring system

### Scoring philosophy
The score should answer one question: **"If I'm a working-class adult in this state considering this program at this school, is this a good investment of my time and money?"**

That question has four components:

### Component 1 — Program quality score (0-25 points)
- Accreditation status: fully accredited = 25, candidate = 15, not accredited = 0
- Completion rate: >60% = 10pts, 40-60% = 6pts, <40% = 2pts
- Program length relative to field average: shorter = higher score
- Pass rate on licensing exam (where published): >80% = 10pts, 60-80% = 6pts, <60% = 0pts

### Component 2 — Employment outcome score (0-25 points)
- 10-year job growth projection: >15% = 25pts, 10-15% = 18pts, 5-10% = 12pts, <5% = 5pts
- State-level employment concentration: high demand states score higher
- Unemployment rate for occupation in state (where available from BLS)

### Component 3 — Income adequacy score (0-25 points)
This is the proprietary insight — not just "what does it pay" but "does it pay enough to live on where you are"

Formula:
```
Income Adequacy = (State median wage for occupation) / (MIT Living Wage for state, single adult)
```

- Ratio >1.5 = 25pts (salary comfortably exceeds living wage)
- Ratio 1.2-1.5 = 18pts
- Ratio 1.0-1.2 = 10pts (barely covers living costs)
- Ratio <1.0 = 0pts (cannot live independently on this salary)

### Component 4 — Accessibility score (0-25 points)
Can a realistic adult actually complete this program?

- In-state tuition vs state median income ratio (lower = better)
- Financial aid availability: Pell Grant eligible institutions score higher
- Part-time options available: yes = 10pts
- Online options available: yes = 8pts
- Prerequisites: none/minimal = 10pts, significant = 5pts

### Total score interpretation
- 85-100: Excellent investment — strong program, good job market, liveable wage, accessible
- 70-84: Good choice with caveats — note specific weaknesses
- 55-69: Acceptable — significant trade-offs, review carefully
- Below 55: Consider alternatives — flag specific concerns

### Score display on page
Show as a visual score with breakdown. Example:

```
SCHOOL RATING: 78/100
Program Quality:     18/25  ★★★★☆
Employment Outlook:  22/25  ★★★★★
Income Adequacy:     20/25  ★★★★☆
Accessibility:       18/25  ★★★★☆

"Strong employment outlook in [state] with median wages comfortably 
above living costs. Completion rates are below field average — ask 
about student support services before enrolling."
```

The auto-generated commentary (based on score components) is what makes this genuinely useful rather than just a number.

---

## Salary interpretation — the right way

### Never just show the number
Bad: "Median salary: $45,230"

Better: "Median salary: $45,230 — which is $8,400 above the living wage for a single adult in Mississippi and $6,100 below the national median for this occupation."

Best (with context): "Vet techs in Texas earn a median $38,140, but our analysis of 2024 BLS data shows entry-level positions at corporate veterinary chains (VCA, Banfield) typically start at $16-18/hour, while private practices in Dallas and Houston often pay $19-22 for certified techs. The state's living wage for a single adult is $17.46/hour — meaning certification meaningfully improves financial stability in most Texas markets."

### The interpretation formula
For every salary data point, provide:
1. The raw number (BLS source, date)
2. Comparison to national median for the same occupation
3. Comparison to state living wage (MIT calculator)
4. Any state-specific nuance (regional variation, sector variation)
5. Trend: is this growing or shrinking relative to inflation?

### Cost of living adjusted salary table
For programs where geography matters significantly, publish a table:

| State | Median Wage | Living Wage | Surplus/Deficit | Our Score |
|-------|-------------|-------------|-----------------|-----------|
| TX | $38,140 | $36,249 | +$1,891 | 72/100 |
| CA | $48,230 | $52,880 | -$4,650 | 54/100 |
| MS | $33,410 | $30,120 | +$3,290 | 68/100 |

This kind of table is genuinely useful, genuinely original, and impossible for AI to generate because the methodology is yours.

---

## Technical implementation

### Database structure

```sql
-- Schools table (from College Navigator / College Scorecard API)
CREATE TABLE schools (
    id INTEGER PRIMARY KEY,
    unitid TEXT UNIQUE,          -- IPEDS unit ID
    name TEXT,
    city TEXT,
    state TEXT,
    zip TEXT,
    institution_type TEXT,       -- public/private-nonprofit/private-forprofit
    accreditation_status TEXT,
    tuition_instate REAL,
    tuition_outofstate REAL,
    completion_rate REAL,
    default_rate REAL,
    pell_grant_eligible INTEGER,
    online_available INTEGER,
    latitude REAL,
    longitude REAL,
    url TEXT,
    last_updated TEXT
);

-- Programs table (CIP code + school combinations)
CREATE TABLE programs (
    id INTEGER PRIMARY KEY,
    school_id INTEGER,
    cip_code TEXT,               -- Classification of Instructional Programs
    program_name TEXT,
    credential_level TEXT,       -- certificate/associate/bachelor
    program_length_months INTEGER,
    online_available INTEGER,
    last_updated TEXT,
    FOREIGN KEY (school_id) REFERENCES schools(id)
);

-- Scores table (computed, cached)
CREATE TABLE program_scores (
    id INTEGER PRIMARY KEY,
    program_id INTEGER,
    state TEXT,
    quality_score REAL,
    employment_score REAL,
    income_score REAL,
    accessibility_score REAL,
    total_score REAL,
    score_commentary TEXT,
    computed_at TEXT,
    FOREIGN KEY (program_id) REFERENCES programs(id)
);

-- Salary data (from BLS OEWS)
CREATE TABLE salary_data (
    id INTEGER PRIMARY KEY,
    soc_code TEXT,
    state TEXT,
    area_name TEXT,
    median_annual REAL,
    employment INTEGER,
    year INTEGER,
    last_updated TEXT
);

-- Living wage data (from MIT calculator)
CREATE TABLE living_wage (
    id INTEGER PRIMARY KEY,
    state TEXT,
    county TEXT,
    living_wage_single REAL,
    living_wage_one_child REAL,
    year INTEGER
);
```

### College Scorecard API
```python
# Fetch all schools offering a specific CIP code in a state
import requests

API_KEY = 'your_api_key'  # Free from data.ed.gov

def get_schools_by_program(cip_code, state, fields=None):
    if not fields:
        fields = [
            'id', 'school.name', 'school.city', 'school.state',
            'school.school_url', 'school.ownership',
            'latest.completion.completion_rate_4yr_150nt',
            'latest.aid.pell_grant_rate',
            'latest.cost.tuition.in_state',
            'latest.cost.tuition.out_of_state',
            'latest.repayment.3_yr_default_rate',
        ]
    
    r = requests.get(
        'https://api.data.ed.gov/ed/collegescorecard/v1/schools',
        params={
            'api_key': API_KEY,
            'school.state': state,
            'programs.cip_4_digit.code': cip_code,
            'fields': ','.join(fields),
            'per_page': 100,
        }
    )
    return r.json().get('results', [])
```

### CIP codes for common niches

| Niche | CIP Code |
|-------|----------|
| Nursing (RN) | 51.3801 |
| Nursing (LPN) | 51.3901 |
| Medical Assisting | 51.0801 |
| Vet Technology | 01.8301 |
| Radiology Tech | 51.0911 |
| Physical Therapy Aide | 51.0806 |
| HVAC | 47.0201 |
| Welding | 48.0508 |
| Culinary Arts | 12.0500 |
| Cosmetology | 12.0401 |
| Dental Assisting | 51.0601 |

---

## Replacing [sp-listings] shortcodes

### Detection
Scan all pages for `[sp-listings]` shortcode via WordPress REST API.

### Replacement strategy
For each page with `[sp-listings]`:

1. Identify the state and program from the page slug/content
2. Query the schools database for matching programs in that state
3. Generate scored HTML listing block
4. Push via REST API replacing the old shortcode content

### HTML structure for new listings

```html
<section class="school-listings">
  <h2>Accredited [Program] Programs in [State]</h2>
  <p class="listings-intro">
    We've evaluated [N] accredited programs in [State] using our 
    proprietary scoring system, which combines program quality, 
    employment outlook, salary adequacy and accessibility.
    <a href="/our-methodology/">How we score programs →</a>
  </p>
  
  <div class="school-card" data-score="78">
    <div class="school-card__header">
      <h3 class="school-card__name">[School Name]</h3>
      <span class="school-card__location">[City], [State]</span>
      <div class="school-card__score">
        <span class="score-number">78</span>
        <span class="score-label">/ 100</span>
      </div>
    </div>
    <div class="school-card__details">
      <div class="school-card__stat">
        <span class="stat-label">Tuition</span>
        <span class="stat-value">$[amount]/year</span>
      </div>
      <div class="school-card__stat">
        <span class="stat-label">Program Length</span>
        <span class="stat-value">[N] months</span>
      </div>
      <div class="school-card__stat">
        <span class="stat-label">Completion Rate</span>
        <span class="stat-value">[N]%</span>
      </div>
      <div class="school-card__stat">
        <span class="stat-label">Pell Grant</span>
        <span class="stat-value">✓ Eligible</span>
      </div>
    </div>
    <div class="school-card__commentary">
      [Auto-generated score commentary]
    </div>
    <a href="[esyoh listing URL]" class="school-card__cta">
      Request Information →
    </a>
  </div>
</section>
```

---

## Methodology page

Create a `/our-methodology/` page on each site explaining the scoring system. This page:
- Demonstrates expertise and transparency
- Explains the data sources (College Scorecard, BLS, MIT Living Wage)
- Describes the scoring components
- Shows update frequency
- Is a strong E-E-A-T signal in itself

This page is essentially the same across all sites with program-specific variations. Template it in the orchestrator.

---

## Implementation roadmap

### Phase 1 — Data infrastructure (2-3 weeks)
- Set up College Scorecard API access
- Build schools and programs tables
- Load BLS salary data by state and SOC code
- Load MIT living wage data by state
- Build scoring engine

### Phase 2 — Score computation (1 week)
- Compute scores for all programs in all states
- Generate score commentary using Claude API
- Cache results in program_scores table

### Phase 3 — Content replacement (ongoing)
- Scan sites for [sp-listings] shortcodes
- Generate new listing HTML for each page
- Push via WordPress REST API
- Verify rendering

### Phase 4 — Enrichment (ongoing)
- Add licensing exam pass rates where available
- Add program-specific accreditation body data
- Add earnings after attendance from College Scorecard
- Update quarterly as new BLS/DOE data is released

---

## Related skills
- Skill 06 — E-E-A-T and Content Authority (scoring system supports expertise signal)
- Skill 05 — Orchestrator Operations (scheduling data refreshes and content pushes)
- Skill 07 — Affiliate Growth Agent (uses scoring data to prioritise content improvements)
