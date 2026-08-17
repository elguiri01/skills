// link-builder-agent — Layer 1 (Node)
// Reads inventory + client roster, scores candidates, writes pending.jsonl

require('dotenv').config({ path: __dirname + '/.env' });
const fs = require('fs');
const path = require('path');

// === REPLACE THESE WITH YOUR OWN PATHS ===
const INVENTORY_PATH = process.env.INVENTORY_PATH || path.join(__dirname, 'inventory.json');
const CLIENT_ROSTER_PATH = process.env.CLIENT_ROSTER_PATH || path.join(__dirname, 'clients');
const VOICE_EXAMPLES_PATH = path.join(__dirname, 'voice-examples.md');
// ==========================================

const PENDING_FILE = path.join(__dirname, 'data', 'pending.jsonl');
const DONE_FILE = path.join(__dirname, 'data', 'done.jsonl');

function loadInventory() {
  if (!fs.existsSync(INVENTORY_PATH)) {
    console.error(`Inventory not found at ${INVENTORY_PATH}. Provide one — see SKILL.md.`);
    process.exit(1);
  }
  return JSON.parse(fs.readFileSync(INVENTORY_PATH, 'utf8'));
}

function loadClients() {
  if (!fs.existsSync(CLIENT_ROSTER_PATH)) {
    console.error(`Client roster dir not found at ${CLIENT_ROSTER_PATH}. Provide one.`);
    process.exit(1);
  }
  const files = fs.readdirSync(CLIENT_ROSTER_PATH).filter(f => f.endsWith('.json'));
  return files.map(f => JSON.parse(fs.readFileSync(path.join(CLIENT_ROSTER_PATH, f), 'utf8')));
}

function getProcessedDomains(clientCode) {
  if (!fs.existsSync(DONE_FILE)) return new Set();
  const lines = fs.readFileSync(DONE_FILE, 'utf8').split('\n').filter(Boolean);
  return new Set(
    lines.map(l => { try { return JSON.parse(l); } catch { return null; } })
      .filter(Boolean)
      .filter(d => d.clientCode === clientCode)
      .map(d => d.domain)
  );
}

function scoreCandidate(site, brief) {
  let score = 0;
  if (site.dr >= brief.minDr) score += 0.3;
  if (site.monthlyTraffic >= brief.minTraffic) score += 0.3;
  if (brief.allowedNiches?.includes(site.niche)) score += 0.2;
  if (brief.geo && site.geo === brief.geo) score += 0.1;
  if (site.lifetimeOutcome === 'positive') score += 0.1;
  return score;
}

(async () => {
  const inventory = loadInventory();
  const clients = loadClients();

  fs.mkdirSync(path.dirname(PENDING_FILE), { recursive: true });
  let queued = 0;

  for (const client of clients) {
    if (!client.active) continue;
    const seen = getProcessedDomains(client.code);

    for (const brief of client.briefs) {
      const candidates = inventory
        .filter(s => !seen.has(s.domain))
        .filter(s => s.contactEmail)
        .map(s => ({ ...s, _score: scoreCandidate(s, brief) }))
        .filter(s => s._score >= 0.6)
        .sort((a, b) => b._score - a._score)
        .slice(0, brief.cap || 5);

      for (const site of candidates) {
        const decision = {
          id: `${client.code}-${site.domain}-${Date.now()}`,
          clientCode: client.code,
          clientName: client.name,
          domain: site.domain,
          contactEmail: site.contactEmail,
          targetUrl: brief.targetUrl,
          anchor: brief.anchor,
          niche: site.niche,
          dr: site.dr,
          score: site._score,
          createdAt: new Date().toISOString()
        };
        fs.appendFileSync(PENDING_FILE, JSON.stringify(decision) + '\n');
        queued++;
      }
    }
  }

  console.log(`Layer 1 done. Queued ${queued} candidates. Orchestrator will pick up next.`);
})();
