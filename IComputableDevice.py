from abc import ABC, abstractmethod

class IComputableDevice(ABC):

    @abstractmethod
    def getName(self):
        pass
    
    @abstractmethod
    def getState(self):
        pass
    
    @abstractmethod
    def turnOn(self):
        pass

    @abstractmethod
    def turnOff(self):
        pass
    