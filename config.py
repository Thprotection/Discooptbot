import os

class Config:
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///:memory:')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    API_KEY = os.getenv('API_KEY', 'your-api-key')
    OTHER_CONFIG = os.getenv('OTHER_CONFIG', 'default-value')
