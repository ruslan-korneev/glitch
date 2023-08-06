import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# General
BASE_DIR = Path(__file__).parent.parent.parent.resolve()
SECRET_KEY = os.environ.get("SECRET_KEY", "insecure")
LOG_DIR = BASE_DIR / "logs"
DEBUG = bool(os.environ.get("DEBUG", False))

# API
PROJECT_NAME = os.environ.get("PROJECT_NAME", "glitch")
API_V1_STR = os.environ.get("API_V1_STR", "/api/v1")
BACKEND_CORS_ORIGINS = os.environ.get("CORS_ORIGINS")
BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:5000")

# Database
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

# Redis
REDIS_HOST = os.environ.get("REDIS_HOST", "127.0.0.1")
REDIS_PORT = int(os.environ.get("REDIS_PORT", "6379"))
REDIS_DB = int(os.environ.get("REDIS_DB", "0"))

# Telegram
AIOGRAM_TOKEN = os.environ.get("AIOGRAM_TOKEN", "")

# Gitlab

GITLAB_HOST = os.environ.get("GITLAB_HOST", "gitlab.com")
GITLAB_APP_ID = os.environ.get("GITLAB_APP_ID", "")
GITLAB_APP_SECRET = os.environ.get("GITLAB_APP_SECRET", "")
GITLAB_AUTH_URL = (
    f"https://{GITLAB_HOST}"
    f"/oauth/authorize?client_id={GITLAB_APP_ID}"
    "&response_type=code&state={state}"
    f"&redirect_uri={BACKEND_URL}/api/v1/gitlab/callback"
)
