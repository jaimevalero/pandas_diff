========
Examples
========

Basic usage
-----------

.. code-block:: python

    import pandas as pd
    from pandas_diff import get_diffs

    before = pd.DataFrame([
        {"hero": "hulk", "power": "strength"},
        {"hero": "black_widow", "power": "spy"},
    ])
    after = pd.DataFrame([
        {"hero": "hulk", "power": "smart"},
        {"hero": "captain marvel", "power": "strength"},
    ])

    df = get_diffs(before, after, keys="hero")

Multi-key comparison
--------------------

.. code-block:: python

    df = get_diffs(before, after, keys=["region", "server_id"])

Ignoring columns
----------------

.. code-block:: python

    df = get_diffs(before, after, keys="id", ignore_columns=["updated_at"])

API Reference
-------------

.. automodule:: pandas_diff.pandas_diff
    :members:
