from typing import Type

from injector import Injector

from infrastructure.flask.request import AppRequest
from infrastructure.flask.response import AppResponse
from interface.controller import AbstractController

injector = Injector()


def handle(controller_type: Type[AbstractController]) -> str:
    """指定されたコントローラーをハンドリングする。

    :param controller_type: コントローラーの型
    """
    controller: AbstractController = injector.get(controller_type)
    request: AppRequest = AppRequest()
    response: AppResponse = AppResponse()
    controller.execute(request, response)
    return response.build()
