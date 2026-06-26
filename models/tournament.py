from dataclasses import dataclass, field

from models.team import Team
from models.ranking import Ranking
from models.result import Result


@dataclass
class Tournament:

    id: int | None = None

    name: str = ""

    mode: str = "Battle Royale"

    status: str = "Draft"

    max_teams: int = 0

    kill_points: int = 1

    teams: list[Team] = field(default_factory=list)

    rankings: list[Ranking] = field(default_factory=list)

    results: list[Result] = field(default_factory=list)
