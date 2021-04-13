from dataclasses import dataclass, field
from typing import Optional

from command.domain.milestone.details import Details
from command.domain.milestone.period import Period
from command.domain.milestone.summary import Summary
from command.domain.milestone.milestone_id import MilestoneID


@dataclass(frozen=True)
class Milestone:
    """タスク"""

    id: MilestoneID
    summary: Summary = field(compare=False)
    details: Optional[Details] = field(compare=False)
    period: Period = field(compare=False)
