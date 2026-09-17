# droplet-tmux

tmux wrapper for Claude Code sessions on the droplet, so an SSH drop stops
costing you a turn.

Without tmux, the interactive `claude` process is a child of the SSH session.
Lose the connection and the process dies mid-turn. `claude --continue` gets the
conversation back from its transcript, but the work that turn was doing is
gone. With tmux the session keeps running on the droplet and you reattach to it.

Two files:

- `claude.conf` - tmux settings tuned for the Claude Code UI
- `cc` - attach-or-create a session per project directory

## Install on the droplet

    mkdir -p ~/.config/tmux ~/bin
    cp ~/skills/droplet-tmux/claude.conf ~/.config/tmux/claude.conf
    cp ~/skills/droplet-tmux/cc ~/bin/cc
    chmod +x ~/bin/cc

If `~/bin` is not already on PATH, add to `~/.bashrc`:

    export PATH="$HOME/bin:$PATH"

Check terminfo before first use. If this prints nothing, edit `claude.conf`
and change `default-terminal` to `screen-256color`:

    infocmp tmux-256color >/dev/null 2>&1 && echo ok

## Use

    cc                      # session for the current directory
    cc ~/orchestrator       # session for the orchestrator project
    cc -r ~/orchestrator    # new session, opens the --resume picker
    cc -n ~/orchestrator    # new session, fresh conversation
    cc -l                   # list running Claude sessions

Sessions are named after the directory: `cc-orchestrator`, `cc-skills`. Running
`cc` against a directory that already has a session attaches to it as it
stands, so it is safe to run repeatedly, and `-r` and `-n` only affect how a
new session starts.

Detach with `Ctrl-b d`. The session, and anything Claude is in the middle of,
keeps running. Reattach with the same `cc` command from a new SSH login.

A directory with no prior conversation starts fresh, because `--continue`
errors out with nothing to continue. The check reads
`~/.claude/projects/<slugified-cwd>/` for transcripts.

## Isolation

`cc` runs on its own tmux server (`tmux -L claude`), so it cannot disturb any
other tmux session or config on the droplet, and `claude.conf` is never
sourced into them. The cost is that a plain `tmux ls` will not show these
sessions. Use `cc -l`, or:

    tmux -L claude ls
    tmux -L claude attach -t cc-orchestrator

## What this does not fix

- A droplet reboot kills tmux sessions like anything else. Durability across a
  reboot comes from the transcripts on disk, which is what `claude --continue`
  and `claude --resume` read.
- Long-running batch work belongs in the orchestrator service, not in a tmux
  session. tmux keeps an interactive session alive; systemd keeps the system
  running. Do not use this to hold a batch job open.
- A detached session that hits a permission prompt sits there waiting. Check
  `cc -l` and reattach if a job has gone quiet.

## Environment overrides

`CC_TMUX_CONF`, `CC_TMUX_SOCKET` and `CC_CLAUDE_BIN` override the config path,
the server socket and the `claude` binary. `CC_CLAUDE_BIN` exists so the
wrapper can be exercised without launching a real session.

## Status

Written 2026-09-17, in a Claude Code web session that has no access to the
droplet. Config parse, session creation, per-directory cwd, the
continue/fresh branch, idempotent reattach and the error paths were all
exercised against tmux 3.4 in the session container. Nothing here has run on
the droplet yet, so treat the first `cc` there as the real test.
