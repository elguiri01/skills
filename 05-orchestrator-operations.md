# Skill 05 — Orchestrator Operations

## Purpose
Day-to-day management of the site orchestrator running on the droplet. Covers checking status, queuing jobs, monitoring spend, handling failures, and keeping the system healthy. Reference this skill whenever you need to interact with the orchestrator directly.

## System location
- Droplet: 143.244.174.8 (user: adrian)
- Orchestrator directory: ~/orchestrator/
- Database: ~/orchestrator/orchestrator.db
- Log file: ~/orchestrator/logs/orchestrator.log
- Config: ~/orchestrator/config/
- Service name: orchestrator (systemd)

---

## Daily health check

Run this first thing to see the state of the system:

```bash
cd ~/orchestrator && python3 -c "
from database import get_db, get_monthly_spend
import json
from datetime import date

conn = get_db()

# Sites
sites = conn.execute('SELECT COUNT(*) FROM sites').fetchone()[0]
pages = conn.execute('SELECT COUNT(*) FROM pages').fetchone()[0]

# Jobs
pending = conn.execute('SELECT COUNT(*) FROM jobs WHERE status=\"pending\"').fetchone()[0]
running = conn.execute('SELECT COUNT(*) FROM jobs WHERE status=\"running\"').fetchone()[0]
complete = conn.execute('SELECT COUNT(*) FROM jobs WHERE status=\"complete\"').fetchone()[0]
failed = conn.execute('SELECT COUNT(*) FROM jobs WHERE status=\"failed\"').fetchone()[0]

conn.close()

# Spend
spend = get_monthly_spend()
total_usd = sum(spend.values())
total_gbp = total_usd / 1.27
remaining = 60.0 - total_gbp

print(f'=== Orchestrator Status {date.today()} ===')
print(f'Sites: {sites} | Pages: {pages}')
print(f'Jobs: {pending} pending | {running} running | {complete} complete | {failed} failed')
print(f'Budget: GBP {total_gbp:.2f} spent | GBP {remaining:.2f} remaining')
print()
if spend:
    print('Spend by model:')
    for model, cost in spend.items():
        print(f'  {model}: \${cost:.4f}')
"
```

---

## Service management

### Check if orchestrator is running
```bash
sudo systemctl status orchestrator
```

### Start / stop / restart
```bash
sudo systemctl start orchestrator
sudo systemctl stop orchestrator
sudo systemctl restart orchestrator
```

### View live log
```bash
tail -f ~/orchestrator/logs/orchestrator.log
```

### View last 50 log lines
```bash
tail -50 ~/orchestrator/logs/orchestrator.log
```

### Check for errors in log
```bash
grep ERROR ~/orchestrator/logs/orchestrator.log | tail -20
```

---

## Job management

### View recent jobs
```bash
cd ~/orchestrator && python3 -c "
from database import get_db
import json
conn = get_db()
jobs = conn.execute('SELECT id, job_type, status, cost_usd, created_at FROM jobs ORDER BY id DESC LIMIT 20').fetchall()
for j in jobs:
    print(f'[{j[\"id\"]}] {j[\"job_type\"]} | {j[\"status\"]} | \${j[\"cost_usd\"]:.4f} | {j[\"created_at\"][:16]}')
conn.close()
"
```

### View pending jobs
```bash
cd ~/orchestrator && python3 -c "
from database import get_pending_jobs
jobs = get_pending_jobs(limit=20)
print(f'{len(jobs)} pending jobs:')
for j in jobs:
    print(f'  [{j[\"id\"]}] {j[\"job_type\"]} | priority {j[\"priority\"]} | {j[\"created_at\"][:16]}')
"
```

### View failed jobs with error messages
```bash
cd ~/orchestrator && python3 -c "
from database import get_db
conn = get_db()
jobs = conn.execute('SELECT id, job_type, error_message, created_at FROM jobs WHERE status=\"failed\" ORDER BY id DESC LIMIT 20').fetchall()
for j in jobs:
    print(f'[{j[\"id\"]}] {j[\"job_type\"]} | {j[\"created_at\"][:16]}')
    print(f'  Error: {j[\"error_message\"]}')
conn.close()
"
```

### View output from a specific job
```bash
cd ~/orchestrator && python3 -c "
from database import get_db
import json, re
conn = get_db()
job = conn.execute('SELECT output_data, job_type, cost_usd FROM jobs WHERE id=JOB_ID').fetchone()
if job and job['output_data']:
    output = json.loads(job['output_data'])
    content = output.get('result', '')
    text = re.sub(r'<[^>]+>', ' ', content)
    text = re.sub(r'\s+', ' ', text)
    words = len(text.split())
    print(f'Type: {job[\"job_type\"]} | Cost: \${job[\"cost_usd\"]:.4f} | Words: {words}')
    print()
    print(content[:2000])
conn.close()
" 2>/dev/null
```
Replace `JOB_ID` with the actual job ID.

