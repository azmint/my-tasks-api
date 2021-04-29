from typing import Dict, Any

from cerberus import Validator
from injector import singleton, inject

from domain.task.relations import Relations
from domain.task.status import Status
from interface.invalid_error import InvalidError
from interface.request import AbstractRequest
from interface.task.create_task.input.summary_definition import SummaryDefinition
from usecase.task.create_task import RequiredData


@singleton
class Mapper:
    """リクエストとユースケースの必須情報のマッピング"""

    @inject
    def __init__(self, summary_definition: SummaryDefinition):
        self.summary_definition: SummaryDefinition = summary_definition

    def map(self, request: AbstractRequest) -> RequiredData:
        """リクエストをユースケースの必須情報に変換する

        :param request: リクエスト
        :return: ユースケースの必須情報
        """
        params: Dict[str, Any] = request.get_params()
        self._validate(params)
        return RequiredData(
            self.summary_definition.map(params),
            None,
            Status.OPEN,
            Relations([]),
            None,
        )

    def _validate(self, params: Dict[str, Any]):
        """バリデーション

        :param params: リクエストで渡された情報
        """
        schema: Dict[str, Any] = {
            definition.KEY: definition.SCHEMA
            for definition in [
                self.summary_definition,
            ]
        }
        validator: Validator = Validator(schema)
        is_valid: bool = validator.validate(params)
        if not is_valid:
            raise InvalidError(validator.errors, params)
