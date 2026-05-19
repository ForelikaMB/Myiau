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

def f(a,b,m):
    if a+b>=259: return m%2==0
    if m == 0 : return 0
    steps = [f(a+1,b,m-1),f(a*2,b,m-1),f(a,b+1,m-1),f(a,b*2,m-1)]
    return any(steps) if m%2!=0 else any(steps)
print([x for x in range(1,36) if  f(x,2)])
print([x for x in range(1,36) if not f(x,1) and f(x,3)])
print([x for x in range(1,36) if not f(x,2) and f(x,4)])