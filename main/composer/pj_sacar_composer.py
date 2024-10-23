from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.pj_sacar_controller import PJSacarController
from src.views.pj_sacar_view import PJSacarView

def pj_sacar_composer():
    model =PessoaJuridicaRepository(db_connection_handler)
    controller = PJSacarController(model)
    view = PJSacarView(controller)

    return view
