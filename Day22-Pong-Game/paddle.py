from turtle import Turtle

MOVEMENT = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        self.goto(x=self.xcor(), y=self.ycor() + MOVEMENT)

    def down(self):
        self.goto(x=self.xcor(), y=self.ycor() - MOVEMENT)


