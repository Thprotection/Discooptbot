import unittest
from database_manager import DatabaseManager

class TestDatabaseManager(unittest.TestCase):

    def setUp(self):
        """Set up a temporary database for testing."""
        self.db_manager = DatabaseManager()
        self.db_manager.setup_database()  # method to set up the temporary database

    def tearDown(self):
        """Tear down the temporary database after tests."""
        self.db_manager.teardown_database()  # method to tear down the temporary database

    def test_insert_record(self):
        """Test inserting a record into the database."""
        result = self.db_manager.insert_record({'name': 'Test', 'value': 123})
        self.assertTrue(result)

    def test_fetch_record(self):
        """Test fetching a record from the database."""
        self.db_manager.insert_record({'name': 'Test', 'value': 123})
        record = self.db_manager.fetch_record('Test')
        self.assertEqual(record['value'], 123)

    def test_update_record(self):
        """Test updating a record in the database."""
        self.db_manager.insert_record({'name': 'Test', 'value': 123})
        self.db_manager.update_record('Test', {'value': 456})
        record = self.db_manager.fetch_record('Test')
        self.assertEqual(record['value'], 456)

    def test_delete_record(self):
        """Test deleting a record from the database."""
        self.db_manager.insert_record({'name': 'Test', 'value': 123})
        self.db_manager.delete_record('Test')
        record = self.db_manager.fetch_record('Test')
        self.assertIsNone(record)

if __name__ == '__main__':
    unittest.main()