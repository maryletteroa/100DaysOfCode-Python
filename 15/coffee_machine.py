# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-18 20:26:36
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-18 22:33:14

from inventory import MENU
from inventory import resources as initial_resources

def print_report(stock, money):
    for st in stock:
        print(f"{st.title()}: {stock[st]}")
    print(f"Money: ${money:.2f}")


def check_stock(request, stock):
    available = 1
    ingredients = MENU[request]["ingredients"]
    for ingredient in ingredients:
        if ingredients[ingredient] > stock[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            available *= 0
    return available

def update_stock(request, stock):
    ingredients = MENU[request]["ingredients"]
    for ingredient in ingredients:
        stock[ingredient] -= ingredients[ingredient]
    return True


def check_cost(request, payment):
    cost = MENU[request]["cost"]
    if cost > payment:
        print("Sorry that's not enough money. Money refunded.")
    elif payment > cost:
        change = payment - cost
        print(f"Heres is ${change:.2f} dollars in change.")
        return True
    else:
        return True 


def calculate_money(quarter, dime, nickle, penny):
    payment = quarter * 0.25 + dime * 0.10 + nickle * 0.05 + penny * 0.01
    return payment

def make_coffee(request, stock):
    print(f"Here is your {request} ☕. Enjoy!")


def main():

    money = 0
    stock = initial_resources

    options = ["espresso", "latte", "cappuccino"]


    request = input("What would you like? (espresso/latte/cappuccino): ")

    while request != "off":
    
        if request == "report":
            print_report(stock, money)
        elif request in options:
            if check_stock(request, stock):
                print("Please insert coins.")
                quarter = int(input("How many quarters?: "))
                dime = int(input("How many dimes?: "))
                nickle = int(input("How many nickles?: "))
                penny = int(input("How many pennies?: "))
                payment = calculate_money(quarter, dime, nickle, penny)
                if check_cost(request, payment):
                    money  += payment
                    update_stock(request, stock)
                    make_coffee(request, stock)
        else:
            print(f"{request} is not in our menu.")

        request = input("What would you like? (espresso/latte/cappuccino): ")



if __name__ == '__main__':
    main()