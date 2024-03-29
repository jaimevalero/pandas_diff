
# Pandas Diff
[![CodeFactor](https://www.codefactor.io/repository/github/jaimevalero/pandas_diff/badge)](https://www.codefactor.io/repository/github/jaimevalero/pandas_diff)
[![Documentation Status](https://readthedocs.org/projects/pandas-diff/badge/?version=latest)](https://pandas-diff.readthedocs.io/en/latest/?badge=latest)
[![Python 3](https://pyup.io/repos/github/jaimevalero/pandas_diff/python-3-shield.svg)](https://pyup.io/repos/github/jaimevalero/pandas_diff/)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/bd60be67332644e2a64401b6f44a3b12)](https://www.codacy.com/gh/jaimevalero/pandas_diff/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jaimevalero/pandas_diff&amp;utm_campaign=Badge_Grade)

Get differences between two pandas dataframes 

## Installation

Install pandas_diff with pip

```bash
pip install pandas_diff
```


## Usage/Examples

```python
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

  operation object_keys  object_values                     object_json                     attribute_changed old_value new_value
0   create     [hero]    captain marvel  {'hero': 'captain marvel', 'power': 'strength'...           NaN           NaN      NaN
1   delete     [hero]       black_widow  {'hero': 'black_widow', 'power': 'spy', 'hamme...           NaN           NaN      NaN
2   modify     [hero]              thor  {'hero': 'thor', 'power': nan, 'hammers': 2.0}          hammers             1        2
3   modify     [hero]              hulk  {'hero': 'hulk', 'power': 'smart', 'hammers': ...         power      strength    smart

```

## Why pandas diff ? Cases of use

<h3>Migrate from batch to event driven architecture</h3>

In my work, we use a lot of data pipelines to get info from external
platforms, (active directory, github, jira). We load the new data
replacing the entire table.

By using pandas_diff we detect how the infraestructure changes between
executions, and stream those change events into a kafka cluster, so
other teams could suscribe to their favourite events. Also, by defining
a pandas_diff step in the master pipeline, every item in our project has
ther life cycle events controlled.


<h3>Events log</h3>


For every item in a table, by using pandas_diff you will have an event
log to audit listing how the resources are being consumed.

<h3>Conciliation of info</h3>

To conciliate one datasource against the source of truth. Eg: You have a CMDB controlling with info regarding virtual machines. As there are several methods for creating those VMs, you use pandas_diff to replicate state of the infraestructure against the CMDB. 

<h3>Disaster recovery environments</h3>
Eg: You have a disaster recovery environment for your platform. You can synch two platforms, production and disaster recovery, using their APIs and pandas_diff to propagate the changes (in objects, users, permissions) from production to disaster recovery environments.


## Features

* Key multicolum
* Blacklist of columns

## Roadmap

* Support for stand alone app

## Documentation

[Documentation](https://pandas-diff.readthedocs.io/en/latest/)




