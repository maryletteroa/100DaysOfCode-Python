from turtle import Screen, Turtle
from snake import Snake
import time

# initialize the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create a three-segment snake from (0,0) to (-60,0)
snake = Snake()


# listen for keystrokes
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


game_is_on = True
while game_is_on:
    # wait until all segments have moved before updating the screen
    screen.update()
    time.sleep(0.1)
    # move snake forwards
    snake.move()
    # move snake by keys

# exit only onclick
screen.exitonclick()