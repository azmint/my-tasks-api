from enum import Enum, auto


class Status(Enum):
    """ステータス"""

    # 未着手
    OPEN = auto()
    # 着手中
    IN_PROGRESS = auto()
    # 内部要因待ち
    WAITING_FOR_INTERNAL_FACTORS = auto()
    # 外部要因待ち
    WAITING_FOR_EXTERNAL_FACTORS = auto()
    # 解決済み
    RESOLVED = auto()
    # 終了済み
    CLOSED = auto()
