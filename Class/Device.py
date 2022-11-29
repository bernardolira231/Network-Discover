import netmiko
class Device():

    def __init__(self):

        self.tipo = ''
        self.hostname = ''
        self.ip = ''

    def createSshDict(self, user, pswd):
        self.con = {
            'device_type': 'cisco_ios',
            'host': self.ip,
            'username': user,
            'password': pswd
        }

    def getHostname(self):
        netConnect = netmiko.ConnectHandler(**self.con)
        output = netConnect.send_command('show running-config | include hostname').split()[1]
        netConnect.disconnect()
        self.hostname = output


    def getType(self):
        netConnect = netmiko.ConnectHandler(**self.con)
        output = netConnect.send_command('show ip interface brief')
        netConnect.disconnect()
        count = 1
        for i in output:
            if i == '\n':
                count = count +1

        if count > 10:
            self.tipo = 'Switch'
        else:
            self.tipo = 'Router'
