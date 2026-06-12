import turtle as t
from random import choice, randint
tim = t.Turtle()
tim.shape("turtle")
tim.pensize(5)
tim.speed("fastest")
t.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    tup = (r, g, b)
    return tup

angle = 0
while angle <= 360:
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(angle)
    angle += 10


screen = t.Screen()
screen.exitonclick()