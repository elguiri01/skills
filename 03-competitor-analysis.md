# Skill 03 — Competitor Analysis

## Purpose
Analyse what is currently ranking for target keywords before generating content. Produces a structured content brief that tells Claude exactly what word count to beat, which topics to cover, and which local zones to mention. Without this step, generated content is generic and unlikely to rank.

## When to use this skill
- Before generating any homepage or service page content for a new site
- Before rewriting existing pages that are not ranking
- When adding new zone pages to an existing site
- When a page has been live for 3+ months without ranking movement

## Prerequisites
- SerpAPI key in `~/orchestrator/config/api_keys.json` under `"serpapi"`
- competitor_crawler.py installed at `~/orchestrator/competitor_crawler.py`
- Knowledge base directory exists: `~/sites/_knowledge/`

---

## How it works

The crawler:
1. Searches Google via SerpAPI for the target keyword
2. Filters out directories, aggregators and irrelevant results
3. Fetches the HTML of the top 5 organic results
4. Extracts word count, H1/H2/H3 structure, and local zone mentions
5. Calculates average word count and sets target at +30%
6. Saves a structured JSON brief to the knowledge base
7. Prints a readable summary

The brief is then injected into content generation prompts so Claude writes to beat the competition, not just fill a page.

---

## Step 1 — Run competitor analysis

### Basic usage

```bash
cd ~/orchestrator && python3 competitor_crawler.py analyse "[keyword]"
```

### With specific location

```bash
cd ~/orchestrator && python3 competitor_crawler.py analyse "[keyword]" "[location]"
```

### Examples

```bash
# Primary keyword
python3 competitor_crawler.py analyse "jardineria alcobendas"

# Service + location
python3 competitor_crawler.py analyse "riego automatico alcobendas" "Alcobendas"

# Zone page keyword
python3 competitor_crawler.py analyse "mantenimiento jardines La Moraleja" "La Moraleja"
python3 competitor_crawler.py analyse "jardineria La Moraleja" "La Moraleja"

# Different niches
python3 competitor_crawler.py analyse "puertas garaje alcobendas" "Alcobendas"
python3 competitor_crawler.py analyse "control plagas alcobendas" "Alcobendas"
python3 competitor_crawler.py analyse "impermeabilizaciones alcobendas" "Alcobendas"
```

---

## Step 2 — Read the output

The crawler prints a summary and saves a JSON brief. Read the summary carefully before generating content.

### What to look for

**Competitors analysed**
How many pages were successfully fetched. 4-5 is good. Below 3 means thin competition — easier to rank but less to learn from.

**Average word count**
What the current ranking pages have. If below 1,000 the niche is weakly contested. If above 2,000 you need substantial content.

**Target word count (+30%)**
This is the minimum your content should hit. Instruct the orchestrator to generate at least this many words.

**Competitor H1s**
What the ranking pages use as their main headline. Your H1 should be clearly differentiated — not a copy of these. If all competitors have generic H1s, a specific benefit-led H1 will stand out.

**Common H2 topics**
Sections that multiple ranking pages cover. These are the topics Google expects to see on a page about this keyword. Cover all of them and go deeper than the competition.

**Zone mentions**
How often local area names appear across competitor pages. If Alcobendas appears 60x and La Moraleja only 3x, that's a gap — mention La Moraleja more than competitors do.

**Ranking URLs**
Visit 1-2 of the top ranking pages manually to understand their tone, structure and depth. The crawler gives you the data — your eyes give you the context.

### Example output interpretation

```
ANALYSIS: riego automatico alcobendas | Alcobendas
Competitors analysed: 5
Avg word count:       1377
Target word count:    1790 (+30%)

Competitor H1s:
  - Servicios de EcoJardines Iris Alcobendas    ← generic, no service mention
  - Instalación de Riego e Instalar Goteo en Alcobendas  ← specific, worth differentiating
  - Cómo elegir el mejor sistema de riego automático en Alcobendas  ← informational
  - Empresas de Instalar riego automatico en Madrid  ← directory, not a real competitor
  - Encuentra las mejores empresas de jardinería en Alcobendas  ← directory

Common H2 topics:
  - profesionales de la jardinería a su servicio en alcobendas
  - paisajismo y jardinería en alcobendas
  - mantenimiento de jardines alcobendas
  - instalación de césped artificial en alcobendas

Zone mentions:
  alcobendas: 60x
  la moraleja: 3x    ← gap to exploit
  tres cantos: 1x
```

