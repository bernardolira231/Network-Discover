import netmiko
from netmiko.ssh_dispatcher import ConnectHandler

def Dict(ip, user, pswd):
    con = {
            'device_type': 'cisco_ios',
            'host': ip,
            'username': user,
            'password': pswd
        }

    return con

