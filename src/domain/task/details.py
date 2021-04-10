from dataclasses import dataclass


@dataclass(frozen=True)
class Details(str):
    """詳細"""

    value: str
