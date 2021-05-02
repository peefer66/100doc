import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

# Create Screen object an set the dimensions
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) # Allow for screen .refresh allowing smoother motion

# Create player object
player = Player()
#create car object
car_manager = CarManager() # Car pobject
scoreboard = Scoreboard() # scoreboard object

screen.listen()
screen.onkey(player.up, 'Up')

#### Main game play ####
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update() # see tracer(0)

    # Turtle  crosses finishing line
    # Increment  scorboard level indicator
    # Increment level speed
    if player.ycor() > 280:
        player.starting_position()
        scoreboard.update_level()
        car_manager.level_up()
     
    # Car manager
    '''
    Create car and define attributes
    '''
    car_manager.create_car()
    car_manager.move()

    # detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 15:
            scoreboard.game_over()
            game_is_on = False
    
    

screen.exitonclick()