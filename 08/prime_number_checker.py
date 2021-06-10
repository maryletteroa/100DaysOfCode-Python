# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-10 20:36:16
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-10 20:42:49


def prime_checker(number=0):
  prime = False
  for r in range(2,number):
    if not number % r:
      prime = True
  
  if prime:
    print("It's not a prime number.")
  else:
    print("It's a prime number.")
    
n = int(input("Check this number: "))
prime_checker(number=n)






