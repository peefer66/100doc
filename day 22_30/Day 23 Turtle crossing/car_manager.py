from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()
        

    def create_car(self):
        """Define the car object. Use random to geneate car 
        only when random number is 1. This paces out the car generation
        and appends it to all_cars list
        """        
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(280, random.randint(-250, 250))
            self.all_cars.append(new_car)        
    

    def move(self):

        """Move each car in all_cars list
        """        
        for car in self.all_cars:
            car.backward(self.car_speed)


    def level_up(self):
               
        """When turtle reaches the finish line
        level-up and inrease difficulty by increasing the speed
        """        
        self.car_speed += MOVE_INCREMENT
