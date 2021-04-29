from typing import Type

from infrastructure.flask.request import AppRequest
from infrastructure.flask.response import AppResponse
from infrastructure.injector.injector_facade import create_injector
from interface.controller import AbstractController

injector = create_injector()


def handle(controller_type: Type[AbstractController]) -> str:
    """指定されたコントローラーをハンドリングする。

    :param controller_type: コントローラーの型
    """
    controller: AbstractController = injector.get(controller_type)
    request: AppRequest = AppRequest()
    response: AppResponse = AppResponse()
    controller.execute(request, response)
    return response.build()
