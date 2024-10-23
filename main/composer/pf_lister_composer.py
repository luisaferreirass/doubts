from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.pf_lister_controller import PFListerController
from src.views.pf_lister_view import PFListerView

def pf_lister_composer():
    model = PessoaFisicaRepository(db_connection_handler)
    controller = PFListerController(model)
    view = PFListerView(controller)

    return view
