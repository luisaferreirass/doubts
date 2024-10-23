from abc import ABC, abstractmethod
from typing import Dict

class PFCreaterControllerInterface(ABC):

    @abstractmethod
    def create(self, people_info: Dict) -> Dict:
        pass
