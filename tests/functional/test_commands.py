# -*- coding: utf-8 -*-
import pytest

from servicedesk.commands import blacken, lint


def test_lint(app):
    runner = app.test_cli_runner()

    result = runner.invoke(lint)

    assert (
        "Checking code style: black --check autoapp.py assets docs servicedesk tests tmp __pycache__"
        in result.output
    )


def test_lint_fix_imports(app):
    runner = app.test_cli_runner()
    result = runner.invoke(lint, ["--fix-imports"])

    assert (
        "Fixing import order: isort -rc autoapp.py assets docs servicedesk tests tmp __pycache_"
        in result.output
    )


def test_format(app):
    runner = app.test_cli_runner()
    result = runner.invoke(blacken)

    assert (
        "Formatting project: black autoapp.py assets docs servicedesk tests tmp __pycache__"
        in result.output
    )
