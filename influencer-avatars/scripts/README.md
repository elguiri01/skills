# scripts/

Scripts that arrive with the uploaded skills, plus any we write. Anything
autonomous follows `agent-resilience/` (three-tier fallback and a run
summary) and writes API spend to the orchestrator spend log per Skill 12.

Nothing here posts to a platform. Higgsfield's `tiktok_publish` and any
YouTube upload are publish actions and stay behind Adrian's go.

Candidates once the skills are in:

- `persona_scaffold.py`: copy `personas/_template.md` and the posting log
  into `personas/<slug>/`, so a new persona starts with the right files.
- `render_cost.py`: read the credit cost of a render from Higgsfield
  `transactions` and append it to the posting log, so estimates are real.
