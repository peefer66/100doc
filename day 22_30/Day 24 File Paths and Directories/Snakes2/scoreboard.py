from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # Grab the high score
        with open("day 22_30\Day 24 File Paths and Directories\Snakes2\data.txt") as data:
            self.high_score = int(data.read())

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    
    def reset(self):
        """Reset the game and check if score is greater than high score
        """        
        if self.score > self.high_score:
            self.high_score = self.score
            with open('day 22_30\Day 24 File Paths and Directories\Snakes2\data.txt',mode='w') as data:
                data.write(str(self.high_score))
        # reset the score to 0
        self.score = 0
        self.update_scoreboard()
        with open('data.txt',mode='w') as data:
            data.write(str(self.high_score))

    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
