from dataclasses import dataclass
from enum import Enum, auto
from typing import List

from command.domain.task.task_id import TaskID


class Type(Enum):
    """関係の種類"""

    # 親
    PARENT = auto()
    # 子
    CHILD = auto()


@dataclass(frozen=True)
class Relation:
    """他タスクとの関係"""

    # 関係種別
    type: Type
    # 関係タスク
    task_id: TaskID


@dataclass
class Relations:
    """関係の一覧"""

    values: List[Relation]
