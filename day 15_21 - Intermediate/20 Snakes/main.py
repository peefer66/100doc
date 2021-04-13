from turtle import Screen
import time
from snakes import Snake
from food import Food
from scoreboard import Scoreboard


# Define the screen
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snakes')
screen.tracer(0)

# create Objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#control snake
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

############################# While Loop ###################
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # If the snake head is < 15 px from the food
    # food is 10x10 px then chances are the snake over the food
    # 
    if snake.head.distance(food) < 15: 
        scoreboard.update_score()
        food.refresh()
        snake.extend_snake()

    # if the snake reaches the edge of the frame ---> GAME OVER
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_on = False
        scoreboard.game_over()

    #If the snake collides with its own tail --> GAME OVER
    # slice the list so that seg ignores the first segment. Which is the head
    for seg in snake.segments[1:-1]:
           if snake.head.distance(seg) < 5:
                game_on = False
                scoreboard.game_over()
###################################################################
            
screen.exitonclick()