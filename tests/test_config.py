import pytest
import os
from config import Config

class TestConfig:
    """Test configuration management"""
    
    def test_config_has_required_attributes(self):
        """Test Config has required attributes"""
        assert hasattr(Config, 'TELEGRAM_TOKEN')
        assert hasattr(Config, 'CRYPTO_PAY_TOKEN')
        assert hasattr(Config, 'TWILIO_ACCOUNT_SID')
        assert hasattr(Config, 'PORT')
    
    def test_default_port(self):
        """Test default port"""
        assert Config.PORT == 5000 or Config.PORT > 1000
    
    def test_subscription_prices(self):
        """Test subscription prices are set"""
        assert Config.STARS_PRICE > 0
        assert float(Config.USDT_PRICE) > 0
        assert float(Config.BTC_PRICE) > 0
    
    def test_subscription_duration(self):
        """Test subscription duration"""
        assert Config.SUBSCRIPTION_DURATION_DAYS == 30
    
    def test_otp_expiry(self):
        """Test OTP expiry time"""
        assert Config.OTP_EXPIRY_MINUTES == 10