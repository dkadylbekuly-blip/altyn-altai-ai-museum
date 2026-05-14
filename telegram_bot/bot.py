import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from bot_config import BOT_TOKEN, SITE_URL
from data.text import TEXTS
from keyboards.reply import get_main_menu, get_language_keyboard
from keyboards.inline import result_buttons, history_buttons
from services.user_language import get_user_language, set_user_language
from services.mineral_lookup import get_mineral_card
from services.mineral_formatter import format_recognition_result
from services.history import add_history, get_user_history, clear_user_history
from ml.predict import predict_image
from services.site_api import send_recognition_to_site


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def t(lang: str, key: str) -> str:
    return TEXTS.get(lang, TEXTS["ru"]).get(key, TEXTS["ru"].get(key, key))


@dp.message(CommandStart())
async def cmd_start(message: Message):
    lang = get_user_language(message.from_user.id)

    await message.answer(
        t(lang, "choose_language"),
        reply_markup=get_language_keyboard()
    )


@dp.message(F.text.in_(["Қазақша", "Русский", "English"]))
async def choose_language(message: Message):
    if message.text == "Қазақша":
        lang = "kk"
    elif message.text == "English":
        lang = "en"
    else:
        lang = "ru"

    set_user_language(message.from_user.id, lang)

    await message.answer(
        t(lang, "language_changed"),
        reply_markup=get_main_menu(lang)
    )

    await message.answer(
        t(lang, "welcome"),
        reply_markup=get_main_menu(lang)
    )


@dp.message(F.photo)
async def handle_photo(message: Message):
    lang = get_user_language(message.from_user.id)
    status = await message.answer(t(lang, "recognizing"))

    try:
        photo = message.photo[-1]
        file = await bot.get_file(photo.file_id)

        file_path = f"telegram_bot/uploads/{photo.file_unique_id}.jpg"
        await bot.download_file(file.file_path, file_path)

        result = predict_image(file_path)

        add_history(
            user_id=message.from_user.id,
            result=result,
            image_path=file_path
        )
        
        send_recognition_to_site(
            user_id=message.from_user.id,
            result=result,
            image_path=file_path
        )

        card = get_mineral_card(result["name"], lang)

        answer = format_recognition_result(
            result=result,
            card=card,
            lang=lang
        )

        await status.delete()

        await message.answer(
            answer,
            reply_markup=result_buttons(SITE_URL, lang),
            parse_mode="HTML"
        )

    except Exception as e:
        await status.delete()

        await message.answer(
            f"❌ Error:\n{e}",
            reply_markup=get_main_menu(lang)
        )


@dp.callback_query(F.data == "recognize_again")
async def recognize_again(callback: CallbackQuery):
    lang = get_user_language(callback.from_user.id)

    await callback.message.answer(
        t(lang, "send_photo"),
        reply_markup=get_main_menu(lang)
    )

    await callback.answer()


@dp.callback_query(F.data == "clear_history")
async def clear_history_callback(callback: CallbackQuery):
    lang = get_user_language(callback.from_user.id)

    clear_user_history(callback.from_user.id)

    texts = {
        "ru": "🗑 История очищена.",
        "kk": "🗑 Тарих тазаланды.",
        "en": "🗑 History cleared.",
    }

    await callback.message.answer(
        texts.get(lang, texts["ru"]),
        reply_markup=get_main_menu(lang)
    )

    await callback.answer()


@dp.message(F.text)
async def menu_handler(message: Message):
    lang = get_user_language(message.from_user.id)
    text = message.text

    recognize_buttons = [
        "🔎 Распознать минерал",
        "🔎 Минералды тану",
        "🔎 Recognize mineral",
    ]

    history_buttons_text = [
        "📜 История",
        "📜 Тарих",
        "📜 History",
    ]

    about_buttons = [
        "🏛 О музее",
        "🏛 Музей туралы",
        "🏛 About museum",
    ]

    site_buttons = [
        "🌐 Открыть сайт",
        "🌐 Сайтты ашу",
        "🌐 Open website",
    ]

    language_buttons = [
        "⚙️ Сменить язык",
        "⚙️ Тілді өзгерту",
        "⚙️ Change language",
    ]

    help_buttons = [
        "🆘 Помощь",
        "🆘 Көмек",
        "🆘 Help",
    ]

    if text in recognize_buttons:
        await message.answer(
            t(lang, "send_photo"),
            reply_markup=get_main_menu(lang)
        )
        return

    if text in history_buttons_text:
        user_history = get_user_history(message.from_user.id)

        if not user_history:
            await message.answer(
                t(lang, "history_empty"),
                reply_markup=get_main_menu(lang)
            )
            return

        titles = {
            "ru": "📜 <b>История распознаваний:</b>",
            "kk": "📜 <b>Тану тарихы:</b>",
            "en": "📜 <b>Recognition history:</b>",
        }

        default_desc = {
            "ru": "Описание пока отсутствует.",
            "kk": "Сипаттама әзірге жоқ.",
            "en": "Description is not available yet.",
        }

        lines = [titles.get(lang, titles["ru"]), ""]

        for i, item in enumerate(user_history[:10], start=1):
            name = item.get("name") or item.get("mineral") or item.get("result") or "Unknown"
            confidence = item.get("confidence", 0)

            card = get_mineral_card(name, lang)
            description = card.get("description", default_desc.get(lang, default_desc["ru"]))

            if len(description) > 180:
                description = description[:180].rstrip() + "..."

            lines.append(
                f"{i}) <b>{name}</b> — {confidence}%\n"
                f"   📖 {description}"
            )

        await message.answer(
            "\n\n".join(lines),
            reply_markup=history_buttons(lang),
            parse_mode="HTML"
        )
        return

    if text in about_buttons:
        await message.answer(
            t(lang, "about"),
            reply_markup=get_main_menu(lang),
            parse_mode="HTML"
        )
        return

    if text in site_buttons:
        await message.answer(
            f"{t(lang, 'open_site')}: {SITE_URL}",
            reply_markup=get_main_menu(lang)
        )
        return

    if text in language_buttons:
        await message.answer(
            t(lang, "choose_language"),
            reply_markup=get_language_keyboard()
        )
        return

    if text in help_buttons:
        await message.answer(
            t(lang, "help"),
            reply_markup=get_main_menu(lang),
            parse_mode="HTML"
        )
        return

    await message.answer(
        t(lang, "unknown"),
        reply_markup=get_main_menu(lang)
    )


async def main():
    print("Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())