import pandas as pd
import unittest



from pandas_diff.pandas_diff import get_diffs
from pandas_diff.pre_process import pre_process

class TestStringMethods(unittest.TestCase):
    def __base_case(self):
        A = pd.DataFrame([{"hero" : "hulk" , "power" : "strength"},
                        {"hero" : "black_widow" , "power" : "spy"},
                        {"hero" : "thor" , "hammers" : 0 } ] )
        B = pd.DataFrame([{"hero" : "hulk" , "power" : "smart"},
                        {"hero" : "captain marvel" , "power" : "strength"},
                        {"hero" : "thor" , "hammers" : 2 } ] )
        A,B , keys = pre_process(A, B, ["hero"])
        return A,B,keys
    def __get_data(self):
        A,B , keys = self.__base_case()
        df = get_diffs(A,B,keys)
        return df
    def test_create(self):
        """ Test create are detected """
        df = self.__get_data()
        self.assertEqual(df.query(" operation == 'create' ").shape[0],1)
    def test_modify(self):
        """ Test modify are detected """
        df = self.__get_data()
        self.assertEqual(df.query(" operation == 'modify' ").shape[0],2)
    def test_delete(self):
        """ Test delete are detected """
        df = self.__get_data()
        self.assertEqual(df.query(" operation == 'delete' ").shape[0],1)
    def test_columns_order(self):
        """ Test column are returned in the correct order"""
        df = self.__get_data()
        ORDER_EXPECTED = ['operation','object_keys','object_values','object_json','attribute_changed','old_value','new_value']
        order = df.columns.values
        result =len([i for i, j in zip(order, ORDER_EXPECTED) if i == j])
        if result != 7: 
            print(f"order unexpected: {order}. The correct was {ORDER_EXPECTED}" )
        self.assertEqual(result,7)
    def test_columns_filter(self):
        """ Test filter is working """
        A,B , keys = self.__base_case()
        df = get_diffs(A ,B ,"hero", ignore_columns=["power"])
        self.assertEqual(df.shape[0],3)
    def test_keys_exists(self):
        """ Test checking keys exist is working """
        A,B , keys = self.__base_case()
        #self.failUnlessRaises(ValueError, get_diffs(A ,B ,"incorrect-key"))
        with self.assertRaises(ValueError) as cm:
            get_diffs(A ,B ,"incorrect-key")
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Key field incorrect-key not in columns ['hero' 'power' 'hammers']")

if __name__ == '__main__':
    unittest.main()
