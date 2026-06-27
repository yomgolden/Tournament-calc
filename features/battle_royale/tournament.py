"""
Battle Royale Tournament
"""

from aiogram.types import (
    Message,
    CallbackQuery
)

from aiogram.fsm.context import FSMContext

from wizard.session import CreateTournament

from wizard.validators import (
    validate_tournament_name,
    validate_num_teams,
    validate_team_name
)

from utils.helpers import (
    delete_user_message,
    edit_setup_message,
    safe_answer
)

from utils.keyboards import (
    cancel_keyboard,
    back_cancel_keyboard
)

from utils.formatting import (
    setup_header
)

from config import (
    TEAM_DISPLAY_LIMIT
)


# ===========================================
# START WIZARD
# ===========================================

async def start(
    callback: CallbackQuery,
    state: FSMContext
):

    await state.clear()

    await state.set_state(
        CreateTournament.name
    )

    await state.update_data(
        teams=[]
    )

    sent = await callback.message.edit_text(

        setup_header(1)

        + "Enter Tournament Name.",

        reply_markup=cancel_keyboard()

    )

    await state.update_data(

        setup_message_id=sent.message_id

    )

    await safe_answer(callback)


# ===========================================
# NAME
# ===========================================

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

        tournament_name=message.text.strip()

    )

    await state.set_state(

        CreateTournament.num_teams

    )

    await delete_user_message(
        message
    )

    text = (

        setup_header(2)

        + f"Name\n"

        + f"<b>{message.text}</b>\n\n"

        + "How many teams?\n\n"

        + "Minimum : 2\n"

        + "Maximum : 100"

    )

    await edit_setup_message(

        message,

        state,

        text,

        back_cancel_keyboard()

    )


# ===========================================
# TEAM COUNT
# ===========================================

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

    count = int(message.text)

    await state.update_data(

        total_teams=count,

        teams=[]

    )

    await state.set_state(

        CreateTournament.entering_teams

    )

    await delete_user_message(
        message
    )

    text = (

        setup_header(3)

        + f"Teams : {count}\n\n"

        + "──────────────\n\n"

        + "Current\n\n"

        + "Enter Team 1 Name"

    )

    await edit_setup_message(

        message,

        state,

        text,

        back_cancel_keyboard()

    )

    # ===========================================
# TEAM ENTRY
# ===========================================

async def handle_team_name(
    message: Message,
    state: FSMContext
):

    data = await state.get_data()

    teams = data.get("teams", [])

    total = data["total_teams"]

    valid, error = validate_team_name(
        message.text,
        teams
    )

    if not valid:

        await message.reply(error)

        return

    team_name = message.text.strip()

    teams.append(team_name)

    await state.update_data(
        teams=teams
    )

    await delete_user_message(
        message
    )

    # Finished entering teams
    if len(teams) >= total:

        await state.set_state(
            CreateTournament.ranking_mode
        )

        text = (

            setup_header(4)

            + "Choose Ranking Style\n\n"

            "🥇 Placement Favours Winners\n"

            "or\n\n"

            "⚖️ Placement Decreases Evenly"

        )

        from aiogram.types import (
            InlineKeyboardMarkup,
            InlineKeyboardButton
        )

        keyboard = InlineKeyboardMarkup(

            inline_keyboard=[

                [
                    InlineKeyboardButton(

                        text="🥇 Favours Winners",

                        callback_data="ranking_winners"

                    )
                ],

                [
                    InlineKeyboardButton(

                        text="⚖️ Decrease Evenly",

                        callback_data="ranking_even"

                    )
                ],

                [
                    InlineKeyboardButton(

                        text="⬅ Back",

                        callback_data="back"

                    ),

                    InlineKeyboardButton(

                        text="❌ Cancel",

                        callback_data="cancel"

                    )

                ]

            ]

        )

        await edit_setup_message(

            message,

            state,

            text,

            keyboard

        )

        return

    # ----------------------------
    # Show last five teams only
    # ----------------------------

    recent = teams[-TEAM_DISPLAY_LIMIT:]

    start_slot = len(teams) - len(recent) + 1

    team_list = ""

    for index, team in enumerate(
        recent,
        start=start_slot
    ):

        team_list += (

            f"{index}. "

            f"{team} - Slot {index}\n"

        )

    next_slot = len(teams) + 1

    text = (

        setup_header(3)

        + f"Teams : {total}\n\n"

        + team_list

        + "\n──────────────\n\n"

        + "Current\n\n"

        + f"Enter Team {next_slot} Name"

    )

    await edit_setup_message(

        message,

        state,

        text,

        back_cancel_keyboard()

    )

    # ===========================================
