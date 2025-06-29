from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.up()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()

        self.goto(-100, 190)
        self.write(arg=f"{self.l_score}", align="center", font=("Courier", 80, "bold"))
        self.goto(100, 190)
        self.write(arg=f"{self.r_score}", align="center", font=("Courier", 80, "bold"))

    def left_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def right_score(self):
        self.r_score += 1
        self.update_scoreboard()
