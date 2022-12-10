from turtle import *
penup()
right(90)
goto(13, 0)
pendown()
speed(100)
color("cyan")
bgcolor("black")
b = 200
while b > 0:
    left(b)
    forward(b * 3)
    b = b - 1
