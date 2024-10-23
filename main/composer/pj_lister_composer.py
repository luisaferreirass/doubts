from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.pj_lister_controler import PJListerController
from src.views.pj_lister_view import PJListerView

def pj_lister_composer():
    model = PessoaJuridicaRepository(db_connection_handler)
    controller = PJListerController(model)
    view = PJListerView(controller)

    return view
