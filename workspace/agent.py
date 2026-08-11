"""
Your agent. You'll build this up one lesson at a time, starting with Lesson B1.
Don't delete anything a later lesson tells you to add on top of — this one file
grows across B1 -> B4.
"""

import anthropic

MODEL = "claude-haiku-4-5-20251001"


def ask_claude(prompt):
    """Send a single text prompt to Claude and return its reply as a string.

    TODO (Lesson B1):
      1. Create a client: client = anthropic.Anthropic()
      2. Call client.messages.create(...) with:
           - model=MODEL
           - max_tokens=1024
           - messages=[{"role": "user", "content": prompt}]
      3. Return the reply text. The response's text lives at
         response.content[0].text
    """
    pass


def send_message(messages, user_input):
    """Add the user's message to `messages`, ask Claude to reply, add Claude's
    reply to `messages` too, and return just the reply text.

    TODO (Lesson B2):
      1. messages.append({"role": "user", "content": user_input})
      2. create a client and call client.messages.create(model=MODEL,
         max_tokens=1024, messages=messages) — pass the WHOLE history, not just
         this one message
      3. pull the reply text out, same as in ask_claude
      4. messages.append({"role": "assistant", "content": reply})
      5. return reply
    """
    pass


def get_word_length(word):
    """Return how many letters are in `word`.

    TODO (Lesson B3): replace `pass` with `return len(word)`.
    """
    pass


# TODO (Lesson B3): fill in WORD_LENGTH_TOOL, the dictionary that describes
# get_word_length to Claude. See the lesson for the exact shape.
WORD_LENGTH_TOOL = {}


# TODO (Lesson B4): list every tool this agent can offer Claude.
TOOLS = [WORD_LENGTH_TOOL]


def run_agent(user_input):
    """Send `user_input` to Claude, offering it TOOLS. If Claude asks to use a
    tool, run it locally and send the result back, then return the final
    answer. See the lesson for the exact steps.

    TODO (Lesson B4): fill in the body — see B4-tool-use-round-trip.md.
    """
    messages = [{"role": "user", "content": user_input}]
    client = anthropic.Anthropic()

    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        tools=TOOLS,
        messages=messages,
    )

    if response.stop_reason == "tool_use":
        pass

    return response.content[0].text


if __name__ == "__main__":
    # This block only runs when you execute `python agent.py` directly — not
    # when this file is imported for a test. It's how you'll try your agent
    # out for real once each lesson's automated check passes.
    messages = []
    print("Chat with your agent. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        reply = send_message(messages, user_input)
        print(f"Claude: {reply}")
