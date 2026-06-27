"""
Message Router

Handles every text message while the
user is inside a tournament wizard.
"""

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from wizard.session import CreateTournament
from features.battle_royale import tournament

router = Router()


# ==========================================
# Tournament Name
# ==========================================

@router.message(CreateTournament.name)
async def tournament_name(
    message: Message,
    state: FSMContext
):
    await tournament.handle_name(
        message,
        state
    )


# ==========================================
# Team Count
# ==========================================

@router.message(CreateTournament.num_teams)
async def team_count(
    message: Message,
    state: FSMContext
):
    await tournament.handle_team_count(
        message,
        state
    )


# ==========================================
# Team Entry
# ==========================================

@router.message(CreateTournament.entering_teams)
async def team_name(
    message: Message,
    state: FSMContext
):
    await tournament.handle_team_name(
        message,
        state
    )


# ==========================================
# Ranking Max Points
# ==========================================

@router.message(CreateTournament.ranking_max_points)
async def ranking_points(
    message: Message,
    state: FSMContext
):
    await tournament.handle_ranking_points(
        message,
        state
    )


# ==========================================
# Kill Points
# ==========================================

@router.message(CreateTournament.ranking_kill_points)
async def kill_points(
    message: Message,
    state: FSMContext
):
    await tournament.handle_kill_points(
        message,
        state
    )
