from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up,'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up,'w')
screen.onkeypress(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 277 or ball.ycor() < -277:
        ball.bounce_y()

    if ball.distance(r_paddle)<50 and ball.xcor() > 320:
        ball.bounce_x_r_paddle()
    if ball.distance(l_paddle)<50 and ball.xcor() < -320:
        ball.bounce_x_l_paddle()


# R paddel misses ball
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

# L paddel misses ball
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()