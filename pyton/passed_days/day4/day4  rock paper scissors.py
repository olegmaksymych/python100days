import random

# ASCII-графіка для варіантів
rock = ('''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
''')

scissors = (''' 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

paper = ('''    
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

# Виведення інструкцій
print("What do you choose? Type 0 for Rock, 1 for Scissors, or 2 for Paper.")

# Список варіантів
list_of_choices = [rock, scissors, paper]

# Вибір гравця
player_choice_index = int(input("Your choice: "))
if player_choice_index not in [0, 1, 2]:
    print("Invalid input! You must choose 0, 1, or 2.")
    exit()

answer_of_player = list_of_choices[player_choice_index]

# Вибір комп'ютера
computer_choice_index = random.randint(0, 2)
answer_of_computer = list_of_choices[computer_choice_index]

# Виведення виборів
print(f'You chose:\n{answer_of_player}')
print(f'Computer chose:\n{answer_of_computer}')

# Логіка визначення переможця
if player_choice_index == computer_choice_index:
    print("It is a DRAW!")
elif (player_choice_index == 0 and computer_choice_index == 1) or \
     (player_choice_index == 1 and computer_choice_index == 2) or \
     (player_choice_index == 2 and computer_choice_index == 0):
    print("You Win!")
else:
    print("You Lose!")


