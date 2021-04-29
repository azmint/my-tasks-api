from injector import Injector, Module

from domain.task.task_repository import TaskRepository
from infrastructure.implements.memory.task_repository_on_memory import TaskRepositoryOnMemory


class _RepositoryModule(Module):
    """リポジトリの実装クラスバインド設定"""

    def configure(self, binder):
        binder.bind(TaskRepository, to=TaskRepositoryOnMemory)


def create_injector() -> Injector:
    """Injectorのインスタンスを作成する

    :return: Injectorのインスタンス
    """
    return Injector(_RepositoryModule)
