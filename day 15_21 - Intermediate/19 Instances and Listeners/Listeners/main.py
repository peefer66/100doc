import turtle as tt

tim = tt.Turtle()
screen = tt.Screen()

def move_forward():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick() 