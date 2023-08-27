from turtle import Turtle


class RoadLines(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.x_cor = -260
        self.y_cor = -240
        self.goto(self.x_cor, self.y_cor)
        self.new_line()

    def new_line(self):
        for _ in range(12):
            self.draw_line()
            self.y_cor += 40
            self.goto(self.x_cor, self.y_cor)

    def draw_line(self):
        for _ in range(7):
            self.pendown()
            self.forward(40)
            self.penup()
            self.forward(40)

