import abc
from typing import TypeVar, Generic, Dict, Any

Type = TypeVar("Type")


class Definition(abc.ABC, Generic[Type]):
    """リクエストされるドメインクラスの定義"""

    KEY: str
    SCHEMA: Dict[str, Any]

    @abc.abstractmethod
    def map(self, params: Dict[str, Any]) -> Type:
        """入力情報をドメインクラスに変換する

        :param params: 入力情報
        :return: ドメインクラス
        """
        raise NotImplementedError()
