# from turtle import Turtle, Screen

# tim = Turtle()
# tim.shape("turtle")
# tim.color("red")
# tim.forward(100)
# tim.right(90)

## make a square

# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

## -----------------
## create dashed lines

# import turtle as t
# tim = t.Turtle()
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

## -----------------
## create shapes
## and colors

# import turtle as t
# import random

# tim = t.Turtle()

# def draw_shape(num_sides):
#     angle = 360/ num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# colors = ["green yellow", 
#     "dark green",
#     "gold",
#     "salmon",
#     "indigo",
#     "medium violet red",
#     "coral",
#     "light sea green",
# ]

# for shape_side_n in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

## -----------------
### draw a random walk
# import turtle as t
# from turtle import Screen
# import random


# tim = t.Turtle()
# screen = Screen()
# screen.colormode(255) # set to use RGB

# colors = ["green yellow", 
#     "dark green",
#     "gold",
#     "salmon",
#     "indigo",
#     "medium violet red",
#     "coral",
#     "light sea green",
# ]

# directions = [0, 90, 180, 270]
#     # 0 - east
#     # 90 - north
#     # 180 - west
#     # 270 - south

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color


# tim.pensize(15)
# tim.speed("fastest")

# for _ in range(200):
#     # tim.color(choice(colors))
#     tim.color(random_color())    
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

## -----------------
## draw a Spirograph
from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)

tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)

draw_spirograph(5)