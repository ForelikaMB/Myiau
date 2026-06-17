# i = "3"*116
# while '333' in i or '7777' in i:
#     if '333' in i:
#         i = i.replace("333","77",1)
#     else: i = i.replace("7777","3",1)
# print(i)
# i = "AB"*52
# while 'AA' in i or 'BB' in i or 'AB' in i:
#         i = i.replace("AA","B",1)
#         i = i.replace("BB","A")
#         i = i.replace("AB","BA")
# print(i)
# for n in range(4,10000):
#     s = "1"+ n*"8"
#     while "18" in s or "388" in s or "888" in s:
#         if "18" in s:
#             s = s.replace("18","8",1)
#         if "388" in s:
#             s = s.replace("388","81",1)
#         if "888" in s:
#             s = s.replace("888","3",1)
#     if s.count('1')==3:
#         print(n)
#         break
# a = set()
# for i in range(2,1000):
#     s = i*"8"
#     while '555'in s or "888"in s :
#         s = s.replace("555","8",1)
#         s = s.replace("888","55",1)
#     a.add(s)
# print(len(a))
# print(a)

# s = '>' + 10*"1" + 20*"2"+ 30*"3"
# while ">1" in s or ">2"in s or ">3" in s:
#     if ">1" in s:
#         s = s.replace(">1","22>",1)
#     if ">2" in s:
#         s = s.replace(">2","2>",1)
#     if ">3" in s:
#         s = s.replace(">3","1>",1)
    
# print(sum(int(x) for x in s[:-1]))
# a = 0
# for n in range(301,1000):
#     s = n*'5'
#     while "55555" in s:
#         s= s.replace('55555','88',1)
#         s = s.replace('888','55',1)
#     if s.count('5') > a:
#         a = s.count('5')
#         print(n,a)
# for x in range(100):
#     for y in range(100):
#         for z in range(100):
#             s = "0" + "1"*x + "2"*y + "3"*z
#             while "01" in s or "02" in s or "03" in s:
#                 s = s.replace("01","30",1)
#                 s = s.replace("02","3103",1)
#                 s = s.replace("03","1201",1)
#             if s.count("1") == 31 and s.count("2")==24 and s.count("3")==46:
#                 print(z)
#                 exit()
# for i in range(50):
#     s = 116*"7"
#     while "333" in s or "7777" in s:
#         if "333" in s:
#             s = s.replace("333","77",1)
#         else: s = s.replace("7777","3",1)
# print(s)            
# s ='1' + 80*'8'
# while "18" in s or "288" in s or "3888" in s:
#     if "18" in s :
#         s = s.replace("18","2",1)
#     if "288" in s :
#         s = s.replace("288","3",1)
#     if "3888" in s :
#         s = s.replace("3888","1",1)
# print(s)
# s = 77*'1'
# while "11" in s:
#     if "222" in s :
#         s = s.replace("222","1",1)
#     else:
#         s = s.replace("11","2",1)
    
# print(s)

b = bin(11001)[2:]
print(b)
print(int('000110010',2))