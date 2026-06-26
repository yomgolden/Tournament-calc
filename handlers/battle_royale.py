from aiogram import Router, F
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from services.state_service import state

router = Router()


@router.callback_query(F.data == "create_tournament")
async def create_tournament(callback: CallbackQuery):

    user_id = callback.from_user.id

    state.create(user_id)

    state.set_step(user_id, "tournament_name")

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="❌ Cancel",
                    callback_data="cancel"
                )
            ]
        ]
    )

    text = (
        "🏆 <b>Tournament Setup</b>\n\n"

        "Step 1 / 5\n\n"

        "Please enter the tournament name."
    )

    await callback.message.edit_text(
        text=text,
        parse_mode="HTML",
        reply_markup=keyboard
    )

    await callback.answer()
