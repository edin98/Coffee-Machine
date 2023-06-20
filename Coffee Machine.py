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

profits = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#This is the function that will check (true or false) if enough resources for a given order
#Also here I used variables x, and i to try to understand how the raw data works in a function
# x is simply the variable of choice(latte, etc.), and 'i' are the values in the dictionaries
def is_resources_sufficient(x):
    for i in x:
        if x[i] > resources[i]:
            print(f"Sorry there is not enough {i}")
            return False
        else:
            return True
#In here is a function when an order is processed, then we need to decrease our
#resources(dictionary).
def make_coffee(drink_name, x):
    for i in x:
        resources[i] -= x[i]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    x = input ("What would you like? (espresso, latte, cappuccino): ")
    if x == "off":
        is_on = False
    elif x == "report":
        print(f" Water: {resources['water']}ml")
        print(f" Milk: {resources['milk']}ml")
        print(f" Coffee: {resources['coffee']}g")
        print(f" Money: {profits}$")
    else:
        drink = MENU[x]
        if is_resources_sufficient(drink["ingredients"]):
            make_coffee(x, drink["ingredients"])



#Here we need to do an if statement and check if resources are sufficient
#To do this I will create a function to check if ingredients are sufficient.