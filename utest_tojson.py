import tojson
import unittest
import json


class ToJsonTest(unittest.TestCase):
    def test_to_json(self):
        var_dict = {"name": "Viktor", "age": 30}
        var_tuple = ("Porsche", "BMW")
        var_string = "Hello, this is my string"
        var_float = 1023.12
        var_tuple_in_dict = {"sex" : ("not_men", "not_women")}
        var_bool = False
        var_none = None

        #testing
        self.assertEqual(tojson.to_json(var_dict), json.dumps(var_dict))
        self.assertEqual(tojson.to_json(var_tuple), json.dumps(var_tuple))
        self.assertEqual(tojson.to_json(var_string), json.dumps(var_string))
        self.assertEqual(tojson.to_json(var_float), json.dumps(var_float))
        self.assertEqual(tojson.to_json(var_tuple_in_dict), json.dumps(var_tuple_in_dict))
        self.assertEqual(tojson.to_json(var_bool), json.dumps(var_bool))
        self.assertEqual(tojson.to_json(var_none), json.dumps(var_none))




if __name__ == '__main__':
    unittest.main()