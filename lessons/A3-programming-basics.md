# A3 — Programming basics

## What you're about to do
Learn the small set of ideas that almost all code is built from — by writing four
tiny functions, one idea at a time, in `workspace/exercises.py`.

## New words
- **Variable**: a name you give a piece of information so you can use it again
  later — like writing a value on a sticky note and giving the note a label.
- **String**: text data — anything wrapped in quotes in Python, like `"hello"`.
- **Function**: a named, reusable block of instructions that can take input
  (**parameters**) and hand back a result (its **return value**). You met this
  word briefly in Lesson A2; here you'll write your own for the first time.
- **Parameter**: a name inside a function's parentheses that stands in for
  whatever value gets passed in when the function is called — in
  `def greet(name):`, `name` is a parameter.
- **Return value**: the result a function hands back to whatever called it, via
  a `return` statement. A function that never uses `return` hands back nothing
  useful.
- **Dictionary**: a collection of `key: value` pairs, written in curly braces —
  `{"name": "Ada", "age": 30}`. You look things up by key (`"name"`), not by
  position, unlike a list.
- **JSON**: a plain-text way of writing dictionaries (and lists, and simple
  values) that almost every programming language and API can read and write.
  A Python dictionary and a JSON object are the same *idea* — JSON is just that
  idea written down as pure text, which is what makes it possible to send it over
  the internet. You'll see this exact format again in Lesson B1.
- **Loop**: an instruction that repeats a block of code once for each item in a
  collection — "for every letter in this word, do something."
- **Conditional**: an `if` statement — code that only runs when some condition is
  true.

## Walkthrough

Open `workspace/exercises.py`. It has four functions, each with a docstring
(the triple-quoted explanation at the top of a function) describing what it
should do, and a `pass` placeholder where your code goes. Work through them in
order — each builds on the previous idea.

1. **`greet(name)`** — variables, strings, and your first `return`. Replace `pass`
   with a line that returns the string `"Hello, "` joined with `name` and `"!"`.
   The cleanest way in Python is an **f-string**:

   ```python
   return f"Hello, {name}!"
   ```

   Anything inside `{}` in an f-string gets swapped in with its real value —
   here, whatever `name` was passed in.

2. **`make_person(name, age)`** — build and return a dictionary using the two
   parameters:

   ```python
   return {"name": name, "age": age}
   ```

3. **`to_json_string(data)`** — convert a dictionary into JSON text. Python's
   built-in `json` module does this for you. Add `import json` at the very top of
   the file, then:

   ```python
   return json.dumps(data)
   ```

   (`dumps` means "dump to a **s**tring.")

4. **`count_vowels(word)`** — your first loop and conditional together:

   ```python
   count = 0
   for letter in word:
       if letter in "aeiou":
           count += 1
   return count
   ```

   Read this one out loud before running it: "start a counter at zero; for every
   letter in the word, if that letter is one of a/e/i/o/u, add one to the
   counter; once you've checked every letter, return the counter."

## Verification
I'll run:

```powershell
python -m pytest tests/test_a3_exercises.py -q
```

Each function has its own check. If one fails, I'll tell you which function and
what it returned versus what was expected — that difference is usually enough to
spot the fix yourself.

## Why this matters
Every one of these four ideas — variables, functions, dictionaries/JSON, loops —
shows up again in the very next lessons. Lesson B1's request to Claude *is* a
dictionary. Lesson B4's tool loop *is* a loop with a conditional inside it. Nothing
here is thrown away once you close this file.

## Before moving on
You don't need to commit yet — Lesson A5 covers git. Just make sure all four
checks are green before continuing.
