# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-07 12:27:02
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-07 12:27:26

# Calculate the sum of all the even numbers from 1 to 100.

sum_even = 0
for num in range(1,101):
  if num % 2 == 0:
    sum_even += num
print(sum_even)