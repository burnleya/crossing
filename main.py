from turtle import Screen
from the_turtle import MyTurtle
from road_lines import RoadLines
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("white")
screen.title("Crossing Game")
screen.tracer(0)

my_turtle = MyTurtle()
my_road_lines = RoadLines()
screen.listen()
screen.onkey(my_turtle.move_up, "Up")
screen.onkey(my_turtle.move_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)


screen.exitonclick()










if __name__ == '__main__':
    pass

