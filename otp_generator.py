import random
import string

class OTPGenerator:
    def __init__(self, length=6):
        self.length = length

    def generate_otp(self):
        digits = string.digits
        otp = ''
        for _ in range(self.length):
            otp += random.choice(digits)
        return otp

    def format_message(self, otp):
        return f'Your OTP code is: {otp}'

# Example usage:
if __name__ == '__main__':
    otp_gen = OTPGenerator()
    otp = otp_gen.generate_otp()
    message = otp_gen.format_message(otp)
    print(message)