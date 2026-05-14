def format_list(items):
    if not items:
        return "—"

    if isinstance(items, str):
        return items

    return "\n".join([f"• {item}" for item in items])


def format_mineral_card(card: dict, lang: str = "ru") -> str:
    title = card.get("title", "Unknown")

    labels = {
        "ru": {
            "type": "Тип",
            "color": "Цвет",
            "formula": "Формула",
            "luster": "Блеск",
            "hardness": "Твёрдость",
            "cleavage": "Спайность",
            "fracture": "Излом",
            "crystal_system": "Сингония",
            "description": "Описание",
            "origin": "Происхождение",
            "uses": "Применение",
            "deposits": "Месторождения",
            "facts": "Интересные факты",
        },
        "kk": {
            "type": "Түрі",
            "color": "Түсі",
            "formula": "Формуласы",
            "luster": "Жылтыры",
            "hardness": "Қаттылығы",
            "cleavage": "Жымдастығы",
            "fracture": "Сынығы",
            "crystal_system": "Сингониясы",
            "description": "Сипаттамасы",
            "origin": "Шығу тегі",
            "uses": "Қолданылуы",
            "deposits": "Кен орындары",
            "facts": "Қызықты деректер",
        },
        "en": {
            "type": "Type",
            "color": "Color",
            "formula": "Formula",
            "luster": "Luster",
            "hardness": "Hardness",
            "cleavage": "Cleavage",
            "fracture": "Fracture",
            "crystal_system": "Crystal system",
            "description": "Description",
            "origin": "Origin",
            "uses": "Uses",
            "deposits": "Deposits",
            "facts": "Interesting facts",
        }
    }

    t = labels.get(lang, labels["ru"])

    text = f"🪨 <b>{title}</b>\n\n"

    fields = [
        ("type", "🧩"),
        ("color", "🎨"),
        ("formula", "🧪"),
        ("luster", "✨"),
        ("hardness", "📏"),
        ("cleavage", "🪓"),
        ("fracture", "💥"),
        ("crystal_system", "🔷"),
        ("description", "📖"),
        ("origin", "🌍"),
        ("uses", "🏭"),
        ("deposits", "⛏"),
        ("interesting_facts", "💡"),
    ]

    for field, emoji in fields:
        value = card.get(field)

        if not value:
            continue

        if field in ["deposits", "interesting_facts"]:
            value = format_list(value)

        label_key = field

        if field == "interesting_facts":
            label_key = "facts"

        text += f"{emoji} <b>{t[label_key]}:</b>\n{value}\n\n"

    return text.strip()

def format_recognition_result(result: dict, card: dict | None, lang: str = "ru") -> str:
    if card is None:
        card = {}

    title = card.get("title", result.get("name", "Unknown"))
    card["title"] = title

    top3 = result.get("top3", [])
    top3_text = "\n".join(
        f"{i}) {item['name']} — {item['confidence']:.2f}%"
        for i, item in enumerate(top3, 1)
    )

    headers = {
        "ru": {
            "title": "🔎 Результат распознавания",
            "main": "🪨 Основной вариант",
            "confidence": "📊 Уверенность",
            "top3": "📌 Top-3 предположения",
        },
        "kk": {
            "title": "🔎 Тану нәтижесі",
            "main": "🪨 Негізгі нұсқа",
            "confidence": "📊 Сенімділік",
            "top3": "📌 Top-3 болжам",
        },
        "en": {
            "title": "🔎 Recognition result",
            "main": "🪨 Main result",
            "confidence": "📊 Confidence",
            "top3": "📌 Top-3 predictions",
        },
    }

    h = headers.get(lang, headers["ru"])

    result_text = (
        f"{h['title']}\n\n"
        f"{h['main']}: {result.get('name', 'Unknown')}\n"
        f"{h['confidence']}: {result.get('confidence', 0):.2f}%\n\n"
        f"{h['top3']}:\n{top3_text}\n\n"
    )

    return result_text + format_mineral_card(card, lang)