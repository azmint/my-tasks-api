from dataclasses import dataclass, field

from domain.task.details import Details
from domain.task.relations import Relations
from domain.task.status import Status
from domain.task.summary import Summary
from domain.task.task_id import TaskID


@dataclass(frozen=True)
class Task:
    """タスク"""

    id: TaskID
    summary: Summary = field(compare=False)
    details: Details = field(compare=False)
    status: Status = field(compare=False)
    relations: Relations = field(compare=False)
