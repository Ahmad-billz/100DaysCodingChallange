from turtle import Turtle
FONT = ("Courier", 8, "bold")
GO_FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-260, 280)
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write("GAME OVER!!!", align='center', font=GO_FONT)