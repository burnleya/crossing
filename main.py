from turtle import Screen
from the_turtle import MyTurtle
from road_lines import RoadLines
from cars import Cars
from score import Score
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("white")
screen.title("Crossing Game")
screen.tracer(0)

my_turtle = MyTurtle()
my_road_lines = RoadLines()
cars = Cars()
score = Score()
screen.listen()
screen.onkey(my_turtle.move_up, "Up")
screen.onkey(my_turtle.move_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    cars.move()
    if my_turtle.ycor() >= 260:
        score.score()
        my_turtle.reset()
        cars.create_cars()
        #cars.cars_speed()
    for car in cars.cars:
        if my_turtle.distance(car) < 20:
            score.game_over()
            game_is_on = False


screen.exitonclick()










if __name__ == '__main__':
    pass

