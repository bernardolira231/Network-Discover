from Class.Device import *
from Connections.DBConection import *
from Connections.cdp import *


def main():
    l = []
    q = []
    ip = input('Ingresa la ip del dispositivo a conectar: ')
    con = connectssh(ip)
    #user = input('Ingresa el usuario de ssh: ')
    #pswd = input('Ingresa la contraseña del ssh: ')
    l.append(ip)
    l, net_connect, q = cdp(con, l, q)
    net_connect.disconnect()

    print(f'1. {l}')
    print(f'1. {q}')

    for i in range(500):
        if i != 0:
            con = connectssh(l[i])
            l, net_connect, q = cdp(con, l, q)
            net_connect.disconnect()

    print(f'2. {l}')
    print(f'2. {q}')

if __name__ == "__main__":
    main()
