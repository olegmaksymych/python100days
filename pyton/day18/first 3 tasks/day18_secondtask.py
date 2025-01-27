import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
tim.pensize(1)  # Optional: Set pen size
steps = 36
step_length = 30
screen.colormode(255)
tim.speed(0)


def color_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for _ in range(steps):
    tim.pencolor(color_generator())
    tim.circle(100)
    tim.left(10)

screen.mainloop()
