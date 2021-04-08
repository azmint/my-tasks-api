from interface.controller import AbstractController
from interface.request import AbstractRequest
from interface.response import AbstractResponse


class RootController(AbstractController):
    """APIルートのコントローラー"""

    def execute(self, request: AbstractRequest, response: AbstractResponse):
        response.set_body(
            {
                "status": "OK",
            }
        )
