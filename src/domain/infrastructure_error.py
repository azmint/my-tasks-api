from typing import Optional, Dict, Any


class InfrastructureError(Exception):
    """インフラストラクチャーレイヤーのエラー

    依存しているライブラリやサービスでのエラーは、このエラーに変換してraiseする。
    """
    def __init__(self,
                 message: str,
                 values: Dict[str, Any] = None,
                 cause: Optional[Exception] = None):
        """

        :param message: エラーメッセージ
        :param values: 付加情報
        :param cause: 原因となったエラー(DBアクセス時に発生した依存ライブラリのエラーなど)
        """
        super().__init__(message)
        self.message: str = message
        self.values: Dict[str, Any] = values if values else {}
        self.cause: Optional[Exception] = cause
