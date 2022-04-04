import unittest
from main import *

class TestGetFeature(unittest.TestCase):
    def get_feature_test(self):
        self.assertEqual(GeojsonFeatureCollection.get_feature(), int)

if __name__ == "__main__":
    unittest.main()