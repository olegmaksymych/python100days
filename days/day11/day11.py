import random
from art import logo
# Constants
ACE = 11
CARDS = [ACE, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4

# Function to draw a card
"""Returns a random card from the deck"""
def draw_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

# Function to calculate total score with ace adjustment
def calculate_score(cards):
    """Take the list of cards and calculate the total score of these cards"""
    total = sum(cards)
    aces = cards.count(ACE)
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

# Function to check for Blackjack
def is_blackjack(cards):
    return len(cards) == 2 and calculate_score(cards) == 21

# Function to draw additional cards if needed
def check_and_draw(deck, cards, current_score, threshold):
    """Automatically draws cards if the score is below a given threshold."""
    if current_score < threshold and current_score < 21:
        new_card = draw_card(deck)
        cards.append(new_card)
        current_score = calculate_score(cards)
    return current_score


# Main game logic
def blackjack():
    # Create a deck and shuffle
    deck = CARDS[:]

    # Initial card draw
    user_cards = [draw_card(deck), draw_card(deck)]
    computer_cards = [draw_card(deck), draw_card(deck)]

    # Check for immediate Blackjack
    if is_blackjack(computer_cards) and is_blackjack(user_cards):
        print(f"Your cards: {user_cards}, Blackjack!")
        print(f"Computer's cards: {computer_cards}, Blackjack!")
        print("It's a draw!")
        return
    elif is_blackjack(computer_cards):
        print(f"Computer's cards: {computer_cards}, Blackjack!")
        print("Computer wins with a Blackjack!")
        return
    elif is_blackjack(user_cards):
        print(f"Your cards: {user_cards}, Blackjack!")
        print("You win with a Blackjack!")
        return

    # Calculate initial scores
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    # User's turn to draw more cards
    while user_score < 21:
        user_choice = input("Type 'y' to get another card, 'n' to pass: ").strip().lower()
        if user_choice == 'y':
            user_cards.append(draw_card(deck))
            user_score = calculate_score(user_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
        else:
            break

        # If user goes over 21, they lose immediately
    if user_score > 21:
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print("You went over. You lose!")
        return

        # Computer's turn to draw more cards
    computer_score = check_and_draw(deck, computer_cards, computer_score, threshold=17)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    # Determine the winner
    if computer_score > 21 or user_score > computer_score:
        print("You win!")
    elif user_score < computer_score:
        print("You lose!")
    else:
        print("It's a draw!")


def choice_to_continue_the_game():
    always_play = True
    while always_play:
        blackjack()
        choice = input("Do you wish to play the game one more time? Type 'y' for yes, 'n' for no: ").strip().lower()
        if choice == 'n':
            always_play = False
            print("Thanks for playing! Goodbye!")

# Run the game
print(logo)
blackjack()
print("Welcome to Blackjack!")  # Replace with your `logo` if applicable
choice_to_continue_the_game()


