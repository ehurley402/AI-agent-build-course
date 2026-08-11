"""Checks for Lesson A3 — programming basics."""

import json

from exercises import count_vowels, greet, make_person, to_json_string


def test_greet():
    assert greet("Ada") == "Hello, Ada!"
    assert greet("Sam") == "Hello, Sam!"


def test_make_person():
    assert make_person("Ada", 30) == {"name": "Ada", "age": 30}


def test_to_json_string():
    result = to_json_string({"name": "Ada", "age": 30})
    assert isinstance(result, str)
    assert json.loads(result) == {"name": "Ada", "age": 30}


def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("sky") == 0
    assert count_vowels("aeiou") == 5
