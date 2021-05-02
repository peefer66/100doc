from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        #self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.velosity = 0.1
                
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce(self, collision):
        if collision == 'wall':
            self.y_move *= -1
        elif collision == 'paddle':
            self.x_move *= -1
            self.velosity *= 0.9
        else:
            self.x_move *= -1
            self.velosity = 0.1

        
            
