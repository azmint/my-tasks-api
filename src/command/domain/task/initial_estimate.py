from dataclasses import dataclass
from datetime import timedelta


@dataclass(frozen=True)
class InitialEstimate:
    """初期見積もり"""

    value: timedelta
