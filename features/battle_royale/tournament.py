"""
Battle Royale Tournament Wizard
"""

from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.fsm.context import FSMContext

from wizard.session import CreateTournament
from wizard.validators import (
    validate_tournament_name,
    validate_num_teams,
    validate_team_name,
    validate_positive_int
)

from wizard.engine import (
    build_team_entry_text
)

from wizard.builder import (
    build_ranking_table,
    format_ranking_preview
)

from database.storage import (
    create_tournament,
    insert_teams,
    insert_rankings
)

from config import DEFAULT_KILL_POINTS


# ============================================================
# START
# ============================================================

async def start(
    callback: CallbackQuery,
    state: FSMContext
):

    await state.clear()

    await state.set_state(
        CreateTournament.name
    )

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

    await callback.message.edit_text(

        "<b>🏆 Tournament Setup</b>\n\n"

        "Step 1 / 5\n\n"

        "Enter Tournament Name.",

        reply_markup=keyboard

    )

    await callback.answer()


# ============================================================
# TOURNAMENT NAME
# ============================================================

async def handle_name(
    message: Message,
    state: FSMContext
):

    valid, error = validate_tournament_name(
        message.text
    )

    if not valid:

        await message.reply(error)

        return

    await state.update_data(
        name=message.text.strip()
    )

    await state.set_state(
        CreateTournament.num_teams
    )

    await message.delete()

    await message.answer(

        "<b>🏆 Tournament Setup</b>\n\n"

        "✅ Tournament Name\n"

        f"{message.text}\n\n"

        "Step 2 / 5\n\n"

        "How many teams?\n\n"

        "Minimum: 2\n"

        "Maximum: 100"

    )


# ============================================================
# NUMBER OF TEAMS
# ============================================================

async def handle_team_count(
    message: Message,
    state: FSMContext
):

    valid, error = validate_num_teams(
        message.text
    )

    if not valid:

        await message.reply(error)

        return

    teams = int(message.text)

    await state.update_data(

        num_teams=teams,

        teams=[]

    )

    await state.set_state(
        CreateTournament.entering_teams
    )

    await message.delete()

    await message.answer(

        build_team_entry_text(

            [],

            1,

            teams

        )

    )
