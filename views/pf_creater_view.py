from src.controllers.interfaces.pf_creater_controller import PFCreaterControllerInterface
from src.validators.pf_creator_validator import pessoa_fisica_creator_validator
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interface.view_interface import ViewInterface

class PFCreaterView(ViewInterface):
    def __init__(self, controller: PFCreaterControllerInterface) -> None:
        self.controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pessoa_fisica_creator_validator(http_request)
        person_info = http_request.body
        body_response = self.controller.create(person_info)

        return HttpResponse(status_code=201, body= body_response)
