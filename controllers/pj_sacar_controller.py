from typing import Dict
from src.models.sqlite.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface

class PJSacarController:
    def __init__(self, pessoa_juridica_repository: PessoaJuridicaRepositoryInterface) -> None:
        self.__pessoa_juridica_repository = pessoa_juridica_repository

    def sacar(self, action_info: Dict) -> Dict:
        nome_fantasia = action_info["nome_fantasia"]
        quantia = action_info["quantia"]

        self.__sacar_in_db(nome_fantasia, quantia)
        formated_response = self.__format_response(action_info)

        return formated_response

    def __sacar_in_db(self, nome_fantasia: str, quantia: int) -> None:
        self.__pessoa_juridica_repository.sacar(nome_fantasia, quantia)

    def __format_response(self, action_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Pessoa Jurídica",
                "count": 1,
                "attributes": action_info
            }
        }
