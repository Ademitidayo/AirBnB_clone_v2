#!/bin/python3
import unittest
import os

class TestSomeFeature(unittest.TestCase):
    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "Test only for DB storage")
    def test_some_db_feature(self):
        """Test something only for DB storage"""
        pass

if __name__ == '__main__':
    unittest.main()
