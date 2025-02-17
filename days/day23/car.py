from turtle import Turtle
import random

CAR_COLORS = ["red", "blue", "yellow", "purple", "orange", "green"]
START_X = 300  # Cars start from the left
MOVE_DISTANCE = 5  # Speed of the cars
Y_POSITIONS = [-215, -155, -95, -35, 35, 95, 155, 215]  # Y-lanes for the cars


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)  # Make it rectangular
        self.penup()
        self.color(random.choice(CAR_COLORS))
        self.goto(START_X, random.choice(Y_POSITIONS))  # Random y-position
        self.setheading(180)  # Move left

    def move(self):
        self.forward(MOVE_DISTANCE)

    def increase_speed(self):
        global MOVE_DISTANCE
        MOVE_DISTANCE += 0.01  # Increase the speed by 1 unit each time
