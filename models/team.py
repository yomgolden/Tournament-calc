from dataclasses import dataclass


@dataclass
class Team:

    slot: int

    name: str

    captain: str | None = None

    logo: str | None = None

    country: str | None = None

    seed: int | None = None

    status: str = "Active"
