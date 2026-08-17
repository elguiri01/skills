-- publisher-crm schema (SQLite)
-- Run: sqlite3 publishers.db < schema.sql

CREATE TABLE IF NOT EXISTS publishers (
  domain TEXT PRIMARY KEY,
  contact_name TEXT,
  contact_email TEXT,
  niche TEXT,
  first_contacted_at TEXT,
  last_contacted_at TEXT,
  last_reply_at TEXT,
  lifetime_sent INTEGER DEFAULT 0,
  lifetime_replied INTEGER DEFAULT 0,
  lifetime_agreed INTEGER DEFAULT 0,
  lifetime_placed INTEGER DEFAULT 0,
  lifetime_paid INTEGER DEFAULT 0,
  notes TEXT,
  payment_method TEXT,
  preferred_topics TEXT,    -- comma-separated or JSON
  banned_topics TEXT,
  avg_turnaround_days INTEGER,
  health TEXT DEFAULT 'active',   -- active / dormant / blacklisted
  tags TEXT,                -- comma-separated or JSON
  created_at TEXT DEFAULT (datetime('now')),
  updated_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_publishers_niche ON publishers(niche);
CREATE INDEX IF NOT EXISTS idx_publishers_health ON publishers(health);
CREATE INDEX IF NOT EXISTS idx_publishers_last_contacted ON publishers(last_contacted_at);

CREATE TABLE IF NOT EXISTS publisher_threads (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  domain TEXT REFERENCES publishers(domain),
  thread_id TEXT,
  client_code TEXT,
  status TEXT,            -- sent / replied / agreed / placed / paid / closed
  agreed_terms TEXT,      -- JSON
  created_at TEXT DEFAULT (datetime('now')),
  updated_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_threads_domain ON publisher_threads(domain);
CREATE INDEX IF NOT EXISTS idx_threads_thread_id ON publisher_threads(thread_id);
CREATE INDEX IF NOT EXISTS idx_threads_client_code ON publisher_threads(client_code);
