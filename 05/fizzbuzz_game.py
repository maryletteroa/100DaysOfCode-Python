# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-07 12:33:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-07 12:35:27

# A program that prints the solution to the 
# FizzBuzz game (https://en.wikipedia.org/wiki/Fizz_buzz)
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for num in range(1,101):
  if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  elif num % 3 == 0:
    print("Fizz")
  elif num % 5 ==0:
    print("Buzz")
  else:
    print(num)