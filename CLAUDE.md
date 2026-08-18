# Operating Rules

## Read the constitution first

At the start of every session, read `~/skills/12-agent-operations.md` in full
before doing any work. It is the operating constitution for this system: the
content pipeline order, the hard gates, the human sign-off matrix, spend
discipline, and change management. When in doubt, follow that file. When that
file is wrong, propose an edit rather than silently deviating.

Skill 12 points to the other skills to read before content work: 05
(orchestrator ops), 09 (page optimisation), 10 (data sources), 11 (content
style).

## The skills index

Numbered skills are portfolio operations. Named directories are agent patterns
that apply across all of them.

- `01` new site build, `02` directory submission, `03` competitor analysis
- `05` orchestrator ops, `06` E-E-A-T authority, `07` school listings data
- `08` video production, `09` page optimisation, `10` accreditation sources
- `11` content style, `12` agent operations (the constitution), `13` architecture
- `14` GSC credentials, `15` technical SEO, `16` persona authority
- `17` GA4 credentials, `18` page performance, `19` affiliate context layer
- `20` one-page site builder — EMD micro-sites, Cloudflare Pages deploy.
  Read the compliance note first: it is for sites we genuinely operate, not
  link networks.
- `21` local SEO agent — GBP health, geogrids, citations. Official APIs only;
  it explicitly refuses Chrome automation of the GBP UI, which breaches ToS.
  Runs in US business hours because off-hours geogrids depress scores.
- `agent-resilience/` — three-tier fallback (silent default / skip+flag / ask a
  human) plus a mandatory run summary. Required in every autonomous script.
  Wired into `autopilot.py`; it caught a parser fault on its first run.
- `agent-ready-audit/` — Lighthouse Agentic Browsing: can an AI agent parse and
  act on the page. See the section below; it corrects three widely repeated
  myths, including that llms.txt is required.
- `seo-strategist-agent/` — the strategy layer above content and links. Its
  `methodology.md` is the important half.

### The Stewart Vickers set ("SEO agency in a box")

Written for an agency with clients. We have no clients, so read them for the
patterns rather than the workflows. Four earn their place immediately, the rest
are on the shelf.

- `approval-gate/` — see the note below; it upgrades what Skill 12 already says.
- `multi-llm-router/` — route each task to the cheapest model that can do it.
  Its `router.js` carries a routing table. The saving for us is not titles
  (already $0.0001 on haiku) but `content_expansion` at $0.1198 a job, where
  DeepSeek-reasoner is roughly a tenth of Sonnet for long-form. `qwen3:4b` is
  installed locally and free for classification and scoring.
- `listicle-agent/` — the answer to our AI Visibility 0. Query the AI engines
  for a target term, find which brands they already cite, then write the piece
  that includes that real consensus. Do NOT invent citations or force our brand
  above where it honestly sits; the method works because the consensus is real.
- `publisher-crm/`, `inventory-database/`, `link-builder-agent/` — the link
  stack. Relevant because automechanicschools needs citations, not words. Note
  the compliance line these carry and keep it: any compensated placement gets
  `rel="sponsored"` or `rel="nofollow"`. Earned editorial coverage is the only
  kind that moves rankings, and it is the only kind worth chasing.
- `cfo-agent/` — a formula-not-vibes spend rule (margin under 25% forces a cut
  before any human sees the number). `autopilot.py` has a hard $60 cap but no
  link between spend and return; this is the shape that fix should take.
- `gp-writer-agent/`, `client-reporting-agent/`, `client-wins-agent/`,
  `firefighter-agent/`, `lead-intel-suite/` — client-facing agency machinery.
  Shelved until there are clients.

**One pattern to refuse.** `client-reporting-agent` specifies "smart display
logic — hide what's bad, lead with what's good". That is defensible for a client
report and corrosive for our own. Every real finding this month came from
looking at what was bad: the control group that turned a +707% into seasonality,
the rolling-window bug that had impressions 28x too high, the guard reverting
healthy zones. Internal reporting shows the bad number first.

### agent-ready-audit

Chrome's Lighthouse "Agentic Browsing" category: can an AI agent actually parse
and act on the page. Directly relevant to the GEO work, since automechanicschools
shows AI Visibility 0 and 8 of 8 sampled queries return an AI Overview.

Three corrections it makes, all of which contradict the popular advice:

1. **It is a checklist, not a grade.** A fraction of checks passed, deliberately
   not a weighted score. Some renderers print a number anyway. Ignore it, and
   never invent one in a report.
2. **Only two checks carry weight**: `agent-accessibility-tree` and
   `cumulative-layout-shift`. WebMCP and llms.txt usually read "Not applicable"
   rather than failing, so a site with neither can still pass cleanly.
3. **llms.txt is not required to pass and is not a ranking factor.** Its check
   only grades the file's quality if the file already exists. Recommend it as a
   cheap addition, never as a fix for a failing audit.

Fix order matters more than coverage: accessible names first (an unnamed control
is invisible to an agent, so it cannot act at all), then layout stability (the
agent can see the page but elements move between locating and clicking), then
llms.txt, then WebMCP. Points 1 and 2 are the same work as fixing the site for
screen reader users, which is a much easier thing to justify.

