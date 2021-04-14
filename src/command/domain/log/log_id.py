from dataclasses import dataclass


@dataclass(frozen=True)
class LogID:
    """ログID"""

    value: str
