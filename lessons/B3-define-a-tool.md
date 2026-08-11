# B3 — Give your agent a tool

## What you're about to do
So far, Claude can only answer using what it already knows. A **tool** lets it
reach outside itself and run actual code you wrote — the thing that turns "a chat
bot" into "an agent." This lesson defines one small tool; the next lesson makes
Claude actually use it.

## New words
- **Tool**: a function in your own code that you describe to Claude, so Claude can
  ask for it to be run when it decides that's the right move — Claude never runs
  your code directly; it only ever *requests* that you run it (you'll see exactly
  how in Lesson B4).
- **Tool definition** / **schema**: the dictionary you write that describes a tool
  to Claude — its name, a plain-language description of what it does, and the
  exact shape of the input it expects. Claude reads this description to decide
  *whether* and *how* to ask for the tool.
- **JSON Schema**: a standard, structured way of describing "what shape of data is
  allowed here" — which fields exist, what type each one is, which are required.
  You met plain JSON in Lesson A3; this is JSON used specifically to describe a
  *shape*, not to hold actual data.

## Walkthrough

1. In `workspace/agent.py`, add a plain Python function that does one simple,
   real thing — nothing to do with Claude yet, just an ordinary function:

   ```python
   def get_word_length(word):
       """Return how many letters are in `word`."""
       return len(word)
   ```

2. Now describe that function to Claude as a tool definition:

   ```python
   WORD_LENGTH_TOOL = {
       "name": "get_word_length",
       "description": "Get the number of letters in a single word.",
       "input_schema": {
           "type": "object",
           "properties": {
               "word": {
                   "type": "string",
                   "description": "The word to measure.",
               }
           },
           "required": ["word"],
       },
   }
   ```

   Walk through this dictionary piece by piece:
   - `"name"` must exactly match the real function's name — this is how you'll
     connect Claude's request back to actual code in the next lesson.
   - `"description"` is the only thing Claude reads to decide *when* this tool is
     useful — write it like you're explaining the tool to a new coworker, not to
     a machine.
   - `"input_schema"` says: the input is an object (a JSON object — same shape as
     a Python dictionary) with one required field, `"word"`, which must be text
     (`"type": "string"`).

## Verification
I'll run:

```powershell
python -m pytest tests/test_b3_define_tool.py -q
```

This check calls `get_word_length` directly (no API involved) to confirm it
behaves correctly, then inspects `WORD_LENGTH_TOOL` to confirm its name,
description, and input schema are all shaped correctly for Claude to read.

## Why this matters
Nothing here talks to Claude yet — on purpose. This lesson is entirely about
getting the *description* right, because in the next lesson, Claude will read
exactly this dictionary to decide whether it needs to ask for this tool at all.

## Before moving on
```powershell
cd workspace
git add agent.py
git commit -m "Complete Lesson B3: define a tool"
```
