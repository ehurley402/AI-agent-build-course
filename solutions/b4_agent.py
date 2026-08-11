"""Reference solution for Lesson B4 — the completed first agent. For tutor use
only."""

import anthropic

MODEL = "claude-haiku-4-5-20251001"


def ask_claude(prompt):
    client = anthropic.Anthropic()
    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text


def send_message(messages, user_input):
    messages.append({"role": "user", "content": user_input})
    client = anthropic.Anthropic()
    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        messages=messages,
    )
    reply = response.content[0].text
    messages.append({"role": "assistant", "content": reply})
    return reply


def get_word_length(word):
    return len(word)


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

TOOLS = [WORD_LENGTH_TOOL]


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
        tool_use_block = None
        for block in response.content:
            if block.type == "tool_use":
                tool_use_block = block

        result = get_word_length(**tool_use_block.input)

        messages.append({"role": "assistant", "content": response.content})
        messages.append(
            {
                "role": "user",
                "content": [
                    {
                        "type": "tool_result",
                        "tool_use_id": tool_use_block.id,
                        "content": str(result),
                    }
                ],
            }
        )

        response = client.messages.create(
            model=MODEL,
            max_tokens=1024,
            tools=TOOLS,
            messages=messages,
        )

    return response.content[0].text


if __name__ == "__main__":
    messages = []
    print("Chat with your agent. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        reply = send_message(messages, user_input)
        print(f"Claude: {reply}")
