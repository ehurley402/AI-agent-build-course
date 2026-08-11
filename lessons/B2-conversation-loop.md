# B2 — A real conversation

## What you're about to do
Right now, `ask_claude` can only ever send one message and forget everything —
each call starts from nothing. Add a second function that keeps a running history
of the conversation, so Claude can remember what was already said.

## New words
- **State**: information a program remembers and carries forward between one
  action and the next. The conversation history is state — without it, every
  message would land on Claude with no memory of what came before.
- **Mutate**: to change something in place, rather than creating a new copy. When
  you `.append(...)` to a list, you're mutating that same list — nothing new is
  created, the original just grows.
- **In-place**: a way of describing a function that changes something it was
  given directly, instead of only returning a new value. You'll write one of
  these in this lesson.

## Walkthrough

1. Look back at the `messages` list you built in Lesson B1 —
   `[{"role": "user", "content": prompt}]`. A conversation is just that same list,
   grown longer over time: one dictionary per message, alternating
   `"user"` and `"assistant"`.

2. In `workspace/agent.py`, add a new function below `ask_claude`:

   ```python
   def send_message(messages, user_input):
       """Add the user's message to `messages`, ask Claude to reply, add
       Claude's reply to `messages` too, and return just the reply text.

       `messages` is changed in place — the caller's list grows by two entries
       each time this runs.
       """
       # TODO:
       #   1. messages.append({"role": "user", "content": user_input})
       #   2. create a client and call client.messages.create(model=MODEL,
       #      max_tokens=1024, messages=messages) — pass the WHOLE history,
       #      not just this one message
       #   3. pull the reply text out, same as in ask_claude
       #   4. messages.append({"role": "assistant", "content": reply})
       #   5. return reply
       pass
   ```

   The key difference from `ask_claude`: you send the *entire* `messages` list
   every time, not just the newest line. Claude has no memory of its own between
   requests — every single call is self-contained, and the only reason it seems to
   "remember" earlier turns is that you're re-sending the whole transcript each
   time.

3. Update the `if __name__ == "__main__":` block at the bottom of the file to a
   real chat loop:

   ```python
   if __name__ == "__main__":
       messages = []
       print("Chat with your agent. Type 'quit' to exit.")
       while True:
           user_input = input("You: ")
           if user_input.lower() == "quit":
               break
           reply = send_message(messages, user_input)
           print(f"Claude: {reply}")
   ```

4. Run it and have an actual back-and-forth:

   ```powershell
   python workspace/agent.py
   ```

   Try asking it something, then referring back to what you just said (e.g. "what
   did I just ask you?") — that only works because `messages` is growing.

## Verification
I'll run:

```powershell
python -m pytest tests/test_b2_conversation_loop.py -q
```

It calls `send_message` twice against a fake client with two scripted replies
queued up, and checks that: each call returns the right reply, and after both
calls, `messages` holds all four entries (two user, two assistant) in the right
order with the right content.

## Why this matters
"Re-send the whole history every time" is how every chat-style AI product works,
including Claude Code itself. There's no hidden memory on the server side — the
state lives entirely in the list you're building and re-sending.

## Before moving on
```powershell
cd workspace
git add agent.py
git commit -m "Complete Lesson B2: conversation loop"
```
