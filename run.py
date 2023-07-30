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
waitdress = ['Becky', 'Tisha', 'Cathy','Sarah','Helen']
print("Hi, My name is " + random.choice(waitdress) + ".\n")
print("We have a large selection of drinks from our menu.\n")

class Item:

    def __init__(self, list, quantity, price):
        self.list = list
        self.quantity = quantity
        self.price = price

class Coffee_Shop:

    def __init__(self):
        self.list_items = []
        self.order = []

    def add_order():
        
        list = [['Latte'],
                ['Flat White'],
                ['Americano'],
                ['Cappucino'],
                ['Mocha']
            ]

        headers = ["Name"]
        print(tabulate(list, headers, tablefmt="rounded_outline"))
        while True:
            try:
                order = str(input("\nWhat coffee would you like off the menu? \n"))
                list.append(order)
            except TypeError:
                print('Enter the product name')
            break
        quantity = []
        quantity = str(input("\nHow many " +  order + " would you like? \n"))
        extra = [["soya milk"], ["cream"], ["chocolate"], ["oat milk"]]
        headers = ["Extra"]
        print(tabulate(extra, headers, tablefmt="rounded_outline"))
        extra = str(input("\nWould you like anything extra with your " + order + "? \n"))
            
        size =  [["Small"], ["Meduim"], ["Large"]]
        headers = ["Size"]
        print(tabulate(size, headers, tablefmt="rounded_outline"))
        size = str(input("\nWhat size would you like? \n"))
        print(f"\nYou have ordered " + quantity +" " + size +" " + order + " with " +  extra  +  " from the menu")

    add_order()

    def cal_price():
            price = [
                    ['Latte', 3.20, 3.50, 3.8],
                    ['Flat White', 3.20, 3.50, 3.8],
                    ['Americano', 3.20, 3.50, 3.8],
                    ['Cappucino', 3.20, 3.50, 3.8],
                    ['Mocha', 3.20, 3.50, 3.8]
                ]

