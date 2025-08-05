# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Chris <goabonga@pm.me>

from .cli import main as cli

__version__: str = "0.13.0"
"""Current version of the release-lab package."""

__all__ = [
    "__version__",
    "cli",
]
