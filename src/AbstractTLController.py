
from abc import ABC, abstractmethod

class AbstractTLController(ABC):

    @abstractmethod
    def control_lights(self):
        pass

