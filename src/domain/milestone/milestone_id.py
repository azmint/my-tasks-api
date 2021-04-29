from dataclasses import dataclass


@dataclass(frozen=True)
class MilestoneID:
    """マイルストーンID"""

    value: str
