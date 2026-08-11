"""Reference solution for Lesson B3. For tutor use only."""

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


if __name__ == "__main__":
    messages = []
    print("Chat with your agent. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        reply = send_message(messages, user_input)
        print(f"Claude: {reply}")
