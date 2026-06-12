from turtle import Turtle, Screen
from random import randint
screen = Screen()

is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Enter your bet", prompt="Which turtle will win the race? enter a color:")
colors = ["red", "green", "blue", "yellow", "orange", "black"]
all_turtles = []
y_start = -125

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    all_turtles.append(new_turtle)
    new_turtle.goto(x=-230, y=y_start)
    y_start += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for t in all_turtles:
        if t.xcor() > 230:
            is_race_on = False
            winner = t.pencolor()
            if winner == user_bet:
                print(f"You've Won!! The winning turtle's color is {winner}.")
            else:
                print(f"You've Lost! The winning turtle's color is {winner}.")
        r_speed = randint(0,10)
        t.forward(r_speed)

screen.exitonclick()