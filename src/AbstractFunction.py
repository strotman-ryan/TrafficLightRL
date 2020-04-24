

from abc import ABC, abstractmethod

class AbstractFunction(ABC):

    @abstractmethod
    def GetResult(self,time):
        pass
