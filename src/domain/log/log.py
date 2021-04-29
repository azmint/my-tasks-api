from dataclasses import dataclass

from domain.log.log_id import LogID
from domain.log.start_datetime import StartDatetime
from domain.log.work_time import WorkTime


@dataclass(frozen=True)
class Log:
    """ログ"""

    id: LogID
    start_datetime: StartDatetime
    work_time: WorkTime
