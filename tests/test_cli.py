# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Chris <goabonga@pm.me>

from hello.cli import main

from click.testing import CliRunner
from os import abort


def test_hello_default() -> None:
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 0
    assert "Hello, world!" in result.output


def test_hello_name() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["Alice"])
    assert result.exit_code == 0
    assert "Hello, Alice!" in result.output
