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

# Welcome message
print("welcome to the 'Supernatural' quiz.")
print("How well do you know the show?")


def start_game(game_data):
    """
    Displays welcome text and instructions as 
    well as getting the users name.
    """
    print("Welcome to the 'Supernatural' quiz")
    print("How well do you know the show?")

