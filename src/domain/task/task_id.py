from dataclasses import dataclass


@dataclass(frozen=True)
class TaskID:
    """タスクID"""

    value: str
