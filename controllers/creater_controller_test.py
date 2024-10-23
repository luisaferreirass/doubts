from src.controllers.pf_creater_controller import PFCreaterController
from src.controllers.pj_creater_controller import PJCreaterController

class MockRepositoryPF:
    def insert_person(self, renda_mensal: int, idade: int, nome_completo: str, 
                      celular: str, email: str, categoria: str, saldo: int):
        pass

class MockRepositoryPJ:
    def insert_person(self, faturamento: int, idade: int, nome_fantasia: str,
    celular: str, email_corporativo: str, categoria: str, saldo: int):
        pass


def test_create_pf():
    person_info = {
        "renda_mensal": 200.0,
        "idade": 15,
        "nome_completo": "Luisa Ferreira",
        "celular": "84998442447",
        "email": "luisaferreirass08@gmail.com",
        "categoria": "sla",
        "saldo": 800.0
    }

    controller = PFCreaterController(MockRepositoryPF())

    response = controller.create(person_info)

    assert response["data"]["type"] == "Pessoa Física"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_info

def test_create_pj():
    person_info = {
        "faturamento": 200.0,
        "idade": 15,
        "nome_fantasia": "Luisa Ferreira",
        "celular": "84998442447",
        "email_corporativo": "nsei",
        "categoria": "sla",
        "saldo": 8000.0
    }

    controller = PJCreaterController(MockRepositoryPJ())
    response = controller.create(person_info)

    assert response["data"]["type"] == "Pessoa Jurídica"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_info
