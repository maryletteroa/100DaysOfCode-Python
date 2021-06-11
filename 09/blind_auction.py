# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-11 17:59:04
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-11 18:05:10


from replit import clear
from art import logo

print(logo)

print("Welcome to the secret auction program.")

bids = {}
others = "yes"

while others == "yes":
  name = input("What is your name? ")
  amount = input("What's your bid? $")
  bids[name] = amount
  others = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  clear()

win_amt = max(bids.values())
for name, amnt in bids.items():
  if amnt == win_amt:
    win_name = name 

clear()

print(f"The winner is {win_name} with a bid of ${win_amt}.")