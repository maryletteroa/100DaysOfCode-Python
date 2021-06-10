# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-10 20:53:18
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-10 21:11:40

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
  cypher = ""
  for t in text:
    index = alphabet.index(t) + shift
    cypher += alphabet[index]
  return cypher


cypher = encrypt(text, shift)
print(cypher)
