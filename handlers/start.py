"""
Start Command
"""

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from database.storage import upsert_user
from utils.keyboards import home_keyboard
from utils.formatting import home_text

router = Router()


@router.message(CommandStart())
async def start(message: Message):

    await upsert_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name
    )

    await message.answer(
        text=home_text(),
        reply_markup=home_keyboard()
    )
