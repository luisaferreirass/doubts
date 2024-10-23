from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.pj_creater_controller import PJCreaterController
from src.views.pj_creater_view import PJCreaterView

def pj_creator_composer():
    model = PessoaJuridicaRepository(db_connection_handler)
    controller = PJCreaterController(model)
    view = PJCreaterView(controller)

    return view
