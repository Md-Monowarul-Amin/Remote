from IComputableDevice import *
from DeviceStateEnum import *

class Computer(IComputableDevice):

    def __init__(self, name: str) -> None:
        self.name = name
        self.state = DeviceState.OFF

    def getName(self):
        return self.name

    def getState(self):
        # print(f"{self.getName() is {self.getState()}}")
        return self.state

    def turnOff(self):
        # print("Computer turning Off")
        self.state = DeviceState.OFF

    def turnOn(self):
        # print("Computer turning ON.")
        self.state = DeviceState.ON
