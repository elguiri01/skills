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
- `seo-strategist-agent/` — the strategy layer above content and links. Its
  `methodology.md` is the important half.

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
