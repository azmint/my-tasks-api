import abc
from typing import TypeVar, Generic

from interface.request import AbstractRequest

ValidatedData = TypeVar("ValidatedData")


class AbstractValidator(abc.ABC, Generic[ValidatedData]):
    """バリデーション機能の基底クラス"""

    @abc.abstractmethod
    def validate(self, request: AbstractRequest) -> ValidatedData:
        """バリデーションを行う。

        :raises InvalidError: バリデーションに失敗した場合

        :param request: リクエスト
        :return: バリデーションしたデータ
        """
        raise NotImplementedError()
