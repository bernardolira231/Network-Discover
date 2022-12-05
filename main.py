from Class.Device import *
from Connections.DBConection import *
from Connections.cdp import *


def main():
    l = []
    q = []
    sql = sqlconect()
    ip = input('Ingresa la ip del dispositivo a conectar: ')
    user = input('Ingresa el usuario de ssh: ')
    pswd = input('Ingresa la contraseña del ssh: ')
    con = connectssh(ip, user, pswd)
    l.append(ip)
    l, net_connect, q = cdp(con, l, q)
    net_connect.disconnect()

    print(f'1. {l}')
    print(f'1. {q}')

    for i in range(100):
        if i != 0:
            user = input('Ingresa el usuario de ssh: ')
            pswd = input('Ingresa la contraseña del ssh: ')
            con = connectssh(l[i], user, pswd)
            l, net_connect, q = cdp(con, l, q)
            net_connect.disconnect()

    print(f'2. {l}')
    print(f'2. {q}')

    dev = []
    for i in q:
        if i[0] == 'R' or i[0] == 'r':
            dev.append(['Router', i])
            sql.insertValues(dev)
        elif q[0] == 'S' or q[0] == 's':
            dev = ['Switch', q]
            sql.insertValues(dev)

    sql.insertValuesInterface(l)

if __name__ == "__main__":
    main()
