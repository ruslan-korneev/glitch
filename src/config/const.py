import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent.parent.parent.resolve()
LOG_DIR = BASE_DIR / "logs"
DEBUG = bool(os.environ.get("DEBUG", False))

POSTGRES_DB = os.environ.get("POSTGRES_DB", "glitch-db")
POSTGRES_USER = os.environ.get("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "postgres")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "127.0.0.1")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT", "5432")

DB_URI = (
    "postgresql+asyncpg://"
    f"{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
    f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

AIOGRAM_TOKEN = os.environ.get("AIOGRAM_TOKEN", "")
GITLAB_APP_ID = os.environ.get("GITLAB_APP_ID", "")
GITLAB_APP_SECRET = os.environ.get("GITLAB_APP_SECRET", "")
