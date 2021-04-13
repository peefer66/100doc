import turtle as tt
import random

turtles = ['red','green', 'blue', 'yellow']
turtle_object_list = []
winner = False
y_axis = -120

screen = tt.Screen()
screen.setup(width=500,height=400)


def turtle_race(turtles):
    """The turtle race... a random turtle is selected from a list of
       turtle objects and the race begins. and a random moves forward between 
       1 and 10 paces. The position of the same turtle is assessed to see if 
       it has finished the race

    Args:
        turtles ([list of turtle objects]): [list of turtle objects]

    Returns:
        [True/ False]: [true stops the race, false continue]
    """    
    #Pick a random turtle and move forward
    turtle = random.choice(turtles) # pick a random turtle
    turtle.forward(random.randint(1,10)) # Move the turtle random distance
    if turtle.xcor() >= 230: # if turtle reaches the finish
        global winning_turtle # The winning turtle is
        winning_turtle = turtle.color()[0]
        return True # End the race stop the while loop
    else:
        return False # Keep racing


user_choice = screen.textinput(title='Make your bet', prompt='Whitch turtle will win the race. Enter a colour red, green, blue or yellow')
# Create instances of Turtle
for turtle_name in turtles:
    colour = turtle_name
    turtle_name = tt.Turtle('turtle') # Create object
    turtle_name.color(colour) # set the colour for each turtle
    turtle_name.penup() # lift pen so no line is drawn
    turtle_object_list.append(turtle_name) # create list of turtle objects
    turtle_name.goto(-230,y_axis) # move to the start line and move each up
    y_axis += 60 # increment the y position for each turtle

while not winner:
    # Pass the turtle list to the turtle race function
    winner =  turtle_race(turtle_object_list)

print(f'The winning turtle is {winning_turtle}, you chose {user_choice}')
    
      
screen.exitonclick()


