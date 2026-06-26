from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

router = Router()


@router.message(CommandStart())
async def start(message: Message):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📂 My Tournaments",
                    callback_data="my_tournaments"
                )
            ],
            [
                InlineKeyboardButton(
                    text="➕ Create Tournament",
                    callback_data="create_tournament"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⚙️ Settings",
                    callback_data="settings"
                ),
                InlineKeyboardButton(
                    text="❓ Help",
                    callback_data="help"
                )
            ]
        ]
    )

    text = (
        "🏆 <b>Tournament Manager</b>\n\n"
        "Welcome!\n\n"
        "Manage Battle Royale tournaments directly from Telegram.\n\n"
        "Choose an option below."
    )

    await message.answer(
        text,
        parse_mode="HTML",
        reply_markup=keyboard
    )
