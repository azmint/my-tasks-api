from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Event:
    """イベント"""

    occurrence_datetime: datetime
