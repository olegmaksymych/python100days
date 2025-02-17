from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "green", "yellow", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100, 140]
all_turtles = []

for turtle_index in range(0, 6):
	new_turtle = Turtle(shape="turtle")
	new_turtle.color(colors[turtle_index])
	new_turtle.penup()
	new_turtle.goto(x=-230, y=y_positions[turtle_index])
	all_turtles.append(new_turtle)

if user_bet:
	is_race_on = True

while is_race_on:
	for runner in all_turtles:
		if runner.xcor() > 230:
			is_race_on = False
			winning_color = runner.pencolor()
			if winning_color == user_bet:
				print(f"You win! The winning color is {winning_color} ")
			else:
				print(f"You lose. The winning color is {winning_color} ")

		rand_distance = random.randint(0, 10)
		runner.forward(rand_distance)


screen.exitonclick()
