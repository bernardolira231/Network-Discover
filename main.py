from Class.Interface import *
from Connections.DBConection import *
from Connections.networkCon import *
import netmiko
import pymysql


def main():
    ip = input('Ingrese la ip del dispositivo a conctar: ')
    user = input('Cual es su usuario del ssh: ')
    pswd = input('Ingrese la contraseña del usuario ssh: ')

    FD = Interface(ip)
    FD.SshConnection(user, pswd)
