from abc import ABC, abstractmethod
from typing import Dict

class PJSacarControllerInterface(ABC):

    @abstractmethod
    def sacar(self, action_info: Dict) -> Dict:
        pass
