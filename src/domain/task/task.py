from dataclasses import dataclass, field
from typing import Optional

from domain.task.details import Details
from domain.task.initial_estimate import InitialEstimate
from domain.task.relations import Relations
from domain.task.status import Status
from domain.task.summary import Summary
from domain.task.task_id import TaskID


@dataclass(frozen=True)
class Task:
    """タスク"""

    id: TaskID
    summary: Summary = field(compare=False)
    details: Optional[Details] = field(compare=False)
    status: Status = field(compare=False)
    relations: Relations = field(compare=False)
    initial_estimate: Optional[InitialEstimate] = field(compare=False)
