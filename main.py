from turtle import Screen
from paddle import Paddle
from pong import Pong
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
pong = Pong()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)

game_is_on = True
time_to_sleep = 0.1

while game_is_on:
    screen.update()
    time.sleep(time_to_sleep)
    pong.move()

    # Detect collision with wall
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.y_bounce()

    # Detect collision with paddle
    if pong.distance(right_paddle) < 50 and pong.xcor() > 330:
        pong.x_bounce()
        time_to_sleep *= 0.9
    elif pong.distance(left_paddle) < 50 and pong.xcor() < -330:
        pong.x_bounce()
        time_to_sleep *= 0.9

    # Detect collision with edge
    if pong.xcor() > 390:
        pong.reset()
        scoreboard.left_score()
        time_to_sleep = 0.1

    elif pong.xcor() < -390:
        pong.reset()
        scoreboard.right_score()
        time_to_sleep = 0.1

screen.exitonclick()