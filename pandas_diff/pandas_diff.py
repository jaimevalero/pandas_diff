"""Main module."""
import pandas as pd
from pre_process import pre_process
#A = pd.DataFrame({'col_1': [1, 2, 3, 4, 5], 'col_2': [1, 2, 3, 4, 5]})
#B = pd.DataFrame({'col_1': [1, 2, 3, 3, 5], 'col_3': [1, 2, 4, 5, 6]})

A = pd.DataFrame([{"hero" : "hulk" , "power" : "strength"},
                  {"hero" : "black_widow" , "power" : "spy"},
                  {"hero" : "thor" , "hammers" : 0 },
                  {"hero" : "thor" , "hammers" : 1 } ] )
B = pd.DataFrame([{"hero" : "hulk" , "power" : "smart"},
                 {"hero" : "captain marvel" , "power" : "strength"},
                 {"hero" : "thor" , "hammers" : 2 } ] )

#df =  pd.DataFrame({'col_1': [1, 2, 3, 3, 5], 'col_3': [1, 2, 4, 5, 6]})
A,B , keys = pre_process(A, B, "hero")

A["___keys"] = A[keys]
B["___keys"] = B[keys]

a=0

