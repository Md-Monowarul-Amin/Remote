from IDevice import IDevice
from DeviceStateEnum import *

class DeviceMenu(object):

    def __init__(self, name) -> None:
        self.name = name
        self.count = 0
        self.DeviceList = []

    def addItem(self, device: IDevice):
        self.DeviceList.append(device)
        self.count += 1
        # device.switchON()
        print(f"{device.getName()} is now ON. ")

    def popFirst(self):
        print(f"{self.DeviceList[self.count-1]} is now going to be OFF. ")
        self.DeviceList[self.count - 1].switchOFF()
        self.DeviceList.pop(self.count - 1)
        self.count -= 1

    
    def popDevice(self, device:IDevice):
        for i in self.count:
            if self.DeviceList[i] == device:
                print(f"{self.DeviceList[i]} is now going to be OFF. ")
                # self.DeviceList[i].switchOFF()
                self.DeviceList.pop(i)
                break
    