---

## Queuing jobs

### Queue a single meta description job
```bash
cd ~/orchestrator && python3 -c "
from database import add_job, get_db
conn = get_db()
site = conn.execute('SELECT id FROM sites WHERE domain=\"DOMAIN\"').fetchone()
conn.close()
job_id = add_job(
    job_type='meta_description',
    priority=8,
    site_id=site['id'],
    model='claude-haiku-4-5-20251001',
    input_data={
        'title': 'PAGE TITLE',
        'niche': 'NICHE',
        'content_snippet': 'BRIEF DESCRIPTION OF PAGE CONTENT'
    }
)
print(f'Job queued: {job_id}')
"
```

### Queue a zone page job
```bash
cd ~/orchestrator && python3 -c "
from database import add_job, get_db
conn = get_db()
site = conn.execute('SELECT id FROM sites WHERE domain=\"DOMAIN\"').fetchone()
conn.close()
job_id = add_job(
    job_type='zone_page',
    priority=7,
    site_id=site['id'],
    model='claude-haiku-4-5-20251001',
    input_data={
        'title': 'TITLE',
        'slug': 'SLUG',
        'niche': 'NICHE',
        'service': 'SERVICE DESCRIPTION',
        'location': 'PRIMARY LOCATION',
        'zone': 'ZONE NAME',
        'parent_location': 'PARENT LOCATION',
        'language': 'es',
        'keywords': ['keyword 1', 'keyword 2'],
        'wp_page_id': WP_PAGE_ID
    }
)
print(f'Job queued: {job_id}')
"
```

### Queue a content rewrite job
```bash
cd ~/orchestrator && python3 -c "
from database import add_job, get_db
conn = get_db()
site = conn.execute('SELECT id FROM sites WHERE domain=\"DOMAIN\"').fetchone()
page = conn.execute('SELECT id FROM pages WHERE slug=\"SLUG\" AND site_id=?', (site['id'],)).fetchone()
conn.close()
job_id = add_job(
    job_type='content_rewrite',
    priority=6,
    site_id=site['id'],
    page_id=page['id'] if page else None,
    model='claude-sonnet-4-6',
    input_data={
        'niche': 'NICHE',
        'target_keywords': ['keyword 1', 'keyword 2'],
        'current_content': 'EXISTING PAGE CONTENT HERE',
        'bls_data': {},
        'school_data': []
    }
)
print(f'Job queued: {job_id}')
"
```

---

## Handling failed jobs

### Reset stuck running jobs (after a crash)
```bash
cd ~/orchestrator && python3 -c "
from database import get_db
conn = get_db()
result = conn.execute('UPDATE jobs SET status=\"failed\" WHERE status=\"running\"')
conn.commit()
print(f'Reset {result.rowcount} stuck jobs')
conn.close()
"
```

### Requeue specific failed jobs
```bash
cd ~/orchestrator && python3 -c "
from database import get_db, add_job
import json
conn = get_db()
# Requeue jobs 14-18 (example)
failed = conn.execute('SELECT id, job_type, site_id, page_id, model, input_data FROM jobs WHERE id BETWEEN 14 AND 18 AND status=\"failed\"').fetchall()
for j in failed:
    new_id = add_job(
        job_type=j['job_type'],
        priority=9,
        site_id=j['site_id'],
        page_id=j['page_id'],
        model=j['model'],
        input_data=json.loads(j['input_data']) if j['input_data'] else {}
    )
    print(f'Requeued job {j[\"id\"]} as job {new_id}')
conn.close()
"
```

### Requeue all failed jobs for a site
```bash
cd ~/orchestrator && python3 -c "
from database import get_db, add_job
import json
conn = get_db()
site = conn.execute('SELECT id FROM sites WHERE domain=\"DOMAIN\"').fetchone()
failed = conn.execute(
    'SELECT id, job_type, site_id, page_id, model, input_data FROM jobs WHERE site_id=? AND status=\"failed\"',
    (site['id'],)
).fetchall()
for j in failed:
    new_id = add_job(
        job_type=j['job_type'],
        priority=8,
        site_id=j['site_id'],
        page_id=j['page_id'],
        model=j['model'],
        input_data=json.loads(j['input_data']) if j['input_data'] else {}
    )
    print(f'Requeued {j[\"job_type\"]} as job {new_id}')
print(f'Total requeued: {len(failed)}')
conn.close()
"
```

---

## Budget monitoring

