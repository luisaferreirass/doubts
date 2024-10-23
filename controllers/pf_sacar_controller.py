from typing import Dict
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface
from src.errors.errors_types.http_bad_request import HttpBadRequestError

class PFSacarController:
    def __init__(self, pessoa_fisica_repository: PessoaFisicaRepositoryInterface) -> None:
        self.__pessoa_fisica_repository = pessoa_fisica_repository

    def sacar(self, action_info: Dict) -> Dict:
        nome_completo = action_info["nome_completo"]
        quantia = action_info["quantia"]

        self.__validate_input(nome_completo, quantia)

        self.__sacar_in_db(nome_completo, quantia)
        formated_response = self.__format_response(action_info)

        return formated_response
    
    def __validate_input(self, nome_completo: str, quantia: float) -> None:
        if (
            not nome_completo
            or not quantia
            or not isinstance(quantia, float)
            or not isinstance(nome_completo, str)
        ): raise HttpBadRequestError("Invalid input")


    def __sacar_in_db(self, nome_completo: str, quantia: int) -> None:
        self.__pessoa_fisica_repository.sacar(nome_completo, quantia)

    def __format_response(self, action_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Pessoa Física",
                "count": 1,
                "attributes": action_info
            }
        }
