# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-07 12:19:58
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-07 12:21:12


# From a list of scores, output the highest score
# without using max()
# Sample Input: 78 65 89 86 55 91 64 89
# Sample Output: The highest score in the class is: 91 

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
max_score = 0
for score in student_scores:
  if score > max_score:
    max_score = score

print(f"The highest score in the class is: {max_score}")




