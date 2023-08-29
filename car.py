from turtle import Turtle
from random import choice, randint


START_POSITIONS = [(260, 180), (260, 140), (260, 100), (260, 60), (260, 20), (260, -20), (260, -60),
                   (260, -100), (260, -140), (260, -180), (260, -220)]

COLOURS = ["blue", "navy", "deep sky blue", "dodger blue", "spring green", "lime green", "aquamarine", "sea green",
           "orange red", "crimson", "magenta", "red", "medium slate blue", "medium purple"]

MOVE_DISTANCE = 2.5


class MyCars:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(choice(COLOURS))
            new_car.shapesize(stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(choice(START_POSITIONS))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(MOVE_DISTANCE)


