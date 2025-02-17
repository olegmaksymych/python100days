from turtle import Turtle, Screen
import random


# Turtle setup
tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed("fastest")  # Make the drawing faster


def color_generator():
    """Function to generate random color"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_row():
    """Function to draw a horizontal row of circles"""
    for _ in range(10):  # Draw 10 circles
        tim.penup()
        tim.hideturtle()
        tim.forward(50)  # Move forward to the next circle position
        tim.pendown()
        tim.dot(20, color_generator())



def move_to_next_row(starting_x, starting_y, row_number):
    """Function to move the turtle to the next row"""
    new_y = starting_y - (50 * row_number)  # Move down by 50 for each row
    tim.penup()
    tim.goto(starting_x, new_y)  # Go to the new position
    tim.pendown()


# Main drawing loop
start_x = -250  # Starting x position
start_y = 220  # Starting y position
tim.penup()
tim.goto(start_x, start_y)
tim.pendown()

for row in range(10):  # 10 rows
    draw_row()
    move_to_next_row(start_x, start_y, row + 1)

# Exit on click
screen.exitonclick()
