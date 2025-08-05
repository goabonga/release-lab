# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Chris <goabonga@pm.me>

from hello import __version__

__expected_version__: str = "0.10.10"


def test_version() -> None:
    assert __version__ == __expected_version__
