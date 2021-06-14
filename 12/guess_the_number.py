# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-14 20:14:34
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-14 21:28:50

import random
from art import logo

ATTEMPTS_EASY = 10
ATTEMPTS_HARD = 5

def set_difficulty():
    """
    Sets levels: easy has 10 attempts, hard has 5 attempts.
    """
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return ATTEMPTS_EASY
    elif difficulty == "hard":
        return ATTEMPTS_HARD

def compare(guess, number, attempts):
    """
    Determines if the guess value is higher, lower, or equals to the number.
    If not equal to the number, an attempt is deducted.
    If equal to number, attempt is set to -1.
    """
    if guess > number:
        attempts -= 1
        print("Too high.")
    elif guess < number:
        attempts -= 1
        print("Too low.")
    elif guess == number:
        print(f"You got it! The answer was {number}!")
        attempts = -1
    return attempts

def game():
    """
    The game proper.
    """
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1,100)
    
    # set initial number of attempts based on difficulty
    attempts = set_difficulty()

    while attempts > 0:
        guess = int(input("Make a guess: "))
        attempts = compare(guess, number, attempts)
        if attempts > 0:
            print("Guess again.")
            print(f"You have {attempts} remaining to guess the number.")
        elif attempts == 0:
            print(f"You've run out of guesses. The number is {number}. You lose.")


if __name__ == '__main__':
    game()