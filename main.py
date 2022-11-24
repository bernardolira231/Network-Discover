from Class.Interface import *
from Connections.DBConection import *
from Connections.networkCon import *
import pymysql


def main():
    ip = input('Ingrese la ip del dispositivo a conctar: ')
    user = input('Cual es su usuario del ssh: ')
    pswd = input('Ingrese la contraseña del usuario ssh: ')

    FD = Interface(ip)
    FD.SshConnection(user, pswd)

    print('Menu\n')
    print('1) Cambiar Banner-Mtod')
    print('2) Cambiar Hostname')
    print('3) Cambiar ')
    a = int( input('R: ') )

    if a == 1:
        bm = input('Que banner-mtod le gustaria ingresar: ')
        FD.ChangeBannerMtod(bm)
