import os

computer_number = 0
my_number = 0
difficulty = ''
attempts = 0
game_over = False

    

def whats_my_number():
    import random
    computer_no = random.randint(1,100)
    print(computer_number)
    return computer_no

def compare_numbers():
    print(my_number, computer_number)
    if my_number == computer_number:
        print('Correct')
        game_over = True
    elif my_number > computer_number:
        print('Too high')
        return attempts - 1
    else:
        print('Too low')
        return attempts - 1

#def play_the_game():
os.system(('cls'))
game_over = False
print('Welcome to the number guessing game')
print('Im thinking of a number between 1 and 100')

difficulty = input('Choose a dificulty easy (e) or hard (h)\n')

if difficulty == 'e':
    attempts = 10
else:
    attempts = 5

computer_number = whats_my_number()
print(computer_number)

while game_over == False:
    print(f'you have {attempts} attempts left to guess the mumber')
    my_number = int(input('Guess a number:\n'))
    
    attempts = compare_numbers()

    if attempts == 0:
        print('Game over')
        game_over = True

# while input('Play the guessing game (y/n)').lower() == 'y':
#     play_the_game()

        
