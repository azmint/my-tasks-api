from datetime import datetime
from typing import Dict

from injector import singleton

from domain.task.event.created_task import CreatedTask
from domain.task.task import Task
from domain.task.task_id import TaskID
from domain.task.task_repository import TaskRepository


@singleton
class TaskRepositoryOnMemory(TaskRepository):
    """メモリ上のリポジトリ実装"""

    def __init__(self):
        """インスタンス化"""
        self.newest_id: int = 0
        self.tasks: Dict[TaskID, Task] = {}

    def generate_id(self) -> TaskID:
        self.newest_id += 1
        return TaskID(str(self.newest_id))

    def store(self, task: Task) -> CreatedTask:
        self.tasks[task.id] = task
        return CreatedTask(
            datetime.now(),
            task.id,
        )
