from typing import Dict
from src.controllers.pf_sacar_controller import PFSacarController
from src.controllers.pj_sacar_controller import PJSacarController

class MockRepositoryPF:
    def sacar(self, action_info: Dict):
        pass

class MockRepositoryPJ:
    def sacar(self, action_info: Dict):
        pass

def test_sacar_pf():

    action_info = {
        "nome_completo": "Luisa Ferreira",
        "quantia": 50.0
    }

    controller = PFSacarController(MockRepositoryPF)
    
    response = controller.sacar(action_info)

    expected_response = {
        "data": {
            "type": "Pessoa Física",
            "count": 1, 
            "attributes": {
                            "nome_completo": "Luisa Ferreira",
                            "quantia": 50.0
                        }
        }
    }

    assert response == expected_response

def test_sacar_pj():

    action_info = {
        "nome_fantasia": "Empresa Ferreira",
        "quantia": 5000.0
    }

    controller = PJSacarController(MockRepositoryPJ)
    
    response = controller.sacar(action_info)

    expected_response = {
        "data": {
            "type": "Pessoa Jurídica",
            "count": 1, 
            "attributes": {
                        "nome_fantasia": "Empresa Ferreira",
                        "quantia": 5000.0
                        }
        }
    }

    assert expected_response == response

