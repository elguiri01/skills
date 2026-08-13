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
