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
        game_choices = input("What would you like to do? \n")
        print("\n")

        if game_choices == "y":
            print("Lets roll!\n")
            break
        elif game_choices == "n":
            print("Goodbye!")
            quit()
        elif game_choices == "s":
            display_top_5_scores()
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

        name = input("What is your name: \n")

        if check_name(name):
            print("\n")
            print(f"Welcome {name}, lets start.")
            print("This is a multiple choice. \n")
            print("Select A, B or C.\n")
            print("Good Luck!")
            data = game.play_game()
            update_score_worksheet(data, name, dt_string)
            menu()

    check_name(name)
    return name.stripe()


def check_name(name):
    """
    This is used to validate the user name.
    An error will display if the name is too long,
    empty, or invalid characters are used.
    """
    try:
        if not name:
            raise ValueError("Please enter a valid name!")
        if len(name) > 8:
            raise ValueError("Name is too long")
        if not name.isalpha():
            raise ValueError("Only letters are permitted")
    except ValueError as e:
        print(f"Invalid: {e}! Try again.\n")
        return False

    return True


def update_score_worksheet(data, name, dt_string):
    """
    Updates the score, name and date and time.
    Entered into a google sheet.
    """
    print("Updating score...\n")
    score_worksheet = SHEET.worksheet("score")

    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    score_worksheet.append_row([data, name, dt_string])
    print("Score has updated.\n")


def game_restart():
    """
    Allow the player to play again.
    """
    while True:
        data = game.play_game()
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        score_worksheet = SHEET.worksheet('score')
        score_worksheet.append_row([data, " ", dt_string])
        menu()


def display_top_5_scores():
    """
    Display the top 5 scores.
    Data is fetched form google sheets via API.
    """
    records_score = SHEET.worksheet('score').get_all_values()[1:]

    for data_set in records_score:
        data_set[0] = int(data_set[0])

    sorted_data = sorted(records_score, reverse=True)

    print("Top 5 scores:")
    print("Score \t Name \t Time")

    for line in range(5):
        print(str(line+1) + str(sorted_data[line]))


def main():
    """
    Run the game functions
    """
    menu()
    player_name()


main()
