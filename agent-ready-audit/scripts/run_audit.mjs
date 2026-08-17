#!/usr/bin/env node
/**
 * Run Lighthouse's agentic-browsing category and print it as a pass/fail list.
 *
 * The raw Lighthouse JSON buries the useful part - which elements failed and why - and
 * its 0-100 number is misleading for this category: Google describes it as a fraction of
 * checks passed, not a weighted score. This prints only what you act on.
 *
 * Node only, no install step. Lighthouse itself is fetched by npx on first run.
 *
 *   node run_audit.mjs https://example.com
 *   node run_audit.mjs https://example.com --mobile --json-out report.json
 */

import { spawnSync } from 'node:child_process';
import { mkdtempSync, existsSync, readFileSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';

const CATEGORY = 'agentic-browsing';

// The audits that carry weight today. The WebMCP and llms.txt audits report "not
// applicable" on sites that have not adopted them, which is not a failure.
const SCORED = new Set(['agent-accessibility-tree', 'cumulative-layout-shift']);

function parseArgs(argv) {
  const opts = { mobile: false, jsonOut: null, noSandbox: false, url: null, passthrough: [] };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--mobile') opts.mobile = true;
    else if (a === '--json-out') opts.jsonOut = argv[++i];
    else if (a === '--no-sandbox') opts.noSandbox = true;
    else if (a.startsWith('--')) opts.passthrough.push(a);
    else if (!opts.url) opts.url = a;
    else opts.passthrough.push(a);
  }
  return opts;
}

/**
 * Assemble Chrome flags, defaulting to --no-sandbox where it would otherwise fail.
 *
 * Chrome's sandbox cannot initialise as uid 0, which is the normal state on a fresh
 * droplet or inside a container, and the resulting crash message is opaque. Turning the
 * sandbox off is acceptable for auditing pages you already trust; keep it on elsewhere.
 */
function chromeFlags(noSandbox) {
  const flags = ['--headless=new'];
  const asRoot = typeof process.getuid === 'function' && process.getuid() === 0;
  if (noSandbox || asRoot) {
    if (asRoot && !noSandbox) {
      process.stderr.write('Running as root - adding --no-sandbox so Chrome can start.\n');
    }
    flags.push('--no-sandbox', '--disable-dev-shm-usage');
  }
  return `--chrome-flags=${flags.join(' ')}`;
}

function runLighthouse(url, mobile, noSandbox, passthrough) {
  const out = join(mkdtempSync(join(tmpdir(), 'lh-agentic-')), 'report.json');
  const args = [
    '--yes', 'lighthouse@latest', url,
    `--only-categories=${CATEGORY}`,
    '--output=json', `--output-path=${out}`,
    '--quiet', chromeFlags(noSandbox),
    ...(mobile ? [] : ['--preset=desktop']),
    ...passthrough,
  ];

  process.stderr.write(`Running Lighthouse against ${url} (${mobile ? 'mobile' : 'desktop'})...\n`);
  // Node refuses to spawn npx.cmd without a shell (EINVAL on Windows), and shell:true
  // would put a user-supplied URL through cmd.exe quoting. Running npm's own npx-cli.js
  // under this Node binary sidesteps both, with a plain `npx` fallback for odd installs.
  const npxCli = join(dirname(process.execPath), 'node_modules', 'npm', 'bin', 'npx-cli.js');
  const res = existsSync(npxCli)
    ? spawnSync(process.execPath, [npxCli, ...args], { encoding: 'utf8' })
    : spawnSync('npx', args, { encoding: 'utf8' });

  if (!existsSync(out)) {
    console.error(
      'Lighthouse did not produce a report.\n' +
      `exit code: ${res.status}${res.error ? ` (${res.error.code})` : ''}\n` +
      `${(res.stderr || '').trim().slice(-2000)}\n\n` +
      'Common causes: Chrome is not installed (set CHROME_PATH to its binary, or\n' +
      'apt install google-chrome-stable / chromium); the category needs Chrome 150+ (on\n' +
      '130-149 it is behind the experimental flag and the CLI may not expose it); Chrome\n' +
      'cannot start as root (try --no-sandbox); or the URL is not reachable from this\n' +
      'machine. Falling back to DevTools > Lighthouse also works.'
    );
    process.exit(1);
  }
  return JSON.parse(readFileSync(out, 'utf8'));
}

