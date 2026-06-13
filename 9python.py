# f = open("2.txt")
# cnt = 0
# for s in f:
#     a = sorted([int(x)for x in s.split()])
#     if ():#условие задачи
#         cnt +=1
# print(cnt)

# f = open("2.txt")
# cnt= 0
# for s in f :
#     a = sorted([int(x) for x in s.split()])
#     if (a[3]>a[0]*a[1]*a[2]) or (a[3]-a[2]==a[2]-a[1] and a[2]-a[1]==a[1]-a[0]):
#         cnt+=1
# print(cnt)
# count = 0
# for s in open('text.txt'):
#     M = [int(x) for x in s.split()]
#     A = [x for x in M if M.count(x) > 1]
#     B = [x for x in M if M.count(x) == 1]
#     if len(B) > 0 and len(A) > 0:
#         if (sum(B) / len(B)) > (sum(A) / len(A)):
#             count += 1
# print(count) 
# count = 0 
# f = open('by.txt')
# for i in f:
#     a = sorted([int(x) for x in i.split()])
#     if ((a[0] not in (a[1],a[2])) and (a[2]**2 > a[0]**2+a[1]**2)):
#         count+=1
# print(count)
# f = open("tip.txt")
# print(f)
# cout = []
# for i in f :
#     a = sorted([int(x) for x in i.split()])
#     if (set(a.count)==3) and (a[2]**2<a[1]**2+a[0]**2):
#         cout+=1
# print(cout)
# f = open('tip.txt')
# cnt = 0
# for i in f:
#     a = sorted([int(x)for x in i.split()])
#     if ((set(a.count)==3) and ((a.count) <=5 )) and (a[0]>= a[1] or a[0]>= a[2] or a[0]>= a[3] or a[0]>= a[4] or a[0]>=a[5]):
#         cnt+=1
#         print(cnt)

# cnt = 0 
# for i in open('4.txt'):
#     a = [int(x)for x in i.split()]
#     if (a[0]==90 and int(int(a[0])+ int(a[1]) +int(a[-1]))==180) or \
#        (a[1]==90 and int(int(a[0])+ int(a[1]) +int(a[-1]))==180) \
#     or (a[-1]==90 and int(int(a[0])+ int(a[1]) +int(a[-1]))==180):
#         cnt+=1
#         print(a)
# print(cnt)

# cnt = 0
# for i in open('4.txt'):
    
#     a = sorted([int(x)for x in i.split()])
#     if (a[0]==90 and ((a[1]) +(a[-1]))==90) or (a[1]==90 and ((a[0] +(a[-1]))==90) or (a[-1]==90 and ((a[0])+ (a[1])))==90):
#         cnt+=1
#         print(a)
# print(cnt)

# cnt = 0
# for i in open("tx3.txt"):
#     a = sorted([int(x) for x in i.split()])
#     if abs(int(a[-1])-int(a[0]))**3<=(int(a[1])+int(a[2]))**2:
#         cnt+=1
# print(cnt)

# zov = set()
# Odinakovie = []
# NeOdinacovie = []
# for i in open('tx4.txt'):
#     a = sorted([int(x)for x in i.split()])
#     print(a)

# cnt = 0
# for i in open('h67.txt'):
#     a = ([int(x)for x in i.split()])
#     per = [x for x in a if a.count(x)==3]
#     penis2 = [x for x in a if a.count(x)==1]
#     if len(per) == 3 and len(penis2)== 3:
#         if (sum(per))**2 > (sum(penis2))**2:
#             cnt+=1
# print(cnt)

# cnt = 0 
# for i in open("1.txt"):
#     a = sorted([int(x)for x in i.split()])
#     if a[-1]<(a[0]+a[1]+a[2]):
#         if a[0]+a[3] == a[1]+a[2]:
#             cnt+=1
# print(cnt)

# cnt = 0
# for i in open('1.txt'):
#     a = sorted([int(x) for x in i.split()])
#     pre = [x for x in a if a.count(x)==2]
#     # vto = [x for x in a  if a.count(x)== 2]
#     tri = [x for x in a if a.count(x)== 1]
#     if len(pre)== 4 and len(tri)== 3:
#         if sum(pre)/4 < sum(tri)/3:
#             cnt+=1
# print(cnt)

# cnt =0
# for i in open('1.txt'):
#     a = [int(x) for x in i.split()]
#     b = [x for x in a if a.count(x)==2]
#     c = sorted([x for x in a if a.count(x)==1])
#     if len(b)==2 and len(c)==5:
#         if ((c[0])*(c[1])*(c[2]))>(b[0])**2:
#             cnt+=1
# print(cnt)

# cnt=0
# for i in open('1.txt'):
#     a = sorted([int(x) for x in i.split()])
#     b = [x for x in a if a.count(x)== 2]
#     c = [x for x in a if a.count(x)== 1]
#     if len(c)==2 and len(b)==2:
#         if ((b[0]%2 ==0) and (b[1]%2 ==0)) and ((c[0]%2!=0) and (c[1]%2!=0)):
#             cnt+=1
# print(cnt)

# cnt= 0
# for i in open('1.txt'):
#     a = sorted([int(x)for x in i.split()])
#     b = [x for x in a if a.count(x)==2]
#     c = sorted([x for x in a if a.count(x)==1])
#     if len(b)==2 and len(c)==5 and c.count(a[0])==1 and c.count(a[-1])==1:
#         cnt+=1
# print(cnt)

# cnt=0
# for i in open('1.txt'):
#     a = ([int(x)for x in i.split()])
#     b = sorted([x for x in a if a.count(x)%2==0])
#     if len(b)==len(a)-len(b):
#         if (b[0]+b[2])==(b[1]+b[1])==(b[3]+b[0]):
#                 cnt +=1
# print(cnt)

# cnt = 0
# for i in open('1.txt'):
#     bruh = ([int(x) for x in i.split()])
#     a = len(bruh) != len(set(bruh))
#     b = sum(1 for x in bruh if x % 2 != 0)==3
#     if a != b:
#         cnt+=1
# print(cnt)

# f = open('9.txt')
# k = 0
# for s in f:
#     a = [int(x) for x in s.split()]
#     a1 = [x for x in a if a.count(x)==4]

#     if len(a1)==4 :
#         a2 = [x for x in a if x != a[0]]
#         if a1[0] ** 2 < sum(a2):
#             k+=1
#         print(k,a)

f = open('1.txt')
k = 0 
for s in f :
    a = [int(x) for x in s.split()]
    if (a[0] +  a[1] + a[2] + a[3])==180:
        k+=1
print(k)
    
            