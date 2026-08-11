"""Checks for Lesson B4 — the tool-use round trip. No real network call is made."""

import anthropic

from fakes import FakeResponse, FakeTextBlock, FakeToolUseBlock, install_fake_client


def test_run_agent_uses_the_tool_and_returns_the_final_answer(monkeypatch):
    fake_client = install_fake_client(
        monkeypatch,
        anthropic,
        responses=[
            FakeResponse(
                [
                    FakeToolUseBlock(
                        id="toolu_01",
                        name="get_word_length",
                        input={"word": "philanthropy"},
                    )
                ],
                stop_reason="tool_use",
            ),
            FakeResponse(
                [FakeTextBlock("There are 12 letters in 'philanthropy'.")]
            ),
        ],
    )

    from agent import run_agent

    result = run_agent("How many letters are in the word philanthropy?")

    assert result == "There are 12 letters in 'philanthropy'."
    assert len(fake_client.messages.calls) == 2

    # The second call must hand back a correctly-shaped tool_result, tagged
    # with the same tool_use_id Claude sent in the first response.
    second_call_messages = fake_client.messages.calls[1]["messages"]
    tool_result_message = second_call_messages[-1]
    assert tool_result_message["role"] == "user"
    tool_result_block = tool_result_message["content"][0]
    assert tool_result_block["type"] == "tool_result"
    assert tool_result_block["tool_use_id"] == "toolu_01"
    assert tool_result_block["content"] == "12"


def test_run_agent_skips_the_tool_when_claude_doesnt_need_it(monkeypatch):
    fake_client = install_fake_client(
        monkeypatch,
        anthropic,
        responses=[FakeResponse([FakeTextBlock("Paris.")])],
    )

    from agent import run_agent

    result = run_agent("What's the capital of France?")

    assert result == "Paris."
    assert len(fake_client.messages.calls) == 1
