import abc
from typing import TypeVar, Generic

from interface.request import AbstractRequest

T = TypeVar("T")


class AbstractValidator(abc.ABC, Generic[T]):
    """バリデーション機能の基底クラス"""

    @abc.abstractmethod
    def validate(self, request: AbstractRequest) -> T:
        """バリデーションを行う。

        :raises InvalidError: バリデーションに失敗した場合

        :param request: リクエスト
        :return: バリデーションしたデータ
        """
        pass
