import abc
from typing import Dict, Any


class AbstractResponse(abc.ABC):
    """レスポンスの基底クラス"""

    @abc.abstractmethod
    def set_body(self, data: Dict[str, Any]):
        """レスポンスボディをセットする。

        :param data: データ
        """
        raise NotImplementedError()
