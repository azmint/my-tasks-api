import abc

from domain.task.event.created_task import CreatedTask
from domain.task.task import Task
from domain.task.task_id import TaskID


class TaskRepository(abc.ABC):
    """タスクのリポジトリ"""

    @abc.abstractmethod
    def generate_id(self) -> TaskID:
        """IDを生成する

        :return: ID
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def store(self, task: Task) -> CreatedTask:
        """登録する

        :param task: タスク
        :return: イベント
        """
        raise NotImplementedError()
