from turtle import Screen
from the_turtle import MyTurtle
from road_lines import RoadLines
from car import MyCars
from score import Score
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("white")
screen.title("Crossing Game")
screen.tracer(0)

my_turtle = MyTurtle()
my_road_lines = RoadLines()
car = MyCars()
score = Score()
screen.listen()
screen.onkey(my_turtle.move_up, "Up")
screen.onkey(my_turtle.move_down, "Down")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    car.create_car()
    car.move()
    if my_turtle.ycor() >= 260:
        score.score()
        my_turtle.reset()
    for car in car.all_cars:
        if my_turtle.distance(car) < 5:
            score.game_over()
            game_is_on = False


screen.exitonclick()

if __name__ == '__main__':
    pass