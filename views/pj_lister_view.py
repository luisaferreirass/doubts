from src.controllers.interfaces.pf_lister_controller import PFListerControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interface.view_interface import ViewInterface

class PJListerView(ViewInterface):
    def __init__(self, controller: PFListerControllerInterface) -> None:
        self.controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.controller.list()

        return HttpResponse(status_code=200, body=body_response)
