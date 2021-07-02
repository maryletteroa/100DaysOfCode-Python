from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
map = Turtle()
map.shape(image)

marker = Turtle()
marker.hideturtle()
marker.penup()

df = pd.read_csv("./50_states.csv")

guessed_states = []
all_states = df.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        coords = df[df.state == answer_state]
        x = coords.x.values[0]
        y = coords.y.values[0]
        marker.goto(x,y)
        marker.write(answer_state)

        ## remove states that were guessed
        all_states.remove(answer_state)

states_to_learn = pd.DataFrame(all_states)

states_to_learn.to_csv("./states_to_learn.csv")