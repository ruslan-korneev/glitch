import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent.parent.parent.resolve()

AIOGRAM_TOKEN = os.environ["AIOGRAM_TOKEN"]
GITLAB_APP_ID = os.environ["GITLAB_APP_ID"]
GITLAB_APP_SECRET = os.environ["GITLAB_APP_SECRET"]
