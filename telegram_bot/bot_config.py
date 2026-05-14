import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

BOT_TOKEN = os.getenv("BOT_TOKEN")
SITE_URL = os.getenv("SITE_URL", "http://127.0.0.1:8000")
BOT_NAME = os.getenv("BOT_NAME", "Altyn Altai Mineral Bot")

UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

ML_DIR = BASE_DIR / "ml"
MODEL_PATH = ML_DIR / "model.pth"
CLASS_NAMES_PATH = ML_DIR / "class_names.json"

DATA_DIR = BASE_DIR / "data"
HISTORY_PATH = DATA_DIR / "history.json"
LANG_PATH = DATA_DIR / "user_languages.json"