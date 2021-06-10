# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-10 21:21:09
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-10 21:21:21

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(direction, plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    if direction == "encode":
      desc = "encoded"
      new_position = position + shift_amount
      cipher_text += alphabet[new_position]
    elif direction == "decode":
      desc = "decoded"
      new_position = position - shift_amount
      cipher_text += alphabet[new_position]
  print(f"The {desc} text is {cipher_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(direction, text, shift)