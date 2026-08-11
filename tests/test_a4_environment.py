"""Checks for Lesson A4 — packages and virtual environments.

If either import fails, pytest reports a collection error naming the missing
package — that error message *is* the feedback for this step.
"""

import anthropic
import pytest


def test_anthropic_is_installed():
    assert anthropic is not None


def test_pytest_is_installed():
    assert pytest is not None
