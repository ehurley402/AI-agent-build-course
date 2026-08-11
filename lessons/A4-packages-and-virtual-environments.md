# A4 — Packages and virtual environments

## What you're about to do
Install the one real package your agent needs (`anthropic`, the official library
for talking to Claude) and the one that checks your work (`pytest`) — but first,
build them a clean, separate space to live in, so they don't collide with anything
else Python-related on your computer.

## New words
- **Package** (a.k.a. **library**): code someone else wrote and published, that
  you install and then use inside your own code, instead of writing it yourself.
  `anthropic` is a package — it already knows how to talk to Claude's API correctly
  so you don't have to build that from scratch.
- **pip**: Python's own package manager — same idea as `winget` from Lesson A1,
  but it installs *Python* packages specifically, not general Windows software.
  `pip` came installed with Python; you don't install it separately.
- **Virtual environment (venv)**: an isolated, self-contained folder of Python
  packages, separate from the rest of your computer. Think of it like a dedicated
  toolbox for this one project — the packages inside it don't affect any other
  project, and no other project's packages leak into this one.
- **Activate** (a venv): telling your terminal "for the rest of this session, use
  the Python and packages inside this specific toolbox, not the computer-wide
  ones." You do this once per terminal session.

## Walkthrough

1. From the tutorial's root folder (not inside `workspace`), create the virtual
   environment:

   ```powershell
   python -m venv venv
   ```

   This creates a new folder called `venv` containing its own private copy of
   Python. (You'll see it appear in your file explorer — you never need to open
   it.)

2. Activate it:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   You'll know it worked because your terminal prompt now starts with `(venv)`.

   **If you get an error** about running scripts being disabled, it's a Windows
   security setting, not a mistake you made. Run this once, then try activating
   again:

   ```powershell
   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
   ```

3. With the venv active, install the two packages:

   ```powershell
   pip install anthropic pytest
   ```

4. Every time you open a **new** terminal to work on this tutorial from now on,
   re-run step 2 (`.\venv\Scripts\Activate.ps1`) first. If you forget, commands
   like `pytest` may not be found, or may run a different, wrong copy of Python.

## Verification
With the venv active, I'll run:

```powershell
python -m pytest tests/test_a4_environment.py -q
```

This check simply tries to `import anthropic` and `import pytest` — if either
package isn't installed where Python can find it, the check fails immediately and
tells you which one's missing.

## Why this matters
"Isolate your project's dependencies" is a habit, not a one-time task — every real
Python project you ever touch will have its own venv. Getting it right once now
means it's never a mystery later.