**What this tells you:**
- Target 1,790+ words
- H1 should specifically mention riego automático (not just jardinería) and be benefit-led
- Cover paisajismo, mantenimiento and césped sections
- Mention La Moraleja much more than competitors — it's a gap
- Two of the five results are directories (Habitissimo, Cronoshare) — the real competition is weak

---

## Step 3 — Where briefs are saved

Briefs are saved automatically to:
```
~/sites/_knowledge/[niche-slug]/[keyword-slug]-brief.json
```

Examples:
```
~/sites/_knowledge/jardineria/jardineria-alcobendas-brief.json
~/sites/_knowledge/riego/riego-automatico-alcobendas-brief.json
~/sites/_knowledge/mantenimiento/mantenimiento-jardines-la-moraleja-brief.json
~/sites/_knowledge/jardineria/jardineria-la-moraleja-brief.json
```

List all saved briefs:
```bash
find ~/sites/_knowledge -name "*.json" | sort
```

View a brief:
```bash
cat ~/sites/_knowledge/jardineria/jardineria-alcobendas-brief.json | python3 -m json.tool
```

---

## Step 4 — Use briefs in content generation

When queuing content jobs, load the brief and pass it as `competitor_brief` in the input data.

### In a queue script

```python
import json

def load_brief(path):
    import os
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return {}

# Load the relevant brief
homepage_brief = load_brief('/home/adrian/sites/_knowledge/jardineria/jardineria-alcobendas-brief.json')
riego_brief = load_brief('/home/adrian/sites/_knowledge/riego/riego-automatico-alcobendas-brief.json')

# Pass into job input_data
add_job(
    job_type='homepage_content',
    input_data={
        'title': 'Jardinería y Riego Automático en Alcobendas',
        'niche': 'jardineria',
        'location': 'Alcobendas',
        'keywords': ['jardineria alcobendas', 'riego automatico alcobendas'],
        'competitor_brief': homepage_brief  # ← brief injected here
    }
)
```

The `handle_homepage_content` and `handle_service_page` handlers in orchestrator.py automatically extract:
- `brief.get('target_word_count')` — sets the word count target in the prompt
- `brief.get('competitor_h1s')` — tells Claude what H1s to differentiate from
- `brief.get('common_h2_topics')` — tells Claude which topics to cover
- `brief.get('zone_mentions')` — tells Claude which local areas to mention

---

## Step 5 — How many keywords to analyse per site

### Minimum (get live fast)
- 1 brief for homepage (primary keyword + location)
- 1 brief for main service page (key service + location)

### Standard (recommended)
- 1 per homepage
- 1 per service page (typically 4-5 per site)
- 1-2 for zone pages (cover the top zones)

### Full (maximum quality)
- 1 per page

### SerpAPI usage planning
Free tier: 100 searches/month
Paid tier: ~1,000 searches/month at $14 (via Azure Grounding with Bing)

At standard level (7 briefs per site), 100 searches covers ~14 sites per month.
At full level (10 briefs per site), 100 searches covers ~10 sites per month.

If building 20 sites per month, upgrade to paid tier.

---

## Step 6 — Reusing briefs across locations

If you build the same niche in multiple locations, you only need to re-run the analysis for the location-specific keywords. The niche-level topics remain consistent.

Example — building irrigation sites in both Alcobendas and San Sebastián de los Reyes:

```bash
# Run once for Alcobendas (already done)
python3 competitor_crawler.py analyse "riego automatico alcobendas" "Alcobendas"

# Run for San Sebastián de los Reyes
python3 competitor_crawler.py analyse "riego automatico san sebastian de los reyes" "San Sebastian de los Reyes"
```

The H2 topics will be largely the same — only the zone mentions and local context will differ. This saves API calls.

---

## Step 7 — Manual competitor review

The crawler gives you data. For the most important pages — homepage and primary service page — also do a quick manual review:

1. Open the top 2-3 ranking URLs from the brief
2. Note anything the crawler missed:
   - Images used (before/after, team photos, equipment)
   - Trust signals (certifications, years in business, number of clients)
   - Specific local references (street names, landmarks, urbanización names)
   - Unique content angles (pricing guides, how-to sections, seasonal tips)
