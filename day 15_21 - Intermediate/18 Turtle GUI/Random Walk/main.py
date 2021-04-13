import turtle as t
import random

# DRAW A SHAPE

def draw_shapes(moves, distance, angle,colour):
    """Timmy draws a shape depending on how many moves and angle.
    colour is the colour of timmy and the pen

    Args:
        moves ([Integer]): [How many moves for timmy]
        distance ([integer]): [How far Timmy mover]
        angle (float): [angle of each turn 90 degrees for a square]
    """    
    for _ in range(moves):
        timmy.color(colour)
        timmy.forward(distance)
        timmy.right(angle)

def timmy_dash(moves, distance):
    """Move Timmy the turtle leaving a dashed line

    Args:
        moves ([integer]): [Number of moves for Timmy]
        distance ([Integer]): [Distance of each move]
    """    
    for _ in range(100):
        timmy.pendown()
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)

def random_walk(direction,colour,angle,pen_size):
    
    timmy.pencolor(colour)
    timmy.pensize(pen_size)
    timmy.forward(50)
    timmy.speed('fastest')
    if direction == 0:
        timmy.left(angle)
    else:
        timmy.right(angle)




timmy = t.Turtle()
# Change the colormode of the turtle module to r,g,b 0-255
t.colormode(255)
timmy.shape('turtle')
timmy.color('red')

# move = timmy_turn_right(100,100,3.6)

###################### DRAW A DASHED LINE ##########################
#dash = timmy_dash(25, 10)

################### DRAW OVERLAPPING SHAPES( TRIANGLE, SQUARE, PENTAGON, HEXAGON ETC) ##############

# for x in range(3,11):
#     # Random draw colour
#     colour = random.choice(['red','green','blue','violet','black','yellow', 'purple'])
#     draw_shapes(x, 100, 360/x, colour)

##################### RANDOM WALK ########################
def random_colour():
    """Generates a random colour r,g,b and returns as a tuple

    Returns:
        [tuple]: [(r,g,b))]
    """    
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r,g,b) # Return a tuple 


for x in range(1000):
    direction = random.randint(0, 1) # Left or right
    #colour = random.choice(['red','green','blue','violet','black','yellow', 'purple'])
    colour = random_colour() 
    angle = random.choice([0,90,180,270]) # North, East, South or West
    random_walk(direction, colour, angle,10)
    

screen = t.Screen()
screen.exitonclick()