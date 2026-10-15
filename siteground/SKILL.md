---
name: siteground
description: Facts about SiteGround shared hosting that change what is possible and what is fast. The dynamic cache and the Vary header that fragments it, why nginx ignores .htaccess for files that exist, what mod_proxy cannot do, how staging differs from live, and the SG Optimizer options worth knowing. Measured on a live site, September and October 2026.
---

# SiteGround: what the platform actually does

Platform-specific companion to `web-performance`. Everything here was
measured on a live SiteGround shared-hosting account running WordPress,
September and October 2026.

**Client site or ours?** Everything here is reversible in one command, which matters more on a client's site than on ours. Prove a cache change on live, because staging cannot show it, and make sure the undo is one line before you run the do.

## The dynamic cache, and the setting that cripples it

SiteGround's dynamic cache works well: a hit serves in **0.30 s** where a
miss costs **1.80 s** on the same page. The difference is a full WordPress
render.

**Check `siteground_optimizer_user_agent_header` first.** When it is `1`,
SG Optimizer sends `Vary: User-Agent` and the cache is keyed on the browser
string. Every distinct User-Agent mints its own copy, so **the first visitor
with any given browser string pays the full render**. Android user-agents
carry the device model *and* the Chrome version, so in practice that is close
to per-device-per-release.

The decisive test is five requests with one never-seen-before agent:

| Request | Cache | TTFB |
| --- | --- | --- |
| 1st | MISS | 1.80 s |
| 2nd to 5th | HIT | 0.30 s |

It is one option, instantly reversible:

```
wp option update siteground_optimizer_user_agent_header 0
wp sg purge
```

**Before switching it off, prove the site serves the same HTML to both.**
Fetch each page type with a mobile and a desktop agent and compare bytes. On
this site five page types were identical except for **one byte**, a
per-second cache-buster on the logo. The header was buying nothing and
costing 1.5 seconds.

It exists for sites that genuinely serve different markup to mobile, such as
AMP or a separate mobile theme. A responsive site does not.

**This also explains a persistent PageSpeed result.** PSI arrives with a
fresh context every run, so with the header on it measures the cache-miss
path every single time. If a client's committed metric is a PSI number, this
setting has been deciding it.

The source is `sg-cachepress/core/Supercacher/Supercacher_Helper.php`.

## Query strings are not part of the cache key

`?anything=1` on a URL does not force a miss. A harness that appends a unique
parameter per run to defeat the browser cache is not defeating the page
cache, and may lead you to blame your tooling for a result that is real.
Verify rather than assume, in both directions.

## nginx serves files that exist, without consulting .htaccess

This is the fact that decides what you can and cannot do.

If a real file or directory exists at the requested path, nginx serves it
directly. `.htaccess` is never consulted. Two consequences:

- **A `.htaccess` redirect for a file that still exists on disk will not
  fire.** Redirect maps for PDFs and other static assets simply do nothing.
  The route is to move the superseded file out of the web root, not to write
  a rule.
- **Static files are the fastest thing the platform can do.** Measured:
  **0.30 s for a static file against 5.27 s to first byte for a WordPress
  page** on the same server. Publishing generated pages as
  `path/index.html` serves them without touching WordPress and needs no DNS
  change.

WordPress's own `.htaccess` already skips real files and directories, so
`/section/slug/index.html` is served directly with no extra rule.

**One thing to protect.** A real directory named for an existing WordPress
route shadows that route, because the web server tries to serve the
directory. Add a small block *above* the WordPress block sending exactly that
path back to `index.php`. Anchor-check it, write it once, and make it
removable.

## mod_proxy is not available

A `[P]` rewrite returns **500**. Shared-hosting customers cannot proxy. Any
plan that involves reverse-proxying part of the site from the same host is
dead on arrival; use static files or an edge worker instead.

## Staging is not live, and the differences matter

A SiteGround staging copy **does not run the dynamic cache**. Every request
misses. Measured on staging: 0 of 4 fresh agents hit, and repeats missed too,
with TTFB pinned around 1.6 s regardless of anything done to the site.

So:

- **A caching change cannot be proved on staging.** It has to be tested on
  live, which means it has to be reversible in one command.
- **Staging TTFB is a floor you cannot optimise past**, and it will make
  every staging measurement look worse than the same page on live. Do not
  compare the two hosts and call the difference a regression.

**Check any new staging copy for these**, which were all wrong on first
creation here: `siteurl` and `home` pointing at the wrong scheme or host,
thousands of rows still pointing at the production domain, so staging serves
media from live, and a rewrite-rule count that does not match live. Export
the database before fixing anything.

## SG Optimizer options worth knowing

| Option | Note |
| --- | --- |
| `siteground_optimizer_user_agent_header` | The cache fragmenter above. Usually wants to be 0 |
| `siteground_optimizer_enable_cache` | Dynamic cache on or off |
| `siteground_optimizer_file_caching` | File cache |
| `siteground_optimizer_remove_query_strings` | Applies to assets, not pages |
| `siteground_optimizer_async_javascript_exclude` | Serialised array of handles |

SG Optimizer also writes a `Header unset Vary` block into `.htaccess`. It
does not remove the header, because the header is added by PHP afterwards.
Do not read its presence as evidence that the header is gone. Check the
response.

Optimised asset copies are served from
`wp-content/uploads/siteground-optimizer-assets/`, so a script's URL will not
contain its plugin path. Any dequeue matching on `/plugins/<name>/` will miss
it once SG Optimizer has processed it.

## Purging

```
wp cache flush --path=<docroot>
wp sg purge --path=<docroot>
```

Purge empties everything, so the next request to each page is a miss. **Warm
the key pages afterwards** and do not take a measurement in the minute after
a purge: that is how a cold render gets reported as a regression.

## Operating notes

- Everything is `wp` over SSH with `--path=<docroot>`; live and staging are
  sibling directories under `~/www/`.
- `wp eval-file` takes positional arguments after the script path, which is
  how to give a patch script a `dry` or `restore` mode.
- A plugin that stores code in the database, such as Code Snippets, is a
  deployment mechanism that needs no file access and gives one-click
  rollback. **Its bodies must not contain a PHP opening tag.** A script that
  installs them should lint, refuse an opening tag, and back up the existing
  body before writing.
