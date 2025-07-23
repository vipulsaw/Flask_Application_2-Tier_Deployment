import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

class Config:
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'default_user')
    MYSQL_PASSWORD = quote_plus(os.getenv('MYSQL_PASSWORD', 'user@123!'))  # URL-encode password
    MYSQL_DB = os.getenv('MYSQL_DB', 'flask_app_db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
