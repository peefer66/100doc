from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.position = position
    
        self.update_score()

    def update_score(self):
        self.setpos(self.position)
        self.clear() # clear before re-writing
        self.write(f'{self.score}',align='center', font=('Arial', 32, 'bold'))
        self.score += 1