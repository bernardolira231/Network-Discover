from Device import *

class Interface(Device):

    def __init__(self, ip, name, id_device):

        self.ip = ip
        self.name = name
        self.id_device = id_device
