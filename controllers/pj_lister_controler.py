from typing import List, Dict
from src.models.sqlite.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable
from .interfaces.pj_lister_controller import PJListerControllerInterface

class PJListerController(PJListerControllerInterface):
    def __init__(self, pessoa_juridica_repository: PessoaJuridicaRepositoryInterface) -> None:
        self.__pessoa_juridica_repository = pessoa_juridica_repository

    def list(self) -> Dict:
        pessoas_juridicas = self.__get_people_in_db()
        formated_response = self.__format_response(pessoas_juridicas)

        return formated_response

    def __get_people_in_db(self) -> List[PessoaJuridicaTable]:
        pessoas_juridicas = self.__pessoa_juridica_repository.list_people()

        return pessoas_juridicas
    
    def __format_response(self, pessoas_juridicas: List[PessoaJuridicaTable]) -> Dict:
        formated_pessoas_juridicas = []

        for person in pessoas_juridicas:
            formated_pessoas_juridicas.append({
                "id": person.id,
                "nome_fantasia": person.nome_fantasia,
                "saldo": person.saldo
            })

        return {
                "data": {
                    "type": "Pessoa Jurídica",
                    "count": len(formated_pessoas_juridicas),
                    "attributes": formated_pessoas_juridicas
                }
            }
