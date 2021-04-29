from dataclasses import dataclass


@dataclass(frozen=True)
class Comment:
    """コメント"""

    value: str
