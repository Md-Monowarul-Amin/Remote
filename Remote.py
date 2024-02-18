from IRemote import IRemote
from IDevice import IDevice
from TV import *
from DeviceMenu import DeviceMenu
from DeviceStateEnum import DeviceState

# tv = TV("Walton")

# print(tv.get_name())


class Remote(IRemote):

    def __init__(self, name: str, deviceMenu: DeviceMenu) -> None:
        self.name = name
        self.DeviceMenu = deviceMenu
        self.LastUsedDevice = None

    def getName(self):
        return self.name

    def switchOff(self):
        self.LastUsedDevice = self.DeviceMenu.popLast()

    def switchOff(self, device:IDevice):
        device.switchOFF()
        self.LastUsedDevice = self.DeviceMenu.popDevice(device)

    def switchON(self, device:IDevice):
        device.switchON()
        self.DeviceMenu.addItem(device)
        self.LastUsedDevice = device

    def undo(self):
        if self.LastUsedDevice.getState() ==  DeviceState.OFF:
            self.switchON(self.LastUsedDevice)
        elif self.LastUsedDevice.getState() == DeviceState.ON:
            self.switchOff(self.LastUsedDevice)
            