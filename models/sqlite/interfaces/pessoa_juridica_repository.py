from abc import ABC, abstractmethod
from typing import List
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable

class PessoaJuridicaRepositoryInterface(ABC):

    @abstractmethod
    def list_people(self) -> List[PessoaJuridicaTable]:
        pass

    @abstractmethod
    def insert_person(self, faturamento: int, idade: int, nome_fantasia: str,
                celular: str, email_corporativo: str, categoria: str, saldo: int):
        pass

    @abstractmethod
    def sacar(self, nome_fantasia: str, quantia: int):
        pass
