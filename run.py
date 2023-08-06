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
extra_items = {"Soya Milk": .50, "Cream": .75, "Chocolate": 1.00,
                "Oat Milk": .50}
total = []
plus = []


def add_coffee():
    global product
    while True:
        item = [['Latte'], ['Flat White'], ['Americano'], ['Cappucino'], ['Mocha']]
        headers = ["Name"]
        print(tabulate(item, headers, tablefmt="rounded_outline"))  

        product = input("\nWhat coffee would you like off the menu? \n")
    
        if product in coffee_items:
            break
        else:
            print()
            print("NOT A VALID OPTION!\n")
        
           
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
    print(f"\nYou have ordered:\n{quantity} - {size} {product} with {extra}.\n")
    total.append(coffee_items[product][size])


add_size()


def cal_price():
    cost = total * int(quantity)
    price = plus * int(quantity)
    total_price = price + cost
    print(f"The total price is:\n €{sum(total_price)}\n")


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