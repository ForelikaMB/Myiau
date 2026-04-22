# # НОМЕР 5
# for i in range(1,1000):
#     r = bin(i)[2:]
#     r2 = ''
#     for n in r:
#         if n == "1": r2+= "10"
#         if n == "0": r2+= "01"
#     if int(r2,2 )> 63:
#         print(int(r2,2))
#         break
# def troi(n):
#     s = ""
#     while n >0:
#         s = str(n%3) + s
#         n //=3
#     return s
# for n in range(1,1000):
#     r= troi(n)
#     if n %3 == 0:
#         r = "1" + r + "02"
#     else: r += troi((n%3)*4)
#     if int(r,3)< 199:
#         print(n)
# ans = []
# for i in range(1,1000):
#     r = bin(i)[2:]
#     if i%3==0:
#         r = r + r[-3:]
#     else: r = r +  bin((i%3)*3)[2:]
#     if int(r,2)>151:
#         ans.append(int(r,2))
# print(min(ans))
# ans = []
# for n in range(1,1000):
#     r = bin(n)[2:]
#     if n %3 == 0:
#         r+= r[-3:]
#     else: r += bin((n%3)*3)[2:]
#     if int(r,2)<170:
#         ans.append(int(r,2))
# print(max(ans))
# for n in range(1,1000):
#     r = bin(n)[2:]
#     if r.count("1") %2 == 0:
#         r ="1"+ r[2:] + "0"
#     else:
#         r = "11" + r[2:] + "1"
#     if  int(r,2) >49:
#         print(n)

# for n in range(1,1000):
#     r = bin(n)[2:]
#     if r.count('1')%2==0:
#         r ="1" + r[2:] +"0"
#     else: r = "11" +r[2:] + "1"
#     if int(r,2)>49:
        
#         print(n,int(r,2))
# nt = []
# for n in range(1,1000):
#     n[0]+n[1]
#     nt+= n
#     n[1]+n[2]
#     nt +=n
#     n[2]+n[3]
#     nt +=n
# print(nt)

# for n in range(1,1000):
#     r = bin(n)[2:]
#     r = r + bin(n%3)
#     r = r + bin(r%5)
#     cnt = r
# print(int(r,2))
# def troi(n):
#     s = ""
#     while n >0:
#         s = str(n%3) + s
#         n //=3
#     return s
# for n in range(1,1000):
#     r= troi(n)
#     if n %3 == 0:
#         r = "1" + r + "02"
#     else: r += troi((n%3)*4)
#     if int(r,3)< 199:
#         print(n)
# def troi(n):
#     s = ""
#     while n >0:
#         s = str(n%3) +s
#         n//=3
#         return s
# for n in range(1,1000):
#     r = troi(n)
#     if sum(r)%3==0 :
#         r = r[-2:] +"112"
#     else:
#         r = r +troi(sum(r))
#     if (int(r,3)%2==0)<679:
#         print(r)
# def f(n):
#     s=''
#     while n > 0:
#         s = str(n%3) + s
#         n //= 3
#     return s
# c = []
# for n in range(1000):
#     s = f(n)
#     summa = s.count('1') + s.count('2')*2
#     if summa%3 == 0:
#         s = '112' + s[2:]
#     else:
#         s = s + f(summa)
#     r = int(s,3)
#     if r <= 679 and r%2 == 0:
#         c.append(r)
# print(max(c))
# count = []
# for i in range(10,1001):
#     a = bin(i)[2:]
#     a[1:]
#     while a[0]==0:
#         a[1:]
#     v = int(a,2)
#     g = int(a)-v
#     count.append(g)
# print(len(count))
# l = []
# for N in range(1,1000):
#     r = bin(N)[2:]
#     r += str((r.count('1')%2))
#     r += str((r.count('1')%2))
#     if int(r,2) >105:
#         l.append(N)
# print(min(l))
# for N in range(1,1000):
#     r = bin(N)[2:]
#     if r%3 == 0:
#         r+= r[-3:]
# l = []
# for N in range(0,256):
#     R = bin(N)[2:]
#     c = int(R,10)
#     while c != 134:
#         # for r in range(1000):
#             R.replace('0','1',1)
            
#         # for l in range(1000):
#             R.replace("0",'1',1)
#             break
# print(c-N)
# print(int('6',10))

# ДЗ 1
# a = []
# for n in range(1,1000):
#     r = bin(n)[2:]
#     r = str(r) + str(r.count('1')%2)
#     r = str(r) + str(r.count('1')%2)
#     if (int(r,2)>105):
#         a.append(n)
# print(min(a))

