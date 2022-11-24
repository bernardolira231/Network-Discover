import netmiko
from netmiko import ConnectHandler
from Device import *

class Interface(Device):

    def __init__(self, ip):

        self.ip = ip
        self.name = ""

    def SshConnection(self, user, pswd):
        self.con = {
            'device_type': 'cisco_ios',
            'host': self.ip,
            'username': user,
            'password': pswd
        }

        self.netConnect = ConnectHandler(**self.con)

    def ChangeBannerMtod(self, bm):
        self.netConnect.config_mode()
        self.netConnect.send_command('banner mtod q %s q'.format(bm))

    def CloseSshConnection(self):
        self.netConnect.disconnect()

