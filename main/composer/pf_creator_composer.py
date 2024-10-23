from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.pf_creater_controller import PFCreaterController
from src.views.pf_creater_view import PFCreaterView

def pf_creator_composer():
    model = PessoaFisicaRepository(db_connection_handler)
    controller = PFCreaterController(model)
    view = PFCreaterView(controller)

    return view
