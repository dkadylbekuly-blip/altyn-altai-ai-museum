from aiogram.utils.keyboard import InlineKeyboardBuilder


def result_buttons(site_url: str, lang: str):
    texts = {
        "ru": {
            "again": "🔁 Распознать ещё",
            "site": "🌐 Открыть сайт",
        },
        "kk": {
            "again": "🔁 Тағы тану",
            "site": "🌐 Сайтты ашу",
        },
        "en": {
            "again": "🔁 Recognize again",
            "site": "🌐 Open website",
        }
    }

    t = texts.get(lang, texts["ru"])

    builder = InlineKeyboardBuilder()
    builder.button(text=t["again"], callback_data="recognize_again")
    builder.button(text=t["site"], url=site_url)
    builder.adjust(1)

    return builder.as_markup()


def history_buttons(lang: str):
    texts = {
        "ru": {"clear": "🗑 Очистить историю"},
        "kk": {"clear": "🗑 Тарихты тазалау"},
        "en": {"clear": "🗑 Clear history"},
    }

    t = texts.get(lang, texts["ru"])

    builder = InlineKeyboardBuilder()
    builder.button(text=t["clear"], callback_data="clear_history")
    builder.adjust(1)

    return builder.as_markup()