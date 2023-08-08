import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
import random
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('cuppa_joe')

print("****Welcome to Cuppa Joe****\n")
waitdress = ['Becky', 'Tisha', 'Cathy', 'Sarah', 'Helen']
print("Hi, My name is " + random.choice(waitdress) + ".\n")
print("We have a large selection of drinks available from our menu.\n")

coffee_items = {"Latte": {"Small": 2.50, "Meduim": 2.75, "Large": 3.00},
                "Flat White": {"Small": 2.50, "Meduim": 2.75, "Large": 3.00},
                "Americano": {"Small": 2.50, "Meduim": 2.75, "Large": 3.00},
                "Cappucino": {"Small": 2.50, "Meduim": 2.75, "Large": 3.00},
                "Mocha": {"Small": 2.50, "Meduim": 2.75, "Large": 3.00}}
extra_items = {"Soya Milk": .50, "Cream": .75,
               "Chocolate": 1.00, "Oat Milk": .50}
total = []
plus = []
 

def add_coffee():
    global product
    while True:
        item = [['Latte'], ['Flat White'], ['Americano'],
                ['Cappucino'], ['Mocha']]
        headers = ["Name"]
        print(tabulate(item, headers, tablefmt="rounded_outline"))
        product = input("\nWhat coffee would you like? \n")
        if product in coffee_items:
            break
        else:
            print()
            print("NOT A VALID OPTION!\n")


def quantity():
    global quantity
    while True:
        quantity = input(f"\nHow many would {product} you like? \n")
        try:
            quantity = int(quantity)
            break
        except ValueError:
            print("Error: Please enter a number!")
            print()


def add_extra():
    global extra
    extra = [["Soya milk"], ["Cream"], ["Chocolate"], ["Oat milk"]]
    headers = ["Extra"]
    print(tabulate(extra, headers, tablefmt="rounded_outline"))
    while True:
        extra = input(f"\nWould you like anything extra with your {product}? \n")
        try:
            if extra in extra_items:
                break
        except ValueError:
            extra.lower()
        else:
            print("Error: Please pick from menu!")
            print()
    plus.append(extra_items[extra])


def add_size():
    global size
    size = [["Small"], ["Meduim"], ["Large"]]
    headers = ["Size"]
    print(tabulate(size, headers, tablefmt="rounded_outline"))
    while True:
        size = input("\nWhat size would you like? \n")
        try:
            size = int(size)
            print("Error: Please pick from menu!")
            print()
        except ValueError:
            break
    print(f"\nYou have ordered:\n {quantity} - {size} {product} with {extra}.\n")
    total.append(coffee_items[product][size])


def cal_price():
    cost = total * int(quantity)
    price = plus * int(quantity)
    total_price = price + cost
    print(f"The total price is:\n €{sum(total_price)}\n")


def order_num():
    print(f"Order number is {random.randint(1,500)}\n")


def options():
    menu = [[0, "Add to Order"], [1, "Cancel Order"], [2, "Pay Order"], [3, "Exit"]]
    headers = ["Code", "Options"]
    print(tabulate(menu, headers, tablefmt="rounded_outline"))
    while True:
        option = int(input("Please enter code: \n"))
        if option in menu[0]:
            return update_order()
        elif option in menu[1]:
            break
        elif option in menu[2]:
            print("Under Construction")
        elif option in menu[3]:
            break
        else:
            print("Invalid Entry")

def update_order():
    coffee = add_coffee()
    coffee.update()
    amount = int(quantity())
    amount.update()
    plus = add_extra()
    plus.update()
    size = add_size()
    size.update()
    

def pay():
    print("Under Construction")


def main():
    add_coffee()
    quantity()
    add_extra()
    add_size()
    cal_price()
    order_num()
    options()
    update_order()
    pay()

main()