### Check current month spend
```bash
cd ~/orchestrator && python3 -c "
from database import get_monthly_spend
spend = get_monthly_spend()
total_usd = sum(spend.values())
total_gbp = total_usd / 1.27
remaining = 60.0 - total_gbp
print(f'Total: \${total_usd:.4f} USD = GBP {total_gbp:.2f}')
print(f'Remaining: GBP {remaining:.2f} of GBP 60.00')
print()
for model, cost in sorted(spend.items(), key=lambda x: x[1], reverse=True):
    print(f'  {model}: \${cost:.4f}')
"
```

### Estimated cost per job type
| Job type | Model | Approx cost |
|---|---|---|
| meta_description | Haiku | $0.0001 |
| schema_generation | Haiku | $0.0002 |
| zone_page | Haiku | $0.0026 |
| content_brief | Haiku | $0.0010 |
| service_page | Sonnet | $0.0462 |
| homepage_content | Sonnet | $0.0613 |
| content_expansion | Sonnet | $0.1404 |
| content_rewrite | Sonnet | $0.0200-0.0600 |

### Monthly budget planning at GBP 60
At current usage patterns (mix of Haiku and Sonnet):
- ~10 complete site content sets (homepage + 4 service + 4 zone): ~GBP 4.50 each = GBP 45
- ~500 meta descriptions at GBP 0.008 each = GBP 4
- ~100 schema generations = GBP 1.50
- Buffer for rewrites and expansions = GBP 9.50
- **Total: GBP 60**

---

## Site and page management

### List all sites in database
```bash
cd ~/orchestrator && python3 -c "
from database import get_db
conn = get_db()
sites = conn.execute('SELECT id, domain, site_type, niche, status FROM sites').fetchall()
for s in sites:
    pages = conn.execute('SELECT COUNT(*) FROM pages WHERE site_id=?', (s['id'],)).fetchone()[0]
    print(f'[{s[\"id\"]}] {s[\"domain\"]} | {s[\"site_type\"]} | {s[\"niche\"]} | {pages} pages | {s[\"status\"]}')
conn.close()
"
```

### List pages for a site
```bash
cd ~/orchestrator && python3 -c "
from database import get_db
conn = get_db()
site = conn.execute('SELECT id FROM sites WHERE domain=\"DOMAIN\"').fetchone()
pages = conn.execute('SELECT id, wp_page_id, slug, title, word_count, page_type FROM pages WHERE site_id=?', (site['id'],)).fetchall()
for p in pages:
    print(f'[{p[\"id\"]}] WP:{p[\"wp_page_id\"]} | {p[\"slug\"]} | {p[\"word_count\"]} words | {p[\"page_type\"]}')
conn.close()
"
```

### Add a new site manually
```bash
cd ~/orchestrator && python3 -c "
from database import add_site
site_id = add_site(
    domain='DOMAIN',
    site_type='rank_rent',
    niche='NICHE',
    location='LOCATION',
    wp_url='https://DOMAIN',
    wp_username='USERNAME',
    wp_app_password='APP PASSWORD',
    hosting='siteground',
    migration_status='complete',
    status='active'
)
print(f'Site added: {site_id}')
"
```

### Update site credentials
```bash
cd ~/orchestrator && python3 -c "
from database import update_site
update_site('DOMAIN',
    wp_app_password='NEW PASSWORD',
    ghl_subaccount_id='GHL ID'
)
print('Updated')
"
```

---

## Crawler operations

### Crawl a single site (fetch all pages and index them)
```bash
cd ~/orchestrator && python3 crawler.py crawl-one DOMAIN
```

### Crawl all sites
```bash
cd ~/orchestrator && python3 crawler.py crawl
```

### Crawl only rank-and-rent sites
```bash
cd ~/orchestrator && python3 crawler.py crawl rank_rent
```

### Crawl only affiliate sites
```bash
cd ~/orchestrator && python3 crawler.py crawl affiliate
```

### Show database stats
```bash
cd ~/orchestrator && python3 crawler.py stats
```

### Queue optimisation jobs for a site
```bash
cd ~/orchestrator && python3 crawler.py queue SITE_ID
```

---

## Pushing content to WordPress

### Push content from a completed job to a WordPress page
```bash
cd ~/orchestrator && python3 -c "
import json, requests
from database import get_db

conn = get_db()
job = conn.execute('SELECT output_data FROM jobs WHERE id=JOB_ID').fetchone()
site = conn.execute('SELECT wp_url, wp_username, wp_app_password FROM sites WHERE domain=\"DOMAIN\"').fetchone()
conn.close()

content = json.loads(job['output_data'])['result']
content = content.strip()
for fence in ['\`\`\`html', '\`\`\`']:
    if content.startswith(fence): content = content[len(fence):]
if content.endswith('\`\`\`'): content = content[:-3]

url = f\"{site['wp_url']}/wp-json/wp/v2/pages/WP_PAGE_ID\"
r = requests.post(url, json={'content': content, 'status': 'publish'},
                  auth=(site['wp_username'], site['wp_app_password']), timeout=30)
print(f'Status: {r.status_code}')
"
```
Replace `JOB_ID`, `DOMAIN` and `WP_PAGE_ID` with actual values.

