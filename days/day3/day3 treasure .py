print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to Treasure Island. \nYour mission is to find the treasure.\n"
      "You're at a cross road. Where do you want to go?")

answer1 = (input('Type "left" or "right"')).lower()
if answer1[0] == 'l':
    print("You fell into a hole. Game Over!")
else:
    print("You've come to a lake. There is an island in the middle of the lake.")
    answer2 = (input("Type 'wait' to wait for a boat. "
                     "Type 'swim' to swim across.")).lower()
    if answer2[0] == 's':
        print('The trout have ate you! Game over!')
    else:
        answer3 = (input("You arrive at the island unharmed. There is a house with 3 doors. \n"
                         "One red, one yellow and one blue. "
                         "Which colour do you choose?")).lower()
        if answer3[0] == 'r':
            print("You enter a room of beasts. Game Over!")
        elif answer3[0] == 'b':
            print("It's a room full of fire. Game Over!")
        else:
            print("You found the treasure! You Win!")
