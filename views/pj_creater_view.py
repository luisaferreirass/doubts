from src.controllers.interfaces.pj_creater_controller import PJCreaterControllerInterface
from src.validators.pj_creator_validator import pessoa_juridica_creator_validator
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interface.view_interface import ViewInterface

class PJCreaterView(ViewInterface):
    def __init__(self, controller: PJCreaterControllerInterface) -> None:
        self.controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pessoa_juridica_creator_validator(http_request)
        person_info = http_request.body
        body_response = self.controller.create(person_info)

        return HttpResponse(status_code=201, body=body_response)
