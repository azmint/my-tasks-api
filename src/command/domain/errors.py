from typing import Optional, Dict, Any


class BaseError(Exception):
    """アプリケーションレイヤーのエラー

    コアロジックでのエラー
    """

    def __init__(
        self,
        message: str,
        values: Optional[Dict[str, Any]] = None,
        cause: Optional[Exception] = None,
    ):
        """

        :param message: エラーメッセージ
        :param values: 付加情報
        :param cause: 原因となったエラー(DBアクセス時に発生した依存ライブラリのエラーなど)
        """
        super().__init__(message)
        self.message: str = message
        self.values: Dict[str, Any] = values if values else {}
        self.cause: Optional[Exception] = cause

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__module__}.{self.__class__.__qualname__}"
            + f"({self.message}, {self.values}, {self.cause})"
        )


class ApplicationError(BaseError):
    """アプリケーションレイヤーのエラー

    コアロジックでのエラー
    """


class InfrastructureError(BaseError):
    """インフラストラクチャーレイヤーのエラー

    依存しているライブラリやサービスでのエラーは、このエラーに変換してraiseする。
    """
