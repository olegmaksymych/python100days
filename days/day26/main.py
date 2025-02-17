import pandas as pd

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# Get user input and convert to uppercase
user_input = input("Enter a word: ").upper()

# Generate the phonetic code list
generated_list = [nato_dict[letter] for letter in user_input if letter in nato_dict]
print(generated_list)
