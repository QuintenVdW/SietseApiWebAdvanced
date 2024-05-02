# config.py

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Settings:
    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")