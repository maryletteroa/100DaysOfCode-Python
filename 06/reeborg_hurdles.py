# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-08 19:13:23
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-08 19:23:30

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

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

for r in range(0,6):
	hurdle()