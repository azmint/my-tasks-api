from dataclasses import dataclass
from datetime import timedelta


@dataclass(frozen=True)
class WorkTime:
    """作業時間"""

    value: timedelta
