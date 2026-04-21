import unittest

class TestPaymentHandler(unittest.TestCase):

    def test_process_payment_success(self):
        # Example test for a successful payment
        amount = 100
        payment_method = 'credit_card'
        response = process_payment(amount, payment_method)
        self.assertEqual(response['status'], 'success')
        self.assertEqual(response['amount'], amount)

    def test_process_payment_failure(self):
        # Example test for a failed payment
        amount = 100
        payment_method = 'invalid_method'
        response = process_payment(amount, payment_method)
        self.assertEqual(response['status'], 'failure')
        self.assertIn('error', response)

    def test_process_payment_insufficient_funds(self):
        # Example test for insufficient funds
        amount = 1000
        payment_method = 'credit_card'
        response = process_payment(amount, payment_method)
        self.assertEqual(response['status'], 'failure')
        self.assertIn('error', response)

if __name__ == '__main__':
    unittest.main()