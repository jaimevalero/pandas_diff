
#Pandas Diff



## Installation

Install pandas_diff with pip

```bash
  pip install pandas_diff
```


## Usage/Examples

```python
import pandas_diff as pd_diff

import pandas as pd
A = pd.DataFrame([{"hero" : "hulk" , "power" : "strength"},
                {"hero" : "black_widow" , "power" : "spy"},
                {"hero" : "thor" , "hammers" : 0 },
                {"hero" : "thor" , "hammers" : 1 } ] )
B = pd.DataFrame([{"hero" : "hulk" , "power" : "smart"},
                {"hero" : "captain marvel" , "power" : "strength"},
                {"hero" : "thor" , "hammers" : 2 } ] )
df = pd_diff.get_diffs(A,B,"hero")

df

  operation object_keys  object_values                     object_json                     attribute_changed old_value new_value
0   create     [hero]    captain marvel  {'hero': 'captain marvel', 'power': 'strength'...           NaN           NaN      NaN
1   delete     [hero]       black_widow  {'hero': 'black_widow', 'power': 'spy', 'hamme...           NaN           NaN      NaN
2   modify     [hero]              thor     {'hero': 'thor', 'power': nan, 'hammers': 2.0}       hammers             1        2
3   modify     [hero]              hulk  {'hero': 'hulk', 'power': 'smart', 'hammers': ...         power      strength    smart

```



Features
--------

* Support for stand alone app


