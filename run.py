from datetime import datetime
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

# Welcome Message

print("Welcome to the 'Supernatural' quiz.")
print("How well do you know the show?")
print("""
      /`\
.----/---\----.
 `'./     \.'`
   /`'.'.'`\
  /,-`   `-,\
  `         `  
""")


def menu():
    """
    Instructions on what options a player has.
    Play game, exit or scoreboard.
    """
    print("\n")
    print("Press 'y' to play. \n")
    print("Press 'n' to exit. \n")
    print("Press 's' for scoreboard. \n")

    while True:
        game_choices = input("What would you like to do? \n").sripe()
        print("\n")

        if game_choices == "y":
            print("Lets roll!\n")
            break
        elif game_choices == "n":
            print("Goodbye!")
            quit()
        elif game_choices == "s":
            display_top_scores()
            menu()
        else:
            print("Please select an option: 'y', 'n' or 's'.")


def player_name():
    """
    Request a name from the player.
    Must be a valid input to work.
    """
    while True:
        print("Please enter your name.\n")
        print("Must contain A-Z or a-z/n")
        print("Max 8 characters.\n")
        print("White space will be taken out.\n")

        now = datetime.now()

        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

