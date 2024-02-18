from IDevice import IDevice
from DeviceStateEnum import *

class TV(IDevice):

    def __init__(self, name: str, state = DeviceState.OFF) -> None:
        self.name = name
        self.state = state

    def getName(self):
        return self.name
    
    def getState(self):
        return self.state
    
    def switchON(self):
        self.state = DeviceState.ON
    
    def switchOFF(self):
        self.state = DeviceState.OFF
    