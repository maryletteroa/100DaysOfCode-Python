# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-17 04:49:36
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-17 05:25:08

import random
from art import logo, vs
from game_data import data
from replit import clear

end_game = False
score = 0
answer = ""

a = random.sample(data,1)[0]
a_followers = a['follower_count']

print(logo)

while not end_game:


    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    a_followers = a['follower_count']

    print(vs)

    b = random.sample(data,1)[0]
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
    b_followers = b['follower_count']

    answer = input("Who has more followers? Type 'A' or 'B': ")

    if answer == "A":
      if a_followers > b_followers:
        score += 1
        clear()
        print(logo)
        print(f"You're right! Current score: {score}")
      else:
        clear()
        print(logo)
        print(f"Sorry you're wrong. Final score {score}")
        end_game = True
    if answer == "B":
      if a_followers < b_followers:
        score += 1
        clear()
        print(logo)
        print(f"You're right! Current score: {score}")
        a = b
      else:
        clear()
        print(logo)
        print(f"Sorry you're wrong. Final score {score}")
        end_game = True

