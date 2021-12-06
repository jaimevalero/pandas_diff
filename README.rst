Pandas Diff
===========

|CodeFactor| |Python 3|

Installation
------------

Install pandas_diff with pip

.. code:: bash

   pip install pandas_diff

Usage/Examples
--------------

.. code:: python

   import pandas_diff as pd_diff

   import pandas as pd

   # Create two example dataframes
   df_infinity_war = pd.DataFrame([
                   {"hero" : "hulk" , "power" : "strength"},
                   {"hero" : "black_widow" , "power" : "spy"},
                   {"hero" : "thor" , "hammers" : 0 },
                   {"hero" : "thor" , "hammers" : 1 } ] )
   df_endgame = pd.DataFrame([
                   {"hero" : "hulk" , "power" : "smart"},
                   {"hero" : "captain marvel" , "power" : "strength"},
                   {"hero" : "thor" , "hammers" : 2 } ] )

   # Get differences, using the key "hero"
   df = pd_diff.get_diffs(df_infinity_war ,df_endgame ,"hero")

   df

   #operation object_keys  object_values                     object_json                     attribute_changed old_value new_value
   #0   create     [hero]    captain marvel  {'hero': 'captain marvel', 'power': 'strength'...           NaN           NaN      NaN
   #1   delete     [hero]       black_widow  {'hero': 'black_widow', 'power': 'spy', 'hamme...           NaN           NaN      NaN
   #2   modify     [hero]              thor     {'hero': 'thor', 'power': nan, 'hammers': 2.0}       hammers             1        2
   #3   modify     [hero]              hulk  {'hero': 'hulk', 'power': 'smart', 'hammers': ...         power      strength    smart

Why pandas diff ? Cases of use
------------------------------

Migrating from batch to an event driven architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In my work, we use a lot of data pipelines to get info from external
platforms, (active directory, github, jira). We load the new data
replacing the entire table.

By using pandas_diff we detect how the infraestructure changes between
executions, and stream those change events into a kafka cluster, so
other teams could suscribe to their favourite events. Also, by defining
a pandas_diff step in the master pipeline, every item in our project has
ther life cycle events controlled.

Events log
~~~~~~~~~~

For every item in a table, by using pandas_diff you will have an event
log to audit of how the resources are being consumed.

Conciliation
~~~~~~~~~~~~

To conciliate one datasource against the source of truth. Eg: You have a CMDB controlling with info regarding virtual machines. As there are several methods for creating those VMs, you use pandas_diff to replicate state of the infraestructure against the CMDB.

Features
--------

-  Filtering of columns

Roadmap
-------

-  Support for stand alone app

Documentation
-------------

`Documentation <https://pandas-diff.readthedocs.io/en/latest/>`__

.. |CodeFactor| image:: https://www.codefactor.io/repository/github/jaimevalero/pandas_diff/badge
   :target: https://www.codefactor.io/repository/github/jaimevalero/pandas_diff
.. |Python 3| image:: https://pyup.io/repos/github/jaimevalero/pandas_diff/python-3-shield.svg
   :target: https://pyup.io/repos/github/jaimevalero/pandas_diff/

