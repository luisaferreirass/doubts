from typing import Dict
from src.models.sqlite.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface
from .interfaces.pj_creater_controller import PJCreaterControllerInterface
from src.errors.errors_types.http_bad_request import HttpBadRequestError

class PJCreaterController(PJCreaterControllerInterface):
    def __init__(self, pessoa_juridica_repository: PessoaJuridicaRepositoryInterface) -> None:
        self.__pessoa_juridica_repository = pessoa_juridica_repository

    def create(self, person_info: Dict) -> Dict:
        faturamento = person_info["faturamento"]
        idade = person_info["idade"]
        nome_fantasia = person_info["nome_fantasia"]
        celular = person_info["celular"]
        email_corporativo = person_info["email_corporativo"]
        categoria = person_info["categoria"]
        saldo = person_info["saldo"]

        self.__validate_input(nome_fantasia, idade, saldo)

        self.__insert_person_in_db(faturamento, idade, nome_fantasia, celular, email_corporativo,
                                   categoria, saldo)
        formated_response = self.__format_response(person_info)

        return formated_response
    
    def __validate_input(self, nome_fantasia: str, idade: int, saldo: float) -> None:
        if (
            not nome_fantasia
            or not idade
            or not saldo
            or not isinstance(idade, int)
            or not isinstance(saldo, float)
            or not isinstance(nome_fantasia, str)
        ): raise HttpBadRequestError("Invalid input")

        def is_alpha_space(frase):
            return all(char.isalpha() or char.isspace() for char in frase)
        
        if not is_alpha_space(nome_fantasia):
            raise HttpBadRequestError("Invalid name")

    def __insert_person_in_db(self, faturamento: int, idade: int, nome_fantasia: str, 
                        celular: str, email_corporativo: str, categoria: str, saldo: int) -> None:
        
        self.__pessoa_juridica_repository.insert_person(faturamento, idade, nome_fantasia, 
                                                celular, email_corporativo, categoria, saldo)

    def __format_response(self, person_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Pessoa Jurídica",
                "count": 1,
                "attributes": person_info
            }
        }
