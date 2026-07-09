# Skill 10 — Accreditation & Program Data Sources by Niche

## The strategic principle

JRCERT-sourced program data is why radiologyed.org ranks. The same moat
exists for every niche that has a recognised accreditation body publishing
program effectiveness data. Our job is to find, scrape and compile that
data before competitors do.

The pattern:
1. Accreditation body publishes program directory (often behind JS)
2. Program pages contain effectiveness data: pass rates, completion rates,
   placement rates, tuition, clinical settings
3. Nobody has compiled it into a state-by-state format
4. We do. We rank.

**The deeper moat: cross-source enrichment**

Any competitor can eventually scrape a single source. What cannot easily
be replicated is the synthesis of multiple sources into a coherent,
state-specific picture that answers the question a student actually has:
"Is this program worth it for me, in my state, at my income level?"

For each program listing, the goal is to combine:
- Accreditation data (pass rates, completion rates, placement rates, tuition)
- BLS salary data (state median, regional breakdown, percentiles)
- MIT Living Wage (does this salary actually cover living costs here?)
- DOL RAPIDS (apprenticeship alternatives in the same state/trade)
- State licensing board (exact requirements, exam pass rates where published)
- Employer data (who hires in this state, from RAPIDS or direct research)
- Our proprietary score (synthesises all of the above into one number)

The proprietary score is the capstone — it forces a methodology decision
that competitors cannot copy without copying the entire reasoning behind it.
A score of 78/100 with a visible breakdown is far more defensible than
a list of raw numbers.

For each niche, we need:
- The accrediting body name and URL
- The program search/directory URL
- Whether data is accessible as plain HTML or requires JS rendering
- What effectiveness data is published
- Update frequency

---

## Cross-source enrichment matrix

For each niche, these sources should be combined per state page.
✅ = available and mappable | 🔄 = to build | ❌ = not applicable

| Source | Radiology | Pharmacy | Vet Tech | Med Assist | Surgical | Electrician | Plumber | Welder | Auto |
|---|---|---|---|---|---|---|---|---|---|
| Accreditation body data | ✅ JRCERT | 🔄 ASHP | 🔄 AVMA | 🔄 CAAHEP | 🔄 CAAHEP | ❌ | ❌ | 🔄 AWS | 🔄 ASE |
| BLS salary (state+metro) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| MIT Living Wage | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| DOL RAPIDS apprenticeships | ❌ | ❌ | ❌ | ❌ | ❌ | 🔄 0159 | 🔄 0275 | 🔄 0431 | 🔄 varies |
| State licensing requirements | ✅ ARRT | 🔄 state boards | 🔄 VTNE | 🔄 state boards | 🔄 state boards | 🔄 state boards | 🔄 state boards | ❌ | ❌ |
| Exam pass rates | ✅ JRCERT | 🔄 NABP | 🔄 AAVSB | 🔄 varies | 🔄 varies | 🔄 state | 🔄 state | ❌ | 🔄 ASE |
| College Scorecard (federal) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Proprietary score | ✅ built | 🔄 | 🔄 | 🔄 | 🔄 | 🔄 | 🔄 | 🔄 | 🔄 |

The College Scorecard API (free, from data.ed.gov) provides a baseline
layer for all niches — completion rates, default rates, earnings after
attendance — for any institution offering that CIP code. This is the
floor. Accreditation body data is the enrichment layer on top.

---

## Data sources by niche

### Radiology / Radiologic Technology
**Sites:** radiologyed.org
**Accreditor:** JRCERT (Joint Review Committee on Education in Radiologic Technology)
**Directory:** https://www.jrcert.org/find-a-program/
**Program pages:** https://www.jrcert.org/programs/[slug]/
**Data available:** Completion rate, credential exam pass rate (5-yr),
job placement rate (5-yr), tuition (resident/non-resident), program length,
clinical settings, program director contact, accreditation length
**Access:** Sitemap-discoverable, plain HTML program pages ✅
**Scraper:** jrcert_scraper.py — COMPLETE
**Update frequency:** Annual (program effectiveness data updated yearly)
**Programs:** ~724

