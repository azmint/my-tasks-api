from dataclasses import dataclass, field
from typing import Optional

from domain.sprint.details import Details
from domain.sprint.period import Period
from domain.sprint.summary import Summary
from domain.sprint.sprint_id import SprintID


@dataclass(frozen=True)
class Sprint:
    """タスク"""

    id: SprintID
    summary: Summary = field(compare=False)
    details: Optional[Details] = field(compare=False)
    period: Period = field(compare=False)
