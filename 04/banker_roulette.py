# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-06 11:19:48
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-06 11:21:50

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


choice_index = random.randint(0,len(names)-1)
name = names[choice_index]

# alternatively
#name = random.choice(names)

print(f"{name} is going to buy the meal today!")




