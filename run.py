import gspread
from google.oauth2.service_account import Credentials
import game

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('supernatural-quiz')


def start_game(game_data):
    """
    Displays welcome text and instructions as 
    well as getting the users name.
    """
    print("Welcome to the 'Supernatural' quiz")
    print("How well do you know the show?")

global name
name = input("What is your name: \n")

while not name.strip():
    print("Please enter your name?\n")
    name = input("What is your name: \n")
else:
    print(f"How well do you know 'Supernatural' {name}!\n")
    print(f"There are {num_of_questions} multiple choice questions.\n")
    print("To choose an answer type A, B or C.\n")
    print("Have fun!\n")
