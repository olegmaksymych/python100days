import time
from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

the_player = Player()
cars = []  # List to store cars
score = Scoreboard()

# Keyboard bindings
screen.listen()
screen.onkey(the_player.move, "Up")      # Move up


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create new cars randomly
    num_cars = min(score.level, 2)  # Максимум 2 машин за один цикл

    for _ in range(num_cars):
        if random.randint(1, 6) == 1:  # Регулюємо частоту
            new_car = Car()
            cars.append(new_car)

    # Move all cars
    for car in cars:
        if car.distance(the_player) < 25:
            game_is_on = False
            score.game_over()
        else:
            car.move()
            if the_player.ycor() >= 280:
                the_player.reset_position()
                score.level_up()
                for car in cars:
                    car.increase_speed()  # Increase car speed when leveling up


screen.exitonclick()

