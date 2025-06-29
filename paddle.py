from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.coordinates = coordinates
        self.create_paddle()
        self.move_distance = 20

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(self.coordinates)

    def up(self):
        y_cor = self.ycor() + self.move_distance
        x_cor = self.xcor()
        self.goto(x_cor, y_cor)

    def down(self):
        y_cor = self.ycor() - self.move_distance
        x_cor = self.xcor()
        self.goto(x_cor, y_cor)

