from dataclasses import dataclass


@dataclass(frozen=True)
class SprintID:
    """スプリントID"""

    value: str
