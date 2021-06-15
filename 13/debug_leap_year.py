# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-15 23:52:28
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-15 23:52:31


year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  