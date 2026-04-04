"""Console script for pandas_diff."""

from __future__ import annotations

import sys
from pathlib import Path

import click
import pandas as pd

from pandas_diff import get_diffs

SUPPORTED_EXTENSIONS = {".csv", ".json", ".parquet"}


def load_dataframe(file_path: str) -> pd.DataFrame:
    """Load a DataFrame from a file, detecting format by extension."""
    path = Path(file_path)
    if not path.exists():
        raise click.BadParameter(f"File not found: {file_path}")

    ext = path.suffix.lower()
    if ext == ".csv":
        return pd.read_csv(path)
    elif ext == ".json":
        return pd.read_json(path)
    elif ext == ".parquet":
        return pd.read_parquet(path)
    else:
        raise click.BadParameter(
            f"Unsupported file format: '{ext}'. Supported: {', '.join(sorted(SUPPORTED_EXTENSIONS))}"
        )


@click.command()
@click.argument("before", type=click.Path())
@click.argument("after", type=click.Path())
@click.option("--keys", required=True, help="Key column(s), comma-separated.")
@click.option("--ignore", default="", help="Columns to ignore, comma-separated.")
@click.option(
    "--format",
    "output_format",
    type=click.Choice(["table", "csv", "json"]),
    default="table",
    help="Output format.",
)
@click.option("--output", "-o", type=click.Path(), default=None, help="Output file (default: stdout).")
def main(
    before: str,
    after: str,
    keys: str,
    ignore: str,
    output_format: str,
    output: str | None,
) -> None:
    """Compare two data files and show row-level differences.

    Supports CSV, JSON (flat records), and Parquet files.

    \b
    Examples:
        pandas_diff before.csv after.csv --keys id
        pandas_diff old.parquet new.parquet --keys name,date --format json
        pandas_diff a.csv b.csv --keys id --ignore updated_at -o diff.csv
    """
    try:
        df_before = load_dataframe(before)
        df_after = load_dataframe(after)
    except click.BadParameter as e:
        raise click.ClickException(str(e))

    key_list = [k.strip() for k in keys.split(",")]
    ignore_list = [c.strip() for c in ignore.split(",") if c.strip()]

    try:
        result = get_diffs(df_before, df_after, key_list, ignore_columns=ignore_list)
    except (ValueError, TypeError) as e:
        raise click.ClickException(str(e))

    if result.empty:
        click.echo("No differences found.")
        return

    if output_format == "json":
        text = result.to_json(orient="records", indent=2)
    elif output_format == "csv":
        text = result.to_csv(index=False)
    else:
        text = result.to_string(index=False)

    if output:
        Path(output).write_text(text)
        click.echo(f"Results written to {output}")
    else:
        click.echo(text)


if __name__ == "__main__":
    sys.exit(main())
