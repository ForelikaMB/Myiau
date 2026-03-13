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
f = open('tip.txt')
cnt = 0
for i in f:
    a = sorted([int(x)for x in i.split()])
    if ((set(a.count)==3) and ((a.count) <=5 )) and (a[0]>= a[1] or a[0]>= a[2] or a[0]>= a[3] or a[0]>= a[4] or a[0]>=a[5]):
        cnt+=1
        print(cnt)