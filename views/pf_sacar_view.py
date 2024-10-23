from src.controllers.interfaces.pf_sacar_controller import PFSacarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interface.view_interface import ViewInterface

class PFSacarView(ViewInterface):
    def __init__(self, controller: PFSacarControllerInterface) -> None:
        self.controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        action_info = http_request.body
        body_response = self.controller.sacar(action_info)

        return HttpResponse(status_code= 200, body=body_response)
    
