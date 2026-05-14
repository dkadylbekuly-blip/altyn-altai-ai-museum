from copy import deepcopy

try:
    from telegram_bot.data.mineral_aliases import ALIAS_TO_CANONICAL
    from telegram_bot.data.minerals import MINERALS
    from telegram_bot.data.mineral_info import MINERAL_INFO
except ModuleNotFoundError:
    from data.mineral_aliases import ALIAS_TO_CANONICAL
    from data.minerals import MINERALS
    from data.mineral_info import MINERAL_INFO


def normalize_key(name: str) -> str:
    if not name:
        return ""

    return (
        name.strip()
        .lower()
        .replace(" ", "")
        .replace("-", "")
        .replace("_", "")
    )


def merge_language_card(base: dict | None, extra: dict | None) -> dict:
    result = deepcopy(base or {})

    if extra:
        for key in ["origin", "uses", "deposits", "interesting_facts"]:
            if key in extra and extra[key]:
                result[key] = extra[key]

    return result


def make_fallback_card(raw_name: str, lang: str = "ru") -> dict:
    fallback = {
        "ru": {
            "title": raw_name,
            "type": "Минерал",
            "color": "—",
            "formula": "—",
            "luster": "—",
            "hardness": "—",
            "cleavage": "—",
            "fracture": "—",
            "crystal_system": "—",
            "description": "Информация об этом минерале пока не добавлена.",
            "origin": "—",
            "uses": "—",
            "deposits": ["—"],
            "interesting_facts": ["—"],
        },
        "kk": {
            "title": raw_name,
            "type": "Минерал",
            "color": "—",
            "formula": "—",
            "luster": "—",
            "hardness": "—",
            "cleavage": "—",
            "fracture": "—",
            "crystal_system": "—",
            "description": "Бұл минерал туралы ақпарат әлі қосылмаған.",
            "origin": "—",
            "uses": "—",
            "deposits": ["—"],
            "interesting_facts": ["—"],
        },
        "en": {
            "title": raw_name,
            "type": "Mineral",
            "color": "—",
            "formula": "—",
            "luster": "—",
            "hardness": "—",
            "cleavage": "—",
            "fracture": "—",
            "crystal_system": "—",
            "description": "Information about this mineral has not been added yet.",
            "origin": "—",
            "uses": "—",
            "deposits": ["—"],
            "interesting_facts": ["—"],
        },
    }

    return fallback.get(lang, fallback["ru"])


def get_mineral_card(raw_name: str, lang: str = "ru"):
    raw_key = normalize_key(raw_name)
    canonical_key = ALIAS_TO_CANONICAL.get(raw_key, raw_key)

    base_all = MINERALS.get(canonical_key)
    info_all = MINERAL_INFO.get(canonical_key)

    if not base_all and not info_all:
        return make_fallback_card(raw_name, lang)

    base_lang = None
    info_lang = None

    if base_all:
        base_lang = (
            base_all.get(lang)
            or base_all.get("ru")
            or base_all.get("kk")
            or base_all.get("en")
        )

    if info_all:
        info_lang = (
            info_all.get(lang)
            or info_all.get("ru")
            or info_all.get("kk")
            or info_all.get("en")
        )

    card = merge_language_card(base_lang, info_lang)

    if not card:
        return make_fallback_card(raw_name, lang)

    if "title" not in card:
        card["title"] = raw_name

    return card