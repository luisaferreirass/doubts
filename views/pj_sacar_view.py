from src.controllers.interfaces.pj_sacar_controller import PJSacarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interface.view_interface import ViewInterface

class PJSacarView(ViewInterface):
    def __init__(self, controller: PJSacarControllerInterface) -> None:
        self.controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        action_info = http_request.body
        body_response = self.controller.sacar(action_info)

        return HttpResponse(status_code= 200, body=body_response)