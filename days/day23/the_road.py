import turtle


class Road:
	def __init__(self):
		self.road_turtle = turtle.Turtle()
		self.road_turtle.hideturtle()
		self.road_turtle.speed(0)

	def draw_lines(self):
		"""
		Draws the 7 lanes of the road on the screen.
		Each lane is 80 pixels high. Leaves 10 pixels at the bottom and 30 pixels at the top.
		"""
		self.road_turtle.penup()
		self.road_turtle.color("black")
		start_y = -270 + 10  # Start position for the first road line

		for i in range(7):  # 7 lanes + 1 extra line at the top
			self.road_turtle.goto(-300, start_y + i * 80)
			self.road_turtle.pendown()
			self.road_turtle.forward(600)  # Draw a horizontal line
			self.road_turtle.penup()
