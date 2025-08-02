# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Chris <goabonga@pm.me>

from hello import __version__


def test_version() -> None:
    assert __version__ == "0.1.0"
