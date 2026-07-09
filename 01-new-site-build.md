# Skill 01 — New Rank & Rent Site Build

## Purpose
End-to-end process for building a new rank-and-rent local service website in Spain. Covers everything from niche selection through to content live, directories submitted and Search Console verified. Target: 30 minutes of human time per site once the system is running.

## System context
- Droplet: 143.244.174.8 (user: adrian)
- Orchestrator: ~/orchestrator/ (running 24/7 as systemd service)
- Sites folder: ~/sites/
- Skills folder: ~/skills/
- Open WebUI: https://workspace.galenahall.com
- WordPress hosting: Siteground
- Stack: WordPress + GeneratePress + GenerateBlocks + AIOSEO + GHL forms

---

## Phase 0 — Niche and domain decision

### Niche selection principles
- Urgency niches rank faster (garage doors, roofing, irrigation repair, pest control)
- Avoid oversaturated niches (locksmith, plumber) until system is proven
- Chalet/luxury market in La Moraleja, Ciudalcampo, El Encinar pays better tenants
- One niche + one primary location per site
- Supporting zone pages for nearby areas (not separate sites)

### Location targeting
Primary targets in order:
1. Alcobendas — best municipality-level target, broad intent
2. La Moraleja — best for luxury/chalet services
3. San Sebastián de los Reyes — strong second municipality
4. Ciudalcampo — high-value chalet market
5. Fuente del Fresno — smaller, good lead quality
6. Mirasierra — useful supporting pages
7. Tres Cantos / Colmenar Viejo — second wave expansion

### Domain format
```
[service][location].es
Examples:
  puertasgarajealcobendas.es
  piscinaslamoraleja.es
  goterasalcobendas.es
  riegoautomaticolamoraleja.es
  plagasalcobendas.es
```

### Before building — validate tenant availability
Before spending time on build, call or WhatsApp 5-10 companies in the niche:
"¿Trabajáis Alcobendas, La Moraleja y San Sebastián de los Reyes, y estáis cogiendo nuevos trabajos?"
Not selling yet — just confirming the market exists.

---

## Phase 1 — Domain and WordPress setup

### Step 1.1 — Register domain
Register at your usual registrar. Point DNS to Siteground nameservers.

### Step 1.2 — Create Siteground hosting
Add new WordPress site in Siteground dashboard.
- WordPress auto-installer
- Note the wp-admin URL, username and password

### Step 1.3 — Add site to orchestrator database
On the droplet:

```bash
cd ~/orchestrator && python3 -c "
from database import add_site
site_id = add_site(
    domain='[domain]',
    site_type='rank_rent',
    niche='[niche]',
    location='[location]',
    wp_url='https://[domain]',
    wp_username='[username]',
    wp_app_password='[app_password]',
    hosting='siteground',
    migration_status='complete',
    status='active'
)
print(f'Site added: {site_id}')
"
```

To create a WordPress application password:
- Go to wp-admin → Users → Profile → Application Passwords
- Name it "Orchestrator" and generate
- Save the password immediately (shown once only)

### Step 1.4 — WordPress foundation via Claude in Chrome

Send this prompt to Claude in Chrome (no screenshots, text report only):

```
Go to [wp-admin URL] and log in. Complete these tasks in order. No screenshots — text report only.

Task 1 — Settings
- Settings → General: Site Title = "[Business Name]", Tagline = "[Tagline]"
- Settings → Permalinks: Post name. Save.
- Settings → Reading: Static page. Create blank page "Inicio", set as homepage.

Task 2 — Install plugins
Install and activate:
- GeneratePress (theme)
- GenerateBlocks
- All in One SEO

Task 3 — Activate licences
GeneratePress Premium licence:
python3 -c "import json; d=json.load(open('/home/adrian/orchestrator/config/licenses.json')); print(d['generatepress premium']['license_key'])"

GenerateBlocks licence:
python3 -c "import json; d=json.load(open('/home/adrian/orchestrator/config/licenses.json')); print(d['generateblocks']['license_key'])"

AIOSEO licence:
python3 -c "import json; d=json.load(open('/home/adrian/orchestrator/config/licenses.json')); print(d['aioseo']['license_key'])"

Task 4 — Delete default content
Delete Sample Page and Hello World post.

Task 5 — Set global layout
Appearance → Customize:
- Sidebar: No sidebar (all layouts)
- Primary colour: [primary hex]
- Secondary colour: [accent hex]

Task 6 — Disable page titles globally (GP Premium required)
- Appearance → Elements → Add New
- Type: Layout
- Name: Disable Page Titles - All Pages
- In the element settings find "Disable Elements"
- Check "Content Title"
- Display Rules → Location → Page → All Pages
- Publish

Task 7 — Create page structure
Create these pages as drafts with exact slugs:
[List pages with slugs from site spec]

Report back: confirmation of each task + page IDs of all created pages.
```

