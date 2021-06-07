# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-07 12:56:41
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-07 12:58:25


#Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password = ""
# for l in range(nr_letters):
#   password += random.choice(letters)
# for s in range(nr_symbols):
#   password += random.choice(symbols)
# for n in range(nr_numbers):
#   password += random.choice(numbers)

# print(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


lpassword = []
for l in range(nr_letters):
  lpassword.append(random.choice(letters))
for s in range(nr_symbols):
  lpassword.append(random.choice(symbols))
for n in range(nr_numbers):
  lpassword.append(random.choice(numbers))

random.shuffle(lpassword)
password = ""
for p in lpassword:
  password += p

print(password)