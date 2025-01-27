import turtle
from color_decorator import random_color_decorator

turtle.colormode(255)  # Allow RGB color range
tim = turtle.Turtle()
screen = turtle.Screen()
tim.shape("turtle")
tim.speed(2)  # Adjust speed for faster drawing
screen.title("Geometric Shapes with Random Colors")


# Decorator to apply random colors
@random_color_decorator
def draw_shape(t, num_sides, length):
    """Draw a polygon with random colors."""
    angle = 360 / num_sides
    for _ in range(sides):
        t.forward(length)
        t.right(angle)
    t.end_fill()


# Starting parameters
initial_sides = 3  # Start with a triangle
max_sides = 10  # Up to a decagon
side_length = 50  # Starting side length


# Draw shapes
for sides in range(initial_sides, max_sides + 1):
    draw_shape(tim, sides, side_length)
    tim.penup()
    tim.forward(side_length)  # Move to the next position
    tim.pendown()
    tim.home()

screen.mainloop()



