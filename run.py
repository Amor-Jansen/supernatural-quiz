from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('supernatural-quiz')

#Welcome message
print("welcome to the 'Supernatural' quiz.\n")
print("How well do you know the show?")

def player_name():
    """
    This will get the player name.
    the request will only end when a valid name is chosen.
    """
    while True:
        print("Choose a user name.\n")
        print("Only characters a-z, A-Z and 0-9 are permitted.")
        print("Maximun of 9 characters.")
        print("White space will be removed.\n")

        datetime = datetime.now()
        datetime_string = now.strftime("%d/%m/%Y %H:%M:%S")

        name = input("Please enter your name: \n")

        if 
