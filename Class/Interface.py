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

    def CloseSshConnection(self):
        self.netConnect.disconnect()

