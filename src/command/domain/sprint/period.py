from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Period:
    """期間"""

    start: datetime
    end: datetime
