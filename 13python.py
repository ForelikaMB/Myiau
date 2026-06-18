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

# from ipaddress import *
# for i in range(33):

#     net = ip_network(f'45.172.106.203/255.255.252.0',0)
#     print(net[1])

# from ipaddress import *
# for m in range(33):
#     ip = ip_network(f'111.81.27.84/{m}',0)
#
#     print(ip, ip.netmask)

# from ipaddress import *
# for m in range(33):
#     ip = ip_network(f"133.57.64.130/{m}",0)
#     print(ip,ip.netmask)

# from ipaddress import *
# for m in range(33):
#     ip1 = ip_network(f"200.154.190.12/{m}",0)
#     ip2 = ip_network(f"200.154.184.0/{m}", 0)
#
#     if (ip_address('200.154.190.12') != ip1.broadcast_address and\
#             ip_address('200.154.190.12') != ip1.network_address and \
#             (ip_address('200.154.184.0') != ip2.broadcast_address and\
#             ip_address('200.154.184.0') != ip2.network_address)):
#             print(ip1,ip2)
#
# from ipaddress import *
# ip1 = ip_address('200.154.190.12')
# ip2 = ip_address('200.154.184.0')
# for m in range(33):
#     net1 = ip_network(f'200.154.190.12/{m}', 0)
#     net2 = ip_network(f'200.154.184.0/{m}', 0)
#     if net1==net2 and ip1 not in [net1[0],net1[-1]] and ip2 not\
#     in [net2[0],net2[-1]]:
#         print(net1)
#
# from ipaddress import *
# net1 = ip_address('201.44.240.33')
# net2 = ip_address('201.44.240.107')
# for m in range(33):
#     ip1 = ip_network(f'201.44.240.33/{m}',0)
#     ip2 = ip_network(f'201.44.240.107/{m}', 0)
#     a = ip1.network_address
#     b = ip2.network_address
#     g = bin(int(a))[2:].zfill(32)
#     d = bin(int(b))[2:].zfill(32)
#     if ip1 ==ip2:
#         if g.count("1")>=5 and d.count('1')>=5:
#     # if ip1 == ip2:
#     #     if ('.'.join(bin(x)[2:].zfill(8) for x in [201,44,240,33])).count('1')>=5  and ('.'.join(bin(x)[2:].zfill(8) for x in [201,44,240,107])).count('1')>=5:
#             print(ip1)
#
# from ipaddress import *
# for m in range(33):
#     ip = ip_network(f'98.81.154.195/255.252.0.0',0)
#     print(ip[-2])
#
# from ipaddress import *
# cnt = 0
#
# ip = ip_network(f"172.16.168.0/255.255.248.0",0)
# for net in ip:
#     g = bin(int(net))[2:].zfill(32)
#     if g.count('1')%5!=0:
#         cnt+=1
# print(cnt)
#
# from ipaddress import *
# ip = ip_network(f"203.111.195.0/255.255.240.0",0)
# cnt=0
# for net in ip:
#     g = bin(int(net))[2:].zfill(32)
#     if g.count('0')%3==0 and '111' in g and '000' in g:
#         cnt+=1
# print(cnt)
#
# from ipaddress import *
# ip = ip_network(f"123.222.111.192/255.255.255.248",0)
# cnt=0
# for net in ip:
#     b = f'{int(net):b}'
#     if b[-8:].count("0")%3!=0:
#         cnt+=1
# print(cnt)

# from ipaddress import *
# ip = ip_network(f'191.128.66.83/255.192.0.0',0)
# print(ip[-2])

# from ipaddress import *
# ip = ip_network(f'172.95.116.174/255.255.192.0', 0)
# print(ip[1])

# d = []
# from ipaddress import *
# ip = ip_network(f'192.168.12.207/255.192.0.0',0)
# for m in ip :
#     b = f'{int(m):b}'
#     if b.count('0') == b.count('1'):
#         d.append(m)
# print(max(d))

# from ipaddress import *
# ip = ip_network(f'46.29.170.214/255.255.128.0',0)
# a = []
# for m in ip.hosts():
#     oct =  sorted([int(x) for x in str(m).split('.')])
#     if oct[0] + oct[1] + oct[2] == oct[3]:
#         a.append(m)
# print(a[-1])

# from ipaddress import *
# for m in range(33):
#     ip1 = ip_network(f'200.154.190.12/{m}',0)
#     ip2 = ip_network(f"200.154.184.0/{m}",0)
#     if ip1==ip2:
#         print(ip1,ip2)

# from ipaddress import *
# ib = ip_address(f'144.131.211.37')
# for m in range(33):
#     cnt=0
#     ip = ip_network(f'143.131.211.37/{m}',0)
#     b = f"{int(ib):b}"
#     if m == 10 :
#         cnt+=1
#     if cnt == 15:
#         b = ip.netmask
#         v = f'{int(b):b}'
#         print(m)
#         break

# from ipaddress import *
# ans = []
# for m in range(32,0,-1):
# net = ip_network(f'143.131.211.37/{m}', 0)
# cnt = 0
# for ip in net:
# b = f'{ip:b}’
# if b.count('1') == 10:
# cnt += 1
# if cnt == 15:
# print(m)
# break

# from ipaddress import  *

# for a in range(1,256):
#     b = ip_address(f'192.214.{a}.184')
#     ip = ip_network(f"192.214.{a}.184/255.255.255.224",0)
#     for k in b:
#         if f'{int(k):b}'.count('1')>15:
#            print(ip)


# from ipaddress import ip_network, ip_address

# # Исходные адреса
# ip1 = ip_address('95.24.2.9')
# ip2 = ip_address('95.24.3.10')

# # Находим общую сеть (маска будет определена автоматически)
# # strict=False позволяет создать сеть, даже если IP не является чистым сетевым адресом
# network = ip_network(f"{ip1}/{ip2}", strict=False)

# count = 0

# # Перебираем все адреса в сети
# for ip in network:
#     # Переводим IP в целое число, затем в двоичную строку (без префикса '0b')
#     binary_str = bin(int(ip))[2:]
    
#     # Считаем количество нулей
#     zero_count = binary_str.count('0')
    
#     # Проверяем условие: чётное количество нулей
#     if zero_count % 2 == 0:
#         count += 1

# print(count)


from ipaddress import *
b = ip_network(f'190.202.83.62/255.255.252.0',0)
print((b[-2]))