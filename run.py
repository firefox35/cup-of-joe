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


def add_coffee():
    global list
    list = [['Latte'],
            ['Flat White'],
            ['Americano'],
            ['Cappucino'],
            ['Mocha']]
    headers = ["Name"]
    print(tabulate(list, headers, tablefmt="rounded_outline"))   
    while True:
        list = input("\nWhat coffee would you like off the menu? \n")
        try:
            list = int(list)
            print("Error: Please pick from menu!")
            print()
        except ValueError:
            break


add_coffee()


def quantity():
    global quantity
    while True:
        quantity = input(f"\nHow many would {list} you like? \n")
        try:
            quantity = int(quantity)
            break
        except ValueError:
            print("Error: Please enter a number!")
            print()


quantity()


def add_extra():
    global extra
    extra = [["soya milk"], ["cream"], ["chocolate"], ["oat milk"]]
    headers = ["Extra"]
    print(tabulate(extra, headers, tablefmt="rounded_outline"))
    while True:
        extra = input(f"\nWould you like anything extra with your {list}? \n")
        try:
            extra = int(extra)
            print("Error: Please pick from menu!")
            print()
        except ValueError:
            break

    
add_extra()


def add_size():
    global size
    size = [["Small"], ["Meduim"], ["Large"]]
    headers = ["Size"]
    print(tabulate(size, headers, tablefmt="rounded_outline"))
    extra = input(f"\nWould you like anything extra with your {list}? \n")
    while True:
        size = input("\nWhat size would you like? \n")
        try:
            size = int(size)
            print("Error: Please pick from menu!")
            print()
        except ValueError:
            break
    print(f"\nYou have ordered {quantity} {size} {list} with {extra}.")


add_size()


def cal_price():
    total: 0
    coffee = [
        ["Latte", "Small", 2.5],
        ["Latte", "Meduim", 3.5],
        ["Latte", "Large", 3.75],
        ["Flat White", "Small", 2.25],
        ["Flat White", "Meduim", 2.5],
        ["Flat White", "Large", 2.75],
        ["Americano", "Small", 2.25],
        ["Americano", "Meduim", 2.5],
        ["Americano", "Large", 2.75],
        ["Cappucino", "Small", 2.65],
        ["Cappucino", "Meduim", 2.85],
        ["Cappucino", "Large", 3.10],
        ["Mocha", "Small", 2.5],
        ["Mocha", "Meduim", 2.75],
        ["Mocha", "Large", 3.00]
    ]

    addon = [
        ["soya milk", 0.50],
        ["cream", 0.75],
        ["chocolate", 1.00],
        ["oat milk", 0.50]
    ]
    if ((coffee  == list  and size == coffee) and (extra == addon)):
        price = coffee[2] + addon[1]
        total = quantity * price
        print(f"Your bill comes to the total of {total}")
    elif ((coffee == list and size == coffee) and (extra == "No")):
        price = coffee[2] + addon[1]
        total = quantity * price
        print(f"Your bill comes to the total of {total}")
    else:
        print("Please order again")


cal_price()


def main():
    pass


main()