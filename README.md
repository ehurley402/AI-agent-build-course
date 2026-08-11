# Build Your First Agent

Welcome — you're going to build a real, working AI agent from scratch, using
Claude. No prior coding experience needed; every term gets explained the first
time it comes up (see [GLOSSARY.md](GLOSSARY.md) any time you want to look one
back up).

## How this works

You already have this folder open in an editor with Claude Code running. To
start (or continue) the tutorial, just type this into the chat:

```
/agent-tutorial
```

Claude will tell you exactly what to do at each step, wait for you to actually do
it, check your work for real, and only move on once it's genuinely working. If
you close everything and come back later, running `/agent-tutorial` again picks
up right where you left off.

## What you'll build

By the end, you'll have a Python program that:
- sends a message to Claude and gets a reply
- holds a real back-and-forth conversation, remembering what was said
- can call a tool — real code you wrote — when it needs to, and use the result
  to give a better answer

That last part is what makes it an **agent** rather than just a chat window: it
can act, not just talk.

## The two parts

- **Foundations (A0–A6)**: the terminal, installing software, writing your first
  file, core programming ideas, git, and handling your API key safely. Skip
  ahead only if you're already confident with all of it.
- **Build the agent (B1–B4)**: the actual agent, built up one working piece at a
  time.

## If you get stuck

Just tell Claude what's happening — what you tried, and what you saw. It won't
hand you the answer outright, but it will help you find it. If you're genuinely
stuck, you can ask it to show you the reference solution for the current step.
