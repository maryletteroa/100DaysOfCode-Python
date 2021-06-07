# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-06 13:37:40
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-06 13:39:37

import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves = [rock, paper, scissors]

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")

player_move = moves[int(player_choice)]
print(player_move)

computer_move = random.choice(moves)
print(f"Computer move: {computer_move}")

if player_move == rock:
  if computer_move == rock:
    print("It's a draw.")
  elif computer_move == paper:
    print("You lose.")
  else:
    print("You win.")
elif player_move == paper:
  if computer_move == rock:
      print("You win.")
  elif computer_move == paper:
    print("It's a draw")
  else:
    pasprint("You lose.")
else:
  if computer_move == rock:
    print("You lose.")
  elif computer_move == paper:
    print("You win.")
  else:
    print("It's a draw.")

print()