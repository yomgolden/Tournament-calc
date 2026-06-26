# wizard/builder.py

from dataclasses import dataclass, field


@dataclass
class TournamentBuilder:

    # Basic Information
    name: str = ""
    mode: str = "Battle Royale"

    # Teams
    max_teams: int = 0
    teams: list = field(default_factory=list)

    # Scoring
    kill_points: int = 1
    rankings: dict = field(default_factory=dict)

    # Tournament
    status: str = "Draft"

    # ------------------------
    # Team Methods
    # ------------------------

    def add_team(self, name: str):

        slot = len(self.teams) + 1

        self.teams.append({
            "slot": slot,
            "name": name
        })

    def rename_team(self, slot: int, name: str):

        self.teams[slot - 1]["name"] = name

    def remove_team(self, slot: int):

        self.teams.pop(slot - 1)

        # Rebuild Slots
        for index, team in enumerate(self.teams):

            team["slot"] = index + 1

    # ------------------------
    # Ranking
    # ------------------------

    def set_points(self, placement: int, points: int):

        self.rankings[placement] = points

    def get_points(self, placement: int):

        return self.rankings.get(placement, 0)

    # ------------------------
    # Helpers
    # ------------------------

    @property
    def team_count(self):

        return len(self.teams)

    @property
    def completed(self):

        return self.team_count == self.max_teams
    
