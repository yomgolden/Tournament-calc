"""
Battle Royale Tournament Wizard
"""

from aiogram.types import (
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.fsm.context import FSMContext

from wizard.session import CreateTournament


# ======================================================
# Start Tournament Wizard
# ======================================================

async def start(callback: CallbackQuery, state: FSMContext):

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

    await state.clear()

    await state.set_state(CreateTournament.name)

    await callback.message.edit_text(

        "<b>🏆 Tournament Setup</b>\n\n"

        "Step 1 of 5\n\n"

        "Enter your tournament name.",

        reply_markup=keyboard

    )

    await callback.answer()


# ======================================================
# Back
# ======================================================

async def back(callback: CallbackQuery, state: FSMContext):

    current = await state.get_state()

    if current == CreateTournament.name.state:

        await callback.answer()

        return

    if current == CreateTournament.num_teams.state:

        await state.set_state(CreateTournament.name)

        await callback.message.edit_text(

            "<b>🏆 Tournament Setup</b>\n\n"

            "Step 1 of 5\n\n"

            "Enter your tournament name."

        )

        return

    if current == CreateTournament.entering_teams.state:

        await state.set_state(CreateTournament.num_teams)

        await callback.message.edit_text(

            "<b>🏆 Tournament Setup</b>\n\n"

            "Step 2 of 5\n\n"

            "How many teams?\n\n"

            "Minimum: 2\n"

            "Maximum: 100"

        )

        return


# ======================================================
# Cancel
# ======================================================

async def cancel(callback: CallbackQuery, state: FSMContext):

    await state.clear()

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

    await callback.message.edit_text(

        "<b>🏆 Tournament Manager</b>\n\n"

        "Tournament creation cancelled.",

        reply_markup=keyboard

    )

    await callback.answer()


# ======================================================
# My Tournaments
# ======================================================

async def my_tournaments(callback: CallbackQuery):

    await callback.answer(

        "Coming Soon",

        show_alert=True

    )
