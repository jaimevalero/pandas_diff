from __future__ import annotations

import warnings

import pandas as pd
import pytest

from pandas_diff import get_diffs

# --- Existing tests, migrated to pytest ---


class TestBasicOperations:
    def test_create(self, heroes_before, heroes_after):
        df = get_diffs(heroes_before, heroes_after, "hero")
        assert df.query("operation == 'create'").shape[0] == 1

    def test_delete(self, heroes_before, heroes_after):
        df = get_diffs(heroes_before, heroes_after, "hero")
        assert df.query("operation == 'delete'").shape[0] == 1

    def test_modify(self, heroes_before, heroes_after):
        df = get_diffs(heroes_before, heroes_after, "hero")
        assert df.query("operation == 'modify'").shape[0] == 2

    def test_columns_order(self, heroes_before, heroes_after):
        df = get_diffs(heroes_before, heroes_after, "hero")
        expected = [
            "operation",
            "object_keys",
            "object_values",
            "object_json",
            "attribute_changed",
            "old_value",
            "new_value",
        ]
        assert list(df.columns) == expected

    def test_columns_filter(self, heroes_before, heroes_after):
        df = get_diffs(heroes_before, heroes_after, "hero", ignore_columns=["power"])
        assert df.shape[0] == 3

    def test_keys_not_found(self, heroes_before, heroes_after):
        with pytest.raises(ValueError, match="Key field incorrect-key not in columns"):
            get_diffs(heroes_before, heroes_after, "incorrect-key")


# --- New tests ---


class TestInputValidation:
    def test_before_not_dataframe(self, heroes_after):
        with pytest.raises(TypeError, match="before must be a pandas DataFrame"):
            get_diffs("not a dataframe", heroes_after, "hero")

    def test_after_not_dataframe(self, heroes_before):
        with pytest.raises(TypeError, match="after must be a pandas DataFrame"):
            get_diffs(heroes_before, [1, 2, 3], "hero")

    def test_empty_keys_string(self, heroes_before, heroes_after):
        with pytest.raises(ValueError):
            get_diffs(heroes_before, heroes_after, "")


class TestEmptyDataFrames:
    def test_both_empty(self):
        empty = pd.DataFrame(columns=["id", "name"])
        df = get_diffs(empty, empty, "id")
        assert df.empty

    def test_before_empty(self):
        empty = pd.DataFrame(columns=["id", "name"])
        after = pd.DataFrame([{"id": 1, "name": "a"}])
        df = get_diffs(empty, after, "id")
        assert df.shape[0] == 1
        assert df.iloc[0]["operation"] == "create"

    def test_after_empty(self):
        before = pd.DataFrame([{"id": 1, "name": "a"}])
        empty = pd.DataFrame(columns=["id", "name"])
        df = get_diffs(before, empty, "id")
        assert df.shape[0] == 1
        assert df.iloc[0]["operation"] == "delete"


class TestNaNHandling:
    def test_nan_to_nan_not_a_change(self):
        before = pd.DataFrame([{"id": 1, "val": float("nan")}])
        after = pd.DataFrame([{"id": 1, "val": float("nan")}])
        df = get_diffs(before, after, "id")
        assert df.empty

    def test_value_to_nan_is_change(self):
        before = pd.DataFrame([{"id": 1, "val": "hello"}])
        after = pd.DataFrame([{"id": 1, "val": float("nan")}])
        df = get_diffs(before, after, "id")
        assert df.shape[0] == 1
        assert df.iloc[0]["operation"] == "modify"

    def test_nan_to_value_is_change(self):
        before = pd.DataFrame([{"id": 1, "val": float("nan")}])
        after = pd.DataFrame([{"id": 1, "val": "hello"}])
        df = get_diffs(before, after, "id")
        assert df.shape[0] == 1


class TestDuplicates:
    def test_duplicates_emit_warning(self):
        before = pd.DataFrame([{"id": 1, "v": "a"}, {"id": 1, "v": "b"}])
        after = pd.DataFrame([{"id": 1, "v": "c"}])
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            get_diffs(before, after, "id")
            assert len(w) >= 1
            assert "duplicated" in str(w[0].message).lower()


class TestMultiKey:
    def test_composite_key(self):
        before = pd.DataFrame([{"a": 1, "b": "x", "val": 10}])
        after = pd.DataFrame([{"a": 1, "b": "x", "val": 20}])
        df = get_diffs(before, after, ["a", "b"])
        assert df.shape[0] == 1
        assert df.iloc[0]["operation"] == "modify"

    def test_composite_key_create(self):
        before = pd.DataFrame([{"a": 1, "b": "x", "val": 10}])
        after = pd.DataFrame(
            [
                {"a": 1, "b": "x", "val": 10},
                {"a": 2, "b": "y", "val": 20},
            ]
        )
        df = get_diffs(before, after, ["a", "b"])
        assert df.shape[0] == 1
        assert df.iloc[0]["operation"] == "create"


class TestAsymmetricColumns:
    def test_extra_column_in_after(self):
        before = pd.DataFrame([{"id": 1, "name": "a"}])
        after = pd.DataFrame([{"id": 1, "name": "a", "extra": "new"}])
        df = get_diffs(before, after, "id")
        assert df.shape[0] == 1
        assert df.iloc[0]["attribute_changed"] == "extra"

    def test_extra_column_in_before(self):
        before = pd.DataFrame([{"id": 1, "name": "a", "old_col": "x"}])
        after = pd.DataFrame([{"id": 1, "name": "a"}])
        df = get_diffs(before, after, "id")
        assert df.shape[0] == 1
        assert df.iloc[0]["attribute_changed"] == "old_col"
