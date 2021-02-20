import random
import os



def compare_numbers(number,guess,turns):
    ''' Compares the guess with the computer
        and returns the number of turns left
     '''
    print(number,guess,turns)
    if guess == number:
        print('You WIN')
        game()
    elif guess > number:
        print('Too high')
        return turns - 1
    else:
        print('Too low')
        return turns - 1


def game():
    guess = 0
    difficulty = input('The computer as picked a number between 1 and 100. Try to guess the number Choose easy(e) or hard (h)\n  ')
    if difficulty == 'e':
        turns = 10
    else:
        turns = 5
   
    # computer picks a  number
    number = random.randint(1,100)
    print(number)

    while guess != number:
        guess = int(input(f'You have {turns} left to guess the number.'))
        turns =  compare_numbers(number, guess, turns)

        if turns == 0:
            print('You loose')
            number = guess
            game()

game()