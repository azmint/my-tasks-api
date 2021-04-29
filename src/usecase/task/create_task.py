from dataclasses import dataclass
from typing import Optional

from injector import inject, singleton

from domain.task.details import Details
from domain.task.event.created_task import CreatedTask
from domain.task.initial_estimate import InitialEstimate
from domain.task.relations import Relations
from domain.task.status import Status
from domain.task.summary import Summary
from domain.task.task import Task
from domain.task.task_id import TaskID
from domain.task.task_repository import TaskRepository


@dataclass
class RequiredData:
    """必要な情報"""

    summary: Summary
    details: Optional[Details]
    status: Status
    relations: Relations
    initial_estimate: Optional[InitialEstimate]


@singleton
class CreateTask:
    """タスクを作成する"""

    @inject
    def __init__(self, task_repository: TaskRepository):
        """インスタンス化

        :param task_repository: タスクのリポジトリ
        """
        self.task_repository: TaskRepository = task_repository

    def execute(self, required_data: RequiredData) -> CreatedTask:
        """サービスを実行する

        :param required_data: 必要な情報
        :return: イベント
        """
        new_id: TaskID = self.task_repository.generate_id()
        new_task: Task = Task(
            new_id,
            required_data.summary,
            required_data.details,
            required_data.status,
            required_data.relations,
            required_data.initial_estimate,
        )
        return self.task_repository.store(new_task)
