# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-07 12:05:58
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-07 12:07:20


# From a list of heights, calculate the average height
# without using len() or sum()
# Sample input: 156 178 165 171 187
# Sample output: 171

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

num_students = 0
sum_heights = 0
for height in student_heights:
  num_students += 1
  sum_heights += height

average_height = round(sum_heights / num_students)

print(average_height)



