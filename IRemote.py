from abc import ABC, abstractmethod 
from IDevice import IDevice

class IRemote(ABC):

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def switchOff(self):
        pass

    @abstractmethod
    def switchOff(self, device:IDevice):
        pass

    @abstractmethod
    def switchON(self, device:IDevice):
        pass



