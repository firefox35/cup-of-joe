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
                "Flat-White": {"Small": 2.50, "Meduim": 2.75, "Large": 3.00},
                "Americano": {"Small": 2.50, "Meduim": 2.75, "Large": 3.00},
                "Cappucino": {"Small": 2.50, "Meduim": 2.75, "Large": 3.00},
                "Mocha": {"Small": 2.50, "Meduim": 2.75, "Large": 3.00}}
extra_items = {"Soya Milk": .50, "Cream": .75, "Chocolate": 1.00,
                "Oat Milk": .50}
total = []
plus = []


def add_coffee():
    global product
    item = [['Latte'], ['Flat White'], ['Americano'], ['Cappucino'], ['Mocha']]
    headers = ["Name"]
    print(tabulate(item, headers, tablefmt="rounded_outline"))   
    while True:
        product = input("\nWhat coffee would you like off the menu? \n")
        try:
            item = int(product)
            print("Error: Please pick from menu!")
            print()
        except ValueError:
            break


add_coffee()


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


quantity()


def add_extra():
    global extra
    extra = [["soya milk"], ["cream"], ["chocolate"], ["oat milk"]]
    headers = ["Extra"]
    print(tabulate(extra, headers, tablefmt="rounded_outline"))
    while True:
        extra = input(f"\nWould you like anything extra with your {product}? \n")
        try:
            extra = int(extra)
            print("Error: Please pick from menu!")
            print()
        except ValueError:
            break
    plus.append(extra_items[extra])
   

add_extra()


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
    print(f"\nYou have ordered {quantity} {size} {product} with {extra}.\n")
    total.append(coffee_items[product][size])


add_size()


def cal_price():
    cost = total * int(quantity)
    price = plus * int(quantity)
    total_price = price + cost
    print(f"Your total cost of your purchase is €{sum(total_price)}\n")


cal_price()

def order_num():
    
    print(f"Your order number is {random.randint(1,10)}\n")


order_num()

def welcome():
        input("Would you like to order again")
        if order == yes:
            get_order_item()              
        else:
            print(sum(total))


welcome()

def main():
    pass


main()