/** Map a Lighthouse audit to PASS / FAIL / N/A. */
function classify(audit) {
  const mode = audit.scoreDisplayMode;
  if (mode === 'notApplicable' || mode === 'manual') return 'N/A';
  if (mode === 'error') return 'ERROR';
  if (mode === 'informative') return 'INFO';
  if (audit.score === null || audit.score === undefined) return 'N/A';
  return audit.score >= 0.9 ? 'PASS' : 'FAIL';
}

const clean = (s, max = 200) =>
  String(s)
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1') // markdown links -> their text
    .replace(/\s+/g, ' ')
    .trim()
    .slice(0, max);

/**
 * Collect the individual findings out of an audit's details.
 *
 * The shapes vary by audit: agent-accessibility-tree nests a table inside a list of
 * list-sections, with one row per violated rule plus the failing node; llms-txt returns
 * a flat table of `message` strings and no nodes at all. Walking the tree rather than
 * indexing a fixed path keeps this working as Lighthouse reshuffles its output.
 */
function findings(details, out = [], limit = 25) {
  if (!details || out.length >= limit) return out;

  for (const item of details.items ?? []) {
    if (out.length >= limit) break;

    if (item?.type === 'list-section' || item?.value?.items) {
      findings(item.value, out, limit); // recurse into the nested table
      continue;
    }

    const rule = item?.description || item?.message || item?.source || '';
    const node = item?.node ?? {};
    const where = node.selector || node.snippet || item?.url || '';
    if (rule || where) out.push({ rule: clean(rule), where: clean(where, 120) });

    for (const sub of item?.subItems?.items ?? []) {
      const subWhere = sub?.node?.selector || sub?.node?.snippet;
      if (subWhere) out.push({ rule: clean(sub.description ?? ''), where: clean(subWhere, 120) });
    }
  }
  return out;
}

function main() {
  const opts = parseArgs(process.argv.slice(2));
  if (!opts.url) {
    console.error('Usage: node run_audit.mjs <url> [--mobile] [--json-out report.json]');
    process.exit(2);
  }

  const report = runLighthouse(opts.url, opts.mobile, opts.noSandbox, opts.passthrough);
  if (opts.jsonOut) writeFileSync(opts.jsonOut, JSON.stringify(report, null, 2));

  const category = report.categories?.[CATEGORY];
  if (!category) {
    console.error(
      'This Lighthouse build has no agentic-browsing category.\n' +
      'It needs Chrome 150+ and a recent Lighthouse. Check with:\n' +
      '  npx lighthouse@latest --list-all-audits'
    );
    process.exit(1);
  }

  console.log(`\nAgentic browsing - ${report.finalDisplayedUrl ?? opts.url}`);
  console.log(`${report.environment?.hostUserAgent ?? 'unknown user agent'}\n`);

  const rows = [];
  const failures = [];
  for (const ref of category.auditRefs ?? []) {
    const audit = report.audits?.[ref.id];
    if (!audit) continue;
    const status = classify(audit);
    rows.push({ status, id: ref.id, title: audit.title ?? '', scored: SCORED.has(ref.id) });
    if (status === 'FAIL' || status === 'ERROR') failures.push({ id: ref.id, audit });
  }

  const width = Math.max(...rows.map((r) => r.id.length), 20);
  for (const r of rows) {
    console.log(
      `  [${r.status.padEnd(5)}] ${r.id.padEnd(width)}  ${r.title}` +
      `  (${r.scored ? 'scored' : 'informational'})`
    );
  }

  const scored = rows.filter((r) => r.scored);
  const passed = scored.filter((r) => r.status === 'PASS').length;
  console.log(
    `\n  ${passed}/${scored.length} scored checks passing. ` +
    `'N/A' means the feature is absent, not that the site failed.\n`
  );

  for (const { id, audit } of failures) {
    console.log(`--- ${id}: ${audit.title}`);
    if (id === 'cumulative-layout-shift') {
      console.log(`    CLS ${audit.displayValue ?? 'n/a'} (good is <= 0.1)`);
    }
    const items = findings(audit.details);
    for (const { rule, where } of items) {
      console.log(`    - ${rule || '(no description)'}`);
      if (where) console.log(`        ${where}`);
    }
    if (!items.length) {
      const desc = clean(audit.description ?? '', 300);
      if (desc) console.log(`    ${desc}`);
    }
    console.log();
  }

  if (failures.length) {
    console.log(
      'Fix in this order: accessible names on interactive elements first (an agent\n' +
      'cannot act on a control it cannot identify), then layout shift (a moving page\n' +
      'makes it act on the wrong one).'
    );
  }
}

main();
