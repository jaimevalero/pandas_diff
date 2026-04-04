======================
Command Line Interface
======================

pandas_diff includes a CLI for comparing data files directly from the terminal.

Usage
-----

.. code-block:: console

    $ pandas_diff BEFORE AFTER --keys KEY [--ignore COLS] [--format FORMAT] [-o FILE]

Supported file formats: CSV, JSON (flat records), Parquet.

Examples
--------

.. code-block:: console

    $ pandas_diff before.csv after.csv --keys id
    $ pandas_diff old.parquet new.parquet --keys name,date --format json
    $ pandas_diff a.csv b.csv --keys id --ignore updated_at -o diff.csv

Output formats
--------------

- ``table`` (default): Human-readable table
- ``csv``: CSV output
- ``json``: JSON array of records
