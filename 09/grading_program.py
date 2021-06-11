# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-11 17:29:44
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-11 17:29:54


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

for student, score in student_scores.items():
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  elif score <= 70:
    student_grades[student] = "Fail"     

print(student_grades)





