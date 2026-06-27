"""
FSM State Groups
"""

from aiogram.fsm.state import State, StatesGroup


class CreateTournament(StatesGroup):

    # Step 1
    name = State()

    # Step 2
    num_teams = State()

    # Step 3
    entering_teams = State()

    # Step 4
    ranking_mode = State()

    ranking_max_points = State()

    ranking_kill_points = State()

    ranking_preview = State()

    # Step 5
    summary = State()


class EnterResult(StatesGroup):

    choose_match = State()

    choose_team = State()

    enter_placement = State()

    enter_kills = State()
