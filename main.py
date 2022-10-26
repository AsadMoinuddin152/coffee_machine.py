# Variable section
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


# Function section
def report(res, profit):
    """Prints the Resources left in the Coffee machine """
    print(
        f"Resources Left : \nWater : {res['water']}ml\tMilf : {res['milk']}ml\tCoffee : {res['coffee']}gm\t Money : {profit}")


def is_order_drink_available(order_ingredients, res):
    """Checks the ingredients availability in the machine and returns that if we can make the drink or not with the
    available resource """
    is_enough = True
    for items in order_ingredients:
        if order_ingredients[items] >= res[items]:
            print(f"Sorry, There is not enough {items}")
            is_enough = False
    return is_enough


def process_coins():
    """Calculate the total value to the coins inserted by the user and gives the total amount"""
    print("Enter the Coins : ")
    total = int(input("Enter the number of quarters (1 quarters = 0.25$) : ")) * 0.25
    total += int(input("Enter the number of dimes (1 dimes = 0.10$) : ")) * 0.10
    total += int(input("Enter the number of nickles (1 nickles = 0.05$) : ")) * 0.05
    total += int(input("Enter the number of pennies (1 pennies = 0.01$) : ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True if the transaction is successful and return False if the transaction is false"""
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change {change}$")
        global profit
        profit += drink_cost
        return True
    else:
        print("“Sorry that's not enough money. The Money will be refunded back.")
        return False


def making_the_drink(drink_name, order_ingredients):
    """Deducts the amount of resources for making the coffee"""
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"Here is your {drink_name}")


# Main Code
profit = 0
is_on = True
while is_on:
    choice = input("What would you like to get (espresso/latte/cappuccino) : ").lower()
    if choice == "report":
        report(resources, profit)
    elif choice == "off":
        is_on = False
    else:
        drink = MENU[choice]
        if is_order_drink_available(drink["ingredients"], resources):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                making_the_drink(choice, drink["ingredients"])
                
