from dataclasses import dataclass


@dataclass(frozen=True)
class Summary:
    """サマリー"""

    value: str
