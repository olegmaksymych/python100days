from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# TODO 1. Create the screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# TODO 2. Create paddles
right_paddle = Paddle((380, 0))  # Paddle on the right
left_paddle = Paddle((-380, 0))  # Paddle on the left

# TODO 3. Create the ball
ball = Ball()
left_score = Scoreboard(100)
right_score = Scoreboard(-100)
# Control the right paddle
screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")


# Game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # Slows down the ball movement for better gameplay
    screen.update()
    ball.move()

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ((ball.distance(right_paddle) < 50 and ball.xcor() > 340)
            or (ball.distance(left_paddle) < 50 and ball.xcor() < -340)):
        ball.bounce_x()

    # Detect if ball goes out of bounds (right paddle misses)
    if ball.xcor() > 380:
        ball.reset_position()
        right_score.increase_score()

    # Detect if ball goes out of bounds (left paddle misses)
    if ball.xcor() < -380:
        ball.reset_position()
        left_score.increase_score()

screen.exitonclick()


# TODO 3. Create another paddle

# TODO 4. Create the ball and make it move

# TODO 5. Detect collision with wall and bounce

# TODO 6. Detect collision with paddle

# TODO 7. Detect when paddle wisses

# TODO 8. Keep score
