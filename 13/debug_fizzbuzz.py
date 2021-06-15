# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-15 23:55:17
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-15 23:55:19

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print([number])