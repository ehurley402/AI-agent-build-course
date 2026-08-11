# B4 — The tool-use round trip

## What you're about to do
Wire everything together: send Claude a request that offers it a tool, notice
when it asks to use that tool, actually run the tool yourself, and send the
result back so Claude can give a final answer. This is a real agent loop —
everything after this lesson is refinement of this same pattern.

## New words
- **Agent loop**: the cycle of "send a request → check whether the model wants a
  tool run → run it → send the result back → repeat until you get a final answer."
  Every AI agent, including Claude Code itself, is this same loop at its core —
  just with more tools and more turns.
- **`stop_reason`**: a field on Claude's response telling you *why* it stopped
  generating. Two you'll see here: `"end_turn"` (a normal finished reply) and
  `"tool_use"` (Claude is pausing to ask you to run a tool before it continues).
- **Content block**: one item inside `response.content`. So far every response
  you've seen has had exactly one block, a `"text"` block. A `tool_use` response
  contains a `"tool_use"` block instead — no plain text yet, just a request.
- **`tool_use_id`**: a unique ID Claude attaches to each tool request. When you
  send the result back, you tag it with this same ID so Claude knows exactly
  which request the result answers — this matters once an agent can request more
  than one tool in the same turn.
- **Round trip**: the full "ask → tool runs → tell it the result" cycle — two
  separate calls to `messages.create`, connected by the tool result in between.

## Walkthrough

1. In `workspace/agent.py`, add the list of tools your agent can offer:

   ```python
   TOOLS = [WORD_LENGTH_TOOL]
   ```

2. Add the function that runs the whole loop:

   ```python
   def run_agent(user_input):
       messages = [{"role": "user", "content": user_input}]
       client = anthropic.Anthropic()

       response = client.messages.create(
           model=MODEL,
           max_tokens=1024,
           tools=TOOLS,
           messages=messages,
       )

       if response.stop_reason == "tool_use":
           # TODO: find the tool_use block inside response.content.
           # Loop over response.content; the block you want has
           # block.type == "tool_use". Save it as `tool_use_block`.

           # TODO: actually run the tool locally:
           # result = get_word_length(**tool_use_block.input)

           # TODO: tell Claude what you just asked it (the tool_use block
           # itself, as the assistant's turn), then hand back the result as a
           # new user turn shaped like this:
           # messages.append({"role": "assistant", "content": response.content})
           # messages.append({
           #     "role": "user",
           #     "content": [
           #         {
           #             "type": "tool_result",
           #             "tool_use_id": tool_use_block.id,
           #             "content": str(result),
           #         }
           #     ],
           # })

           # TODO: call client.messages.create(...) again with the SAME
           # arguments as above (model, max_tokens, tools, messages) — this is
           # the second half of the round trip. Save it back into `response`.
           pass

       return response.content[0].text
   ```

   Read through the TODOs before you write anything — this function makes two
   separate requests to Claude when a tool gets used, and it's worth seeing the
   shape of the whole round trip before filling in any one piece.

3. Try it for real (make sure you're standing inside `workspace` first):

   ```powershell
   cd workspace
   python -c "from agent import run_agent; print(run_agent('How many letters are in the word philanthropy?'))"
   ```

   Claude has no idea how to count letters reliably on its own — this is a real
   case where it needs the tool, not a toy example. Also try a question that
   doesn't need the tool at all (e.g. `run_agent("What's the capital of France?")`)
   and confirm it still answers directly, skipping the tool entirely.

## Verification
I'll run:

```powershell
python -m pytest tests/test_b4_tool_loop.py -q
```

It scripts a fake first response with `stop_reason="tool_use"` requesting
`get_word_length`, and a fake second response with the final text — then checks
that your function returns the right final answer, that the tool actually ran with
the right input, and that the second request included a correctly-shaped
`tool_result`.

## Why this matters
This is the whole idea behind "agent" as opposed to "chat bot": the model doesn't
just talk *about* the world, it can act — run real code, get a real result, and
factor that into its answer. You just built that, from scratch, in about forty
lines of Python.

## Before moving on — and after
```powershell
cd workspace
git add agent.py
git commit -m "Complete Lesson B4: tool-use round trip — first working agent"
git log --oneline
```

That last command should show every commit you've made since Lesson A5, in order —
your whole build, end to end.
