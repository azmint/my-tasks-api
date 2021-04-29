from typing import Dict, Any

from injector import singleton

from domain.task.summary import Summary
from interface.definition import Definition


@singleton
class SummaryDefinition(Definition[Summary]):
    """Summaryの定義"""

    KEY = "summary"
    SCHEMA = {
        "type": "string",
        "required": True,
        "nullable": False,
        "minlength": 1,
        "maxlength": 128,
    }

    def map(self, params: Dict[str, Any]) -> Summary:
        # value: str = params[self.get_key()]
        value: str = params[self.KEY]
        return Summary(value)
