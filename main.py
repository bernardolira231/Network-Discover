from Class.Device import *
from Connections.DBConection import *


def main():
    sqlConection = sqlconect()
    ip = input('Ingrese la ip del dispositivo a conctar: ')
    user = input('Cual es su usuario del ssh: ')
    pswd = input('Ingrese la contraseña del usuario ssh: ')
    device = Device()
    device.ip = ip
    device.createSshDict(user, pswd)
    device.getHostname()
    dev = (device.tipo, device.hostname)
    inte = (device.ip, device.hostname)
    sqlConection.insertValues(dev, inte)


if __name__ == "__main__":
    main()
