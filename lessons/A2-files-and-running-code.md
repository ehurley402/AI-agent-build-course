# A2 — Files and running code

## What you're about to do
Create your very first file, put one line of Python in it, and get the computer to
run it. This is the smallest possible version of everything you'll do for the rest
of the tutorial — write text into a file, then tell Python to run that file.

## New words
- **File**: a named chunk of saved content sitting on your computer's storage —
  same idea as a paper document in a filing cabinet, just digital. A `.py` file is
  a file containing Python code.
- **Extension**: the letters after the dot at the end of a filename (`.py`,
  `.md`, `.txt`). It tells programs what *kind* of content is inside — `.py` means
  "this is Python code."
- **Script**: a file full of code that runs top-to-bottom when you tell Python to
  run it. Every `.py` file you write in this tutorial is a script.
- **Run** (a script): telling Python to read your file and actually carry out the
  instructions in it, line by line, top to bottom.
- **Function**: a named, reusable block of instructions. `print(...)` is a
  function that already exists inside Python — its job is "show this text on
  screen." You'll write your own functions starting in the next lesson.

## Walkthrough

1. Make sure your terminal is standing in the `workspace` folder inside this
   tutorial (use `cd workspace` if you're not sure — `cd` means **c**hange
   **d**irectory).

2. Create a new file called `hello.py`, using the Explorer from Lesson A0:
   - In the Explorer, right-click directly on the `workspace` folder itself
     (not the tutorial's top-level folder, and not an existing file).
   - Choose **New File** from the menu that pops up.
   - Type the name `hello.py` exactly, then press Enter.
   - VS Code creates the file and opens it immediately in the editor pane — you
     should see an empty tab titled `hello.py` with a blinking cursor in it.

   (If you'd rather use the terminal: make sure it's standing in `workspace`
   — `cd workspace` — then run `New-Item hello.py`, and double-click `hello.py`
   in the Explorer to open it.)

3. Click into that empty editor tab and type this one line into it, exactly:

   ```python
   print("Hello, world!")
   ```

   Save the file: `Ctrl+S`. You'll see a small dot on the file's tab disappear
   once it's saved — that dot means "unsaved changes," so its disappearing is
   your confirmation.

4. Run it:

   ```powershell
   python hello.py
   ```

## Verification
I'll run:

```powershell
python workspace/hello.py
```

and check that it prints exactly `Hello, world!` with no errors. If Python
complains, copy and paste the exact error message into the chat — the wording
tells us precisely what's wrong (a typo, a missing quote, wrong indentation), and
reading that message carefully is a skill you'll use constantly from here on.

## Why this matters
"Write code into a file, run the file, read what happened" is the entire loop
you'll repeat for the rest of this tutorial — and for as long as you write
software. Everything after this just makes the code inside the file more
interesting.
