from dataclasses import dataclass, field

from command.domain.task.details import Details
from command.domain.task.relations import Relations
from command.domain.task.status import Status
from command.domain.task.summary import Summary
from command.domain.task.task_id import TaskID


@dataclass(frozen=True)
class Task:
    """タスク"""

    id: TaskID
    summary: Summary = field(compare=False)
    details: Details = field(compare=False)
    status: Status = field(compare=False)
    relations: Relations = field(compare=False)
