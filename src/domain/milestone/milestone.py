from dataclasses import dataclass, field

from domain.milestone.details import Details
from domain.milestone.period import Period
from domain.milestone.summary import Summary
from domain.milestone.milestone_id import MilestoneID


@dataclass(frozen=True)
class Milestone:
    """タスク"""

    id: MilestoneID
    summary: Summary = field(compare=False)
    details: Details = field(compare=False)
    period: Period = field(compare=False)
