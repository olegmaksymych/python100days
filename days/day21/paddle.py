from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)  # Stretch to make it a rectangle

    def move_up(self):
        """Move the paddle up."""
        if self.ycor() < 230:  # Keep the paddle within the upper boundary
            self.sety(self.ycor() + 40)

    def move_down(self):
        """Move the paddle down."""
        if self.ycor() > -230:  # Keep the paddle within the lower boundary
            self.sety(self.ycor() - 40)
