import netmiko

def connectssh(ip, user, pswd):
    connection = {  'device_type': 'cisco_ios',
                    'host': ip,
                    'username': user,
                    'password': pswd
                }
    return connection

def cdp(con, l, q):
    net_connect = netmiko.ConnectHandler(**con)
    cdp = 'show cdp neighbors detail'
    output = net_connect.send_command(cdp, use_textfsm=True)
    l = addlistip(output, l)
    q = addlisthost(output, q)
    return l, net_connect, q

def addlisthost(output, q):
    for i in range(len(output)):
        if output[i]['destination_host'] not in q:
            q.append(output[i]['destination_host'])
    return q

def addlistip(output, l):
    for i in range(len(output)):
        if output[i]['management_ip'] not in l:
            l.append([output[i]['management_ip']['destination_host']])
    return l

