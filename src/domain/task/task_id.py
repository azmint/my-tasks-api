from dataclasses import dataclass


@dataclass(frozen=True)
class TaskID(str):
    """タスクID"""

    value: str
