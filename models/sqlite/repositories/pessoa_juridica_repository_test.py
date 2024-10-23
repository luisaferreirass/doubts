# pylint: disable=locally-disabled, multiple-statements, fixme, line-too-long
from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable
from .pessoa_juridica_repository import PessoaJuridicaRepository


class MockConnection:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
            data = [
                (
                    [mock.call.query(PessoaJuridicaTable)],
                    [PessoaJuridicaTable(nome_fantasia="Empresa A", saldo= 345600),
                    PessoaJuridicaTable(nome_fantasia="Empresa B", saldo=600000)]
                )
            ]
        )

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def test_list_pj():
    mock_connection = MockConnection()
    repo = PessoaJuridicaRepository(mock_connection)

    response = repo.list_people()
    print(response)

def test_sacar_pj():
    mock_connection = MockConnection()
    repo = PessoaJuridicaRepository(mock_connection)
    repo.sacar("Nome", 900)

    mock_connection.session.query.assert_called_once_with(PessoaJuridicaTable)
    mock_connection.session.filter.assert_called_once_with(PessoaJuridicaTable.nome_fantasia == "Nome")
    mock_connection.session.one.assert_called_once()
    mock_connection.session.commit.assert_called_once()

def test_insert_pj():
    faturamento = 90000
    idade = 14
    nome_fantasia= "Luisa Ferreira"
    celular = "84 998442447"
    email_corporativo = "luisaferreirass08@gmail.com"
    categoria = "nsei"
    saldo = 70

    mock_connection = MockConnection()
    repo = PessoaJuridicaRepository(mock_connection)
    
    repo.insert_person(faturamento, idade, nome_fantasia, 
                       celular, email_corporativo, categoria, saldo)

    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()
