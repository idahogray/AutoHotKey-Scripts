import subprocess

ip = input('New IP Address (Blank for DHCP): ')
if ip != '':
    mask = input('New Netmask (255.255.255.0): ')
    if mask == '':
        mask = '255.255.255.0'
    gateway = input('New Default Gateway (Blank): ')

netsh_call = ['runas', '/user:kgray@powereng', '\"netsh interface ipv4 set address \'Local Area Connection\'\"']
if ip == '':
    netsh_call.append('dhcp')
else:
    netsh_call.append('static')
    netsh_call.append(ip)
    netsh_call.append(mask)
    netsh_call.append(gateway)


print(netsh_call)
subprocess.call(netsh_call)
input('IP Address Changed')
