from turtle import Turtle

STARTING_POSITION = (0, -290)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.starting_position()

    def up(self):
        new_y = self.ycor() + 20
        self.goto(0, new_y)

    def starting_position(self):
        self.goto(STARTING_POSITION)



