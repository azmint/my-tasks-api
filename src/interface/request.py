import abc
from typing import Dict, Any


class AbstractRequest(abc.ABC):
    """リクエストの基底クラス"""

    @abc.abstractmethod
    def get_params(self) -> Dict[str, Any]:
        """リクエストパラメータを返す

        :return: パラメータのdict
        """
        raise NotImplementedError()
