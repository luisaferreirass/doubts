# pylint: disable=locally-disabled, multiple-statements, fixme, line-too-long
import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pessoa_fisica_repository import PessoaFisicaRepository
from .pessoa_juridica_repository import PessoaJuridicaRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="interação com o banco")
def test_insert_person_pf():
    renda_mensal = 90
    idade = 14
    nome_completo = "Luisa Ferreira"
    celular = "84 998442447"
    email = "luisaferreirass08@gmail.com"
    categoria = "nsei"
    saldo = 70

    repo = PessoaFisicaRepository(db_connection_handler)
    repo.insert_person(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)

@pytest.mark.skip(reason="interação com o banco")
def test_list_people_pf():
    repo = PessoaFisicaRepository(db_connection_handler)

    response = repo.list_people()
    print(response)

@pytest.mark.skip(reason="interação com o banco")
def test_sacar_pf():
    repo = PessoaFisicaRepository(db_connection_handler)
    repo.sacar("João da Silva", 100)

@pytest.mark.skip(reason="interação com o banco")
def test_list_people_pj():
    repo = PessoaJuridicaRepository(db_connection_handler)
    response = repo.list_people()

    print(response)

@pytest.mark.skip(reason="interação com o banco")
def test_sacar_pj():
    repo = PessoaJuridicaRepository(db_connection_handler)
    repo.sacar("Empresa 123", 5000)

@pytest.mark.skip(reason="interação com o banco")
def test_insert_person_pj():
    faturamento = 90
    idade = 15
    nome_fantasia = "Jus"
    celular = "84 998442447"
    email_corporativo = "jus@gmail.com"
    categoria = "nsei"
    saldo = 70000

    repo = PessoaJuridicaRepository(db_connection_handler)
    repo.insert_person(faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)
