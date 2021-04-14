from dataclasses import dataclass


@dataclass(frozen=True)
class CommentID:
    """コメントID"""

    value: str
