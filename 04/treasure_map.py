# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-06 11:33:55
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-06 13:26:01

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

col = position[0]
row = position[1]

map[int(row)-1][int(col)-1] = "X"

print(f"{row1}\n{row2}\n{row3}")