**Our measured position, 2026-08-18.** Chrome IS on this droplet, bundled by
Playwright (Chrome for Testing 148), which is what `perf_audit.py` renders with.
Only npm is missing, and apt would pull 449 packages for it. So `agent_ready.py`
skips Lighthouse and reads the same tree Lighthouse reads, straight from Chrome
over CDP (`Accessibility.getFullAXTree`), and joins CLS from `perf_audits`
rather than re-measuring. Both weighted checks are covered with nothing
installed.

The static heuristic is kept behind `--static` and flagged as overcounting,
because it does: on lisclare.com it reported 335 interactive and 18 unnamed
where the real tree is 46 and 2. A collapsed mega-menu is `ignored` in the tree,
and Elementor tab controls get names at runtime. Treat any static figure as an
upper bound only.

Measured with the real tree: 0-2 unnamed controls per site, and two sites at
zero. Nearly all of it is unlabelled `<select>` dropdowns surfacing as unnamed
`combobox` nodes, plus the odd logo link. CLS is 0.000 to 0.003 across the
board. A theme-level fix of an hour, not a project. llms.txt is present and
passing on 9 of 10 (AIOSEO generates it); automechanicschools is the exception
at 404.

### approval-gate vs Skill 12

They agree. Skill 12 defines WHO signs off; approval-gate defines HOW the queue
works. `review_sheet.py` is already an implementation of it. Four things
approval-gate has that we do not:

1. **A timeout.** Items with no response in 24h escalate or auto-close. Our
   sheet has 52 rows awaiting a decision with no expiry, so "pending" and
   "abandoned" are indistinguishable.
2. **Batch approval.** One approval covers a class of similar actions rather
   than one row each. Fifty near-identical state pages should be one decision.
3. **A fallback approver**, so nothing sits forever when Adrian is away.
4. **Confidence thresholds instead of blocking** for high-volume routine work —
   auto-execute above 0.9, queue below 0.7. Worth considering for meta and title
   rewrites, never for published page content.

The publication gate in Skill 12 stands unchanged: nothing reaches a live site
without Adrian. These are refinements to the queue, not to the gate.

### What the strategist skill changes about how we pick work

Three rules worth applying beyond that skill, because our own data agrees:

1. **Never rank by Keyword Difficulty.** Use the lowest-DR site in the top 5 —
   the actual bar to clear. KD is a synthetic score.
2. **Filter for buyer intent, not volume.** This is the same lesson
   `opportunity_rank.py` already learned the expensive way: scmedu.org has
   220k impressions and earns 29 clicks a month.
3. **Anchor distribution is audited, never engineered.** Flag exact-match above
   30% as a risk to investigate. Do not buy placements to shape it — that is a
   link scheme, and compensated links get `rel="sponsored"` regardless.

The skill assumes Ahrefs. We do not have it; DataForSEO gives the same inputs
(SERP results, domain rank via the Backlinks API, CPC) at roughly $0.0006 a
query, so the methodology transfers even though the tool does not.

## Off limits

Never read, print, or modify anything under:

- `~/orchestrator/config/` (API keys and secrets; never committed, never
  printed, not even partially or in redacted form)
- `~/migrate/` (migration-era files including live credentials, such as the
  Cloudflare API token read by `sendgrid_dns.py`)

This holds regardless of how a task is framed. Partial or redacted output does
not count as compliance. If something appears to require access to either path,
stop and ask Adrian rather than working around it.

The IDE integration bypasses this rule without either party intending it:
selecting lines in an attached editor forwards their contents to the agent as a
system message, no paste needed. Highlighting a key in `config/api_keys.json` to
copy it elsewhere is enough, and it happened on 2026-08-13 with a live
Cloudflare token. Copy from those files in an editor that is not attached to
Claude Code, and treat any credential selected in an attached one as disclosed
and due for rotation.

Scripts may read these paths at runtime; agents may not. Running
`sendgrid_dns.py` is fine even though it reads the Cloudflare token, because the
credential never passes through the agent. If a task needs a secret, invoke the
script that reads it. Never read it and pass it along.

## Querying tables with credentials

Never `SELECT *` on `affiliate_sites` or `sites`. Both carry live credentials
(`wp_app_password`, `wp_password`, `google_password`, recovery emails, and
more). Always name the columns you need explicitly, so credentials are never
pulled into terminal output, logs, or an agent's context by accident. This is
the query-time counterpart to the secrets boundary above: the data is in the
database rather than `config/`, but it is the same class of secret.

## Where work happens

Work happens in `~/orchestrator` and `~/skills`. Both are git repositories.

- Commit AND PUSH in both at the end of every working session, with meaningful
  messages. The repos exist because Skill 09 once vanished without one; both
  now have private GitHub remotes (`elguiri01/orchestrator`, `elguiri01/skills`),
  added 2026-08-07 after it emerged that 43 and 16 commits existed nowhere but
  the droplet. A commit that never leaves the droplet does not survive losing
  the droplet. Verify with `git log --oneline -1 origin/master`, not `git log`.
- Patches are files, never pasted heredocs. Patch scripts are idempotent,
  anchor-checked, abort without writing on any mismatch, and back up the target
  first.
- Locate code by content, never by remembered line number.
- After any edit to `orchestrator.py`: syntax check, restart the `orchestrator`
  service, verify with a single test job before batch work.
- Changes to files in `~/skills` are proposed as diffs for Adrian to commit,
  per the sign-off matrix in Skill 12.
