# A5 — Git basics

## What you're about to do
Start tracking your own work with **git** — the tool that saves labeled snapshots
of your code over time, so you can always see what changed and, if needed, go back.
You'll turn `workspace` into its own git project and make your first commit.

## New words
- **Version control**: the general idea of saving a history of changes to your
  files over time, with notes on what changed and why — instead of only ever
  having "the current version" and no memory of how it got that way.
- **Repository** (or **repo**): a folder that git is keeping history for. Right
  now, `workspace` is just a folder. After this lesson, it's a repo.
- **Commit**: one saved snapshot in that history, with a short message describing
  what changed. Think of it like a save point in a video game — you can always see
  exactly what the project looked like at that point, and jump back to it later.
- **Staging** (the "staged" area): a holding area where you pick *which* changes
  you want included in your next commit, before you actually make the commit.
  `git add` moves a file into staging; `git commit` then takes a snapshot of
  everything sitting in staging.
- **Status**: a summary of what's changed since your last commit, and what's
  currently staged — your "where do things stand right now" check.

## Walkthrough

1. Move into `workspace` and turn it into a git repository:

   ```powershell
   cd workspace
   git init
   ```

2. Check what git sees:

   ```powershell
   git status
   ```

   You'll see `hello.py` and `exercises.py` listed as untracked — git has noticed
   they exist, but isn't saving history for them yet.

3. Stage both files:

   ```powershell
   git add hello.py exercises.py
   ```

   Run `git status` again — they now show as staged, ready to be committed.

4. Make your first commit:

   ```powershell
   git commit -m "Complete lessons A2 and A3"
   ```

   The `-m` flag lets you attach the commit's message directly on the command
   line, instead of opening a separate editor for it.

5. Confirm it's there:

   ```powershell
   git log --oneline
   ```

   You should see one line: a short code followed by your message.

## Verification
I'll run, from inside `workspace`:

```powershell
git log --oneline
```

I'm checking for at least one commit in the history. If it's empty, something in
steps 1–4 didn't complete — tell me what `git status` shows right now and we'll
trace back from there.

## Why this matters
Starting with lesson B1, every step ends with "now commit your progress." That's
not busywork — it means if a later step ever goes sideways, you (or I) can look at
exactly what changed between one working state and the next, instead of guessing.
