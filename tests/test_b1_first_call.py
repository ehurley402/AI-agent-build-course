"""Checks for Lesson B1 — first API call. No real network call is made."""

import anthropic

from fakes import FakeTextBlock, FakeResponse, install_fake_client


def test_ask_claude_returns_the_reply_text(monkeypatch):
    fake_client = install_fake_client(
        monkeypatch,
        anthropic,
        responses=[FakeResponse([FakeTextBlock("I'm doing well, thanks!")])],
    )

    from agent import ask_claude

    result = ask_claude("How are you?")

    assert result == "I'm doing well, thanks!"


def test_ask_claude_sends_a_correctly_shaped_request(monkeypatch):
    fake_client = install_fake_client(
        monkeypatch,
        anthropic,
        responses=[FakeResponse([FakeTextBlock("hi")])],
    )

    from agent import ask_claude

    ask_claude("How are you?")

    assert len(fake_client.messages.calls) == 1
    call = fake_client.messages.calls[0]
    assert "model" in call
    assert "max_tokens" in call
    assert call["messages"] == [{"role": "user", "content": "How are you?"}]
