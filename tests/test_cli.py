from __future__ import annotations

import json
import os
import tempfile

import pandas as pd
import pytest
from click.testing import CliRunner

from pandas_diff.cli import main


@pytest.fixture
def csv_files():
    """Create temporary CSV files for testing."""
    before = pd.DataFrame([{"id": 1, "name": "alice"}, {"id": 2, "name": "bob"}])
    after = pd.DataFrame([{"id": 1, "name": "alice_v2"}, {"id": 3, "name": "charlie"}])
    with tempfile.TemporaryDirectory() as tmpdir:
        before_path = os.path.join(tmpdir, "before.csv")
        after_path = os.path.join(tmpdir, "after.csv")
        before.to_csv(before_path, index=False)
        after.to_csv(after_path, index=False)
        yield before_path, after_path


class TestCLI:
    def test_csv_default_output(self, csv_files):
        runner = CliRunner()
        before_path, after_path = csv_files
        result = runner.invoke(main, [before_path, after_path, "--keys", "id"])
        assert result.exit_code == 0
        assert "create" in result.output or "delete" in result.output or "modify" in result.output

    def test_csv_json_output(self, csv_files):
        runner = CliRunner()
        before_path, after_path = csv_files
        result = runner.invoke(main, [before_path, after_path, "--keys", "id", "--format", "json"])
        assert result.exit_code == 0
        parsed = json.loads(result.output)
        assert isinstance(parsed, list)

    def test_csv_csv_output(self, csv_files):
        runner = CliRunner()
        before_path, after_path = csv_files
        result = runner.invoke(main, [before_path, after_path, "--keys", "id", "--format", "csv"])
        assert result.exit_code == 0
        assert "operation" in result.output

    def test_missing_file(self):
        runner = CliRunner()
        result = runner.invoke(main, ["nonexistent.csv", "also_no.csv", "--keys", "id"])
        assert result.exit_code != 0

    def test_unsupported_format(self, csv_files):
        runner = CliRunner()
        before_path, after_path = csv_files
        result = runner.invoke(main, [before_path, after_path, "--keys", "id", "--format", "xml"])
        assert result.exit_code != 0

    def test_ignore_columns(self, csv_files):
        runner = CliRunner()
        before_path, after_path = csv_files
        result = runner.invoke(main, [before_path, after_path, "--keys", "id", "--ignore", "name"])
        assert result.exit_code == 0
