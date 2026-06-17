# c = 4*625**9-25**15+2*5**11-7
# cnt = 0
# while c>0:
#     if c%5==4:
#         cnt+=1
#     c//=5
# print(cnt)

# cnt =0
# x = 7*512**1912 + 6*64**1954 - 5*8**1991 - 4*8**1980 - 2022
# while x>0:
#     if x%8 == 7:
#         cnt +=1
#     x//=8
# print(cnt)

# x = 1331**650 - 55*121**610+77*11**510-3*11**100-221
# cnt=0
# while x>0:
#     if x%11==10:
#         cnt +=1
#     x//=11
# print(cnt)

# x = 9**8 + 3**25 - 14
# s = 0
# while x>0:
#     s += x%3
#     x//=3
# print(s)

# x = 8**888 + 15*15**1515-2**444
# s = oct(x)[2:]
# print(sum(s.count(f'7{x}') for x in '123456'))

# for x in '0123456789ABCDE':
#     x = int('123' + x + '5',15)+ int('1'+x +'233',15)
#     if x%14==0:
#         print(x//14)
#         break

# for x in '0123456789ABCDEFGHIJKL':
#     x = int('18'+ x + '89957',22)+ int('80'+x+ "33",22) + int('521'+x+'6',22)
#     if x%21==0:
#         print(x//21)
#         break

# for x in '0123456789ABCDEFGHIJKL':
#     for y in '0123456789ABC':
#         c = int(x + '23' + x + '5',22) - int('67'+y + '9' + y,13)
#         if c%57== 0:
#             print(x,y, c//57)

# for x in range(1,2301):
#     cnt = 0 
#     c = 7**350+7**150-x
#     while c>0:
#         if c%7==0:
#             cnt+=1
#         c//=7
#     if cnt==200:
#         print(x)

# mx = 0
# for x in range(1,3001):
#     cnt = 0
#     c = 4**210+4**110-x
#     while c>0:
#         if c%4 == 0:
#             cnt+=1
#         c//=4
#     if cnt>mx:
#         mx =cnt
#         print(x)

# c = 2*2401**525 +3 *343**524 - 4*49**523+5*49**522-6*7**521-35
# cnt = 0
# while c>0:
#     if c%49 <=9:
#         cnt+=1
#     c//=49
# print(cnt)

# cnt=0
# c = 30*36**231+18*6**101-3*36**45-2357
# while c>0:
#     if ((c%36)%3==0 or (c%36)%5==0) and (not((c%36)%3==0 and (c%36)%5==0)):
#         cnt+=1
#     c//=36
# print(cnt)


# bim = ()
# for x in range(1,2031):
#     cnt = 0
#     c = 6**2030+6**100-x
#     while c>0:
#         if c%6==0:
#             cnt+=1
#         c//=6
#     print(cnt)
#     break

# for a in range(1,100_000):
#     cnt = [0,0,0]
#     c = 3**10+3**7+3**2+2-a
#     while c >0:
#         cnt[c%3]+=1
#         c//=3
#     if cnt[0]==cnt[1]==cnt[2]:
#         print(a)
#         break

# c = (2**345+16**65-4**135)*(8**120-2**89)
# s = 0
# while c>0:
#     if c%8!=0:
#         s+=(c%8)
#     c//=8
# print(int('632',8))


# for x in range(2,100):
#     sum = 0
#     c = (99+3*9**x)*9**x+99+9**9
#     while c>0:
#         sum+=c%9
#         c//=9
    
# print(sum)

# for x in '0123456789ABCD':
#     try:
#         c = int(f'122{x}3',15) + int(f'12{x}3',17)
#     except:
#         continue
#     if c%11 == 0:
#         print(c//11)

# for y in '0123456789ABCDEFG':
#     for x in '0123456789ABC':
#         c = int(f'233{x}1',15)+int(f'68{y}9',17)
#         if c%131==0:
#             print(x,y,c//131)
    
# for x in range(100_000):
#     if len(hex(x)[2:])<=8:
#         if len(bin(x)[2:])>=11:
#             if x[-1]==5:
#                 print(x)

# print(int('10000000000', 8)) 
# print(int('ffffffff', 16))
# print((4294967295 - 1073741824) // 10 + 1)

# sum = 0
# for x in range(158):
#     c1 = 2*158**4 + 7 *158**3 + 3*158**2 + x*158**1 + 2*158**0
#     c2 = 1*158**4 + x*158**3 + 3*158**2 + 9*158**1 + 0*158**0
#     c3 = c1+c2
#     if c3%73==0:
#         sum+=(c3//73)
# print(sum)

# for p in range(100):
#     for x in range(p):
#         for y in range(p):
#             for z in range(p):
#                 for w in range(p):
#                     c1 = z*p**4 + x*p**3 + y*p**2 + x*p**1 + 9*p**0
#                     c2= x*p**4 + y*p**3 + 7*p**2 + 4*p**1 + 8*p**0
#                     c3= w*p**4 + z*p**3 + x*p**2 + 6*p**1 + 1*p**0
#                     if c1+c2==c3:
#                         print(x*p**3 + y*p**2+ z*p**1 + w*p**0)

# cnt = []
# ma = 0
# for x in '0123456789ABCDEFGHIJK':
#     for y in '0123456789ABCDEFGHIJK':
#         b =int(f"943697{x}21",21)-int(f"2{y}9253",21)
#         if b%20==0:
#             max==b
#             cnt.append(ma//2)

# print(max(ma))

# from string import*
# for x in printable[:21]:
#     for y in printable[:21]:
#         q1 = int(f'32{y}{x}A',21)
#         q2 = int(f'16{y}18',21)
#         q = q1 + q2
#         if q % 12 == 0:
#             print(y,q//12)
# c = []
# cnt = 0
# for x in range(1,2300):
    
#     v = 7**350 + 7**150 - x
#     while x>0:
#         if x%7 == 0:
#             cnt+=1
#         if cnt==200:
#             c.append(x)
# print(min(c))

# n = []
# for x in '0123456789ABCDEFGHIGKLMNOPQRS':
#     v = int(f'42{x}158',29) + int(f'16{x}234',29)
#     if v%28==0:
#         n.append(x)

# print((int(f'42A158',29) + int(f'16A234',29))//28)

from string import printable
v = 2*729**75 + 2*243**78 + 81**81 + 2*9**87 +58
cb=[]
while v>0:
    cb.append(v%27)
    v//=27
print(cb.count(0))
