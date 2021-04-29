from typing import Dict, Any, List


class InvalidError(Exception):
    """バリデーションのエラー

    コアロジックでのエラー
    """

    def __init__(self, details: Dict[str, List[str]], values: Dict[str, Any] = None):
        """

        :param details: エラー詳細
        :param values: 付加情報
        """
        super().__init__("Invalid Error")
        self.details: Dict[str, List[str]] = details
        self.values: Dict[str, Any] = values if values else {}
