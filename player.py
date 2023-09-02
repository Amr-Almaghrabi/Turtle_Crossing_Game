from turtle import Turtle

FINAL_Y = 280
STARTING_POSITION = (0, -280)

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.shapesize(1)
        self.setheading(90)
        self.go_to_start()

    def up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def at_finish_line(self):
        if self.ycor() > FINAL_Y:
            return True

    def go_to_start(self):
        self.goto(STARTING_POSITION)

