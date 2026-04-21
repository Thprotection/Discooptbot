import unittest
from otp_generator import generate_otp 

class TestOTPGenerator(unittest.TestCase):
    def test_generate_otp_length(self):
        otp = generate_otp()
        self.assertEqual(len(otp), 6, "OTP should be 6 digits long")

    def test_generate_otp_numeric(self):
        otp = generate_otp()
        self.assertTrue(otp.isdigit(), "OTP should be numeric")

    def test_generate_otp_range(self):
        otp = generate_otp()
        self.assertIn(int(otp), range(100000, 1000000), "OTP should be in the range from 100000 to 999999")

if __name__ == '__main__':
    unittest.main()