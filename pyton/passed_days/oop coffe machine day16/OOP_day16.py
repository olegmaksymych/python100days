from turtle import Turtle, Screen
from random import random
from prettytable import PrettyTable


# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('SpringGreen4')
# timmy.forward(100)
# angle = int(random() * 360)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmnder"])
table.add_column("Type", ["Electric", "Water", "Fire"])



print(table)

