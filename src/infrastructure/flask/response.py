import json
from typing import Dict, Any

from flask import Response

from infrastructure.latency_measurement import LatencyMeasurement
from interface.response import AbstractResponse


class AppResponse(AbstractResponse):
    """レスポンス"""

    def __init__(self):
        self.body: Dict[str, Any] = {}
        self.response: Response = Response()
        self.latency_measurement: LatencyMeasurement = LatencyMeasurement()

    def set_body(self, data: Dict[str, Any]):
        self.body = data

    def build(self) -> str:
        """レスポンスを構築する。

        :return: レスポンスデータ
        """
        latency_ms: float = self.latency_measurement.result_as_seconds()
        return json.dumps(
            {
                "latency_ms": latency_ms,
                "body": self.body,
            }
        )
