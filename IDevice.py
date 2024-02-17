from abc import ABC, abstractmethod 

class IDevice(ABC):

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getState(self):
        pass

    @abstractmethod
    def switchON(self):
        pass

    @abstractmethod
    def switchOFF(self):
        pass
    