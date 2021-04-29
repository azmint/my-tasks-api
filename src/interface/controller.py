import abc

from interface.request import AbstractRequest
from interface.response import AbstractResponse


class AbstractController(abc.ABC):
    """コントローラーの基底クラス"""

    @abc.abstractmethod
    def execute(self, request: AbstractRequest, response: AbstractResponse):
        """エンドポイントの処理を実行する。

        :param request: リクエスト
        :param response: レスポンス
        """
        raise NotImplementedError()
