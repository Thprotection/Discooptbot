import unittest
from discooptbot import bot

class TestBotMessageHandlers(unittest.TestCase):

    def setUp(self):
        # Set up the test client or bot instance here
        self.bot = bot.Bot()

    def test_command_process(self):
        # Test a command processing with expected output
        message = '!test_command'
        expected_response = 'Command processed successfully'
        response = self.bot.process_message(message)
        self.assertEqual(response, expected_response)

    def test_message_handler(self):
        # Test the message handler for a specific message type
        message = 'Hello Bot!'
        expected_response = 'Hello User!'
        response = self.bot.handle_message(message)
        self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()