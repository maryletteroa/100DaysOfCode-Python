from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# initialize the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create a three-segment snake from (0,0) to (-60,0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()


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

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    # detect wall collision
    if snake.head.xcor () > 280 or snake.head.xcor() <-280 \
        or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # detect collision with tail
    # if the head collides with any segment in tail:
        # trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# exit only onclick
screen.exitonclick()