import sqlite3
import logging
from typing import Optional, Dict, Any
from config import Config

logger = logging.getLogger(__name__)

class Database:
    """Database management for DiscoOTPbot"""
    
    def __init__(self, db_file: str = Config.DB_FILE):
        self.db_file = db_file
        self.init_db()
    
    def get_connection(self) -> sqlite3.Connection:
        """Get database connection"""
        conn = sqlite3.connect(self.db_file)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_db(self) -> None:
        """Initialize database schema"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    phone TEXT,
                    subscribed BOOLEAN DEFAULT 0,
                    sub_expires REAL DEFAULT 0,
                    card_issuer TEXT DEFAULT NULL,
                    sms_enabled BOOLEAN DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
            conn.close()
            logger.info("Database initialized successfully")
        except Exception as e:
            logger.error(f"Database initialization error: {str(e)}")
            raise
    
    def get_user(self, user_id: int) -> Dict[str, Any]:
        """Get user data"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT phone, subscribed, sub_expires, card_issuer, sms_enabled FROM users WHERE user_id = ?",
                (user_id,)
            )
            row = cursor.fetchone()
            conn.close()
            
            if row:
                return {
                    "phone": row[0],
                    "subscribed": bool(row[1]),
                    "sub_expires": row[2],
                    "card_issuer": row[3],
                    "sms_enabled": bool(row[4])
                }
            return {
                "phone": None,
                "subscribed": False,
                "sub_expires": 0,
                "card_issuer": None,
                "sms_enabled": False
            }
        except Exception as e:
            logger.error(f"Error fetching user {user_id}: {str(e)}")
            return {}
    
    def save_user(
        self,
        user_id: int,
        phone: Optional[str] = None,
        subscribed: Optional[bool] = None,
        sub_expires: Optional[float] = None,
        card_issuer: Optional[str] = None,
        sms_enabled: Optional[bool] = None
    ) -> bool:
        """Save or update user data"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute("SELECT 1 FROM users WHERE user_id = ?", (user_id,))
            exists = cursor.fetchone()
            
            if exists:
                updates, params = [], []
                if phone is not None:
                    updates.append("phone = ?")
                    params.append(phone)
                if subscribed is not None:
                    updates.append("subscribed = ?")
                    params.append(1 if subscribed else 0)
                if sub_expires is not None:
                    updates.append("sub_expires = ?")
                    params.append(sub_expires)
                if card_issuer is not None:
                    updates.append("card_issuer = ?")
                    params.append(card_issuer)
                if sms_enabled is not None:
                    updates.append("sms_enabled = ?")
                    params.append(1 if sms_enabled else 0)
                
                if updates:
                    updates.append("updated_at = CURRENT_TIMESTAMP")
                    query = f"UPDATE users SET {', '.join(updates)} WHERE user_id = ?"
                    params.append(user_id)
                    cursor.execute(query, params)
            else:
                cursor.execute('''
                    INSERT INTO users (user_id, phone, subscribed, sub_expires, card_issuer, sms_enabled)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    user_id,
                    phone,
                    1 if subscribed else 0,
                    sub_expires or 0,
                    card_issuer,
                    1 if sms_enabled else 0
                ))
            
            conn.commit()
            conn.close()
            logger.info(f"User {user_id} saved successfully")
            return True
        except Exception as e:
            logger.error(f"Error saving user {user_id}: {str(e)}")
            return False