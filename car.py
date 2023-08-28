from turtle import Turtle
from random import randint

START_POSITIONS = [(260, 180), (260, 140), (260, 100), (260, 60), (260, 20), (260, -20), (260, -60),
                   (260, -100), (260, -140), (260, -180), (260, -220)]


class MyCars(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = 2.5
        self.create_car()

    def create_car(self):
        self.shape("square")
        self.color("green")
        self.shapesize(stretch_len=2)
        self.penup()
        self.setheading(180)
        self.goto(START_POSITIONS[randint(0, 10)])

    def move(self):
        self.forward(2.5)

    def cars_speed(self):
        self.car_speed /= 0.9
