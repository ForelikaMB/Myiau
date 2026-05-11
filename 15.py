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

def f(x,a):
    return((x%17==0) <= (x%53!=0)) or (a>=90000000-x)
for a in range(89999000,90001000):
    if all(f(x,a) for x in range(1,10000)):
        print(a)
        break