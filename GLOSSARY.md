# Glossary

Every term introduced across the tutorial, in the order you meet it. Each lesson
defines its own new words the first time you need them — this file just collects
them all in one place so you can look one back up later without hunting through
old lessons.

## A0 — Orientation
- **Sidebar**: the narrow strip of icons down the far-left edge of VS Code, each
  one opening a different panel.
- **Explorer**: the sidebar panel showing every open file/folder as an
  expandable tree — how you find and open files. Icon: two overlapping pages.
- **Editor (pane)**: the large central area where a file's contents show up
  once you click it in the Explorer — where you actually type code.
- **Panel**: one distinct section of the VS Code window — the Explorer, the
  terminal, and the Claude Code chat are all panels.
- **Terminal**: a panel where you type text commands instead of clicking
  buttons, and the computer types text back.
- **Command**: one instruction you type into the terminal and press Enter to run.
- **Command line**: another name for the terminal.
- **PowerShell**: the specific kind of terminal Windows uses.
- **Working directory**: the one folder the terminal is "standing in" right now.
- **Copy / paste**: copying grabs text without removing it from where it was;
  pasting drops that copy somewhere else (`Ctrl+C` to copy, click into the
  destination, `Ctrl+V` to paste).

## A1 — Installing your tools
- **Software package**: a chunk of software someone else built that you install
  onto your own computer to use.
- **Dependency**: something your project needs in order to run, that isn't part
  of the project itself.
- **Package manager**: a program whose job is installing and updating other
  software for you (Windows's built-in one is `winget`).
- **Flag**: extra text added after a command to change how it behaves, usually
  starting with a dash (e.g. `-e`).

## A2 — Files and running code
- **File**: a named chunk of saved content sitting on your computer's storage.
- **Extension**: the letters after the dot at the end of a filename (`.py`),
  telling programs what kind of content is inside.
- **Script**: a file full of code that runs top-to-bottom when you run it.
- **Run** (a script): telling Python to read your file and carry out its
  instructions.
- **Function**: a named, reusable block of instructions.

## A3 — Programming basics
- **Variable**: a name you give a piece of information so you can use it again
  later.
- **String**: text data, wrapped in quotes.
- **Parameter**: a name inside a function's parentheses standing in for whatever
  value gets passed in when it's called.
- **Return value**: the result a function hands back via a `return` statement.
- **Dictionary**: a collection of `key: value` pairs, written in curly braces.
- **JSON**: a plain-text way of writing dictionaries (and lists, and simple
  values) that almost every programming language and API can read and write.
- **Loop**: an instruction that repeats a block of code once per item in a
  collection.
- **Conditional**: an `if` statement — code that only runs when something's true.

## A4 — Packages and virtual environments
- **Package** (a.k.a. **library**): code someone else wrote and published, that
  you install and use inside your own code.
- **pip**: Python's own package manager.
- **Virtual environment (venv)**: an isolated, self-contained folder of Python
  packages, separate from the rest of your computer.
- **Activate** (a venv): telling your terminal to use the Python and packages
  inside a specific venv for the rest of the session.

## A5 — Git basics
- **Version control**: saving a history of changes to your files over time, with
  notes on what changed and why.
- **Repository (repo)**: a folder that git is keeping history for.
- **Commit**: one saved snapshot in that history, with a short message
  describing what changed.
- **Staging**: a holding area where you pick which changes go into your next
  commit, before you actually make it.
- **Status**: a summary of what's changed since your last commit and what's
  currently staged.

## A6 — APIs and secrets
- **API**: a defined way for one piece of software to ask another to do
  something — your code "calling the Claude API" sends a request over the
  internet and gets a response back.
- **API key**: a secret string proving who's making a request, functioning like
  a password.
- **Environment variable**: a named piece of information stored by your terminal
  session itself, not inside any file.
- **Secret**: any piece of information — a password, key, or token — that must
  stay private.

## B1 — First API call
- **Client**: an object in your code representing a connection to a specific
  service.
- **Request / response**: what your client sends to an API, and what it gets
  back.
- **Model**: the specific AI model handling a request, specified by name.
- **Token**: roughly, a chunk of a word — Claude reads and writes in tokens.
- **Attribute**: a named piece of data attached to an object, accessed with a
  dot (`response.content`).

## B2 — Conversation loop
- **State**: information a program remembers and carries forward between one
  action and the next.
- **Mutate**: to change something in place, rather than creating a new copy.
- **In-place**: describes a function that changes something it was given
  directly, instead of only returning a new value.

## B3 — Define a tool
- **Tool**: a function in your own code that you describe to Claude, so Claude
  can ask for it to be run.
- **Tool definition / schema**: the dictionary describing a tool to Claude — its
  name, description, and expected input shape.
- **JSON Schema**: a standard way of describing "what shape of data is allowed
  here."

## B4 — Tool-use round trip
- **Agent loop**: the cycle of sending a request, checking whether the model
  wants a tool run, running it, sending the result back, and repeating until a
  final answer.
- **`stop_reason`**: a field on Claude's response explaining why it stopped —
  `"end_turn"` (finished) or `"tool_use"` (asking you to run a tool first).
- **Content block**: one item inside `response.content` — a `"text"` block or a
  `"tool_use"` block.
- **`tool_use_id`**: a unique ID Claude attaches to each tool request, so you can
  tag the matching result.
- **Round trip**: the full "ask → tool runs → tell it the result" cycle — two
  calls to `messages.create`, connected by the tool result in between.
