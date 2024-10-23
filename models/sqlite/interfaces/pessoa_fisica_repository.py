from abc import ABC, abstractmethod
from typing import List
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable

class PessoaFisicaRepositoryInterface(ABC):

    @abstractmethod
    def list_people(self) -> List[PessoaFisicaTable]:
        pass

    @abstractmethod
    def insert_person(self, renda_mensal: int, idade: int, nome_completo: str, 
                      celular: str, email: str, categoria: str, saldo: int):
        pass

    @abstractmethod
    def sacar(self, nome_completo: str, quantia: int):
        pass
