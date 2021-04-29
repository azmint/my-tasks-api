from dataclasses import dataclass

from domain.event import Event
from domain.task.task_id import TaskID


@dataclass(frozen=True)
class CreatedTask(Event):
    """タスク作成イベント"""

    created_task_id: TaskID
