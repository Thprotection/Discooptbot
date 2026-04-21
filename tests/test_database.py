import unittest
from your_module import get_user, save_user, init_db

class TestDatabaseOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setup code to initialize the database if necessary
        init_db()

    def test_save_user(self):
        user_data = {'username': 'testuser', 'email': 'test@example.com'}
        result = save_user(user_data)
        self.assertTrue(result)

    def test_get_user(self):
        user_data = {'username': 'testuser', 'email': 'test@example.com'}
        save_user(user_data)
        user = get_user('testuser')
        self.assertEqual(user['email'], 'test@example.com')

    @classmethod
    def tearDownClass(cls):
        # Cleanup code to tear down the database if necessary
        pass

if __name__ == '__main__':
    unittest.main()