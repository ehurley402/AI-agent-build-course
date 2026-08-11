"""Shared pytest setup for the tutorial's checks.

This makes the learner's files in workspace/ importable as plain modules
(e.g. `import exercises`, `import agent`) no matter where pytest is run from.
Learners never need to read or edit this file.
"""

import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent / "workspace"
if str(WORKSPACE) not in sys.path:
    sys.path.insert(0, str(WORKSPACE))
