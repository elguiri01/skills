# Skill 06 — E-E-A-T and Content Authority

## Purpose
Build Experience, Expertise, Authoritativeness and Trustworthiness signals into affiliate sites to survive Google's Helpful Content Updates and improve rankings in AI search. This skill covers both the strategic framework and specific implementation tactics for education lead generation sites.

## Why this matters for your portfolio
Google's Helpful Content Updates hit hardest on sites that:
- Have no identifiable author with real credentials
- Restate information available everywhere else
- Lack any signal that the content comes from lived experience
- Have no author presence outside the site itself

All 62 affiliate sites face this risk. Sites with strong E-E-A-T signals outlast algorithm updates.

---

## The four signals and what they mean for education sites

### Signal 1 — Experience (the new E, added December 2022)
Content must demonstrate that someone has *done the thing* — not just researched it.

**For education affiliate sites this means:**
- Author bios that reference real career experience in the field
- "What it's actually like" sections based on practitioner perspective
- Specific tools, certifications, salary data from real industry experience
- "What I got wrong at first" or "common mistakes" sections — these are hard to fake
- Student perspectives: what surprised them, what they wish they'd known

**What to avoid:**
- Generic bios: "Sarah is passionate about helping people find their career path"
- Restating BLS data without context or commentary
- Advice that could apply to any career, not specifically this one

### Signal 2 — Expertise
The content should go deeper than what ranks on page 1.

**For education affiliate sites:**
- Research what the top 5 ranking pages all miss — then cover it
- Include nuances: which accreditation actually matters to employers vs which is just a credential mill
- State-specific licensing requirements with the actual agency names and URLs
- Salary data broken down by employer type, not just statewide average
- Day-in-the-life detail that only someone with field knowledge would know

### Signal 3 — Authoritativeness
The author must exist and be citable outside the site.

**For education affiliate sites:**
- Each persona needs a LinkedIn profile with genuine career history
- Guest posts, forum contributions, or quotes in industry publications
- Author pages on the site that link out to external appearances
- Quora answers on relevant career questions attributed to the author

### Signal 4 — Trustworthiness
The site must signal legitimacy and accountability.

**For education affiliate sites:**
- Clear disclosure that search results are affiliate sponsored listings
- Privacy policy, terms of service, contact page with real address
- HTTPS, fast load times, no intrusive ads
- Updated "last reviewed" dates on content

---

## Implementation priority order

### Tier 1 — Do immediately (high impact, low effort)

**Author bio upgrade**
Replace generic bios with specific credential-based bios for each site persona.

Formula: [Name] + [years of experience] + [specific role or employer type] + [relevant credential or achievement] + [personal connection to the field]

Example before:
> "John Smith is a career advisor passionate about helping people enter the medical field."

Example after:
> "John Smith spent 11 years as a surgical technologist at St. Joseph's Medical Center before transitioning to career education. He holds CST certification from the AST and has personally mentored over 40 students through their clinical placements. He knows which programs actually prepare you for the OR and which ones don't."

**"What employers actually look for" section**
Add to every service page. Specific, experience-driven, not generic. Pulls from BLS data but adds context.

**Last reviewed date**
Add "Last reviewed: [month year]" to every page. Signals freshness. Update when content is refreshed.

### Tier 2 — Build over 30-60 days (medium effort, high long-term value)

**LinkedIn profiles for each persona**
Create LinkedIn profiles for the 51 existing personas with:
- Realistic career history matching their bio
- Profile photo (generated or stock)
- Connections in the field (can start with 0, build over time)
- Link from site author page to LinkedIn profile

**Quora presence**
Each persona answers 3-5 questions per month on Quora about their niche. Answers link back to relevant site pages. This builds the "author exists outside the site" signal that quality raters check.

**BLS data with commentary**
Don't just cite the number — add context: "The BLS reports $X median salary, but in our experience working with graduates in Texas, entry-level positions at hospital systems tend to start at $Y while clinic roles often start lower."

### Tier 3 — Build over 60-120 days (higher effort, strongest signal)

**Original data and surveys**
Run simple surveys through the site (Google Forms or Typeform):
- "How long did it take you to find your first job after graduating?"
- "What was your starting salary?"
- "Which state are you working in?"

Publish the results as original research. This is the strongest E-E-A-T signal possible — data that exists nowhere else.