# RANKING MODE
# ===========================================

async def ranking_winners(
    callback: CallbackQuery,
    state: FSMContext
):

    await state.update_data(
        ranking_mode="winner"
    )

    await state.set_state(
        CreateTournament.ranking_max_points
    )

    text = (

        setup_header(4)

        + "Ranking Style\n\n"

        + "🥇 Placement Favours Winners\n\n"

        + "Enter points for 1st Place."

    )

    await callback.message.edit_text(
        text,
        reply_markup=back_cancel_keyboard()
    )

    await safe_answer(callback)


async def ranking_even(
    callback: CallbackQuery,
    state: FSMContext
):

    await state.update_data(
        ranking_mode="even"
    )

    await state.set_state(
        CreateTournament.ranking_max_points
    )

    text = (

        setup_header(4)

        + "Ranking Style\n\n"

        + "⚖️ Placement Decreases Evenly\n\n"

        + "Enter points for 1st Place."

    )

    await callback.message.edit_text(
        text,
        reply_markup=back_cancel_keyboard()
    )

    await safe_answer(callback)


# ===========================================
# MAX PLACEMENT POINTS
# ===========================================

async def handle_ranking_points(
    message: Message,
    state: FSMContext
):

    from wizard.validators import (
        validate_positive_int
    )

    valid, error = validate_positive_int(
        message.text,
        "Placement Points"
    )

    if not valid:

        await message.reply(error)

        return

    max_points = int(message.text)

    await state.update_data(
        first_place=max_points
    )

    await state.set_state(
        CreateTournament.ranking_kill_points
    )

    await delete_user_message(
        message
    )

    text = (

        setup_header(4)

        + f"1st Place : {max_points}\n\n"

        + "Kill Points\n\n"

        + "Enter kill points.\n\n"

        + "Recommended: 1"

    )

    await edit_setup_message(

        message,

        state,

        text,

        back_cancel_keyboard()

    )

    # ===========================================
# KILL POINTS
# ===========================================

async def handle_kill_points(
    message: Message,
    state: FSMContext
):

    from wizard.validators import (
        validate_positive_int
    )

    from features.battle_royale.ranking import (
        generate_ranking,
        ranking_preview
    )

    valid, error = validate_positive_int(
        message.text,
        "Kill Points"
    )

    if not valid:

        await message.reply(error)

        return

    kill_points = int(message.text)

    data = await state.get_data()

    first_place = data["first_place"]

    total_teams = data["total_teams"]

    ranking_mode = data["ranking_mode"]

    rankings = generate_ranking(

        total_teams=total_teams,

        first_place=first_place,

        mode=ranking_mode

    )

    await state.update_data(

        kill_points=kill_points,

        rankings=rankings

    )

    await delete_user_message(
        message
    )

    await state.set_state(
        CreateTournament.summary
    )

    preview = ranking_preview(rankings)

    text = (

        setup_header(5)

        + "<b>Tournament Summary</b>\n\n"

        + f"Name : {data['tournament_name']}\n"

        + "Mode : Battle Royale\n"

        + f"Teams : {total_teams}\n"

        + f"Kill Points : {kill_points}\n\n"

        + preview

    )

    from utils.keyboards import (
        summary_keyboard
    )

    await edit_setup_message(

        message,

        state,

        text,

        summary_keyboard()

    )


# ===========================================
# SAVE TOURNAMENT
# ===========================================

async def save(
    callback: CallbackQuery,
    state: FSMContext
):

    from database.storage import (
        create_tournament,
        insert_teams,
        insert_rankings
    )

    from utils.formatting import (
        tournament_dashboard
    )

    from utils.keyboards import (
        tournament_keyboard
    )

    data = await state.get_data()

    tournament_id = await create_tournament(

        owner_id=callback.from_user.id,

        name=data["tournament_name"],

        mode="Battle Royale",

        max_teams=data["total_teams"],

        kill_points=data["kill_points"]

    )

    await insert_teams(

        tournament_id,

        data["teams"]

    )

    await insert_rankings(

        tournament_id,

        data["rankings"]

    )

    await state.clear()

    await callback.message.edit_text(

        tournament_dashboard(

            data["tournament_name"],

            "Battle Royale",

            "Active"

        ),

        reply_markup=tournament_keyboard()

    )

    await safe_answer(callback)
