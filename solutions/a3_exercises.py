"""Reference solution for Lesson A3. For tutor use only — not shown to the
learner unless they explicitly ask for the answer after a real attempt."""

import json


def greet(name):
    return f"Hello, {name}!"


def make_person(name, age):
    return {"name": name, "age": age}


def to_json_string(data):
    return json.dumps(data)


def count_vowels(word):
    count = 0
    for letter in word:
        if letter in "aeiou":
            count += 1
    return count
