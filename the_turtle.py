from turtle import Turtle

HEADING = 90
START = (0, -280)


class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.setheading(HEADING)
        self.goto(START)

    def move_up(self):
        self.forward(5)

    def move_down(self):
        self.backward(5)
