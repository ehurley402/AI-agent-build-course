# A1 — Installing your tools

## What you're about to do
Install the two pieces of software everything else in this tutorial depends on:
**Python** (the language you'll write your agent in) and **git** (the tool that
saves snapshots of your work as you go). Then prove to the terminal — and to me —
that they're really there.

## New words
- **Software package**: a chunk of software someone else built that you install
  onto your own computer to use. Python and git are both packages.
- **Dependency**: something your project needs in order to run, that isn't part of
  the project itself. Python and git are dependencies of *everything* you'll do in
  this tutorial — nothing else works until they're installed. You'll meet a second,
  smaller kind of dependency later (a **package**, singular library, installed with
  `pip`) — same idea, smaller scale.
- **Package manager**: a program whose whole job is installing and updating other
  software for you, so you don't have to hunt down a website and click through an
  installer by hand. Windows 11 comes with one built in, called **winget**
  (short for **Win**dows Package Manager **Get**).
- **Flag**: extra text you add after a command to change how it behaves — usually
  starting with a dash, like `-e` below. Think of it as a switch you flip on for
  that one run of the command.

## Walkthrough

1. Check whether Python is already installed:

   ```powershell
   python --version
   ```

   If you see something like `Python 3.12.10`, it's already there — skip to step 3.
   If you see an error, or it opens the Microsoft Store, continue to step 2.

2. Install Python using winget:

   ```powershell
   winget install --id Python.Python.3.12 -e
   ```

   The `-e` flag means **exact** — install precisely the package with that ID, not
   something winget merely thinks is close. Close and reopen your terminal panel
   after this finishes (Windows needs a fresh terminal to notice the new software),
   then re-run `python --version` to confirm it worked.

3. Check whether git is already installed:

   ```powershell
   git --version
   ```

   If you see a version number, skip to the verification step. Otherwise:

   ```powershell
   winget install --id Git.Git -e
   ```

   Again, close and reopen your terminal panel afterward, then re-run
   `git --version`.

## Verification
Run both of these and paste me the output:

```powershell
python --version
git --version
```

I'm looking for a version number on each line — something like `Python 3.12.10`
and `git version 2.54.0.windows.1`. Any error means the install didn't finish; tell
me the exact error text and I'll help you read it.

## Why this matters
Everything from here on assumes these two commands just work. If either one is
shaky, every later step gets confusing for the wrong reason — so we nail this down
first, once, and never think about it again.
