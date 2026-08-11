"""A fake stand-in for the real anthropic.Anthropic client, used by the Track B
tests so checking a learner's code never makes a real (billed) API call.

Learners never need to read this file. It mimics just enough of the real SDK's
shape (response.content[i].type/.text, response.stop_reason, block.name/.input/.id)
for the tutorial's checks to work.
"""


class FakeTextBlock:
    def __init__(self, text):
        self.type = "text"
        self.text = text


class FakeToolUseBlock:
    def __init__(self, id, name, input):
        self.type = "tool_use"
        self.id = id
        self.name = name
        self.input = input


class FakeResponse:
    def __init__(self, content, stop_reason="end_turn"):
        self.content = content
        self.stop_reason = stop_reason


class FakeMessages:
    def __init__(self, responses):
        self._responses = list(responses)
        self.calls = []

    def create(self, **kwargs):
        # Snapshot the `messages` list at call time — the caller's list is
        # mutated (grown) after this returns, and we don't want that later
        # mutation silently changing what an already-recorded call looks like.
        recorded = dict(kwargs)
        if "messages" in recorded:
            recorded["messages"] = list(recorded["messages"])
        self.calls.append(recorded)
        if not self._responses:
            raise AssertionError(
                "The fake client received more calls to messages.create() than "
                "this test expected a real agent to make."
            )
        return self._responses.pop(0)


class FakeAnthropicClient:
    """Stands in for `anthropic.Anthropic()`."""

    def __init__(self, responses):
        self.messages = FakeMessages(responses)


def install_fake_client(monkeypatch, anthropic_module, responses):
    """Patch anthropic.Anthropic so any `anthropic.Anthropic()` in the learner's
    code returns a fake client that plays back `responses` in order. Returns the
    fake client so the test can inspect the calls it received.
    """
    fake_client = FakeAnthropicClient(responses)
    monkeypatch.setattr(anthropic_module, "Anthropic", lambda *a, **k: fake_client)
    return fake_client
