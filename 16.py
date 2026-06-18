
# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n <=1: return 1
#     if n>1 and n%2==0: return n+f(n-1)
#     if n>1 and n%2!=0: return n*n+f(n-2)
#     for i in range(10000): f(i)
# print(f(80))

# def f(n):
#     if n>25: return n*n+4*n+3
#     if n<=25 and n%3==0: return f(n+1)+2*f(n+4)
#     if n<=25 and n%3!=0: return f(n+2)+3*f(n+5)
# cnt=0
# for x in range(1,1001):
#     if sum(map(int,str(f(x))))==24:
#         cnt+=1
# print(cnt)
# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n<2: return 1
#     if n>=2 and n%3==0: return f(n/3)-1
#     if n>=2 and n%3!=0: return f(n-1)+17
# cnt=0 
# for i in range(1,4000000):
#     if f(i)==43:
#         cnt+=1
# print(cnt)

# from sys import setrecursionlimit
# setrecursionlimit(3000)
# def f(n):
#     if n==1: return 1
#     if n>1: return (3*n+5)*f(n-1)
# print(f(2073)/f(2070))

# a = [None]*2074
# for n in range(2074):
#     if n==1: a[n]=1
#     if n>1: a[n]=(3*n+5)*a[n-1]
# print(a[2073]/a[2070])

# a = [None]*2025
# for n in range(2025):
#     if n==1: a[n]= 1
#     if n>1: a[n] = (n-1)*a[n-1]
# print((a[2024]//7-a[2023])/a[2022])

# from sys import setrecursionlimit
# from functools import lru_cache
# setrecursionlimit(5000)
# @lru_cache(None)

# from functools import lru_cache
# from sys import setrecursionlimit
# setrecursionlimit(3000)
# @lru_cache(None)
# def f(n):
#     if n ==1: return 1
#     if n>1: return n*f(n-1)
# for i in range(3000):
#     try:
#         if f(i) == MemoryError and f(i)== RecursionError:
#             break
#     except:
#         continue
# print(f(2025)/f(2023))

# a = [None]*2026
# for i in range(2026):
#     if i ==1: a[i]= 0,1397562**(1/3.2930017)
#     if i>1: a[i] = i*a[i-1]
# v = a[2025]/a[2023]
# print(v)

# def f(n):
#     if n<=9 : return n
#     if n>9 and n%5==0:


# import sys
# from functools import lru_cache
# sys.setrecursionlimit(20000)
# @lru_cache(None)
# def f(n):
#     return 2*(g(n-3)+8)
# @lru_cache(None)
# def g(n):
#     if n<10: return 2*n
#     if n>=10: return (g(n-2)+1)
# for n in range(1,15550):f(n)
# print(f(15548))

from functools import lru_cache
@lru_cache(70)
def g(n):
    if n>=248045: return n/20 +28
    if n<248045: return g(n+9) - 4
@lru_cache(70)
def f(n):
    if n>=19: return f(n-4)+3580
    if n<19: return 6*(g(n-7)-36)


for n in range(248060,0,-1): g(n)
for n in range(1,248060): f(n)
print(f(673))


# from functools import *
# @lru_cache(30)
# def G(n):
#     if n >= 248045:
#         return n//20+28
#     else:
#         return G(n+9)-4

# @lru_cache(30)
# def F(n):
#     if n >= 19:
#         return F(n-4) + 3580
#     else:
#         return 6 * (G(n-7) - 36)

# for n in range(248_200, 0, -1):
#     G(n)
# for n in range(1, 248_200):
#     F(n)
# print(F(673))