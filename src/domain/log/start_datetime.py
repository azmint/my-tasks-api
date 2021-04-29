from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class StartDatetime:
    """開始日時"""

    value: datetime
