from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-260, 260)
        self.speed = 0.1
        self.score_board()

    def score_board(self):
        self.write(f"Level: {self.level}", font=("Arial", 12, "bold"))

    def game_speed(self):
        self.speed *= 0.9

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", True, font=("Arial", 12, "bold"))

    def score(self):
        self.level += 1
        self.clear()
        self.score_board()
        self.game_speed()