---

### Pharmacy Technician
**Sites:** pharmacistschools.org
**Accreditor:** ASHP (American Society of Health-System Pharmacists)
**Directory:** https://www.ashp.org/pharmacy-practice/accreditation-programs/pharmacy-technician-education-programs
**Also:** ACPE (Accreditation Council for Pharmacy Education) for PharmD
**Data available:** TBD — needs investigation
**Access:** TBD
**Scraper:** To build
**Notes:** ASHP accredits pharmacy technician training programs specifically.
This is a rich source for pharmacistschools.org which is our 4th highest
revenue site. Strong opportunity.

---

### Medical Assisting
**Sites:** medassisting.org
**Accreditor (primary):** CAAHEP (Commission on Accreditation of Allied Health
Education Programs) — accredits via MAERB (Medical Assisting Education Review Board)
**Directory:** https://www.caahep.org/Find-An-Accredited-Program.aspx
**Accreditor (secondary):** ABHES (Accrediting Bureau of Health Education Schools)
**Directory:** https://abhes.org/accreditedprograms/
**Data available:** TBD
**Access:** TBD
**Scraper:** To build
**Notes:** Two separate accreditors means two scraping jobs. CAAHEP is the
more widely recognised. ABHES tends to accredit more vocational/proprietary schools.

---

### Surgical Technology
**Sites:** surgicaltechedu.org
**Accreditor:** CAAHEP (via ARC/STSA — Accreditation Review Council on Education
in Surgical Technology and Surgical Assisting)
**Directory:** https://www.caahep.org/Find-An-Accredited-Program.aspx
(filter by Surgical Technology)
**Data available:** TBD
**Access:** TBD
**Scraper:** To build (shares CAAHEP infrastructure with medical assisting)
**Notes:** Same CAAHEP directory as medical assisting — one scraper may serve both.

---

### Veterinary Technology
**Sites:** vettechnicians.org
**Accreditor:** AVMA-CVTEA (American Veterinary Medical Association Committee
on Veterinary Technician Education and Activities)
**Directory:** https://www.avma.org/education/accreditation/veterinary-technology-programs
**Data available:** TBD — AVMA publishes program lists, effectiveness data varies
**Access:** TBD
**Scraper:** To build
**Notes:** AVMA also publishes pass rate data for the VTNE (Veterinary Technician
National Examination) by program. This may be on a separate AAVSB page.
AAVSB (American Association of Veterinary State Boards):
https://www.aavsb.org/vtne/

---

### Physical Therapy Assistant
**Sites:** ptassistant.org
**Accreditor:** CAPTE (Commission on Accreditation in Physical Therapy Education)
**Directory:** https://aptaapps.apta.org/accreditedschools/
**Data available:** Graduation rates, licensure exam pass rates, employment rates
**Access:** TBD — APTA publishes annual outcome data
**Scraper:** To build
**Notes:** CAPTE publishes detailed annual program effectiveness data.
This is likely as rich as JRCERT. Strong opportunity for ptassistant.org.

---

### Dental Assisting
**Sites:** dentalassistantedu.org
**Accreditor:** CODA (Commission on Dental Accreditation) — part of ADA
**Directory:** https://coda.ada.org/en/find-a-dental-program
**Data available:** TBD
**Access:** TBD
**Scraper:** To build

---

### Sterile Processing / Central Service
**Sites:** sterileprocessingtech.org, centralservicetech.com
**Accreditor:** No single national accreditor for sterile processing programs
**Certification bodies:**
- IAHCSMM (International Association of Healthcare Central Service Materiel Management)
  https://www.iahcsmm.org/
- CBSPD (Certification Board for Sterile Processing and Distribution)
  https://www.sterileprocessing.org/
**Data available:** Certification pass rates (published annually by IAHCSMM)
**Notes:** Accreditation is not required for sterile processing programs —
this is a weakness vs other niches. Focus on certification pass rates instead.
IAHCSMM publishes a list of approved education programs.

---

