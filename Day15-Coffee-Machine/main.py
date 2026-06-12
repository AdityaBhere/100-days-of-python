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

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    for k,v in resources.items():
        print(f"{k} = {v} ml")
    print(f"money: {money}")

def coin_total(q, d, n, p):
    return q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01

def check_ingredients(choice):
    for x in MENU[choice]["ingredients"]:
        if MENU[choice]["ingredients"][x] > resources[x]:
            print(f"Sorry there is not enough {x}.")
            return False
    return True

def make_coffee(choice):
    for x in MENU[choice]["ingredients"]:
        resources[x] -= MENU[choice]["ingredients"][x]

def refund_money(choice, total):
    if total > MENU[choice]["cost"]:
        refund = total - MENU[choice]['cost']
        print(f"Here is ${round(refund, 2)} in change.")
    else:
        print("Sorry that's not enough money. Money refunded.")

def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino):")
        if choice == "off":
            break
        elif choice == "report":
            report()
        else:
            if check_ingredients(choice):
                print("Please insert coins")
                q = int(input("How many quarters:"))
                d = int(input("How many dimes:"))
                n = int(input("How many nickels:"))
                p = int(input("How many pennies:"))
                total = coin_total(q, d, n, p)
                if total >= MENU[choice]["cost"]:
                    make_coffee(choice)
                    refund_money(choice, total)
                    global money
                    money += MENU[choice]["cost"]
                    print(f"Here is your {choice}. Enjoy!")


coffee_machine()