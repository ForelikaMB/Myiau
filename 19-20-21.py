# def f(s,m):
#     if s >= 59: return m%2==0
#     if m == 0 : return 0
#     steps = [f(s+1,m-1),f(s+4,m-1),f(s*3,m-1)]
#     return any(steps) if m%2!=0 else all(steps)
# print([x for x in range(1,59) if  f(x,2)])
# print([x for x in range(1,59) if not f(x,1) and f(x,3)])
# print([x for x in range(1,59) if not f(x,2) and f(x,4)])

# def f(s,m):
#     if 36 <= s <= 59: return m%2==0
#     if s >60: return m%2!=0
#     if m == 0 : return 0
#     steps = [f(s+1,m-1),f(s*2,m-1),f(s*3,m-1)]
#     return any(steps) if m%2!=0 else all(steps)
# print([x for x in range(1,36) if  f(x,2)])
# print([x for x in range(1,36) if not f(x,1) and f(x,3)])
# print([x for x in range(1,36) if not f(x,2) and f(x,4)])

# def f(a,b,m):
#     if a+b>=259: return m%2==0
#     if m == 0 : return 0
#     steps = [f(a+1,b,m-1),f(a*2,b,m-1),f(a,b+1,m-1),f(a,b*2,m-1)]
#     return any(steps) if m%2!=0 else any(steps)
# print([x for x in range(1,242) if  f(17,x,2)])
# print([x for x in range(1,242) if not f(17,x,1) and f(17,x,3)])
# print([x for x in range(1,242) if not f(17,x,2) and f(17,x,4)])

#     steps = [f(s+1,m-1),f(s+4,m-1),f(s*3,m-1)]
#     return any(steps) if m%2!=0 else all(steps)
# print([x for x in range(1,59) if  f(x,2)])
# print([x for x in range(1,59) if not f(x,1) and f(x,3)])
# print([x for x in range(1,59) if not f(x,2) and f(x,4)])

# def f(a,b):
#     if a>=435: return b%2==0
#     if b==0: return 0
#     steps = [f(a+5,b-1),f(a*3,b-1)]
#     return any(steps) if b%2!=0 else all(steps)
# print([x for x in range(1,435) if f(x,2)])
# print([x for x in range(1,435) if not f(x,1) and f(x,3)])
# print([x for x in range(1,435) if not f(x,2) and f(x,4)])

# def f(s,m):
#     if 36 <= s <=60 : return m%2==0
#     if s > 60: return m%2!=0
#     if m == 0 : return 0
#     steps = [f(s+1,m-1),f(s*2,m-1),f(s*3,m-1)]
#     return any(steps) if m%2!=0 else all(steps)
# print([x for x in range(1,36) if f(x,2)])
# print([x for x in range(1,36) if not f(x,1) and f(x,3)])
# print([x for x in range(1,36) if not f(x,2) and f(x,4)])


# def f(s,m):
#     if s <=12 : return m%2==0
#     if m ==0: return 0
#     steps = [f(s//3,m-1),f(s-12,m-1)]
#     return any(steps) if m%2!=0 else any(steps)
# print([x for x in range(13,10000) if f(x,2)])
# print([x for x in range(13,1000) if not f(x,1) and f(x,3)])
# print([x for x in range(13,1000) if not f(x,2) and f(x,4)])

# def f(s,a,m):
#     if s+a>=123: return m%2==0
#     if m == 0: return 0
#     steps = [f(s+1,a, m-1),f(s*2,a,m-1),f(s,a+1,m-1),f(s, a*2,m-1)]
#     return any(steps) if m%2!=0 else all(steps)
# # print([x for x in range(1,110)if f(13,x,2)])
# print([x for x in range(1,110) if not f(13,x,1) and f(13,x,3)])
# print([x for x in range(1,110) if not f(13,x,2) and f(13,x,4)])

def f(s,m):
    if s >=124: return m%2 ==0
    if m == 0 : return 0 
    steps = [f(s+1,m-1),f(s+5,m-1),f(s*3,m-1)]
    return any(steps) if m%2 !=0 else all(steps)
print([x for x in range(1,124) if f(x,2)])