---

## Job type reference

| Job type | Handler | Model | Description |
|---|---|---|---|
| `meta_description` | handle_meta_description | Haiku | Generate meta description for a page |
| `schema_generation` | handle_schema_generation | Haiku | Generate JSON-LD schema markup |
| `content_brief` | handle_content_brief | Haiku | Generate structured content brief |
| `zone_page` | handle_zone_page | Haiku | Generate full zone/location page |
| `service_page` | handle_service_page | Sonnet | Generate full service page |
| `homepage_content` | handle_homepage_content | Sonnet | Generate full homepage content |
| `content_rewrite` | handle_content_rewrite | Sonnet | Rewrite existing page with new data |
| `content_expansion` | handle_content_expansion | Sonnet | Expand existing content to hit word count target |

---

## Common issues and fixes

### Orchestrator not picking up jobs
1. Check it is running: `sudo systemctl status orchestrator`
2. Check the database path is correct: jobs should be in `~/orchestrator/orchestrator.db`
3. Ensure you are in `~/orchestrator/` when running scripts that add jobs
4. Check for budget limit: if spend is near GBP 60 the orchestrator pauses automatically

### Jobs failing with "Unknown job type"
A new job type was queued before the handler was added to orchestrator.py. Add the handler function and register it in `JOB_HANDLERS`, then restart:
```bash
sudo systemctl restart orchestrator
```
Then requeue the failed jobs.

### Jobs failing with "Connection error"
Usually a temporary network issue or Anthropic API timeout. Simply requeue the failed jobs — they will succeed on retry.

### Out of memory crash
Happened on 2GB droplet when running Sonnet jobs. Now running on 8GB — should not recur. If it does, check droplet memory: `free -h`

### Log file empty despite orchestrator running
The log file may have wrong permissions. Fix:
```bash
sudo chown adrian:adrian ~/orchestrator/logs/orchestrator.log
chmod 664 ~/orchestrator/logs/orchestrator.log
sudo systemctl restart orchestrator
```

### Orchestrator restarting repeatedly
Check journalctl for the actual error:
```bash
sudo journalctl -u orchestrator -n 50 --no-pager
```

---

## Telegram notifications

The orchestrator sends these notifications automatically:

| Event | Level | When |
|---|---|---|
| Orchestrator started | ✅ success | On service start |
| Job failed | ❌ error | When any job fails |
| Budget low | ⚠️ warning | When < GBP 5 remaining |
| Daily summary | 📊 daily | At midnight UTC |

### Send a test notification
```bash
cd ~/orchestrator && python3 -c "
from notify import send
send('Test notification from orchestrator', level='info')
"
```

### Send a daily summary manually
```bash
cd ~/orchestrator && python3 -c "
from notify import daily_summary
from database import get_monthly_spend
spend = get_monthly_spend()
total = sum(spend.values())
daily_summary({
    'Sites in database': '1',
    'Budget spent': f'GBP {total/1.27:.2f}',
    'Budget remaining': f'GBP {60 - total/1.27:.2f}',
})
"
```

---

## File reference

| File | Purpose |
|---|---|
| `orchestrator.py` | Main job runner — job handlers and run loop |
| `database.py` | All database operations |
| `notify.py` | Telegram notification functions |
| `crawler.py` | WordPress page crawler and job queuer |
| `competitor_crawler.py` | SerpAPI competitor analysis |
| `directory_manager.py` | Directory submission tracking |
| `expand_content.py` | Queue content expansion jobs |
| `config/api_keys.json` | Anthropic, OpenAI, Gemini, SerpAPI keys |
| `config/telegram.json` | Telegram bot token and chat ID |
| `config/licenses.json` | GP, GB, AIOSEO, GHL licence keys |
| `logs/orchestrator.log` | Rolling daily log |
| `orchestrator.db` | SQLite database — all sites, pages, jobs, spend |

---

## Related skills

- Skill 01 — New Site Build (uses orchestrator to generate content)
- Skill 03 — Competitor Analysis (generates briefs that feed into jobs)
- Skill 06 — Affiliate Site Optimisation (uses orchestrator for content rewrites)

## Page conversion classification (electricalschool.org pattern)

Not all traffic converts. The agent must classify pages before prioritising
content work:

CONVERTS: state pages (/tx/, /ca/ etc.), Spanish state pages (/es/tx/),
          article/career guide pages, salary pages
NO CONVERT: glossary pages, reference term pages, tool pages
STRATEGY: only queue content expansion on converting page types.
          Glossary traffic is a link building residual, not a revenue driver.
          Video production should target queries that land on state and article
          pages, not glossary queries.
