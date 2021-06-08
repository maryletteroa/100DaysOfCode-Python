# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-08 19:39:27
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-08 19:39:36

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_around():
    turn_left()
    turn_left()
    turn_left()    

def hurdle():
    turn_left()
    m = 0
    while not right_is_clear():
        move()
        m += 1
    turn_around()
    move()
    turn_around()
    for m in range(m):
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()