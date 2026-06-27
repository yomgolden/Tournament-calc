"""
Message router.
Handles all user text while using the wizard.
"""

from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from wizard.session import CreateTournament
from features.battle_royale import tournament

router = Router()


# =====================================================
# TOURNAMENT NAME
# =====================================================

@router.message(CreateTournament.name)
async def tournament_name(
    message: Message,
    state: FSMContext
):
    await tournament.handle_name(
        message,
        state
    )


# =====================================================
# NUMBER OF TEAMS
# =====================================================

@router.message(CreateTournament.num_teams)
async def number_of_teams(
    message: Message,
    state: FSMContext
):
    await tournament.handle_team_count(
        message,
        state
    )


# =====================================================
# TEAM ENTRY
# =====================================================

@router.message(CreateTournament.entering_teams)
async def team_entry(
    message: Message,
    state: FSMContext
):
    await tournament.handle_team_name(
        message,
        state
    )


# =====================================================
# RANKING POINTS
# =====================================================

@router.message(CreateTournament.ranking_max_points)
async def ranking_points(
    message: Message,
    state: FSMContext
):
    await tournament.handle_ranking_points(
        message,
        state
    )


# =====================================================
# KILL POINTS
# =====================================================

@router.message(CreateTournament.ranking_kill_points)
async def kill_points(
    message: Message,
    state: FSMContext
):
    await tournament.handle_kill_points(
        message,
        state
    )
