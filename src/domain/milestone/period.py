from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class Period:
    """期間"""

    start: datetime
    end: Optional[datetime]
