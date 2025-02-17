import turtle
from car import Car
from the_road import Road
from scoreboard import Scoreboard
import time

# Set up the screen
screen = turtle.Screen()
screen.setup(width=700, height=600)
screen.bgcolor("white")
screen.tracer(0)  # Turn off automatic screen updates for smoother animation

# Create the road and draw the road lines
road = Road()
road.draw_lines()

# Create the player (turtle)
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.goto(0, -280)
player.setheading(90)  # Facing up

# Function to move the player in all directions
def move_turtle(direction):
    if direction == "up":
        player.sety(player.ycor() + 20)
    elif direction == "down":
        player.sety(player.ycor() - 20)
    elif direction == "left":
        player.setx(player.xcor() - 20)
    elif direction == "right":
        player.setx(player.xcor() + 20)

# Keyboard bindings
screen.listen()
screen.onkey(lambda: move_turtle("up"), "Up")       # Move up
screen.onkey(lambda: move_turtle("down"), "Down")   # Move down
screen.onkey(lambda: move_turtle("left"), "Left")   # Move left
screen.onkey(lambda: move_turtle("right"), "Right") # Move right

# Create scoreboard
scoreboard = Scoreboard()

# Main game loop
def game_loop():
    car_speed = 5  # Initial car speed
    cars = [Car(car_speed) for _ in range(8)]  # Create 5 cars

    # Main game loop
    while True:
        time.sleep(0.1)  # Slow down the loop for smoother animation
        screen.update()  # Refresh the screen

        # Move each car
        for car in cars:
            car.move()

        # Check for collision with cars
        for car in cars:
            if player.distance(car.car) < 10:  # Simple collision detection
                print("Game Over!")
                return  # Exit the game loop if a collision happens

        # If player reaches top, increase score and restart the game with faster cars
        if player.ycor() > 290:
            scoreboard.increase_score()
            player.goto(0, -280)  # Reset player to start position
            car_speed += 2  # Increase car speed
            cars = [Car(car_speed) for _ in range(8)]  # Create new cars with increased speed

# Start the game loop
game_loop()

# Keep the window open
screen.mainloop()
