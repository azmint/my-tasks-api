from typing import Dict, Any, List


class InvalidDetail:
    """バリデーションエラーの詳細"""

    def __init__(self, item_name: str, message: str):
        self.item_name: str = item_name
        self.message: str = message

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__module__}.{self.__class__.__qualname__}"
            + f"({self.item_name}, {self.message})"
        )


class InvalidError(Exception):
    """バリデーションのエラー

    コアロジックでのエラー
    """

    def __init__(self, details: List[InvalidDetail], values: Dict[str, Any] = None):
        """

        :param details: エラー詳細
        :param values: 付加情報
        """
        super().__init__("Invalid Error")
        self.details: List[InvalidDetail] = details
        self.values: Dict[str, Any] = values if values else {}
