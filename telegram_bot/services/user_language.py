import json
from bot_config import LANG_PATH


def _load():
    if not LANG_PATH.exists():
        return {}
    try:
        with open(LANG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def _save(data):
    LANG_PATH.parent.mkdir(exist_ok=True)
    with open(LANG_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_user_language(user_id: int) -> str:
    data = _load()
    return data.get(str(user_id), "ru")


def set_user_language(user_id: int, lang: str):
    data = _load()
    data[str(user_id)] = lang
    _save(data)