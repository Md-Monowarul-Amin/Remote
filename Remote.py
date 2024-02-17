from IRemote import IRemote
from IDevice import IDevice
from TV import *
from DeviceMenu import DeviceMenu

# tv = TV("Walton")

# print(tv.get_name())


class Remote(IRemote):

    def __init__(self, name: str, deviceMenu: DeviceMenu) -> None:
        self.name = name
        self.DeviceMenu = deviceMenu

    def getName(self):
        return self.name


    def switchOff(self):
        self.DeviceMenu.popFirst()


    def switchOff(self, device:IDevice):
        device.switchOFF()
        self.DeviceMenu.popDevice(device)


    def switchON(self, device:IDevice):
        device.switchON()
        self.DeviceMenu.addItem(device)
