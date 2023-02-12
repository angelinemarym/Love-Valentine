import turtle
import math

def love(t):
    x = 16 * (math.sin(t) ** 3)
    y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    return x, y

turtle.setup(800, 800)
turtle.bgcolor('black')
turtle.pensize(2)
turtle.pencolor('red')
turtle.speed(0.1)

factor = 20
factor2 = 10
turtle.penup()

for i in range(0, 200):
    x, y = love(i)
    turtle.goto(x * factor, y * factor)

    turtle.pendown()

for i in range(0, 200):
    x, y = love(i + 500)
    turtle.goto(x * factor2, y * factor2 - 40)

    turtle.pendown()

turtle.exitonclick()