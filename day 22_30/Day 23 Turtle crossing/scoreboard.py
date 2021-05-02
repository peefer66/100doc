from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color('black')
        self.hideturtle()
        # call the update method
        self.update_level()
             

    def update_level(self):
        '''
        Ipdate the score after food eaten
        '''
        self.setpos(-250,250)
        self.clear() # clear before re-writing
        self.write(f'Level: {self.level}',align='center', font=('Arial', 14, 'bold'))
        self.level += 1

    def game_over(self):
        '''
        Game Over - 
        '''
        self.goto(0,0)
        self.write('Game Over',align='center', font=('Arial', 20, 'bold'))

    
        
    
    
