import art
import random
from game_data import data as d



# TODO Display Personalities Randomly pick two personalities from the dataset.
#  Display details for both personalities (e.g., Name and Description).


def displaying_the_persons(person1, person2):
    compare_A = f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}"
    against_B = f"Against B: {person2['name']}, a {person2['description']}, from {person2['country']}"
    print(compare_A)
    print(art.vs)
    print(against_B)


# TODO Get User Input: Prompt the player to guess which personality has more followers (A or B).
def get_user_input():
    while True:  # Start a loop that will run until valid input is provided
        user_input = input("Who has more followers? Type 'A' or 'B': ").strip().lower()
        if user_input in ['a', 'b']:
            return user_input  # Return the valid input and exit the loop
        else:
            print("It is not a valid answer. Please try answering 'A' or 'B'.")


# TODO Compare and Update Score. Compare the follower counts of the two personalities.
#  Check if the player’s guess is correct:
#  - If correct, increment the score.
#  - If incorrect, end the game.


def compare_and_update_score():
    """Game logic for comparing follower counts and updating score."""
    print("\n" * 20)
    print(art.logo)
    score = 0
    first_person = random.choice(d)
    second_person = random.choice(d)

    # Ensure second_person is different from first_person initially
    while second_person == first_person:
        second_person = random.choice(d)

    while True:
        displaying_the_persons(first_person, second_person)
        user_input = get_user_input()

        # Determine if the user guessed correctly
        correct = (
            (user_input == 'a' and first_person['follower_count'] > second_person['follower_count']) or
            (user_input == 'b' and second_person['follower_count'] > first_person['follower_count']))
        if correct:
            score += 1
            print(f"Correct! Your current score is: {score}")
            # Randomly decide the new first person
            first_person = random.choice([first_person, second_person])
            # Select a new second person, ensuring it is not the same as the updated first person
            second_person = random.choice(d)
            while second_person == first_person:
                second_person = random.choice(d)
        else:
            print(f"Wrong! Your final score is: {score}")
            break

# Start the game
compare_and_update_score()
