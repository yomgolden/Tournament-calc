"""
/start command
"""

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from database.storage import upsert_user

router = Router()


@router.message(CommandStart())
async def start(message: Message):

    # Save or update user
    await upsert_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username
    )

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
        "<b>🏆 Tournament Manager</b>\n\n"
        "Welcome to Tournament Manager.\n\n"
        "Create and manage Battle Royale tournaments directly from Telegram.\n\n"
        "Choose an option below."
    )

    await message.answer(
        text=text,
        reply_markup=keyboard
    )
