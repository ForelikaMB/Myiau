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

print('.'.join(bin(x)[2:].zfill(8) for x in [98,162,71,94]))
print('.'.join(bin(x)[2:].zfill(8) for x in [98,162,71,64]))