### Dialysis Technician
**Sites:** dialysistechs.org
**Accreditor:** No mandatory national accreditor
**Certification:** BONENT (Board of Nephrology Examiners Nursing and Technology)
https://www.bonent.org/
**Also:** NNCC (Nephrology Nursing Certification Commission)
**Data available:** TBD
**Notes:** Similar to sterile processing — no single accreditor.
Focus on BONENT certification requirements and approved training programs.

---

### EKG / Phlebotomy
**Sites:** ekgtechs.com, wetrainphlebotomists.com
**Accreditor:** No mandatory national accreditor
**Certification bodies:**
- NHA (National Healthcareer Association) — https://www.nhanow.com/
- AMCA (American Medical Certification Association)
- ASPT (American Society of Phlebotomy Technicians)
**Data available:** Limited — these are short certificate programs
**Notes:** Program quality varies enormously. Focus on employer recognition
of certifications rather than program accreditation.

---

### HVAC
**Sites:** hvacprograms.net, cursoshvac.com
**Accreditor:** HVAC Excellence — https://www.hvacexcellence.org/
**Also:** PAHRA (Partnership for Air-Conditioning, Heating, Refrigeration Accreditation)
**Certification:** EPA 608, NATE certification
**Data available:** TBD
**Notes:** HVAC Excellence publishes an accredited program directory.
Apprenticeship programs (ACCA, union-affiliated) are separate from vocational schools.

---

### Electrician
**Sites:** electricalschool.org, escuelaselectricas.com
**Accreditor:** No national accreditor — state licensing boards govern

**The moat for electrician content is apprenticeship data, not school accreditation.**
Most searchers are trying to understand the apprenticeship vs trade school decision.
Colleges ranking on brand don't cover apprenticeships — it's not in their interest.
We do. This is the content gap.

**Data sources:**

IBEW (International Brotherhood of Electrical Workers)
- Local union directory: ibew.org/electrical-workers/local-unions
- ~900 IBEW locals, each with its own JATC
- Each JATC publishes wage progression tables, application windows, ratios
- Data is public but scattered — compiling it state by state is the moat

Electrical Training Alliance (formerly NJATC)
- https://www.electricaltrainingalliance.org/
- National standards for IBEW apprenticeships

IEC (Independent Electrical Contractors) — non-union track
- https://www.iec.org/apprenticeship

DOL RAPIDS API (highest value source)
- https://www.apprenticeship.gov/developers
- Federal registry of ALL registered apprenticeship programs
- RAPIDS code: 0159 | SOC: 47-2111
- Returns: employer, location, number of apprentices, OJT hours, wages
- Free API, no authentication — same principle as College Scorecard
- Covers union and non-union in one place
- Caveat: ~12 states (including California, Washington) use their own
  state systems instead of RAPIDS — need state agency data for those

State licensing boards
- Journeyman and master electrician license requirements per state
- Exam pass rates where published
- Reciprocity agreements between states

**Content angles that work:**
- "Apprenticeship vs trade school: which is right for you in [state]?"
- "IBEW Local [X] apprenticeship: wages, requirements, how to apply"
- "How long does an electrician apprenticeship take in [state]?"
- "Electrician license requirements in [state]: step by step"
- "Union vs non-union electrician: salary comparison in [state]"

---

### Welding
**Sites:** weldingtech.net
**Accreditor:** AWS (American Welding Society) — SENSE program
https://www.aws.org/education/sense-program
**Certification:** AWS Certified Welder, CWI (Certified Welding Inspector)
**RAPIDS code:** 0431 | **SOC:** 51-4121
**Data available:** SENSE accredited schools list + DOL registered apprenticeships
**Notes:** AWS certification matters more than apprenticeship for welders.
DOL RAPIDS gives employer names and locations useful for "where can I work
as a welder in [state]" content. AWS SENSE school list is the accreditation angle.

---

### Plumbing
**Sites:** wetrainplumbers.com
**Accreditor:** No national accreditor — state licensing boards govern
**Key source:** UA (United Association of Journeymen and Apprentices of
the Plumbing and Pipe Fitting Industry) for union apprenticeships
**Also:** PHCC (Plumbing-Heating-Cooling Contractors Association)
**RAPIDS code:** 0275 | **SOC:** 47-2152
**Notes:** Same DOL RAPIDS API as electricians — one query per state gives
all registered plumbing apprenticeship programs. State licensing requirement
data is the primary differentiator for content.

