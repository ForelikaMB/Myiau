# from turtle import *
# screensize(2000,2000)
# tracer(0)
# m = 15
# left(90)
# for i in range(9):
#     forward(27*m)
#     right(90)
#     forward(30*m)
#     right(90)
# penup()
# forward(3*m)
# right(90)
# forward(6*m)
# left(90)
# pendown()
# for i in range(9):
#     forward(77*m)
#     right(90)
#     forward(66*m)
#     right(90)
# penup()


# for x in range(-40,40):
#     for y in range(-40,40):
#         setpos(x*m,y*m)
#         dot()
#         color("red")
# done()
# from turtle import *
# screensize(-2000,2000)
# tracer(0)
# left(90)
# m = 30
# for i in range(4):
#     forward(5*m)
#     right(90)
#     forward(10*m)
#     right(90)
# penup()
# for x in range(-20,20):
#     for y in range(-20,20):
#         dot()
#         setpos(x*m,y*m)
# done() 


# from turtle import *
# screensize(-2000,2000)
# tracer(0)
# m = 30
# left(90)
# for i in range(2):
#     forward(10*m)
#     right(90)
#     forward(18*m)
#     right(90)
# penup()
# forward(5*m)
# right(90)
# forward(7*m)
# left(90)
# pendown()
# for i in range(2):
#     forward(10*m)
#     right(90)
#     forward(7*m)
#     right(90)
# penup()
# for x in range(-20,20):
#     for y in range(-20,20):
#         setpos(x*m,y*m)
#         dot()
#         color("purple")
# done()
# ЕСЛИ ФИГУРА СТРАШНАЯ ТО СЧИТАЕМ ТОЧКИ ПО ТРИУГОЛЬНИКАМ КВАДРАТАМ(Разбиваем на графические примитивы)
# from turtle import *
# screensize(-2000,2000)
# tracer(0)
# m = 30
# left(90) 
# for i in range(2):
#     right(120)
#     forward(9*m)
# right(300)
# for i in range(2):
#     right(120)
#     forward(9*m)
# penup()

# for x in range(-60,60):
#     for y in range(-60,60):
#         setpos(x*m,y*m)
#         dot()
#         color("purple")
# done()

# from turtle import *
# screensize(-2000,2000)
# tracer(0)
# m = 60
# left(90)
# for i in range(2):
#     right(120)
#     forward(7*m)
# penup()
# right(300)
# pendown()
# for i in range(2):
#     right(120)
#     forward(7*m)
# penup()

# for x in range(-30,30):
#     for y in range(-30,30):
#         setpos(x*m,y*m)
#         dot()
#         color('purple')
# done()

# from turtle import *
# screensize(-2000,2000)
# tracer(0)
# m = 30
# left(90)
# for i in range(4):
#     forward(5*m)
#     right(90)
#     forward(7*m)
#     right(90)
# penup()
# for x in range(-30,30):
#     for y in range(-30,30):
#         setpos(x*m,y*m)
#         dot()
#         color('purple')
# done()
# from turtle import *
# screensize(-2000,2000)
# tracer(0)
# m = 30
# left(90)
# for i in range(3):
#     forward(20*m)
#     right(90)
#     forward(4*m)
#     right(90)
# for i in range(3):
#     forward(6*m)
#     right(90)
#     forward(13*m)
#     right(90)
# penup()

# for x in range(-30,30):
#     for y in range(-30,30):
#         setpos(x*m,y*m)
#         dot()
#         color("purple")
# done()

# from turtle import *
# screensize(-2000,2000)
# tracer(0)
# m = 30
# left(90)
# for i in range(4):
#     forward(7*m)
#     right(90)
#     forward(7*m)
#     left(90)
#     forward(7*m)
#     right(90)
# penup(
# )
# for x in range(-30,30):
#     for y in range(-30,30):
#         setpos(x*m,y*m)
#         dot()

# done()
# from turtle import *
# screensize(-2000,2000)
# tracer(0)
# m = 30
# for k in range(4):
#     forward(14*m)
#     right(90)

# for k in range(5):
#     forward(5*m)
#     right(45)
# penup()
# for x in range(-100,100):
#     for y in range(-100,100):
#         setpos(x*m,y*m)
#         dot()

# done()
# from turtle import *
# screensize(-2000,2000)
# m = 10
# tracer(0)

# right(315)

# for k in range(7):
#     forward(72*m)
#     right(45)
#     forward(43*m)
#     right(135)
# penup()
# for x in range(-100,100):
#     for y in range(-100,100):
#         setpos(x*m,y*m)
#         dot()
# done()

# from turtle import *
# screensize(-2000,2000)
# m = 30
# tracer(0)
# left(90)
# for k in range(2):
#     forward(3*m)
#     right(90)
#     forward(20*m)
#     right(90)
# penup()
# back(8*m)
# right(90)
# forward(9*m)
# left(90)
# pendown()
# for k in range(2):
#     forward(16*m)
#     right(90)
#     forward(8*m)
#     right(90)
# penup()
# for x in range(-100,100):
#     for y in range(-100,100):
#         setpos(x*m,y*m)
#         dot()
# done()

from turtle import *
screensize(-2000,2000)
m = 30
tracer(0)
left(90)
right(30)
for k in range(3):
    right(45)
    forward(4*m)
    right(45)
right(315)
forward(4*m)
for k in range(2):
    right(90)
    forward(4*m)
penup()
for x in range(-100,100):
    for y in range(-100,100):
        setpos(x*m,y*m)
        dot()
done()