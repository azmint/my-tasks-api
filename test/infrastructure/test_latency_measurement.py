from unittest import mock
from unittest.mock import MagicMock


class TestLatencyMeasurement:
    """LatencyMeasurementのテスト"""

    def test_result_as_seconds(self):
        """result_as_secondsのテスト"""
        from datetime import datetime

        with mock.patch("datetime.datetime", MagicMock()) as datetime_mock:
            from infrastructure.latency_measurement import LatencyMeasurement

            datetime_mock.now.return_value = datetime(2021, 4, 8, 22, 22, 0, 0)
            latency_measurement: LatencyMeasurement = LatencyMeasurement()
            datetime_mock.now.return_value = datetime(2021, 4, 8, 22, 22, 1, 100 * 1000)
            result: float = latency_measurement.result_as_seconds()
            assert result == 1.1
