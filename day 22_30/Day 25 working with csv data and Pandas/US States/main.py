import turtle
import pandas as pd

image = r'C:\Users\pfiel\Documents\Python\100doc\day 22_30\Day 25 working with csv data and Pandas\US States\blank_states_img.gif'
screen = turtle.Screen()
screen.title('U.S States Game')
screen.addshape(image)
turtle.shape(image) # Map

data = pd.read_csv(r"C:\Users\pfiel\Documents\Python\100doc\day 22_30\Day 25 working with csv data and Pandas\US States\50_states.csv")
all_states = data.state.to_list()
correct_count = 0

guessed_states = []
missing_states = []

while len(guessed_states)< 50:
    answer_state = screen.textinput(f'{correct_count}/50 Correct', 'Enter a State name' ).title()
    if answer_state == 'Exit':
        break
    if answer_state in all_states:
        if answer_state not in guessed_states:
            # Create Turtle
            correct_count += 1
            guessed_states.append(answer_state)
            #Create turtle
            tt = turtle.Turtle()
            tt.hideturtle()
            tt.penup()
            state_data = data[data.state == answer_state]
            # Coords in the csv are in string therfore convert to int
            tt.goto(int(state_data.x), int(state_data.y))
            tt.write(answer_state)

#  Create a list of the missed states
# for state in all_states:
#     if state not in guessed_states:
#         missing_states.append(state)
missing_states = [state for state in all_states if state not in guessed_states]

missing_path = r'C:\Users\pfiel\Documents\Python\100doc\day 22_30\Day 25 working with csv data and Pandas\US States\missing_states.txt'
 # if the file already exists clear the contents
if missing_path:
    with open(missing_path, 'w') as f:
        f.truncate(0)
# Create a list of the missed states
for state in missing_states:
    with open(missing_path, mode='a') as f:
        f.write(state)
        f.write('\n')





            


