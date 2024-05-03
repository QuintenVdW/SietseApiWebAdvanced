import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
cors_origins = os.environ.get("ALLOWED_ORIGINS", "*")
documentation_url = os.environ.get("DOCS_URL", None)