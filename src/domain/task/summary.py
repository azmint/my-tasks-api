from dataclasses import dataclass


@dataclass(frozen=True)
class Summary(str):
    """サマリー"""

    value: str
