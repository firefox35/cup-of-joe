import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('cuppa_joe')

def choose():
        print("****Welcome to Cuppa Joe****\n") 
        print("Please select from the following menu\n")
        list = [['Latte', 3.20, 3.50, 3.75],
                ['Flat White', 2.30, 2.50, 2.80],
                ['Americano', 2.50, 2.80, 3.10],
                ['Cappucino', 3.20, 3.50, 3.75],
                ['Mocha', 3.20, 3.50, 3.75]
            ]

        headers = ["Code", "Name","Small","Meduim","Large"]
        print(tabulate(list, headers, showindex="always", tablefmt="rounded_outline"))

        list = input("Enter here your selection : \n")
        print("\nYou have selected " + list + " from the menu")

choose()