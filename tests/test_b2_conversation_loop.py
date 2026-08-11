"""Checks for Lesson B2 — conversation loop. No real network call is made."""

import anthropic

from fakes import FakeTextBlock, FakeResponse, install_fake_client


def test_send_message_returns_each_reply_and_builds_history(monkeypatch):
    fake_client = install_fake_client(
        monkeypatch,
        anthropic,
        responses=[
            FakeResponse([FakeTextBlock("Hi there!")]),
            FakeResponse([FakeTextBlock("It's a kind of legume.")]),
        ],
    )

    from agent import send_message

    messages = []

    first_reply = send_message(messages, "Hello")
    assert first_reply == "Hi there!"

    second_reply = send_message(messages, "What's a peanut?")
    assert second_reply == "It's a kind of legume."

    assert messages == [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi there!"},
        {"role": "user", "content": "What's a peanut?"},
        {"role": "assistant", "content": "It's a kind of legume."},
    ]

    # The second call must have sent the WHOLE history so far, not just the
    # newest message.
    assert len(fake_client.messages.calls) == 2
    second_call = fake_client.messages.calls[1]
    assert second_call["messages"] == messages[:3]
