from abc import ABC, abstractmethod
from typing import Dict

class PJCreaterControllerInterface(ABC):

    @abstractmethod
    def create(self, person_info: Dict) -> Dict:
        pass