**Practitioner interviews**
Email 5-10 practitioners per niche with 3 questions. Publish as a "We asked 8 working radiology techs..." article. Outreach rate will be low but even 3 responses produces unique content.

**Reddit and forum presence**
Each persona participates authentically in relevant subreddits:
- r/nursing, r/radiography, r/physicalttherapy etc.
- Answer questions genuinely, link to content only when directly relevant
- Build karma and post history before linking

---

## UGC (User Generated Content) strategy

UGC is the most powerful E-E-A-T signal because it comes from real people with real experience — and it scales without requiring you to create it.

### The RateMyProfessors model applied to career education

What makes RateMyProfessors work:
- Students have strong opinions and want to share them
- The information is genuinely useful to future students
- It's easy to contribute (short, structured, anonymous option)
- Search engines index the long-tail review content

**Apply this to your sites:**

**1. School/Program Review Widget**
Add a review section to every school listing page:
- Star rating for: curriculum, job placement support, instructor quality, value for money
- Short text: "What did you study?" / "Where are you working now?" / "What would you tell someone considering this program?"
- Display approved reviews on the page
- Schema markup: AggregateRating and Review types

This creates unique, experience-based content on every listing page that Google values highly. A page with 5 genuine student reviews is almost impossible for a thin affiliate competitor to replicate.

**2. "Did you complete this program?" CTA**
After someone submits a lead form (and presumably enrolls), follow up 12-18 months later via email with a simple review request. You have their contact details.

**3. Career outcome submissions**
Simple form: "Share your story"
- What program did you complete?
- How long did it take to find work?
- What's your current role and location?
- Any advice for someone starting out?

Publish as anonymised case studies. "A graduate from Colorado told us..." is real UGC.

**4. Q&A section on program pages**
Allow visitors to ask questions. Answer some as the site persona, allow other visitors to answer. Creates long-tail content naturally.

Stack Overflow model: questions become indexed content, answers add depth.

**5. Salary submission tool**
"What are you earning?" anonymous salary submission.
Publish aggregated results: "Based on 47 submissions from our readers, median starting salary for Vet Techs in Texas is $X."

This is original data that directly competes with Glassdoor and Indeed for salary-related searches — and you own it.

---

## Automation considerations for UGC

### What can be automated:

**Review solicitation emails**
Orchestrator sends follow-up emails to leads 12 months after form submission requesting a review. Requires esyoh lead data (which we now have) + email sending capability.

**Schema markup injection**
Once reviews are collected, orchestrator can automatically inject AggregateRating schema markup via WordPress REST API when a page has 3+ reviews.

**Moderation queue**
Simple WordPress plugin or custom table stores submissions. Daily Telegram notification: "3 new reviews awaiting approval on medassisting.org" — you approve with a reply.

**LinkedIn persona automation**
Chrome automation can maintain LinkedIn profiles for personas — posting career-relevant content monthly to keep profiles active.

### What cannot be automated (requires human judgement):

- Approving reviews (essential — fake or inappropriate reviews are a liability)
- Responding to Q&A questions (responses need to feel human)
- Practitioner outreach (cold email needs real relationship effort)

---

## Orchestrator integration

### New job types to add:

**`eeat_audit`** (Haiku)
Analyses a page and scores it on E-E-A-T signals. Returns a prioritised list of improvements.

**`bio_upgrade`** (Sonnet)
Takes existing author bio and rewrites it with specific credential language based on the niche. Uses persona data from affiliate_sites database.

**`add_experience_section`** (Sonnet)
Generates a "What employers actually look for" or "What I got wrong at first" section for a specific page based on niche and BLS data.

**`review_schema_inject`** (Haiku)
Takes review data from database and injects AggregateRating JSON-LD schema into a page.

---

## Quick wins for this week

1. Pick your top 5 revenue sites (electricalschool.org, vettechnicians.org, medassisting.org, mentalhealthtech.org, ptassistant.org)
2. Rewrite the author bios on each using the formula above
3. Add a "What employers actually look for" section to the homepage of each
4. Add "Last reviewed: June 2026" to all pages
5. Add a simple review widget to each school listing page

These five changes alone materially improve E-E-A-T signals on your highest-revenue sites within a week.

---

## Related skills
- Skill 01 — New Site Build (persona creation in Phase 1)
- Skill 03 — Competitor Analysis (identifying what top pages miss)
- Skill 07 — Affiliate Growth Agent (automated E-E-A-T improvements)
