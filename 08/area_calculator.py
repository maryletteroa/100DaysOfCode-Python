# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-10 20:07:11
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-10 20:07:36

import math

def paint_calc(height=0, width=0, cover=0):
  num_cans = math.ceil((height * width) / coverage)
  print(f"You'll need {num_cans} of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


