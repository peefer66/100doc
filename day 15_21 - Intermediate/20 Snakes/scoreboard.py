from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        # call the update method
        self.update_score()
             

    def update_score(self):
        '''
        Ipdate the score after food eaten
        '''
        self.setpos(0,280)
        self.clear() # clear before re-writing
        self.write(f'Score: {self.score}',align='center', font=('Arial', 14, 'bold'))
        self.score += 1

    def game_over(self):
        '''
        Game Over - 
        '''
        self.goto(0,0)
        self.write('Game Over',align='center', font=('Arial', 20, 'bold'))

    