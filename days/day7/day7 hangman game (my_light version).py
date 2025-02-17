import random
# Project web-site:
import random

logo = ('''
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/
''')

print(logo)
# A list of meaningful words


# Word pool
word_pool = [
    "apple", "banana", "cherry", "date", "grape", "kiwi", "lemon", "mango", "orange", "peach",
    "pear", "plum", "berry", "melon", "apricot", "fig", "lime", "papaya", "nectarine", "pineapple",
    "carrot", "potato", "tomato", "onion", "garlic", "cucumber", "pepper", "spinach", "broccoli", "lettuce",
    "dog", "cat", "mouse", "elephant", "tiger", "lion", "rabbit", "horse", "zebra", "bear",
    "house", "table", "chair", "window", "door", "garden", "school", "office", "book", "pen"
]

# Select a random word
random_word = random.choice(word_pool)
hidden_word = len(random_word) * '_'
print(f'Word to guess: {hidden_word}')
amount_of_attempts = 6


# Function to reveal guessed letters
def reveal_letter(random_word, hidden_word, guessed_letter):
    hidden_list = list(hidden_word)  # Convert hidden word to list for easier manipulation
    for index, letter in enumerate(random_word):
        if letter == guessed_letter:
            hidden_list[index] = guessed_letter
    return ''.join(hidden_list)  # Convert back to a string


# Game loop
while amount_of_attempts > 0:
    guessed_letter = input('Guess a letter: ').lower()

    # Update the hidden word
    new_hidden_word = reveal_letter(random_word, hidden_word, guessed_letter)

    if new_hidden_word == hidden_word:  # Incorrect guess
        print(f'Incorrect guess! Word to guess: {hidden_word}')
        amount_of_attempts -= 1  # Deduct an attempt
        print(f'You have {amount_of_attempts} ammount of attempts to guess')
    else:  # Correct guess
        print(f"Good guess! The word now: {new_hidden_word}")

    # Update the hidden word
    hidden_word = new_hidden_word

    # Check if the player has guessed the word
    if hidden_word == random_word:
        print(f"Congratulations! You guessed the word: {random_word}")
        break
else:
    print(f"Out of attempts! The word was: {random_word}")

