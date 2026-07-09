# Skill 02 — Directory Submission

## Purpose
Submit rank-and-rent and affiliate sites to free Spanish business directories to aid indexation, build initial domain authority, and establish local citations. Run once per new site, shortly after going live.

## When to use this skill
- A new rank-and-rent site has just gone live
- The site has been live for less than 2 weeks and has no directory listings
- A site needs citation cleanup or additional listings

## Prerequisites
- Site is live and accessible
- Business profile exists at `~/sites/[site-folder]/business-profile.json`
- If profile doesn't exist, create it first (see Step 1)
- directory_manager.py is installed at `~/orchestrator/directory_manager.py`

---

## Step 1 — Create the business profile

Run on the droplet:

```bash
cd ~/orchestrator && python3 directory_manager.py create [domain]
```

Example:
```bash
cd ~/orchestrator && python3 directory_manager.py create jardineriaalcobendas.com
```

For sites without a preset, edit the generated profile manually:
```bash
nano ~/sites/[site-folder]/business-profile.json
```

**Critical rules for the business profile:**
- `phone` — leave blank until a tenant is signed
- `email` — leave blank until a tenant is signed
- `address_street` — leave blank, use city only
- `business_name` — must match the domain intent exactly
- `description_long` — 150-200 words, natural Spanish, no invented facts

**Check the profile looks correct:**
```bash
cd ~/orchestrator && python3 directory_manager.py status [domain]
```

---

## Step 2 — Generate the submission prompt

```bash
cd ~/orchestrator && python3 directory_manager.py prompt [domain]
```

This generates a Claude in Chrome prompt and saves it to:
```
~/orchestrator/submission_prompt_[sitename].txt
```

View it:
```bash
cat ~/orchestrator/submission_prompt_[sitename].txt
```

---

## Step 3 — Run the Claude in Chrome submission session

Open a new Claude in Chrome session. Paste the full prompt from Step 2.

**Before starting, tell Claude in Chrome:**
- Do not take screenshots
- Report results in text only
- If a directory requires a phone number, skip it and note it
- If a directory requires email verification, complete signup and note it needs verification
- Maximum 6 directories per session to avoid timeouts

**Claude in Chrome will submit to directories in this order:**

| Priority | Directory | URL | Value | Notes |
|---|---|---|---|---|
| 1 | Google Business Profile | business.google.com/create | Critical | Requires phone verification — will pause and notify |
| 2 | Bing Places | bingplaces.com | High | Can import from GBP if done first |
| 3 | Páginas Amarillas | paginasamarillas.es/empresas/alta-empresa | High | DA 60+, Spain's main directory |
| 4 | Yelp España | biz.yelp.es/signup | High | DA 70+ |
| 5 | Hotfrog España | hotfrog.es/AddBusiness.aspx | Medium | Easy submission |
| 6 | Cylex España | cylex.es/agregar-empresa | Medium | Local directory |
| 7 | Kompass España | es.kompass.com/a/free-registration/ | Medium | B2B trust signal |
| 8 | Infoisinfo España | infoisinfo.es/add_company | Medium | Spanish directory |
| 9 | Tuugo España | tuugo.es/addBusiness | Low | Simple submission |
| 10 | Empresite (El Economista) | empresite.eleconomista.es/alta-empresa.html | Medium | Newspaper-backed |
| 11 | Donde.es | donde.es/alta-empresa | Low | Local directory |
| 12 | Travelful | travelful.net/add-listing | Low | General directory |

Run directories 1-6 in session 1, then 7-12 in session 2.

---

## Step 4 — Handle Google Business Profile verification

GBP requires phone verification. When Claude in Chrome reaches the verification step:

1. You receive a Telegram notification (once this is wired in)
2. Google calls or texts the phone number
3. For rank-and-rent sites with no tenant yet: use a temporary GHL tracking number
4. Enter the verification code
5. Mark as verified:

```bash
cd ~/orchestrator && python3 directory_manager.py mark [domain] google_business_profile submitted
```

Once verified, set up the GBP listing fully:
- Add all services
- Add description from business profile
- Set service area (not a physical address)
- Add website URL
- Set hours
- Upload 3-5 placeholder images (generic local service images, no faces)

---

## Step 5 — Log results

After each submission session, mark directories as done:

```bash
cd ~/orchestrator && python3 directory_manager.py mark [domain] [directory_key] [status]
```

Status options:
- `submitted` — successfully listed
- `failed` — could not submit, note reason
- `requires-phone` — needs phone number, retry when tenant signed
- `requires-verification` — email sent, needs clicking
- `requires-paid` — free tier not available

Example:
```bash
python3 directory_manager.py mark jardineriaalcobendas.com paginas_amarillas submitted
python3 directory_manager.py mark jardineriaalcobendas.com yelp_es requires-verification
```

Check overall status:
```bash
python3 directory_manager.py status jardineriaalcobendas.com
```

---

## Step 6 — Submit sitemap to Google Search Console

After GBP is set up:

1. Go to search.google.com/search-console
2. Add property — URL prefix — enter the full domain
3. Verify via Google Analytics or HTML tag
4. Go to Sitemaps
5. Submit: `https://[domain]/sitemap.xml`
6. Request indexing for the homepage via URL Inspection tool

Note: Each site has its own Google account. Log in with the correct account before adding the property.

---

## Directory key reference

Use these exact keys with the `mark` command:

```
google_business_profile
bing_places
paginas_amarillas
yelp_es
hotfrog_es
cylex_es
kompass_es
infoisinfo_es
tuugo_es
empresite
donde_es
travelful
```

---

## Adding this to a new site build checklist

After a site goes live, run in this order:

```bash
# 1. Create business profile
cd ~/orchestrator && python3 directory_manager.py create [domain]

# 2. Generate submission prompt
python3 directory_manager.py prompt [domain]

# 3. Check status
python3 directory_manager.py status [domain]

# 4. Paste prompt into Claude in Chrome session
# (run directories 1-6)

# 5. Log results
python3 directory_manager.py mark [domain] [key] [status]

# 6. Run second Claude in Chrome session
# (directories 7-12)

# 7. Submit sitemap to Search Console
```

Total time per site: approximately 45-60 minutes including GBP verification.

---

## Troubleshooting

**Profile not found error:**
Check the site folder exists and contains business-profile.json:
```bash
ls ~/sites/
find ~/sites -name "business-profile.json"
```

**Directory already submitted but showing pending:**
Mark it manually:
```bash
python3 directory_manager.py mark [domain] [key] submitted
```

**Claude in Chrome times out mid-session:**
Start a new session and generate a fresh prompt. The prompt generator only includes pending directories so it will pick up where it left off.

**GBP phone verification — no tenant yet:**
Create a GHL tracking number for the site, use that for verification, forward calls to a generic voicemail. Update when tenant is signed.

---

## Scaling to 50 sites

For 50 sites, directory submission becomes a background operation. Suggested schedule:

- New site goes live → create profile immediately
- Within 48 hours → run Claude in Chrome submission session (directories 1-6)
- Within 7 days → run second session (directories 7-12)
- When tenant signed → add phone number to profile, resubmit directories that required phone

At 50 sites this is roughly 2-3 Claude in Chrome sessions per week during the build phase, each handling 2-3 sites in sequence.
