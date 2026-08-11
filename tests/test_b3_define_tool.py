"""Checks for Lesson B3 — defining a tool. No API call involved."""

from agent import WORD_LENGTH_TOOL, get_word_length


def test_get_word_length_is_a_real_working_function():
    assert get_word_length("hello") == 5
    assert get_word_length("a") == 1


def test_tool_definition_has_the_right_name_and_description():
    assert WORD_LENGTH_TOOL["name"] == "get_word_length"
    assert isinstance(WORD_LENGTH_TOOL.get("description"), str)
    assert len(WORD_LENGTH_TOOL["description"]) > 0


def test_tool_definition_input_schema_is_shaped_correctly():
    schema = WORD_LENGTH_TOOL["input_schema"]
    assert schema["type"] == "object"
    assert "word" in schema["properties"]
    assert schema["properties"]["word"]["type"] == "string"
    assert "word" in schema["required"]
