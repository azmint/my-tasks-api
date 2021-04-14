from dataclasses import dataclass

from command.domain.event import Event
from command.domain.task.task_id import TaskID


@dataclass(frozen=True)
class CreatedTask(Event):
    """タスク作成イベント"""

    created_task_id: TaskID
