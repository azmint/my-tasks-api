from datetime import datetime


class LatencyMeasurement:
    """レイテンシ計測"""

    def __init__(self):
        self.start_time: datetime = datetime.now()

    def result_as_seconds(self) -> float:
        """インスタンス生成時〜このメソッド実行時までの処理時間を秒単位で返す。

        :return: 処理時間(秒単位)
        """
        end_time: datetime = datetime.now()
        return (end_time - self.start_time).total_seconds()
