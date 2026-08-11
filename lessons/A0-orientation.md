# A0 — Orientation: what you're actually looking at

## What you're about to do
Before writing anything, get oriented on the editor window itself — where files
live, where you'll type code, and where you'll type commands. Every later lesson
assumes you already know your way around these few landmarks, so we nail them
down now, once, in detail.

## New words
- **Sidebar**: the narrow strip of icons running down the far-left edge of the VS
  Code window. Each icon opens a different panel in the space next to it — which
  one you click changes what shows up there.
- **Explorer**: the sidebar panel that shows every file and folder currently open
  in VS Code, arranged as an expandable tree. This is how you'll find and open
  files for the rest of the tutorial. Its icon looks like two overlapping
  pages/documents.
- **Editor** (pane): the large area taking up most of the window — once you click
  a file in the Explorer, its contents show up here, and this is where you'll
  actually type code.
- **Panel**: a general word for one distinct section of the VS Code window. The
  Explorer, the terminal, and the Claude Code chat are all panels — just in
  different spots around the same window.
- **Terminal**: a panel where you type text commands instead of clicking buttons,
  and the computer types text back. Think of it like texting the computer
  directly instead of pointing and clicking — same computer, different way of
  talking to it.
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
- **Copy / paste**: copying grabs text without removing it from where it was;
  pasting drops that copy somewhere else. In the terminal: select text with your
  mouse, then press `Ctrl+C`. To paste it somewhere else (like the chat box):
  click into that box first, then press `Ctrl+V`. You'll do this constantly —
  any time I ask you to show me what the terminal printed, this is how.

## Walkthrough

### Part 1 — finding your way around the window

1. Look at the far-left edge of the VS Code window — a thin vertical column of
   icons, separate from everything else. That's the **sidebar**.
2. Find the icon that looks like two overlapping pages (or press `Ctrl+Shift+E`).
   Click it. This opens the **Explorer** — a panel listing the files and folders
   in this project as a tree.
3. In that tree, find the folder named `workspace`. Click the small arrow (▸)
   just to its left to expand it — or click the folder name itself. You should
   now see files listed underneath it.
4. Click on `README.md` in that list. It opens in the big central area — the
   **editor**. That's the whole loop you'll repeat constantly from here on:
   click a file in the Explorer on the left, it opens in the editor in the
   middle.

### Part 2 — the terminal

5. Find the terminal panel (your proctor will point it out if you're not sure
   which one it is — it's usually docked below the editor, a dark strip with a
   blinking cursor).
6. Click into it, then run this command — type it exactly, then press Enter:

   ```powershell
   pwd
   ```

   `pwd` stands for **p**rint **w**orking **d**irectory. It just asks the
   terminal "where are you standing right now?" and prints the answer — a file
   path, which is just the address of a folder on your computer, written as a
   chain of folder names separated by backslashes.

7. Now run:

   ```powershell
   dir
   ```

   `dir` (short for **dir**ectory) lists everything sitting in the current
   folder — files and sub-folders. This is the terminal's version of the
   Explorer tree you just used in Part 1.

8. Copy everything the terminal showed after running both commands, and paste it
   into the **chat with me** — not back into the terminal. (Copying: after
   running a command, select the text in the terminal with your mouse, then
   `Ctrl+C` to copy it. Pasting into the chat box: click into it and `Ctrl+V`.)
   I'll confirm you're standing in the right folder before we go further.

## Verification
No automated check on this step — copy and paste the terminal output from both
commands into the chat with me, and I'll read it to confirm you're oriented
correctly.

## Why this matters
Every later lesson says things like "open `agent.py`" or "create a new file" and
assumes you already know that means: Explorer on the left, editor in the middle.
Same with the terminal — every command from here on happens in that same panel.
There's nothing new to learn later about *where* things are — just more to do
once you're there.
