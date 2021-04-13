import turtle as tt

tim = tt.Turtle()
screen = tt.Screen()

def move_forward():
    tim.forward(5)

def move_backwards():
    tim.backward(5)

def turn_right():
    tim.right(5)

def turn_left():
    tim.left(5)

def clear_screen():
    tim.clear()
    tim.reset()

def undo_last():
    tim.undo()

screen.listen()
screen.onkeypress(key='w', fun=move_forward)
screen.onkeypress(key='s', fun=move_backwards)
screen.onkeypress(key='d', fun=turn_right)
screen.onkeypress(key='a', fun=turn_left)
screen.onkeypress(key='c', fun=(clear_screen))
screen.onkeypress(key='u', fun=(undo_last))

screen.exitonclick()