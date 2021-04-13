import turtle as tt
import random

# Define the turtle

tim = tt.Turtle()
# set the colormode to 255
tt.colormode(255)
# set parameters for tim
tim.pensize(2)
tim.speed('fastest')

# Randomize colour
def random_colour():
    """Generates a random colour r,g,b and returns as a tuple

    Returns:
        [tuple]: [(r,g,b))]
    """    
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r,g,b) # Return a tuple 

# itterate 6 times in total
def draw_spirograph(size_of_gap):
    """Funtion to draw the spirograph. A gap size
    between iterations of circle is passed.
    The total number of itteratios is 360 dgrees divided by the gap size

    Args:
        size_of_gap ([integer]): [gap between each iteration of circl]
    """    
    for i in range(int(360/size_of_gap)):
        # set random colour
        tim.pencolor(random_colour())
        #draw circle of radius 100
        tim.circle(100)
        # move the heading left by the size of gap
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

#Set screen to close on click
screen = tt.Screen()
screen.exitonclick()
