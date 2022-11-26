import netmiko
class Device():

    def __init__(self):

        self.tipo = ''
        self.hostname = ''
        self.ip = ''

    def pIp(self):
        print(self.ip)

    def createSshDict(self, user, pswd):
        self.con = {
            'device_type': 'cisco_ios',
            'host': self.ip,
            'username': user,
            'password': pswd
        }


    def showInterfacesUp(self):
        netConnect = netmiko.ConnectHandler(**self.con)
        output = netConnect.send_command('show ip interface brief | include down')
        netConnect.disconnect()
        count = 1
        for i in output:
            if i == '\n':
                count = count +1
        print('Total de interfaces disponibles en S8:  %i \n\n' %(count))
