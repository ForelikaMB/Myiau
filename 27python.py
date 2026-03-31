# def center(c):
#     mindist = 10**10
#     xc = yc = 0
#     for i in c:
#         curl = 0
#         for j in c:
#             curl += ((i[0]-j[0])**2 + (i[1]-j[1])**2)**0.5
#         if curl < mindist:
#             mindist,xc,yc = curl,i[0],i[1]
#     return xc, yc

# f = open('27B_1.txt')
# c1 = []; c2 = []; c3=[]
# for s in f:
#     x, y = map(float, s.split())
#     if y < 3: c1.append([x,y])
#     if 3 <= y <= 7: c2.append([x,y])
#     if y > 7: c3.append([x,y])
# x1,y1 = center(c1)
# x2,y2 = center(c2)
# x3,y3 = center(c3)
# print(int((x1+x2+x3)*10000/3), int((y1+y2+y3)*10000/3))




# def center(c):
#     mindist = 10**10
#     xc = yc = 0
#     for i in c:
#         curl = 0
#         for j in c:
#             curl += ((i[0]-j[0])**2 + (i[1]-j[1])**2)**0.5
#         if curl < mindist:
#             mindist,xc,yc = curl,i[0],i[1]
#     return xc, yc

# f = open('27B_2.txt')
# c1 = []; c2 = []; c3=[]
# f.readline()
# for s in f:
#     x, y = map(float, s.replace(',','.').split())
#     if y < -x+8: c1.append([x,y])
#     elif y < 6 and x > 7: c2.append([x,y])
#     else: c3.append([x,y])
# x1,y1 = center(c1)
# x2,y2 = center(c2)
# x3,y3 = center(c3)
# print(int((x1+x2+x3)*100000/3), int((y1+y2+y3)*100000/3))

from ipaddress import *
ip = ip_network(f"123.222.111.192/255.255.255.248",0)
cnt=0
for net in ip:
    b = f'{int(net):b}'
    if b[-8:].count("0")%3!=0:
        cnt+=1
print(cnt)