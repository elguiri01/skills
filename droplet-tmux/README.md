# droplet-tmux

tmux wrapper for Claude Code sessions on the droplet, so an SSH drop stops
costing you a turn.

Without tmux, the interactive `claude` process is a child of the SSH session.
Lose the connection and the process dies mid-turn. `claude --continue` gets the
conversation back from its transcript, but the work that turn was doing is
gone. With tmux the session keeps running on the droplet and you reattach to it.

Two files:

- `claude.conf` - tmux settings tuned for the Claude Code UI
- `ccs` - attach-or-create a session per project directory

## Install on the droplet

    mkdir -p ~/.config/tmux ~/bin
    cp ~/skills/droplet-tmux/claude.conf ~/.config/tmux/claude.conf
    cp ~/skills/droplet-tmux/ccs ~/bin/ccs
    chmod +x ~/bin/ccs

If `~/bin` is not already on PATH, add to `~/.bashrc`:

    export PATH="$HOME/bin:$PATH"

Ubuntu's stock `~/.profile` adds `~/bin` on its own, but only if the directory
already exists when you log in. Creating it during this install is too late
for the shell you are standing in, so export it once by hand as well:

    export PATH="$HOME/bin:$PATH"

That puts `~/bin` ahead of `/usr/bin`, so anything in it shadows a system
command of the same name. Confirm `ccs` resolves to your copy and has not
landed on top of something else:

    command -v ccs        # must print /home/adrian/bin/ccs

The tool is called `ccs` and not `cc` for exactly this reason: `cc` is the C
compiler, and putting `~/bin` first would have shadowed it.

Check terminfo before first use. If this prints nothing, edit `claude.conf`
and change `default-terminal` to `screen-256color`:

    infocmp tmux-256color >/dev/null 2>&1 && echo ok

## Use

    ccs                      # session for the current directory
    ccs ~/orchestrator       # session for the orchestrator project
    ccs -c ~/orchestrator    # new session, continue the last conversation
    ccs -r ~/orchestrator    # new session, opens the --resume picker
    ccs -l                   # list running Claude sessions

Sessions are named after the directory: `ccs-orchestrator`, `ccs-skills`.
Running `ccs` against a directory that already has a session attaches to it as
it stands, so it is safe to run repeatedly, and `-c` and `-r` only affect how
a new session starts.

Attaching is the case that matters. After a dropped connection the session is
still running, so you rejoin the live process mid-turn and no flag is
involved. `-c` and `-r` are for when the session itself is gone: a reboot, or
you exited it. `-r` opens the picker whether or not the directory has history,
so it is the safer of the two when you are not sure.

Detach with `Ctrl-b d`. The session, and anything Claude is in the middle of,
keeps running. Reattach with the same `ccs` command from a new SSH login.

A new session starts fresh unless you ask for `-c` or `-r`. `-c` passes
`--continue` straight through, so it can still come back with "No conversation
found to continue" when Claude has no history it will resume for that
directory.

## Isolation

`ccs` runs on its own tmux server (`tmux -L claude`), so it cannot disturb any
other tmux session or config on the droplet, and `claude.conf` is never
sourced into them. The cost is that a plain `tmux ls` will not show these
sessions. Use `ccs -l`, or:

    tmux -L claude ls
    tmux -L claude attach -t ccs-orchestrator

## What this does not fix

- A droplet reboot kills tmux sessions like anything else. Durability across a
  reboot comes from the transcripts on disk, which is what `claude --continue`
  and `claude --resume` read.
- Long-running batch work belongs in the orchestrator service, not in a tmux
  session. tmux keeps an interactive session alive; systemd keeps the system
  running. Do not use this to hold a batch job open.
- A detached session that hits a permission prompt sits there waiting. Check
  `ccs -l` and reattach if a job has gone quiet.

## Environment overrides

`CCS_TMUX_CONF`, `CCS_TMUX_SOCKET` and `CCS_CLAUDE_BIN` override the config
path, the server socket and the `claude` binary. `CCS_CLAUDE_BIN` exists so
the wrapper can be exercised without launching a real session:

    CCS_CLAUDE_BIN='echo FAKE' ccs /tmp && ccs -l
    tmux -L claude kill-session -t ccs-tmp

## Status

Written 2026-09-17, in a Claude Code web session that has no access to the
droplet. Config parse, session creation, per-directory cwd, the
continue/fresh branch, idempotent reattach and the error paths were all
exercised against tmux 3.4 in the session container. Nothing here has run on
the droplet yet, so treat the first `ccs` there as the real test.

Renamed from `cc` to `ccs` on 2026-09-19, after the first install attempt on
the droplet ran `/usr/bin/cc` and handed back linker errors.

Also on 2026-09-19: the wrapper used to sniff `~/.claude/projects/` for
transcripts and pick `--continue` or a fresh start on that basis. It read an
internal layout it has no business depending on, and the first real run chose
`--continue` into a directory Claude would not resume. That check is gone.
`-c` is explicit and the default is a fresh conversation.