---

### Auto Mechanics
**Sites:** automechanicschools.com, usmechanicedu.com, escuelasmecanica.com
**Accreditor:** ASE Education Foundation (formerly NATEF)
https://www.aseeducationfoundation.org/
**Certification:** ASE (Automotive Service Excellence) certification
**RAPIDS code:** varies (Automotive Technician Specialist listed) | **SOC:** 49-3023
**Data available:** ASE Education Foundation publishes accredited program list
+ DOL RAPIDS registered apprenticeship programs
**Notes:** ASE accreditation is well-recognised by employers. Program list
is on their website. DOL RAPIDS also covers automotive apprenticeships —
dealer-sponsored programs (Ford, GM, Toyota) are often registered here.

---

### Home Inspection
**Sites:** homeinspectorcertification.org
**Accreditor:** No mandatory national accreditor
**Key body:** ASHI (American Society of Home Inspectors) — https://www.homeinspector.org/
**Also:** InterNACHI (International Association of Certified Home Inspectors)
**Licensing:** State-by-state — about 30 states require licensing
**Notes:** InterNACHI provides free training and certification, which is
widely recognised. State licensing requirements are the primary content angle.

---

### Culinary / Pastry
**Sites:** pastryschool.org, okchef.org, escuelascocina.com
**Accreditor:** ACFEF (American Culinary Federation Education Foundation)
https://www.acfchefs.org/ACF/Education/
**Also:** ACCSC (Accrediting Commission of Career Schools and Colleges)
**Notes:** ACF accreditation is a quality signal but not mandatory.
For these sites, program reputation and employer recognition matter more.

---

### Freight / Logistics
**Sites:** freightbrokerschools.org, freightagentschools.com, 90dayfreightbroker.com
**Accreditor:** No specific accreditor for freight broker training
**Licensing:** FMCSA (Federal Motor Carrier Safety Administration) — broker
authority required via FMCSA registration, not school accreditation
**Notes:** The licensing/registration process is the content angle —
how to get freight broker authority, bonding requirements, carrier relationships.

---

## Priority order for scraper development

Based on site revenue and data availability:

| Priority | Niche | Site | Accreditor | Revenue YTD |
|---|---|---|---|---|
| 1 | Radiology | radiologyed.org | JRCERT | $2,465 ✅ DONE |
| 2 | Pharmacy Tech | pharmacistschools.org | ASHP | $3,255 |
| 3 | Vet Tech | vettechnicians.org | AVMA-CVTEA | $6,108 |
| 4 | Medical Assisting | medassisting.org | CAAHEP/ABHES | $2,826 |
| 5 | PT Assistant | ptassistant.org | CAPTE | $777 |
| 6 | Surgical Tech | surgicaltechedu.org | CAAHEP | $1,028 |
| 7 | Dental Assisting | dentalassistantedu.org | CODA | $707 |
| 8 | Auto Mechanics | automechanicschools.com | ASE Ed Foundation | $1,880 |
| 9 | Electrician | electricalschool.org | State boards | $6,299 |
| 10 | HVAC | hvacprograms.net | HVAC Excellence | $120 |

---

## Investigation process for new accreditor

For each new accreditor:

1. Find the program directory URL
2. Test if plain HTML is accessible from the droplet:
   `curl -s [URL] | wc -c`
3. If >10KB returned, plain HTML — build requests-based scraper
4. If <1KB, JS-rendered — check for sitemap or API endpoint
5. Find the sitemap: `[domain]/sitemap.xml`
6. If programs in sitemap, scrape via sitemap (JRCERT pattern)
7. If not, check for AJAX endpoints in page source
8. Build scraper following jrcert_scraper.py as template
9. Store in orchestrator database, separate table per accreditor
10. Cross-reference against existing site page listings

---

## Related skills
- Skill 07 — School Listings and Proprietary Scoring System
- Skill 09 — Page Optimisation Process
