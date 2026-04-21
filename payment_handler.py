import logging
import requests
from typing import Tuple
from config import Config

logger = logging.getLogger(__name__)

class PaymentHandler:
    """Handle payment processing via Twilio and Crypto Pay"""
    
    @staticmethod
    def send_sms_via_twilio(phone: str, message: str) -> Tuple[bool, str]:
        """Send SMS via Twilio"""
        if not all([
            Config.TWILIO_ACCOUNT_SID,
            Config.TWILIO_AUTH_TOKEN,
            Config.TWILIO_PHONE_NUMBER
        ]):
            logger.warning("SMS gateway not configured")
            return False, "SMS gateway not configured."
        
        try:
            from twilio.rest import Client
            client = Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)
            msg = client.messages.create(
                body=message,
                from_=Config.TWILIO_PHONE_NUMBER,
                to=phone
            )
            logger.info(f"SMS sent to {phone} (SID: {msg.sid})")
            return True, f"SMS sent (SID: {msg.sid})"
        except Exception as e:
            logger.error(f"SMS failed for {phone}: {str(e)}")
            return False, f"SMS failed: {str(e)}"
    
    @staticmethod
    def create_crypto_invoice(
        user_id: int,
        asset: str = "USDT",
        amount: str = "5.00"
    ) -> Tuple[bool, dict]:
        """Create cryptocurrency invoice via Crypto Pay"""
        try:
            payload = {
                "asset": asset,
                "amount": amount,
                "description": f"DiscoOTPbot Premium Monthly ({asset})",
                "payload": f"user_{user_id}",
                "paid_btn_name": "open_app",
                "paid_btn_url": "https://t.me/DiscoOTPbot"
            }
            headers = {"Crypto-Pay-API-Token": Config.CRYPTO_PAY_TOKEN}
            
            response = requests.post(
                "https://pay.crypt.bot/api/createInvoice",
                json=payload,
                headers=headers,
                timeout=10
            )
            
            data = response.json()
            if data.get("ok"):
                logger.info(f"Crypto invoice created for user {user_id}")
                return True, data.get("result", {})
            else:
                logger.error(f"Crypto invoice error: {data}")
                return False, {"error": data.get("error", "Unknown error")}
        except Exception as e:
            logger.error(f"Crypto invoice creation failed: {str(e)}")
            return False, {"error": str(e)}