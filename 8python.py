# перестановка permutations - смена мест у переменных
# размещение product - расстановка по местам определённых символов из основного словаря Повтор допускается
# сочитания Combinations -  не меняет буквы местами а смотрит сколько комбинаци можно составить из данного колличества букв
# (combinations_with_replacepent - допускает повторение букв)
# библиотека itertools
# from itertools import *
# cnt = 0
# for i in product('1234',repeat=3):
#     a = ''.join(i)
#     if a.count('2') == 1:
#         cnt +=1
# print(cnt)

# from itertools import *
# cnt = 0
# for i in product("ГЕПАРД", repeat=5):
#     a = ''.join(i)
#     if a.count("Г")==1 and a[0] != 'А' and a[-1] !='Е':
#         cnt +=1
# print(cnt)

# from itertools import *
# cnt = 0
# for i in product('ВИШНЯ',repeat=6):
#     a = ''.join(i)
#     if a.count("В")<=1 and a[0]!="Ш" and a[-1] not in'ЯИ':
#        cnt+=1 
# print(cnt)

# from itertools import *
# cnt = 0
# for i in product("012345678", repeat=5):
#     a = ''.join(i)
#     a = a.replace('5','n').replace('7','n')
#     a = a.replace('6','n').replace('8','n')
#     if a[0]!= "0" and a.count("3")==1 and "n3" not in a and "3n" not in a:
#         cnt +=1
# print(cnt)

# from itertools import *
# cnt = 0
# bad = ['53','35','63','36','73','37','83','38',]
# for i in product("012345678", repeat=5):
#     a = ''.join(i)
#     if a[0]!= "0" and a.count("3")==1 and\
#     all(x not in a for x in bad):
#         cnt +=1
# print(cnt)

# from itertools import *

# s = set()
# for i in permutations("МАРИНА"):
#     a = ''.join(i)
#     if a[0] not in 'АИ':
#         s.add(a)
# print(len(s))

# from itertools import *
# cnt = 0
# for i in product(sorted("МАНГУСТ"), repeat=6):
#     a = ''.join(i)
#     cnt+=1
#     if a[0]!='У' and a.count("М")==2 and a.count("Г") <=1:
#         print(cnt,a)

# from itertools import *
# cnr = 0
# for i  in product(sorted("МАРИЯ"),repeat=4):
#     a = ''.join(i)
#     cnr +=1
#     if cnr == 211:
#         print (cnr,a)
# from itertools import *
# cnt = 0
# pos = 0
# for i in product("АЕКМНЬ",repeat=6):
#     a = ''.join(i)
#     cnt +=1
#     if a[0] != "Ь" and a.count("М")==2 and a.count("А")<=1:
#         pos = cnt
# print(pos)
# from itertools import *
# cnt = 0
# for i in product("012345678", repeat=7):
#     a = ''.join(i)
#     if (a.count('8')==1 and a[0] not in "1357" and a[-1] not in "02468" and a[0]!="0"):
#         cnt+=1
# print(cnt)
# from itertools import *
# cnt = 0
# s = ["ОО", "АА","ОА","РС", "РМ", "РХ", "СМ", "СХ", "МХ"]
# for i in combinations(sorted("РОСОМАХА")):
#     a = ''.join(i)
#     if a.count('О')==2 and a.count("А")==2 and a.count("Р")==1 and a.count("С")==1 and a.count("М")==1 and a.count("Х")==1:
#         if s[0] not in "ОО" "АА""ОА" and s[0] not in "РС" "РМ" "РХ" "СМ" "СХ" "МХ" :
#             cnt +=a
# print(cnt)

from itertools import *
cnt = 0
for i in permutations("МАТВЕЙ"):
    a = ''.join(i)
    if a[0] != 'Й' and a.count('АЕ')==0:
        cnt+=1

print(cnt)
from itertools import *
cnt = 0 
for i in product("ЕГЭ",repeat=5):
    if i[0] not in "Г":
        cnt+=1
print(cnt)