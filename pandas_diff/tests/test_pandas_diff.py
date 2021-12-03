import pandas as pd
import unittest



from pandas_diff import get_diffs
from pre_process import pre_process

class TestStringMethods(unittest.TestCase):
    def __get_data(self):
        A = pd.DataFrame([{"hero" : "hulk" , "power" : "strength"},
                        {"hero" : "black_widow" , "power" : "spy"},
                        {"hero" : "thor" , "hammers" : 0 },
                        {"hero" : "thor" , "hammers" : 1 } ] )
        B = pd.DataFrame([{"hero" : "hulk" , "power" : "smart"},
                        {"hero" : "captain marvel" , "power" : "strength"},
                        {"hero" : "thor" , "hammers" : 2 } ] )
        A,B , keys = pre_process(A, B, ["hero"])
        df = pandas_diff.get_diffs(A,B,keys)
        return df
    def test_create(self):
        df = self.__get_data()
        self.assertEqual(df.query(" operation == 'create' ").shape[0],1)
    def test_delete(self):
        df = self.__get_data()
        self.assertEqual(df.query(" operation == 'modify' ").shape[0],2)
