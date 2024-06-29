#!/bin/python3
import unittest
import MySQLdb
import os

class TestDBStorage(unittest.TestCase):
    def setUp(self):
        """Set up database connection before each test"""
        self.db = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        self.cursor = self.db.cursor()

    def tearDown(self):
        """Close database connection after each test"""
        self.cursor.close()
        self.db.close()

    def test_create_state(self):
        """Test creating a new state"""
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]

        create_state('California')

        self.cursor.execute("SELECT COUNT(*) FROM states")
        final_count = self.cursor.fetchone()[0]

        self.assertEqual(final_count, initial_count + 1)

if __name__ == '__main__':
    unittest.main()

