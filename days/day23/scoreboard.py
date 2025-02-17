from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1  # Start at level 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)  # Position in the top-left
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard display."""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        """Increases the level and updates the display."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write(f"GAME OVER \n Your score is {self.level}", align="center", font=FONT)
