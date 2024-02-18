from IDevice import IDevice
from DeviceStateEnum import *

class DeviceMenu(object):

    def __init__(self, name:str) -> None:
        self.name = name
        self.count = 0
        self.DeviceList : IDevice = []

    def addItem(self, device: IDevice) -> None:
        self.DeviceList.append(device)
        self.count += 1
        # device.switchON()
        print(f"{device.getName()} is now ON. ")

    def popLast(self) -> IDevice:
        print(f"{self.DeviceList[self.count-1]} is now going to be OFF. ")
        popedDevice = self.DeviceList.pop(self.count - 1)
        popedDevice.SwitchOFF()
        self.count -= 1
        return popedDevice

    
    def popDevice(self, device:IDevice) -> IDevice:
        for i in range(self.count):
            if self.DeviceList[i] == device:
                print(f"{self.DeviceList[i].getName()} is now going to be OFF. ")
                # self.DeviceList[i].switchOFF()
                poppedDevice = self.DeviceList.pop(i)
                return poppedDevice
    