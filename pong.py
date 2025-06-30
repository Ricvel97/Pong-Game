from turtle import Turtle

class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_distance = 10
        self.y_distance = 10

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        new_x_cor = self.xcor() + self.x_distance
        new_y_cor = self.ycor() + self.y_distance
        self.goto(new_x_cor, new_y_cor)

    def y_bounce(self):
        self.y_distance *= -1

    def x_bounce(self):
        self.x_distance *= -1

    def reset(self):
        self.goto(0, 0)
        self.x_bounce()