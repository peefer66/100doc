import turtle as tt
import random

tim = tt.Turtle()
tt.colormode(255)

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49),
              (223, 201, 135), (52, 93, 124), (172, 154, 40),
              (140, 30, 19), (133, 163, 185), (198, 91, 71), 
              (46, 122, 86), (72, 43, 35), (145, 178, 148), 
              (13, 99, 71), (233, 175, 164), (161, 142, 158),
              (105, 74, 77), (55, 46, 50), (183, 205, 171), 
              (36, 60, 74), (18, 86, 90), (81, 148, 129),
              (148, 17, 20), (14, 70, 64), (30, 68, 100), 
              (107, 127, 153), (174, 94, 97), (176, 192, 209)]

tim.penup()
tim.hideturtle()
tim.setheading(225)# WSW
tim.forward(300)
tim.setheading(0)#East
tim.speed('fastest')
number_of_dots = 100

for dot_count in range(1,number_of_dots +1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
# display 10 dots per line then
# move up and forward 50
# move to the beginnig of 
    if dot_count % 10 == 0: # end of the lin
        tim.setheading(90) # set heading North
        tim.forward(50) # move up 50
        tim.setheading(180)# West
        tim.forward(500)# go to the beginning of the line
        tim.setheading(0) # Turn East .... next iteration of the loop



screen = tt.Screen()
screen.exitonclick()
