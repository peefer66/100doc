from turtle import Turtle, Screen
import time

STARTING_POSITION = [(0,0),(-20,0),(-40,0)] # Start of game positionfor the first 3 segments
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

     # Use the add_segment to initialize the snake
     # with three segmants
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
           
    # Add segmant used by the iniializer and the extender methods
    def add_segment(self,position):
        new_snake_segment = Turtle('square')
        new_snake_segment.penup()
        new_snake_segment.color('white')
        new_snake_segment.goto(position)
        self.segments.append(new_snake_segment)
    
    # Use the add segment def to extend the length of the snake
    # when food consumed
    def extend_snake(self):
        self.tail = self.segments[len(self.segments)-1]
        position = self.tail.position()
        self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1): # Start, finish, step
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

# Direction control - not allowed to go back on itself
# Make use of CONSTANTS

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)

    