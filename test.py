import unittest
from main import *

class TestGetFeature(unittest.TestCase):
    def get_feature_test(self):
        self.assertEqual(GeojsonFeatureCollection.get_feature("01"), "01")

# def add(num):
#     return num + 2

# class TestAdd(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(2), 5)

if __name__ == "__main__":
    unittest.main()