from injector import inject, singleton

from domain.task.event.created_task import CreatedTask
from interface.controller import AbstractController
from interface.request import AbstractRequest
from interface.response import AbstractResponse
from interface.task.create_task.input.mapper import Mapper
from usecase.task.create_task import RequiredData, CreateTask


@singleton
class CreateTaskController(AbstractController):
    """タスク作成処理のコントローラー"""

    @inject
    def __init__(self, input_data_mapper: Mapper, create_task: CreateTask):
        self.input_data_mapper: Mapper = input_data_mapper
        self.create_task: CreateTask = create_task

    def execute(self, request: AbstractRequest, response: AbstractResponse):
        required_data: RequiredData = self.input_data_mapper.map(request)
        event: CreatedTask = self.create_task.execute(required_data)
        response.set_body({
            'occurrence_datetime': event.occurrence_datetime.strftime('%Y-%m-%d %H:%M:%S.%f'),
            'created_task_id': event.created_task_id.value,
        })
