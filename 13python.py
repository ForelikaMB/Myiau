# print('.'.join(bin(x)[2:].zfill(8) for x in [148,196,140,28]))
# print('.'.join(bin(x)[2:].zfill(8) for x in [148,196,140,0]))

# from ipaddress import *
# for m in range(33):
#     ip = ip_network(f'148.196.140.28/{m}',0)
#     print(ip)

# print('.'.join(bin(x)[2:].zfill(8) for x in [215,181,200,27]))
# print('.'.join(bin(x)[2:].zfill(8) for x in [215,181,192,0]))
# print(int('11110000',2))
# from ipaddress import *
# for m in range(33):
#     ip = ip_network(f'215.181.200.27/{m}',0)
#     print(ip, ip.netmask)
# from ipaddress import *
# for m in range(33):
#     ip = ip_network(f'76.155.48.2/{m}',0)
#     print(ip)
# from ipaddress import *
# for m in range(33):
#     ip = ip_network(f'108.133.75.91/{m}',0)
#     print(ip, ip.num_addresses)

# from ipaddress import *
# net = ip_network('172.16.192.0/255.255.192.0',0)
# cnt = 0
# for ip in net:
#     ipb = f'{ip:b}'
#     if ipb.count('1')% 5 !=0:
#         cnt +=1
# print(cnt)

# from ipaddress import *
# net = ip_network('172.16.192.0/255.255.192.0',0)
# cnt = 0
# for ip in net.hosts():
#     ipb = f'{ip:b}'
#     if ipb[16:].count('0') % 2 !=0:
#         if ipb[:16].count('1')<= ipb[16:].count('0'):
#             cnt +=1
# print(cnt)

# print('.'.join(bin(x)[2:].zfill(8) for x in [84,77,47,132]))
# print('.'.join(bin(x)[2:].zfill(8) for x in [84,77,48,132]))

# from ipaddress import *
# for m in range(33):
#     ip = ip_network(f'98.162.71.94/{m}',0)
#     print(ip)

# print('.'.join(bin(x)[2:].zfill(8) for x in [98,162,71,94]))
# print('.'.join(bin(x)[2:].zfill(8) for x in [98,162,71,64]))

# print('.'.join(bin(x)[2:].zfill(8) for x in [215,181,200,27]))
# print('.'.join(bin(x)[2:].zfill(8) for x in [215,181,192,0]))
# from ipaddress import *
# for m in range(32):
#     ip = ip_network(f'215.181.200.27/{m}',0)
#     print(ip, ip.netmask)

# from ipaddress import *
# for m in range(33):

#     ip = ip_network(f'76.155.48.2/{m}',0)
#     print(ip,ip.netmask)

# from ipaddress import *
# for m in range(33):
#     ip = ip_network(f'108.133.75.91/{m}',0)
#     print(ip,ip.num_addresses)

# from ipaddress import *
# for m in range(33):
#     ip1 = ip_network(f'157.127.182.76/{m}',0)
#     ip2 = ip_network(f'157.127.190.80/{m}',0)
#     if ip1 != ip2:

#         print(ip1,ip1.netmask,'     ',ip2,ip2.netmask)

# from ipaddress import *
# for m in range(33):
#     ip1 = ip_network(f'118.187.59.255/{m}',0)
#     ip2 = ip_network(f'118.187.65.115/{m}',0)
#     if ip1 != ip2:
#         if (ip_address('118.187.59.255') != ip1.broadcast_address and\
#         ip_address('118.187.59.255') !=ip1.network_address and\
#         (ip_address('118.187.65.115') !=ip2.broadcast_address and\
#         ip_address('118.187.65.115') !=ip2.network_address)):
# #             print(ip1, ip2)

# from ipaddress import *
# net = ip_network(f'105.224.200.224/255.255.255.224',0)
# cnt=0
# for ip in net:
#     b =bin(int(ip))[2:].zfill(32)
#     if b.count('1')%4==0:
#         cnt+=1   
# print(cnt)

from ipaddress import *
for i in range(33):

    net = ip_network(f'45.172.106.203/255.255.252.0',0)
    print(net[1])