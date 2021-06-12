# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-12 17:36:38
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-12 17:36:45

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year = 0, month = 0):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year):
    days = month_days[month - 1]
    if days == 28:
      days = 29
      return days
  else:
    days = month_days[month - 1]
    return days
  

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)











