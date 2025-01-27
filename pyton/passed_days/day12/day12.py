from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check the answer with the number to guess
def check_the_answer(user_gess, actual_number, turns):
    """CHECKS answer against guess , returns the number of turns remaining"""
    if user_gess > actual_number:
        print(f"Too high.")
        return turns - 1
    elif user_gess < actual_number:
        print(f"Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_number}")

# Function to set difficulty
def select_the_difficulty():
    select_the_difficult = input("Choose difficulty.Type 'easy' or 'hard':").lower()
    if select_the_difficult == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def the_game():
    print(logo)
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    actual_answer = randint(1, 100)
    turns = select_the_difficulty()

    # .Repeat. the guessing functionality if they get it wrong
    guess = 0
    while guess != actual_answer:
        # Let the user guess a number
        print(f"You have {turns} attempts to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_the_answer(guess, actual_answer, turns)
        if turns == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            return
        elif guess != actual_answer:
            print("Guess again!")

the_game()





