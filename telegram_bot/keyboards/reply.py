from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_language_keyboard():
    keyboard = [
        [
            KeyboardButton(text="Қазақша"),
            KeyboardButton(text="Русский"),
            KeyboardButton(text="English"),
        ]
    ]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )


def get_main_menu(lang="ru"):

    texts = {
        "ru": {
            "recognize": "🔎 Распознать минерал",
            "history": "📜 История",
            "about": "🏛 О музее",
            "site": "🌐 Открыть сайт",
            "language": "⚙️ Сменить язык",
            "help": "🆘 Помощь",
        },

        "kk": {
            "recognize": "🔎 Минералды тану",
            "history": "📜 Тарих",
            "about": "🏛 Музей туралы",
            "site": "🌐 Сайтты ашу",
            "language": "⚙️ Тілді өзгерту",
            "help": "🆘 Көмек",
        },

        "en": {
            "recognize": "🔎 Recognize mineral",
            "history": "📜 History",
            "about": "🏛 About museum",
            "site": "🌐 Open website",
            "language": "⚙️ Change language",
            "help": "🆘 Help",
        }
    }

    t = texts.get(lang, texts["ru"])

    keyboard = [
        [
            KeyboardButton(text=t["recognize"])
        ],
        [
            KeyboardButton(text=t["history"]),
            KeyboardButton(text=t["about"]),
        ],
        [
            KeyboardButton(text=t["site"]),
            KeyboardButton(text=t["language"]),
        ],
        [
            KeyboardButton(text=t["help"]),
        ]
    ]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )