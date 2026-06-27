"""
Input Validators
"""

from config import (
    MIN_TEAMS,
    MAX_TEAMS
)


def validate_tournament_name(name: str):

    name = name.strip()

    if not name:

        return False, "Tournament name cannot be empty."

    if len(name) > 64:

        return False, "Tournament name is too long."

    return True, ""


def validate_num_teams(value: str):

    try:

        teams = int(value)

    except ValueError:

        return False, f"Enter a number between {MIN_TEAMS} and {MAX_TEAMS}."

    if teams < MIN_TEAMS:

        return False, f"Minimum teams is {MIN_TEAMS}."

    if teams > MAX_TEAMS:

        return False, f"Maximum teams is {MAX_TEAMS}."

    return True, ""


def validate_team_name(

    name: str,

    existing: list[str]

):

    name = name.strip()

    if not name:

        return False, "Team name cannot be empty."

    if len(name) > 32:

        return False, "Team name is too long."

    for team in existing:

        if team.lower() == name.lower():

            return False, "Team already exists."

    return True, ""


def validate_positive_int(

    value: str,

    label: str = "Value"

):

    try:

        number = int(value)

    except ValueError:

        return False, f"{label} must be a number."

    if number < 1:

        return False, f"{label} must be greater than zero."

    return True, ""