# s = []
# for n in range(1,1000):
#     r = bin(n)[2:]
#     if int(n)%3==0:
#          r = r + r[-3:]
#     else:
#          r = r + bin((n%3)*3)[2:] 
#     if int(r,2)<100:
#          s.append(n)
        
# print(max(s))   

# a = []
# def f(n):
#      s=''
#      while n > 0:
#          s = str(n%3) + s
#          n //= 3
#      return s
# for n in range(1,1000):
#      r = f(n)
#      if n%3 == 0 :
#           r = r + r[-3:]
#      else:
#           r = r + f((n%3)*3)
#      if int(r,3)<76:
#         a.append(n)
# print(max(a))

#4
# a = []
# for n in range(1,1000):
#     r = bin(n)[2:]
#     if (r.count("1")%2)==0:
#         r ='10' + r[2:] + '0'
#     else:
#         r = '11'+ r[2:] +'1'
#     if int(r,2)>30:
#        a.append(n)
# print(min(a))


# a = []
# for n in range(1,1000):
#     r = oct(n)[2:]
#     if (str(n).count('2')+str(n).count('4')+str(n).count('6')+str(n).count('0'))%2 != 0:
#         r = r[-3:] + '46'
#     if (str(n).count('2')+str(n).count('4')+str(n).count('6')+str(n).count('0'))%2 == 0:
#         r = oct((n%8)*5)[2:] + r
#     if n >=80:
#         r = int(r,8)
#         a.append(r)
# print(min(a))

# c = []
# for n in range(1,1000):
#     r = bin(n)[2:]
#     r = r + str((r.count('1'))%2)
#     r = r + str((r.count('1'))%2)
#     if int(r,2)<=120:
#         c.append(n)
# print(max(c))

# a = []
# for n in range(1,1000):
#     r = bin(n)[2:]
#     if r.count('0')>r.count('1'):
#         r = '10' + r[2:] + '0'
#     else:
#         r = '1' + r[:-2] + '10'
#     r = int(r,2)
#     if r >=98:
#         a.append(n)
# print(min(a))

# a = []
# def troi(n):
#     s = ''
#     while n >0:
#         s = str(n%3) +s
#         n//=3
#     return s
# for n in range(1,1000):
#     r = troi(n)
#     if n%3 == 0:
#         r = r + r[-2:]
#     else:
#         r = r +troi((n%3)*5)
#     if int(r,3) >213:
#         a.append(int(r,3))
# print(min(a))

# a=[]
# for n in range(1,1000):
#     r = bin(n)[2:]
#     if n%2==0:
#         r+='10'
#     else:
#         r= '1'+r+'1'
#     if 9<int(r,2) <99:
#         a.append(n)
# print(min(a))
# a = []
# for n in range(1,1000):
#     r = bin(n)[2:]
#     if len(r)%2==0:
#         r = r[len(r)//2:]+r[:len(r)//2]
#     if int(r,2)<=26:
#         a.append(n)
# print(max(a))

# a =[]
# for n in range(1,1000):
#     r = bin(n)[2:]
#     if n%7==0:
#         if r.count('1')%2==0:
#          r +="1"
#         else: r+='0'
#         if int(r,2)%2==0:
#          r+='10'
#         else: r+='01'
#         if int(r,2)<1000:
#          a.append(int(r,2))
# print(max(a))

# a = []
# for n in range(101,1000):
#     r = hex(n)[2:]
#     r = r.replace("b",'2')
#     if len([x for x in r if x in '13579bdf'])>2:
#         r+="e"
#     else:
#         r= "f"+ r
#         if int(r,16)>4001:
#             a.append([int(r,16),n])
# print(sorted(a))
# s = []
# for n in range(1,10000):
#     r = bin(n)[2:]
#     if r.count('0')%2==0:
#         r = r + r.count('0')*"0"
#     else: 
#         r = r.count('1')*'1' + r
#     if int(r,2)>2000:
#         s.append(n)

# print(min(s))
# c = []
# def troi(n):
#     s = ''
#     while n >0:
#          s = str(n%3) +s
#          n//=3
#     return s

# for n in range(1,1000):
#     r = troi(n)
#     if n%3==0:
#           r = r + r[-2:]
#     else:
#           r = r + troi(((n%3)*5))
#     if int(r,3)>150:
#          c.append(int(r,3))
# print(min(c))
c = ()
def troi(n):
    s = ''
    while n>0:
        s = str(n%3) + s
        n//=3
    return s
for n in range(1,1000):
    r = troi(n)
    summa = sum(int(d) for d in r )
    r = r + r[-1]
    if summa%3==0:
        r = '2'+r+'1'
    else:
        r = r + troi((summa%3)*2)
    if int(r)>1000:
        c += (int(r,3))

print(min(c))