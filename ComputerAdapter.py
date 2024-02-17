from IDevice import IDevice
from IComputableDevice import IComputableDevice

class ComputerAdapter(IDevice):

    def __init__(self, computingDevice: IComputableDevice) -> None:
        self.Device = computingDevice

    def getName(self):
        return self.Device.getName()
    
    def getState(self):
        return self.Device.getState()
    
    def switchON(self):
        self.Device.turnOn()
    
    def switchOFF(self):
        self.Device.turnOff()
        