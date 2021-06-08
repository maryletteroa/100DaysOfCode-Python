# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-08 19:22:50
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-08 19:23:00


# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

def turn_around():
   turn_left()
   turn_left()
   turn_left()    

def hurdle():
    move()
    turn_left()
    move()
    turn_around()
    move()
    turn_around()
    move()
    turn_left()

while not at_goal():
    hurdle()