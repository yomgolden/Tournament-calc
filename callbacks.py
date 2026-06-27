"""
Global callback router.

This file should remain small.
It only forwards callback queries to the correct module.
"""

from aiogram import Router, F
from aiogram.types import CallbackQuery

from modules.battle_royale import tournament

router = Router()


# ===============================
# HOME
# ===============================

@router.callback_query(F.data == "create_tournament")
async def create_tournament(callback: CallbackQuery):

    await tournament.start(callback)


@router.callback_query(F.data == "my_tournaments")
async def my_tournaments(callback: CallbackQuery):

    await tournament.my_tournaments(callback)


@router.callback_query(F.data == "settings")
async def settings(callback: CallbackQuery):

    await callback.answer(
        "Coming Soon",
        show_alert=True
    )


@router.callback_query(F.data == "help")
async def help_menu(callback: CallbackQuery):

    await callback.answer(
        "Coming Soon",
        show_alert=True
    )


# ===============================
# NAVIGATION
# ===============================

@router.callback_query(F.data == "back")
async def back(callback: CallbackQuery):

    await tournament.back(callback)


@router.callback_query(F.data == "cancel")
async def cancel(callback: CallbackQuery):

    await tournament.cancel(callback)
