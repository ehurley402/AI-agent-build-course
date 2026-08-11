# B1 — Your first API call

## What you're about to do
Write the first real piece of your agent: a function that sends one message to
Claude and returns Claude's reply. Every later lesson builds on top of this.

## New words
- **Client**: an object in your code that represents "a connection to a specific
  service" — here, `anthropic.Anthropic()` creates a client object that knows how
  to talk to Anthropic's servers. You'll create one, then ask it to do things.
- **Request** / **response**: your client sends a *request* ("here's a message,
  please reply"); the API sends back a *response* — the data structure containing
  Claude's reply and some metadata about it.
- **Model**: the specific AI model you want handling the request — Anthropic runs
  several (faster/cheaper ones, slower/more capable ones). You specify which one
  by name, as plain text, every time you make a request.
- **Token**: roughly, a chunk of a word — Claude reads and writes in tokens, not
  raw characters. `max_tokens` caps how long a reply is allowed to be, measured in
  tokens rather than words or characters.
- **Attribute**: a named piece of data attached to an object, accessed with a dot
  — `response.content` reads the `content` attribute off the `response` object.

## Walkthrough

1. Open `workspace/agent.py`. It already has a skeleton with a `MODEL` constant
   and an empty `ask_claude` function — read the TODO comment inside it.

2. Replace the `pass` with real code that:
   - creates a client: `client = anthropic.Anthropic()`
   - calls `client.messages.create(...)`, passing `model=MODEL`,
     `max_tokens=1024`, and `messages=[{"role": "user", "content": prompt}]`
   - returns `response.content[0].text` (make sure you save the result of
     `messages.create(...)` into a variable, e.g. `response`, first)

   Note the shape of that `messages` list: it's a list containing one
   **dictionary** (you met these in Lesson A3) with two keys, `role` and
   `content`. `role` is always one of a small fixed set of values — `"user"` for
   things you send, `"assistant"` for Claude's replies. You'll reuse this exact
   shape in every lesson from here on.

3. Try running it for real (make sure your venv is active and
   `ANTHROPIC_API_KEY` is set — Lessons A4 and A6):

   ```powershell
   python workspace/agent.py
   ```

   You should see an actual reply from Claude printed to your terminal.

## Verification
I'll run:

```powershell
python -m pytest tests/test_b1_first_call.py -q
```

This check never uses your real API key or makes a real network call — it swaps
in a stand-in client that returns a fixed, fake reply, then checks that your
function returns that exact text and that you called `messages.create` with the
right shape of request. That's why step 3 above (running it for real) matters too
— it's the only place you actually see Claude respond.

## Why this matters
This one function — send a message, get text back — is the core operation every
more complex agent is built from. A conversation, a tool call, a multi-step agent
loop: all of them are just this same request/response pattern, called more than
once, with more information passed along each time.

## Before moving on
Commit your progress (Lesson A5):

```powershell
cd workspace
git add agent.py
git commit -m "Complete Lesson B1: first API call"
```