3. Add these observations as notes in the brief JSON or site spec

This takes 10 minutes and meaningfully improves content quality for pages that need to rank for competitive terms.

---

## Troubleshooting

**No results returned:**
```
SerpAPI search error: 401 Client Error
```
Check the SerpAPI key in api_keys.json. Go to serpapi.com, log in, copy the key from the dashboard.

**Only 2-3 competitors fetched instead of 5:**
Some pages time out or block the crawler. This is normal. 3 competitors is enough data for a usable brief.

**Directories dominating results (Habitissimo, Cronoshare, Yelp):**
The crawler filters common directories but some get through. If most results are directories, the real competition is weak — good news for ranking. The word count target may be lower than expected.

**Brief saved but word count seems wrong:**
The word count is extracted from visible text after stripping HTML. SVG code, scripts and hidden elements are excluded. A page with lots of SVG icons may show lower word count than it appears.

**Knowledge base directory not found:**
```bash
mkdir -p ~/sites/_knowledge
```

---

## Brief JSON structure reference

```json
{
  "keyword": "riego automatico alcobendas",
  "location": "Alcobendas",
  "competitors_analysed": 5,
  "avg_word_count": 1377,
  "target_word_count": 1790,
  "competitor_h1s": [
    "Servicios de EcoJardines Iris Alcobendas",
    "Instalación de Riego e Instalar Goteo en Alcobendas"
  ],
  "common_h2_topics": [
    "profesionales de la jardinería a su servicio en alcobendas",
    "mantenimiento de jardines alcobendas"
  ],
  "common_h3_topics": [],
  "zone_mentions": {
    "alcobendas": 60,
    "la moraleja": 3,
    "tres cantos": 1
  },
  "competitor_urls": [
    "https://ecojardinesiris.com/servicios-jardineria-alcobendas/",
    "https://jardimadrid.com/instalacion-de-riego-alcobendas.html"
  ],
  "text_samples": [],
  "created_at": "2026-06-22T15:30:00"
}
```

---

## Keywords to analyse per niche — quick reference

### Jardinería / Riego
```bash
python3 competitor_crawler.py analyse "jardineria alcobendas"
python3 competitor_crawler.py analyse "riego automatico alcobendas" "Alcobendas"
python3 competitor_crawler.py analyse "mantenimiento jardines la moraleja" "La Moraleja"
python3 competitor_crawler.py analyse "jardineria la moraleja" "La Moraleja"
python3 competitor_crawler.py analyse "poda arboles alcobendas" "Alcobendas"
```

### Puertas de garaje
```bash
python3 competitor_crawler.py analyse "puertas garaje alcobendas"
python3 competitor_crawler.py analyse "reparacion puertas garaje alcobendas" "Alcobendas"
python3 competitor_crawler.py analyse "puertas automaticas la moraleja" "La Moraleja"
python3 competitor_crawler.py analyse "motor puerta garaje alcobendas" "Alcobendas"
```

### Tejados / Impermeabilizaciones
```bash
python3 competitor_crawler.py analyse "goteras alcobendas"
python3 competitor_crawler.py analyse "impermeabilizacion alcobendas" "Alcobendas"
python3 competitor_crawler.py analyse "reparacion tejados alcobendas" "Alcobendas"
python3 competitor_crawler.py analyse "goteras la moraleja" "La Moraleja"
```

### Piscinas
```bash
python3 competitor_crawler.py analyse "mantenimiento piscinas la moraleja" "La Moraleja"
python3 competitor_crawler.py analyse "piscinas alcobendas"
python3 competitor_crawler.py analyse "mantenimiento piscinas ciudalcampo" "Ciudalcampo"
```

### Control de plagas
```bash
python3 competitor_crawler.py analyse "control plagas alcobendas"
python3 competitor_crawler.py analyse "eliminar avispas alcobendas" "Alcobendas"
python3 competitor_crawler.py analyse "termitas la moraleja" "La Moraleja"
```

---

## Related skills

- Skill 01 — New Site Build (Step 2.2 calls this skill)
- Skill 05 — Orchestrator Operations (queuing content jobs with briefs)
