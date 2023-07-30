import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent.parent.parent.resolve()
LOG_DIR = BASE_DIR / "logs"
DEBUG = bool(os.environ.get("DEBUG", False))

DB_URI = os.environ.get("DB_URI", "")

AIOGRAM_TOKEN = os.environ.get("AIOGRAM_TOKEN", "")
GITLAB_APP_ID = os.environ.get("GITLAB_APP_ID", "")
GITLAB_APP_SECRET = os.environ.get("GITLAB_APP_SECRET", "")
