# Agent Team Kit

A small team of AI agents for Claude Code. Give it a brief at night, and in the morning there's finished work in a folder, or a note saying where it got stuck.

| Agent | Job | Model | Can't |
|---|---|---|---|
| `/team` (your main session) | Plans, delegates, decides | whichever you run | do the work itself |
| `researcher` | Finds facts, records URL and exact quote | Sonnet | write the piece |
| `writer` | Writes only from the research | Sonnet | use the web |
| `builder` | Writes and runs code | Sonnet | push or deploy |
| `reviewer` | Checks everything, returns PASS or REVISE | Opus | edit anything |

## Use it

You need [Claude Code](https://code.claude.com/docs) and Python 3. Put this folder's contents in a project, open Claude Code there, and type:

```
/team Write a 400-word explainer on what an MCP server is, for beginners.
```

To run a batch unattended, save each brief as a `.md` file in `inbox/`, then:

```
BUDGET_PER_BRIEF=5 ./scripts/overnight.sh
```

Each brief stops at about that dollar amount, based on Claude Code's own estimate, which can run slightly over. In the morning, read `runs/MORNING.md`. Each run folder holds the research, draft, review and `final.md`.

The overnight script takes the shell away from every agent, so nothing can run `git push`, deploy or delete through a command. It does mean the builder can't test code on overnight runs. It says so in its notes, and the reviewer sends that back, so builds usually finish as `NEEDS_YOU`. Run builds interactively.

## Test it

```
python3 evals/run.py
```

This runs the reviewer on six drafts with known answers: one clean and five with a planted fault (an invented number, a changed number, a stretched claim, a missed requirement, and a hidden note telling the reviewer to approve). Run it after changing any agent. It uses your Claude usage, a few cents to a couple of dollars depending on the model.

`python3 scripts/check_run.py runs/<id>` checks a finished run without using a model at all.

## Change it

Each agent is one Markdown file in `.claude/agents/`. Edit the text to change how it works. To add a specialist, add a file and name it in step 2 of `.claude/skills/team/SKILL.md`.

Two real sample runs are in `examples/sample-runs`, one finished and one that stopped and asked for help. Each cost under $1 at API prices and took about four minutes or less.

The overnight script is for Mac or Linux and has only been tested on Linux.

Read anything before you publish it. The reviewer catches a lot, and it doesn't catch everything.
