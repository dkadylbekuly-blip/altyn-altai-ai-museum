import json
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
HISTORY_PATH = BASE_DIR / "data" / "history.json"


def load_history():
    if not HISTORY_PATH.exists():
        return {}

    with open(HISTORY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_history(data):
    HISTORY_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(HISTORY_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def add_history(user_id: int, result: dict, image_path: str):
    data = load_history()
    user_key = str(user_id)

    if user_key not in data:
        data[user_key] = []

    data[user_key].insert(0, {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "name": result.get("name"),
        "confidence": round(result.get("confidence", 0), 2),
        "image_path": image_path,
        "top3": result.get("top3", [])
    })

    data[user_key] = data[user_key][:20]
    save_history(data)


def get_user_history(user_id: int):
    data = load_history()
    return data.get(str(user_id), [])


def clear_user_history(user_id: int):
    data = load_history()
    user_key = str(user_id)

    if user_key in data:
        data[user_key] = []

    save_history(data)