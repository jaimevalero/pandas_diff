import pandas as pd
import unittest


import pandas_diff.pandas_diff as pd_diff

from pandas_diff.pandas_diff import get_diffs
from pandas_diff.pre_process import pre_process

class TestStringMethods(unittest.TestCase):
    def __get_data(self):
        A = pd.DataFrame([{"hero" : "hulk" , "power" : "strength"},
                        {"hero" : "black_widow" , "power" : "spy"},
                        {"hero" : "thor" , "hammers" : 0 } ] )
        B = pd.DataFrame([{"hero" : "hulk" , "power" : "smart"},
                        {"hero" : "captain marvel" , "power" : "strength"},
                        {"hero" : "thor" , "hammers" : 2 } ] )
        A,B , keys = pre_process(A, B, ["hero"])
        df = pd_diff.get_diffs(A,B,keys)
        return df
    def test_create(self):
        df = self.__get_data()
        self.assertEqual(df.query(" operation == 'create' ").shape[0],1)
    def test_modify(self):
        df = self.__get_data()
        self.assertEqual(df.query(" operation == 'modify' ").shape[0],2)
    def test_delete(self):
        df = self.__get_data()
        self.assertEqual(df.query(" operation == 'delete' ").shape[0],1)
    def test_columns_order(self):
        df = self.__get_data()
        ORDER_EXPECTED = ['operation','object_keys','object_values','object_json','attribute_changed','old_value','new_value']
        order = df.columns.values
        result =len([i for i, j in zip(order, ORDER_EXPECTED) if i == j])
        self.assertEqual(result,7)

if __name__ == '__main__':
    unittest.main()
