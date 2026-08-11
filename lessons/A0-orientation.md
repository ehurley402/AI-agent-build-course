# A0 — Orientation: what you're actually looking at

## What you're about to do
Before writing anything, get oriented on the tool you'll be typing into for the rest
of this tutorial: the **terminal**.

## New words
- **Terminal**: a window where you type text commands instead of clicking buttons,
  and the computer types text back. Think of it like texting the computer directly
  instead of pointing and clicking — same computer, different way of talking to it.
- **Command**: one instruction you type into the terminal and press Enter to run.
- **Command line**: another name for the terminal — the "line" where you type
  commands.
- **PowerShell**: the specific *kind* of terminal Windows uses. There are other
  kinds (other operating systems use different ones), but everything in this
  tutorial assumes PowerShell, since that's what Windows gives you.
- **Working directory**: the one folder the terminal is "standing in" right now.
  Every command that touches files acts on this folder unless you tell it
  otherwise — like being in a room and saying "the box" instead of giving a full
  address; it means the box *in this room*.

## Walkthrough

1. Find the terminal panel in your editor (your proctor will point it out if you're
   not sure which panel it is). It's usually a dark strip near the bottom with a
   blinking cursor.
2. Run this command — type it exactly, then press Enter:

   ```powershell
   pwd
   ```

   `pwd` stands for **p**rint **w**orking **d**irectory. It just asks the terminal
   "where are you standing right now?" and prints the answer — a file path, which
   is just the address of a folder on your computer, written as a chain of folder
   names separated by backslashes.

3. Now run:

   ```powershell
   dir
   ```

   `dir` (short for **dir**ectory) lists everything sitting in the current folder —
   files and sub-folders. This is the terminal equivalent of opening a folder in
   File Explorer and looking at what's inside.

4. Tell me (in the chat, not the terminal) what `pwd` printed and what `dir` showed.
   I'll confirm you're standing in the right folder before we go further.

## Verification
No automated check on this step — tell me what the two commands printed and I'll
read it and confirm you're oriented correctly.

## Why this matters
Every single step from here on happens by typing commands into this same window.
There's no new tool to learn later — just more commands, in the same place.