---

## Phase 2 — Site spec and competitor analysis

### Step 2.1 — Create site spec on droplet

```bash
mkdir -p ~/sites/[site-folder]/content
cp ~/sites/_templates/site-spec-template.md ~/sites/[site-folder]/site-spec.md
```

Edit the spec with niche, location, brand colours, tenant target, keywords.

### Step 2.2 — Run competitor analysis

```bash
cd ~/orchestrator

# Primary keyword
python3 competitor_crawler.py analyse "[primary keyword] [location]"

# Secondary keywords
python3 competitor_crawler.py analyse "[service] [location]" "[location]"
python3 competitor_crawler.py analyse "[service] La Moraleja" "La Moraleja"
```

Briefs are saved to:
```
~/sites/_knowledge/[niche]/[keyword-slug]-brief.json
```

Review the output:
- Note avg word count and target word count
- Note competitor H1s (differentiate from these)
- Note common H2 topics (cover and expand these)
- Note zone mentions (include all zones competitors mention)

---

## Phase 3 — Content generation

### Step 3.1 — Queue content jobs with competitor briefs

Create a queue script from the template:
```bash
cp ~/orchestrator/queue_jardineria.py ~/orchestrator/queue_[site].py
```

Edit the script:
- Update domain
- Update wp_page_id mappings from Phase 1 page IDs
- Update keywords per page
- Update brief paths to point to correct knowledge base files

Run:
```bash
cd ~/orchestrator && python3 queue_[site].py
```

Watch the orchestrator process jobs:
```bash
tail -f ~/orchestrator/logs/orchestrator.log
```

### Step 3.2 — Check content quality

After all jobs complete, check homepage word count:
```bash
cd ~/orchestrator && python3 -c "
from database import get_db
import json, re
conn = get_db()
# Replace JOB_ID with the homepage job ID from the log
job = conn.execute('SELECT output_data FROM jobs WHERE id=JOB_ID').fetchone()
content = json.loads(job['output_data'])['result']
content = content.strip()
for fence in ['\`\`\`html', '\`\`\`']:
    if content.startswith(fence): content = content[len(fence):]
if content.endswith('\`\`\`'): content = content[:-3]
text = re.sub(r'<[^>]+>', ' ', content)
words = len(text.split())
print(f'Words: {words} | HTML: {len(content)} chars')
conn.close()
"
```

If word count is below target, queue an expansion job:
```bash
cd ~/orchestrator && python3 expand_content.py
```

### Step 3.3 — Push content to WordPress

Create push script:
```bash
cp ~/orchestrator/push_jardineria.py ~/orchestrator/push_[site].py
```

Update job ID to page ID mappings, then:
```bash
cd ~/orchestrator && python3 push_[site].py
```

---

## Phase 4 — Design and CSS

### Step 4.1 — Generate site CSS

Each site uses a prefixed CSS class system based on the site initials.
Example: jardineriaalcobendas.com → `ja-` prefix

Colour palette decisions:
- Pick palette appropriate to niche and location
- Reference niche colour guidelines in site spec
- Keep it professional — local trades don't need flashy colours

CSS structure (copy from closest existing site and adapt colours):
- Tejados: `ta-` prefix, navy/orange
- Jardines: `ja-` prefix, dark green/gold
- New sites: choose prefix from initials, choose 2 core colours

### Step 4.2 — Apply CSS via Claude in Chrome

Send Claude in Chrome to wp-admin → Appearance → Customize → Additional CSS.
Paste the full site CSS. Publish.

### Step 4.3 — Fix full-width homepage layout

Two options depending on GP Premium status:

**Option A — GP Elements (preferred, requires GP Premium)**
Create a Hook Element:
- Type: Block
- Hook: generate_after_header
- Display: Front Page only
- Content: the full homepage HTML
Then clear page 11/Inicio content and hide content area:
```css
body.home .content-area,
body.home .entry-content,
body.home article { display: none !important; }
```

**Option B — CSS workaround (if GP Premium not yet active)**
Add to Additional CSS:
```css
body.home .entry-header { display: none !important; }
body.home .inside-article { padding: 0 !important; }
body.home .content-area { width: 100% !important; max-width: 100% !important; }
```

### Step 4.4 — Publish all draft pages

