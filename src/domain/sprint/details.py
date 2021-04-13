from dataclasses import dataclass


@dataclass(frozen=True)
class Details:
    """詳細"""

    value: str
