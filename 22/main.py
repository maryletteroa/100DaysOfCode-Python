from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

# do not show screen
screen.tracer(0)

# create paddles
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

# create ball
ball = Ball()

# create scoreboard
scoreboard = Scoreboard()

# game controls
screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)


game_is_on = True
while game_is_on:
    # show screen after paddles and ball have been created
    # sleep slows down the movement of the ball
    time.sleep(0.1)
    screen.update()
    
    # move ball
    ball.move()

    #detect collisionw with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddles
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or \
        ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
    
    #detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    


screen.exitonclick()