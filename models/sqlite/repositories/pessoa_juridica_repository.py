# pylint: disable=locally-disabled, multiple-statements, fixme, line-too-long
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable
from src.models.sqlite.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface

class PessoaJuridicaRepository(PessoaJuridicaRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_people(self) -> List[PessoaJuridicaTable]:
        with self.__db_connection as database:
            try:
                people = database.session.query(PessoaJuridicaTable).all()
                return people

            except NoResultFound:
                return []
    
    def insert_person(self, faturamento: int, idade: int, nome_fantasia: str,
                celular: str, email_corporativo: str, categoria: str, saldo: int):
        with self.__db_connection as database:
            try:
                person = PessoaJuridicaTable(
                    faturamento= faturamento,
                    idade= idade,
                    nome_fantasia= nome_fantasia,
                    celular= celular,
                    email_corporativo= email_corporativo,
                    categoria= categoria,
                    saldo= saldo
                )

                database.session.add(person)
                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception
            
    def sacar(self, nome_fantasia: str, quantia: int):
        with self.__db_connection as database:
            try:
                if quantia > 10000:
                    raise ValueError("A quantia ultrapassa o valor de saque")


                person = (database.session
                          .query(PessoaJuridicaTable)
                          .filter(PessoaJuridicaTable.nome_fantasia == nome_fantasia)
                          .one())
                
                if person.saldo < quantia:
                    raise ValueError("Saldo insuficiente")
                
                person.saldo -= quantia

                database.session.commit()
            
            except Exception as exception:
                database.session.rollback()
                raise exception
