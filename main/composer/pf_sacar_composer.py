from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.pf_sacar_controller import PFSacarController
from src.views.pf_sacar_view import PFSacarView


def pf_sacar_composer():
    model = PessoaFisicaRepository(db_connection_handler)
    controller = PFSacarController(model)
    view = PFSacarView(controller)

    return view 
