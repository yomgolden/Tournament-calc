"""
Global Callback Router
"""

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from features.battle_royale import tournament

router = Router()


# ================================
# HOME
# ================================

@router.callback_query(
    F.data == "create_tournament"
)
async def create_tournament(
    callback: CallbackQuery,
    state: FSMContext
):
    await tournament.start(
        callback,
        state
    )


@router.callback_query(
    F.data == "my_tournaments"
)
async def my_tournaments(
    callback: CallbackQuery
):
    await tournament.my_tournaments(
        callback
    )


@router.callback_query(
    F.data == "settings"
)
async def settings(
    callback: CallbackQuery
):

    await callback.answer(
        "Coming Soon",
        show_alert=True
    )


@router.callback_query(
    F.data == "help"
)
async def help(
    callback: CallbackQuery
):

    await callback.answer(
        "Coming Soon",
        show_alert=True
    )


# ================================
# NAVIGATION
# ================================

@router.callback_query(
    F.data == "back"
)
async def back(
    callback: CallbackQuery,
    state: FSMContext
):
    await tournament.back(
        callback,
        state
    )


@router.callback_query(
    F.data == "cancel"
)
async def cancel(
    callback: CallbackQuery,
    state: FSMContext
):
    await tournament.cancel(
        callback,
        state
    )


# ================================
# SUMMARY
# ================================

@router.callback_query(
    F.data == "save_tournament"
)
async def save_tournament(
    callback: CallbackQuery,
    state: FSMContext
):
    await tournament.save(
        callback,
        state
    )


# ================================
# DASHBOARD
# ================================

@router.callback_query(
    F.data == "teams"
)
async def teams(
    callback: CallbackQuery
):
    await tournament.teams(
        callback
    )


@router.callback_query(
    F.data == "results"
)
async def results(
    callback: CallbackQuery
):
    await tournament.results(
        callback
    )


@router.callback_query(
    F.data == "leaderboard"
)
async def leaderboard(
    callback: CallbackQuery
):
    await tournament.leaderboard(
        callback
    )


@router.callback_query(
    F.data == "tournament_settings"
)
async def tournament_settings(
    callback: CallbackQuery
):
    await tournament.settings(
        callback
    )