All pages created in Phase 1 are drafts. Publish them:
```bash
cd ~/orchestrator && python3 -c "
import requests
WP_URL = 'https://[domain]'
AUTH = ('[username]', '[app_password]')
# Get all draft pages
r = requests.get(f'{WP_URL}/wp-json/wp/v2/pages', auth=AUTH, params={'status': 'draft', 'per_page': 50})
pages = r.json()
for page in pages:
    pub = requests.post(f'{WP_URL}/wp-json/wp/v2/pages/{page[\"id\"]}', auth=AUTH, json={'status': 'publish'})
    print(f'Published: {page[\"slug\"]} - {pub.status_code}')
"
```

---

## Phase 5 — GHL form setup

### Step 5.1 — Create GHL subaccount
- Log into GoHighLevel agency dashboard
- Create new subaccount: [Business Name] - [Domain]
- Set up basic pipeline: New Lead → Contacted → Qualified → Rented

### Step 5.2 — Create lead capture form
- Go to Sites → Forms → Add Form
- Fields: Nombre, Teléfono, Tipo de servicio (dropdown), Mensaje
- Style to match site colours
- Copy the embed code

### Step 5.3 — Embed form in site
Add form to contact page and hero section via Claude in Chrome or REST API.

Update the site record in the database:
```bash
cd ~/orchestrator && python3 -c "
from database import update_site
update_site('[domain]', ghl_subaccount_id='[subaccount_id]')
"
```

---

## Phase 6 — Directory submission

Follow Skill 02 — Directory Submission.

Quick reference:
```bash
cd ~/orchestrator && python3 directory_manager.py create [domain]
python3 directory_manager.py prompt [domain]
# Paste prompt into Claude in Chrome
python3 directory_manager.py status [domain]
```

---

## Phase 7 — Search Console

### Step 7.1 — Add property
- Log into the correct Google account for this site
- Go to search.google.com/search-console
- Add property → URL prefix → https://[domain]
- Verify via AIOSEO HTML tag method (easiest)

### Step 7.2 — Submit sitemap
- Sitemaps → Add sitemap → [domain]/sitemap.xml
- Submit

### Step 7.3 — Request indexing
- URL Inspection → enter homepage URL
- Request Indexing
- Repeat for main service pages

---

## Phase 8 — Final checks

Run through this checklist before considering the site complete:

**Content:**
- [ ] Homepage published and live
- [ ] All service pages published
- [ ] All zone pages published
- [ ] Contact page published
- [ ] No placeholder phone numbers visible
- [ ] No placeholder WhatsApp links visible
- [ ] All CTAs point to /contacto/
- [ ] No fake reviews or testimonials

**Technical:**
- [ ] SSL working (https://)
- [ ] Sitemap accessible at /sitemap.xml
- [ ] Search Console verified and sitemap submitted
- [ ] AIOSEO activated and configured
- [ ] Homepage shows correct H1 and meta description
- [ ] Mobile layout working

**Local:**
- [ ] GBP listing created (may need phone to verify)
- [ ] At least 3 directories submitted
- [ ] GHL form working and capturing leads to subaccount

**Database:**
- [ ] Site in orchestrator database with correct credentials
- [ ] Pages crawled and in pages table
- [ ] Business profile created

---

## Site build time targets

| Phase | Target time | Notes |
|---|---|---|
| Domain + WordPress setup | 15 mins | Manual |
| WordPress foundation (Claude in Chrome) | 20 mins | Automated |
| Competitor analysis | 10 mins | Automated |
| Content generation | 0 mins | Orchestrator runs overnight |
| CSS + design | 20 mins | Semi-automated |
| GHL form | 10 mins | Manual |
| Directory submission | 30 mins | Claude in Chrome |
| Search Console | 10 mins | Manual |
| **Total human time** | **~2 hours** | First site |
| **At scale (templates ready)** | **~45 mins** | Sites 10+ |

---

## Reusable assets per site

Each completed site produces reusable assets for future builds:

- `~/sites/[domain]/site-spec.md` — niche and brand decisions
- `~/sites/[domain]/business-profile.json` — directory submission profile
- `~/sites/_knowledge/[niche]/` — competitor briefs (reuse for same niche in different location)
- CSS template — copy and recolour for same niche in new location
- Queue script — copy and update domain/page IDs

By site 10 in a niche, the build is mostly copy-paste with location substitution.

---

## Related skills

- Skill 02 — Directory Submission
- Skill 03 — Competitor Analysis
- Skill 04 — CSS Design System
- Skill 05 — Orchestrator Operations
