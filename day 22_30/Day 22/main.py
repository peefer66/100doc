from turtle import Turtle, Screen
import time

from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball



# Define the Screen
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

#Create paddle with the starting positions
r_paddle = Paddle((380,0)) 
l_paddle = Paddle((-380,0))

screen.listen()
screen.onkey(r_paddle.up,'Up')
screen.onkey(r_paddle.down,'Down')

screen.onkey(l_paddle.up,'a')
screen.onkey(l_paddle.down,'z')

# Scoreboard
r_scoreboard = Scoreboard((20, 250))
l_scoreboard = Scoreboard((-20, 250))

# Ball
ball = Ball()

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.velosity)
    ball.move()

    # Detect collision with top and bottom
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce('wall')
    # Detect collision wth paddle
    if ball.distance(r_paddle) < 40 and ball.xcor() >320 or ball.distance(l_paddle) < 40 and ball.xcor() < -320:
        ball.bounce('paddle')

    # When the ball goes past the paddle increment the score of the opposite paddle
    # return ball to the center and servr in the opposite direction
    if ball.xcor() > 400:
        r_scoreboard.update_score()
        # Restart
        ball.goto(0,0)
        ball.bounce('paddle') # Reverses the direction of the ball
     
    if ball.xcor() < -400:
        l_scoreboard.update_score()
        # Restart
        ball.goto(0,0)
        ball.bounce('restart') # Reverses the direction of the ball
       

# Close the screen
screen.exitonclick()