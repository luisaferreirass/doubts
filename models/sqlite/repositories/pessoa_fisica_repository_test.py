# pylint: disable=locally-disabled, multiple-statements, fixme, line-too-long
from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from .pessoa_fisica_repository import PessoaFisicaRepository


class MockConnection:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
            data = [
                (
                    [mock.call.query(PessoaFisicaTable)],
                    [PessoaFisicaTable(nome_completo="Luisa", saldo= 3456),
                    PessoaFisicaTable(nome_completo="Nina", saldo=6000)]
                )
            ]
        )

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def test_list_pf():
    mock_connection = MockConnection()
    repo = PessoaFisicaRepository(mock_connection)

    response = repo.list_people()
    print(response)

def test_sacar_pf():
    mock_connection = MockConnection()
    repo = PessoaFisicaRepository(mock_connection)
    repo.sacar("Nome", 90)

    mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
    mock_connection.session.filter.assert_called_once_with(PessoaFisicaTable.nome_completo == "Nome")
    mock_connection.session.one.assert_called_once()
    mock_connection.session.commit.assert_called_once()

def test_insert_pf():
    renda_mensal = 90
    idade = 14
    nome_completo = "Luisa Ferreira"
    celular = "84 998442447"
    email = "luisaferreirass08@gmail.com"
    categoria = "nsei"
    saldo = 70

    mock_connection = MockConnection()
    repo = PessoaFisicaRepository(mock_connection)
    
    repo.insert_person(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)

    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()
