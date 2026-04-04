from __future__ import annotations

import pandas as pd


def get_key_values(row: pd.Series, keys: list[str]) -> str:
    key_values = ",".join(str(row[key]) for key in keys)
    return key_values


def format_results_create_delete(row: pd.Series, operation: str, keys: list[str]) -> dict:
    """Process create and delete entry."""
    key_values = get_key_values(row, keys)
    d = {
        "operation": operation,
        "object_keys": keys,
        "object_values": key_values,
        "object_json": row.to_dict(),
    }
    return d


def format_results_modify(
    row: pd.Series,
    keys: list[str],
    attribute_changed: str,
    old_value: object,
    new_value: object,
) -> dict:
    """Process modification entry."""
    key_values = get_key_values(row, keys)
    d = {
        "operation": "modify",
        "object_keys": keys,
        "object_values": key_values,
        "object_json": row.to_dict(),
        "attribute_changed": attribute_changed,
        "old_value": old_value,
        "new_value": new_value,
    }
    return d
