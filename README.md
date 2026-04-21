# DiscoOTPbot 🔐

A powerful Telegram bot for OTP (One-Time Password) code generation and delivery with multi-card support and flexible payment options.

## Overview

DiscoOTPbot is a Telegram bot application that generates and delivers one-time passwords (OTPs) for various payment card issuers including Discover, Best Buy, Chase, American Express, Visa, and Mastercard. The bot supports multiple subscription payment methods including Telegram Stars, USDT cryptocurrency, and Bitcoin.

## Features

### Card Support
- **Discover Card**
- **Best Buy Credit Card**
- **Chase**
- **American Express (Amex)**
- **Visa**
- **Mastercard**

### Payment Options
- 💫 Telegram Stars (499 XTR/month)
- 💰 USDT Cryptocurrency (5.00 USDT/month)
- ₿ Bitcoin (0.0003 BTC/month)

### Core Features
- ✅ Multi-card OTP generation
- ✅ Phone number management
- ✅ Premium subscription system
- ✅ Real SMS delivery via Twilio
- ✅ In-chat OTP display
- ✅ Webhook-based Telegram integration
- ✅ Crypto Pay integration
- ✅ SQLite database for user persistence

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- Twilio Account (optional, for SMS delivery)
- Crypto Pay API Token (for crypto payments)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Thprotection/Discooptbot.git
cd Discooptbot
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
cp .env.example .env
```

Edit `.env` and add your API credentials:
```env
TELEGRAM_TOKEN=your_telegram_token_here
CRYPTO_PAY_TOKEN=your_crypto_pay_token_here
TWILIO_ACCOUNT_SID=your_twilio_account_sid_here
TWILIO_AUTH_TOKEN=your_twilio_auth_token_here
TWILIO_PHONE_NUMBER=your_twilio_phone_number_here
PORT=5000
RENDER_EXTERNAL_URL=https://your-app.onrender.com
```

### 5. Initialize Database
```bash
python -c "from disco_otp_bot_full import init_db; init_db()"
```

### 6. Run the Bot
```bash
python disco_otp_bot_full.py
```

## Bot Commands

| Command | Description |
|---------|-------------|
| `/start` | Show main menu and available commands |
| `/help` | Display help information |
| `/discover` | Select Discover Card |
| `/bestbuy` | Select Best Buy Credit Card |
| `/chase` | Select Chase Card |
| `/amex` | Select American Express |
| `/visa` | Select Visa Card |
| `/mastercard` | Select Mastercard |
| `/phone` | Set phone number for OTP delivery |
| `/code` | Request OTP code (premium required) |
| `/subscribe` | Subscribe via Telegram Stars |
| `/subscribe_crypto` | Subscribe via USDT |
| `/subscribe_crypto_btc` | Subscribe via Bitcoin |
| `/sms enable` | Enable real SMS delivery |
| `/sms disable` | Disable real SMS (in-chat only) |
| `/pin_demo` | Show carousel demo |

## Usage

1. **Start the Bot**: Send `/start` to @DiscoOTPbot
2. **Select Card**: Use `/discover`, `/visa`, etc. to choose a card
3. **Set Phone**: Use `/phone` and enter your phone number
4. **Subscribe**: Choose a payment method and subscribe
5. **Get OTP**: Use `/code` to generate and receive OTP

## Configuration

### Environment Variables

- `TELEGRAM_TOKEN` - Your Telegram bot token from BotFather
- `CRYPTO_PAY_TOKEN` - API token for Crypto Pay
- `TWILIO_ACCOUNT_SID` - Twilio account SID
- `TWILIO_AUTH_TOKEN` - Twilio authentication token
- `TWILIO_PHONE_NUMBER` - Twilio phone number for SMS
- `PORT` - Server port (default: 5000)
- `RENDER_EXTERNAL_URL` - External URL for webhooks

### Database

The bot uses SQLite database stored at `/data/discootp.db`. The database schema includes:

- `user_id` (INTEGER PRIMARY KEY)
- `phone` (TEXT)
- `subscribed` (BOOLEAN)
- `sub_expires` (REAL) - Unix timestamp
- `card_issuer` (TEXT)
- `sms_enabled` (BOOLEAN)

## Deployment

### Heroku/Render

1. Push code to GitHub
2. Connect GitHub repo to Heroku/Render
3. Set environment variables in deployment dashboard
4. Configure Procfile (already included)
5. Deploy

### Docker

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "disco_otp_bot_full:app"]
```

Build and run:
```bash
docker build -t discootp .
docker run -p 5000:5000 --env-file .env discootp
```

## Project Structure

```
Discooptbot/
├── disco_otp_bot_full.py      # Main application
├── requirements.txt            # Python dependencies
├── Procfile                    # Deployment configuration
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
├── README.md                  # This file
├── tests/                     # Test suite
│   ├── test_bot.py
│   ├── test_database.py
│   └── test_payments.py
├── config/                    # Configuration modules
│   └── settings.py
└── docs/                      # Documentation
    └── API.md
```

## Dependencies

- **pyTelegramBotAPI** - Telegram bot framework
- **flask** - Web framework for webhooks
- **requests** - HTTP client
- **gunicorn** - WSGI HTTP server
- **twilio** - SMS delivery service

## Security Considerations

⚠️ **IMPORTANT SECURITY NOTES:**

1. **Never commit `.env` files** - Use `.env.example` as template
2. **Rotate API tokens regularly** - Invalidate exposed credentials immediately
3. **Use environment variables only** - Never hardcode secrets in source code
4. **Enable 2FA** - Secure your Telegram and Twilio accounts
5. **Validate user input** - Sanitize phone numbers and other inputs
6. **Use HTTPS** - Ensure all webhooks use secure connections
7. **Monitor logs** - Watch for suspicious activity

## Logging

The application logs to console. For production, consider using:
- Sentry for error tracking
- CloudWatch for AWS deployments
- Stackdriver for Google Cloud

## Testing

Run tests with pytest:

```bash
pip install pytest pytest-cov
pytest tests/ -v --cov=disco_otp_bot_full
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is provided as-is for educational purposes.

## Support

For issues and questions:
- Open an issue on GitHub
- Contact via Telegram: @Thprotection

## Disclaimer

This bot is for educational purposes only. Users are responsible for complying with Telegram's Terms of Service and all applicable laws and regulations. Unauthorized use of OTP codes or impersonation is illegal.

## Changelog

### Version 1.0.0 (2026-04-21)
- Initial release
- Multi-card OTP support
- Crypto and Stars payment integration
- Real SMS delivery via Twilio
