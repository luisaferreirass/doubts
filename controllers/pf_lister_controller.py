from typing import Dict, List
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from .interfaces.pf_lister_controller import PFListerControllerInterface

class PFListerController(PFListerControllerInterface):
    def __init__(self, pessoa_fisica_repository: PessoaFisicaRepositoryInterface) -> None:
        self.__pessoa_fisica_repository = pessoa_fisica_repository

    def list(self) -> Dict:
        pessoas_fisicas = self.__get_list_in_db()
        formated_response = self.__format_response(pessoas_fisicas)

        return formated_response
    
    def __get_list_in_db(self) -> List[PessoaFisicaTable]:
        pessoas_fisicas = self.__pessoa_fisica_repository.list_people()

        return pessoas_fisicas
    
    def __format_response(self, pessoas_fisicas: List[PessoaFisicaTable]) -> Dict:
        pessoas_fisicas_format = []

        for person in pessoas_fisicas:
            pessoas_fisicas_format.append({
                "id": person.id,
                "nome_completo": person.nome_completo,
                "saldo": person.saldo
            })

        return {
            "data": {
                "type": "Pessoa Física",
                "count": len(pessoas_fisicas_format),
                "attributes": pessoas_fisicas_format
            }
        }
