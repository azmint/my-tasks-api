import abc

from command.domain.task.event.created_task import CreatedTask
from command.domain.task.task import Task


class TaskRepository(abc.ABC):
    """タスクのリポジトリ"""

    @abc.abstractmethod
    def store(self, task: Task) -> CreatedTask:
        """登録する

        :param task: タスク
        :return: イベント
        """
        raise NotImplementedError()
