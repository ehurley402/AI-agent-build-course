"""Reference solution for Lesson B1. For tutor use only."""

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


if __name__ == "__main__":
    reply = ask_claude("Say hello in one short sentence.")
    print(reply)
