# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-13 16:36:27
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-13 17:47:02

from art import logo
import random
from replit import clear

def draw(n):
    """
    Assume that there is infinite deck
    """
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    cards = random.sample(deck, n)
    return cards

def score(cards):
    if 11 in cards:
        if sum(cards) > 21:
            return sum(cards) - 10
        else:
            return sum(cards)
    else:
        return sum(cards)

def evaluate(computer_score, player_score):
    if computer_score > 21:
        if player_score > 21:
            return "You both went over. Draw."
        else:
            return "Your opponent went over. You win. 😁"
    elif computer_score == player_score:
        return "You have the same core. Draw."
    elif computer_score < 21:
        if player_score < 21:
            if (21 - computer_score) > (21 - player_score):
                return "You score closer to 21. You win. 😁"
            else:
                return "Your opponent scored closer to 21. You win. 😁"

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while play == "y":

    clear()
    print(logo)

    computer_cards = draw(2)
    player_cards = draw(2)

    player_score = score(player_cards)
    computer_score = score(computer_cards)

    print(f"\tYour cards: {player_cards}, current score: {player_score}")
    print(f"\tComputer's first card: {computer_cards[0]}")

    get_card = input("Type 'y' to get another card, type 'n' to pass: ")

    if get_card == "y":
        player_cards.extend(draw(1))

    if computer_score < 17:
        computer_cards.extend(draw(1))

    player_score = score(player_cards)
    computer_score = score(computer_cards)


    print(f"\tYour cards: {player_cards}, current score: {player_score}")
    print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")


    if computer_score > 21:
        if player_score > 21:
            print("You both went over. Draw.")
        else:
            print("Your opponent's score went over. You win.")
    elif computer_score == player_score:
        print("You have the same score. Draw.")
    elif computer_score < 21:
        if player_score < 21:
            if (21 - computer_score) > (21 - player_score):
                print("You scored closer to 21. You win.")
            else:
                print("Your opponent scored closer to 21. You lose.")
        else:
            print("You went over 21. You lose.")

    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")


