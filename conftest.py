"""Test configuration for repository.

Ensures the repository root is importable when tests are executed from the
`tests` directory.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
