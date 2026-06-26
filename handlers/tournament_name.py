from aiogram import Router
from aiogram.types import Message

from services.state_service import state

router = Router()


@router.message()
async def tournament_name(message: Message):

    user_id = message.from_user.id

    if state.get_step(user_id) != "tournament_name":
        return

    tournament_name = message.text.strip()

    state.set_data(
        user_id,
        "name",
        tournament_name
    )

    state.set_step(
        user_id,
        "team_count"
    )

    await message.delete()

    await message.answer(

        "🏆 <b>Tournament Setup</b>\n\n"

        "✅ Tournament Name\n"

        f"{tournament_name}\n\n"

        "Step 2 / 5\n\n"

        "How many teams?\n"

        "<i>Minimum: 2\nMaximum: 100</i>",

        parse_mode="HTML"

    )
