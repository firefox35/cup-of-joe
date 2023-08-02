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
print("We have a large selection of drinks available from our menu.\n")


def add_coffee():
    global list
    list = [['Latte'],
            ['Flat White'],
            ['Americano'],
            ['Cappucino'],
            ['Mocha']
        ]
    headers = ["Name"]
    print(tabulate(list, headers, tablefmt="rounded_outline"))
    list = input("\nWhat coffee would you like off the menu? \n")

add_coffee()

def quantity():
        global quantity
        quantity = int(input(f"\nHow many would {list} you like? \n"))
   
quantity() 


def add_extra():
    global extra
    extra = [["soya milk"], ["cream"], ["chocolate"], ["oat milk"]]
    headers = ["Extra"]
    print(tabulate(extra, headers, tablefmt="rounded_outline"))
    extra = input(f"\nWould you like anything extra with your {list}? \n")
    
add_extra()


def add_size():
    global size
    size = [["Small"], ["Meduim"], ["Large"]]
    headers = ["Size"]
    print(tabulate(size, headers, tablefmt="rounded_outline"))
    size = input("\nWhat size would you like? \n")
    print (f"\nYou have ordered {quantity} {size} {list} with {extra} from the menu")

add_size()



def cal_price(self):
    
    total = quantity * price

def main():
    pass