# Proctor notes

Not shown to learners — this is for you.

## Setup, per learner

1. **Copy this whole `agent-coding-tutor` folder** for each learner (or have them
   clone/copy it themselves) — each learner needs their own copy, since
   `progress.json` and `workspace/`'s git history are per-learner state, and
   Lesson A5 has each learner run `git init` inside their own `workspace/`.
2. You handle: installing VSCode, installing the Claude Code extension, and
   opening this folder in it, for each learner. The tutorial itself starts from
   "the editor is already open" (Lesson A0).
3. When they reach **Lesson A6**, give them an Anthropic API key (a string
   starting `sk-ant-`). They set it as an environment variable themselves — it
   never gets typed into a file or committed to git. One key per learner (or per
   small group) makes it easy to track usage and revoke individually afterward.

## Cost

The tutorial defaults every learner's agent to **Claude Haiku 4.5**
(`claude-haiku-4-5-20251001`) — the fastest, cheapest model — since they'll run
their agent live many times over one session. The automated checks Claude runs
after each step (`pytest`) never call the real API at all, so the only real spend
is the learner's own experimentation in Lessons B1–B4, plus A0/orientation-style
manual runs. This should be very low per learner (a handful of short requests).

## Resetting a learner's progress

If someone wants to restart, or you're reusing a machine for a new learner:

```powershell
Remove-Item progress.json -ErrorAction SilentlyContinue
Remove-Item workspace -Recurse -Force
git checkout -- workspace   # if this repo itself is under git and workspace was tracked
```

Simplest in practice: just hand out a fresh copy of the folder rather than
resetting one in place.

## If you want to edit the tutorial itself

- `lessons/` — the actual lesson content the learner and Claude read from.
- `tests/` — the automated checks. `tests/fakes.py` is the fake Anthropic client
  that makes checking free and offline; `tests/conftest.py` makes the learner's
  `workspace/` files importable.
- `solutions/` — reference solutions, one per step, shown to a learner only as a
  last resort (see `.claude/skills/agent-tutorial/SKILL.md`, ground rule 2).
- `.claude/skills/agent-tutorial/SKILL.md` — the instructions that drive Claude's
  behavior when a learner runs `/agent-tutorial`. Edit this to change tone, pacing,
  or how many failed attempts trigger an offered solution.

After editing a lesson or its test, verify it the same way this tutorial was
built: temporarily copy the matching `solutions/*.py` file over the `workspace/`
stub, run `python -m pytest tests/ -q` and confirm it passes, then restore the
stub. Don't ship a lesson whose check you haven't actually watched pass and fail.

## Known scope boundary

This tutorial assumes Windows + PowerShell + winget, and assumes you (the
proctor) handle installing VSCode and the Claude Code extension before a learner
starts. It does not cover GitHub remotes, pull requests, or CI — only local git
(`init`/`add`/`commit`). If you need those covered too, that's a separate
follow-on module, not a change to this one.
