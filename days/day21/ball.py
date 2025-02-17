from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.x_move = 10  # Initial x-axis movement step
        self.y_move = 10  # Initial y-axis movement step
        self.move_speed = 0.1

    def move(self):
        """Move the ball."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Reverse the ball's y-direction (e.g., when hitting top/bottom walls)."""
        self.y_move *= -1


    def bounce_x(self):
        """Reverse the ball's x-direction (e.g., when hitting paddles)."""
        self.x_move *= -1


    def reset_position(self):
        """Reset the ball to the center and reverse its x-direction."""
        self.goto(0, 0)
        self.bounce_x()