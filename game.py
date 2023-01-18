def play_game():
    """
    All of the questions of the game.
    if the user gets an answer right score will increase by 1.
    """

    score = 0

    while True:
        print("Who are the main two characters?")
        answer1 = input(
            "A.Sam and Dean \nB.Mike and Ike \nC.Joe and Bo \nAnswer: \n"
        ).strip()
        if answer1.upper() == "A":
            print("Correct!\n")
            score += 1
            break
        elif answer1.upper() == "B" or answer1.upper() == "C":
            print("Incorrect!\n")
            break
        else:
            print("Invalid input!! Please choose between 'A' 'B' or 'C'\n")