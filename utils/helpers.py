"""
Common Helper Functions
"""

from aiogram.types import Message
from aiogram.fsm.context import FSMContext


async def delete_user_message(message: Message):
    """
    Delete user message silently.
    """
    try:
        await message.delete()
    except Exception:
        pass


async def edit_setup_message(
    message: Message,
    state: FSMContext,
    text: str,
    reply_markup=None
):
    """
    Edit the setup message instead of
    sending a new one.
    """

    data = await state.get_data()

    setup_message_id = data.get(
        "setup_message_id"
    )

    if setup_message_id:

        await message.bot.edit_message_text(

            chat_id=message.chat.id,

            message_id=setup_message_id,

            text=text,

            reply_markup=reply_markup,

            parse_mode="HTML"

        )

    else:

        sent = await message.answer(
            text=text,
            reply_markup=reply_markup
        )

        await state.update_data(
            setup_message_id=sent.message_id
        )


async def safe_answer(callback):
    """
    Prevent Telegram callback timeout.
    """

    try:
        await callback.answer()
    except Exception:
        pass
