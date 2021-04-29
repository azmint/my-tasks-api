from typing import Dict, Any

from flask import request

from interface.request import AbstractRequest


class AppRequest(AbstractRequest):
    """リクエスト"""

    def get_params(self) -> Dict[str, Any]:
        return request.args
