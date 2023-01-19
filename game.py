# This is the questions for the game and the score and final messages.

def play_game():
    """
    The questions and score data. if a player
    gets the questions right the score increases by 1.
    """
    score = 0

    while True:
        # Question 1
        print("Who are the main two characters?")
        answer1 = input("A. Mike and Ike \nB. Sam and Dean \nC. Lou and Moe \nAnswer: \n").strip()
        if answer1.upper() == "B":
            print("Yes!\n")
            score += 1
            break
        elif answer1.upper() == "A" or answer1.upper() == "C":
            print("Oops!\n")
            break
        else:
            print("Invalid input!! Please use 'A' 'B' or 'C'\n")

        # Question 2
        print("What was Sam studying in Stanford?")
        answer1 = input("A. Law \nB. Accounting \nC. Business \nAnswer: \n").strip()
        if answer1.upper() == "A":
            print("Yes!\n")
            score += 1
            break
        elif answer1.upper() == "B" or answer1.upper() == "C":
            print("Oops!\n")
            break
        else:
            print("Invalid input!! Please use 'A' 'B' or 'C'\n")

        # Question 3
        print("In the episode “The Slice Girls”\n what was Deans Daughters name?")
        answer1 = input("A. Emma \nB. Amanda \nC. Jenny \nAnswer: \n").strip()
        if answer1.upper() == "A":
            print("Yes!\n")
            score += 1
            break
        elif answer1.upper() == "B" or answer1.upper() == "C":
            print("Oops!\n")
            break
        else:
            print("Invalid input!! Please use 'A' 'B' or 'C'\n")

        # Question 4
game_data = [

    {"question": "In the episode “Yellow Fever” what happened to Dean?",
     "answers": {"A": "He gets shot",
                 "B": "He gets stabbed",
                 "C": "He gets haunted"},
     "correct_answer": "C"},
    {"question": "What does Sam add to Deans car?",
     "answers": {"A": "A new radio",
                 "B": "An IPod jack",
                 "C": "A drink holder"},
     "correct_answer": "B"},
    {"question": "When the apocalypse starts who \n is the first horseman they face?",
     "answers": {"A": "Death",
                 "B": "Famine",
                 "C": "War"},
     "correct_answer": "C"},
    {"question": "How many meat suits has Ruby had?",
     "answers": {"A": "Four",
                 "B": "Six",
                 "C": "One"},
     "correct_answer": "A"},
    {"question": "What are Crowley`s nick names for the boys?",
     "answers": {"A": "Shaggy and Scooby",
                 "B": "Moose and Squirrel",
                 "C": "Mouse and Elephant"},
     "correct_answer": "B"},
    {"question": "How many things cannot be killed by the Colt?",
     "answers": {"A": "Eight",
                 "B": "Two",
                 "C": "Five"},
     "correct_answer": "C"},
    {"question": "What was the name of Sams dog (when Dean was missing)??",
     "answers": {"A": "Rover",
                 "B": "Spot",
                 "C": "Riot"},
     "correct_answer": "C"},
    {"question": "What car does Dean drive?",
     "answers": {"A": "`69 Chevy Impala",
                 "B": "`67 Chevy Impala",
                 "C": "`69 Ford Mustang"},
     "correct_answer": "B"},
    {"question": "What is the family business?",
     "answers": {"A": "Saving people, hunting things.",
                 "B": "Helping people, killing monsters",
                 "C": "Helping people, hunting things."},
     "correct_answer": "A"},
    {"question": "What is the name of Castiel`s vessles wife??",
     "answers": {"A": "Anne Novak",
                 "B": "Amelia Novak",
                 "C": "Sarah Novak"},
     "correct_answer": "B"},
    {"question": "How many Winchesters have appeared on the show?",
     "answers": {"A": "Six",
                 "B": "Eight",
                 "C": "Two"},
     "correct_answer": "A"},
    {"question": "What are the names of the 4 Princes of Hell?",
     "answers": {"A": "Azreal, Rancial, Dagron, Amrodus",
                 "B": "Azreal, Rheagon, Damrus, Asphodel",
                 "C": "Azazel, Ramiel, Dagon, Asmodeus"},
     "correct_answer": "C"},
    {"question": "What was the first “thing” \n the boys faced in the “Pilot” episode?",
     "answers": {"A": "A Wendigo",
                 "B": "Woman in white",
                 "C": "A Trickster"},
     "correct_answer": "B"},
    {"question": "In the episode “in the beginning” \n what year is Dean sent to?",
     "answers": {"A": "1969",
                 "B": "1943",
                 "C": "1973"},
     "correct_answer": "C"},
    {"question": "Where is the bunker that the boys call home from season 8?",
     "answers": {"A": "Kansas",
                 "B": "Denver",
                 "C": "Nebraska"},
     "correct_answer": "A"},
    {"question": "Which figures (Biblical) are the boys related to?",
     "answers": {"A": "Cain and Abel",
                 "B": "Jacob and Rachel",
                 "C": "Moses and Abraham"},
     "correct_answer": "A"},
    {"question": "Charlie has a figurine of which character on her desk?",
     "answers": {"A": "Princess Peach",
                 "B": "Hermione Granger",
                 "C": "Golum"},
     "correct_answer": "B"},
    ]


def count_keys(game_data):
    """
    This will counnt the number of questions and allow
    more to be added or even taken away.
    """
    count = 0
    for i in enumerate(game_data):
        count += 1
    return count


num_of_questions = (count_keys(game_data))
    