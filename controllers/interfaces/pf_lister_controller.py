from typing import Dict
from abc import ABC, abstractmethod

class PFListerControllerInterface(ABC):

    @abstractmethod
    def list(self) -> Dict:
        pass
