from Connections.DBConection import *
from netmiko import ConnectHandler
from Class.Device import *

class Interface(Device):

    def __init__(self):

        self.ip = ''
        self.name = ''
        self.neighbor = []

    def SshConnection(self, user, pswd):
        self.con = {
            'device_type': 'cisco_ios',
            'host': self.ip,
            'username': user,
            'password': pswd
        }

        self.netConnect = ConnectHandler(**self.con)

    def Mapping_topology(self):
        print(self.hostname + '\n'\
              'esta conectado por')

    def ChangeBannerMtod(self, bm):
        self.netConnect.config_mode()
        self.netConnect.send_command('banner mtod q %s q'.format(bm))

    def CloseSshConnection(self):
        self.netConnect.disconnect()

