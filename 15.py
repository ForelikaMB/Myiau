# def f(x,a):
#     return(x%a!=0) <= ((x%6==0) <= (x%9!=0))
# for a in range(1,1000):
#     if all(f(x,a) for x in range(1,1000)):
#         print(a)

# def g(x,a):
#     return(x%a!=0) <= ((x%24==0) <= (96%x!=0))
# for a in range(1,1000):
#     if all(g(x,a) for x in range(1,1000)):
#         print(a)

# def g(x,y):
#     return(x%20==0) <= (x%11!=0) or (x+y>=300)
# for y in range(1,1000):
#     if all(g(x,y) for x in range(1,1000)):
#         print(y)

# def g(x,a):
#     return(x%a!=0) <= ((x%28==0)<=(x%49!=0))
# for a in range(1,1000):
#     if all(g(x,a) for x in range(1,1000)):
#         print(a)

# def f(x,a):
#     return(a%25==0) and (((x%24==0)and (x%75==0))<= (x%a==0))
# cnt = 0
# for a in range(-1000,1000):
#     if a == 0: continue
#     if all(f(x,a) for x in range(-1000,1000)):
#         cnt+=1
# print(cnt)

# def f(x,a):
#     return((x%17==0) <= (x%53!=0)) or (a>=90000000-x)
# for a in range(89999000,90001000):
#     if all(f(x,a) for x in range(1,10000)):
#         print(a)
#         break

# отрезки

# def f(x):
#     p = 57892<=x<=478683
#     q = 123456<=x<=760123
#     r = 592916<=x<=977654
#     a = a1<=x<=a2
#     return q <= ((not p) <= (((not r) and (not a)) <= (not
# q)))
# ox = [y for x in (57892,123456,592916,478683,760123,977654) 
# for y in (x, x+0.01, x-0.01)]
# m = []
# for a1 in ox:
#     for a2 in ox:
#         if a2>a1 and all(f(x)==1 for x in ox):
#             m.append(a2-a1)
# print(round(min(m)))

#графики
# def f(x,y,a):
#     return ((y+2*x)<a) or (x>15) or (y>30)
# for a in range(1000):
#     if all(f(x,y,a) for x in range(1000) for y in range(1000)):
#         print(a)
#         break

# def f(x,y,a):
#     return ((2*x +3*y)>30) or ((x+y)<=a)
# for a in range(1000):
#     if all(f(x,y,a) for x in range(1000) for y in range(1000)):
#         print(a)
#         break

# def f(x,y,a):
#     return ((2*x + y )!=70) or (x<y) or (a<x)
# for a in range(1000):
#     if all(f(x,y,a) for x in range(1000) for y in range(1000)):
#         print(a)
        
# def f(x,y,a):
#     return (x*y<120) or (y>a) or (x>a)
# for a in range(1000):
#     if all(f(x,y,a) for x in range(1000) for y in range(1000)):
#         print(a)
        
# def f(x,y,a):
#     return ((680*y + 256*x)<a) or ((5*x + 3*y)>11111)
# for a in range(10000000):
#     if all(f(x,y,a) for x in range(10000000) for y in range(10000000)):
#         print(a)
        
#коньюнкция 

# def f(x,y):
#     return((x&52!=0)and(x&48==0))<= (not(x&y==0))
# for y in range(1000):
#     if all(f(x,y) for x in range(1000)):
#         print(y)
#         break
# print(bin(52)[2:])
# print(bin(48)[2:])
# print(int('100',2))

# def f(x,y):
#     return (x&29==0)or ((x&11==0)<=(not(x&y==0)))
# for y in range(1,1000):
#     if all(f(x,y) for x in range(15,31)):
#         print(y)
#         break

# def f(x,y):
#     return (x&y!=0)<=((x&698==0)<=(x&321!=0))
# for y in range(1,2000):
#     if all(f(x,y) for x in range(1,2000)):
#         print(y)
        
# def f(x,y):
#     return (x&y!=0)<=(((x&17==0)and(x&5==0))<=(x&3!=0))
# for y in range(1000):
#     if all(f(x,y) for x in range(1000)):
#         print(y)

# def f(x,y):
#     return ((x&49)==0)<=((x&28!=0)<=(x&y!=0))
# for y in range(1000):
#     if all(f(x,y) for x in range(1000)):
#         print(y)
#         break