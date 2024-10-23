from typing import List
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable
from src.controllers.pf_lister_controller import PFListerController
from src.controllers.pj_lister_controler import PJListerController

class MockRepositoryPF:
    def list_people(self) -> List[PessoaFisicaTable]:
        return [
            PessoaFisicaTable(renda_mensal= 800, idade=12, nome_completo="Luisa Ferreira", 
                              celular="84998442447", email="nn", categoria="mm", saldo=900, id=1),
            PessoaFisicaTable(renda_mensal= 870, idade=17, nome_completo="Nina Ferreira", 
                              celular="849559848", email="nn", categoria="mm", saldo=7700, id=2)
        ]
    
class MockRepositoryPJ:
    def list_people(self) -> List[PessoaJuridicaTable]:
        return [
            PessoaJuridicaTable(faturamento= 4500, idade= 9, nome_fantasia="BlaBla",
                                celular= "8442218", email_corporativo="kkkk", categoria= "nsei", saldo= 90000, id=4), 
            PessoaJuridicaTable(faturamento= 4500, idade= 9, nome_fantasia="Jus",
                                celular= "8442218", email_corporativo="kkkk", categoria= "nsei", saldo= 98504, id=2)]
        
def test_list_pf():
    controller = PFListerController(MockRepositoryPF())
    response = controller.list()

    expected_response =  {
            "data": {
                "type": "Pessoa Física",
                "count": 2,
                "attributes": [{
                    "id": 1, 
                    "nome_completo": "Luisa Ferreira",
                    "saldo": 900
                },
                {
                    "id": 2,
                    "nome_completo": "Nina Ferreira",
                    "saldo": 7700
                }]
            }
        }

    assert response == expected_response

def test_list_pj():
    controller = PJListerController(MockRepositoryPJ())
    response = controller.list()

    expected_response = {
        
        "data": {
                "type": "Pessoa Jurídica",
                "count": 2,
                "attributes": [{
                    "id": 4, 
                    "nome_fantasia": "BlaBla",
                    "saldo": 90000
                },
                {
                    "id": 2,
                    "nome_fantasia": "Jus",
                    "saldo": 98504
                }]
            }
        }
    
    assert response == expected_response