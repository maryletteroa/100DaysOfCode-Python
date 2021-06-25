from turtle import Screen, Turtle
import time

# initialize the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create a three-segment snake from (0,0) to (-60,0)
segments = []
starting_positions = [(0,0), (-20,0), (-40,0), ]
for starting_position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(starting_position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    # wait until all segments have moved before updating the screen
    screen.update()
    time.sleep(0.1)
    # move the segments from last to first
    # following the movements of the first (aka head)
    # this "links" the snake segments
    for seg_num in range(len(segments)-1,0,-1):
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

# exit only onclick
screen.exitonclick()