#!/usr/bin/env python3

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report():
    for key in resources:
        print(f"{key}: {resources[key]}")


def insert_coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total = quarters * 25 + dimes * 10 + nickles * 5 + pennies
    return total


def enough_resource(coffee):
    ingredients = MENU[coffee]['ingredients']
    for key in ingredients:
        if ingredients[key] > resources[key]:
            return False
    return True


def get_price_in_cent(coffee):
    return MENU[coffee]['cost'] * 100


def make_coffee(coffee):
    ingredients = MENU[coffee]['ingredients']
    for key in ingredients:
        resources[key] -= ingredients[key]


def cal_changes(coffee, total):
    cost = get_price_in_cent(coffee)
    return total - cost


def coffee_machine():
    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino/report, exit): ")
        if user_input == 'report':
            print_report()
        elif user_input == 'exit':
            return
        else:
            total = insert_coins()
            if not enough_resource(user_input):
                print("Sorry, not enough resources")
            elif total < get_price_in_cent(user_input):
                print("Sorry, not enough coins")
            else:
                make_coffee(user_input)
                change = cal_changes(user_input,total)
                print("Change is {} cents".format(change))


if __name__ == "__main__":
    coffee_machine()
