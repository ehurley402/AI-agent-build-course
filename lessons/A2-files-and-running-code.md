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

2. Create a new file called `hello.py` inside `workspace`. You can do this in your
   editor's file explorer (right-click → New File) or from the terminal:

   ```powershell
   New-Item hello.py
   ```

3. Open `hello.py` and type this one line into it, exactly:

   ```python
   print("Hello, world!")
   ```

   Save the file.

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
complains, read me the exact error message — the wording tells us precisely what's
wrong (a typo, a missing quote, wrong indentation), and reading that message
carefully is a skill you'll use constantly from here on.

## Why this matters
"Write code into a file, run the file, read what happened" is the entire loop
you'll repeat for the rest of this tutorial — and for as long as you write
software. Everything after this just makes the code inside the file more
interesting.
