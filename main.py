from TV import TV
from Computer import Computer
from Remote import Remote
from DeviceMenu import DeviceMenu
from ComputerAdapter import ComputerAdapter


deviceMenu1 = DeviceMenu("DeviceMenu1")
remote1 = Remote("Remote1", deviceMenu1)
tv1 = TV("TV1")
remote1.switchON(tv1)

computer1 = Computer("PC-1")
computerAdapter = ComputerAdapter(computer1)
remote1.switchON(computerAdapter)

tv2 = TV("TV-2")
remote1.switchON(tv2)

# print(remote1.LastUsedDevice.getName())
remote1.undo()

