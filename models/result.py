from dataclasses import dataclass


@dataclass
class Result:

    match_number: int

    slot: int

    placement: int

    kills: int

    placement_points: int

    total_points: int
