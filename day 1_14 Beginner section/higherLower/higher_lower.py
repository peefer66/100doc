# Imports
import random
import os
from art import logo, vs
from game_data import data

end_game = False

def compare_answers(foll_a,foll_b,answer,score):
    ''' Compare the answers and return score + 1 if correct
    or 0 if wrong. foll = followers for A & B
    pass answer A & B and score 
    '''
    if answer == 'a':
        if foll_a > foll_b:
            return score + 1
        else:
            return 0
    else:
        if foll_b > foll_a:
            return score + 1
        else:
            return 0


def get_questions(data):
    ''' Picks random questions from the dictionary and passed back'''
    return random.choice(data)



def game(end_game):
    ''' main game '''
    score = 0
    optdict_a = {}
    optdict_b = {}

    while not end_game: 
        # if its the first question in a sequence       
        if optdict_a == {}:
            optdict_a = get_questions(data)
        else:
            # if its not the first  question B becoame question A
            optdict_a = optdict_b

        optdict_b = get_questions(data)
        
        # get the number of followers for each
        follower_count_a = optdict_a['follower_count']
        follower_count_b = optdict_b['follower_count']

        print(logo)
        print(f"Your current score is {score}")
        print('Select the who has the most Instagram followers from the following')
        print(f"OPtion A: {optdict_a['name']} a {optdict_a['description']} from {optdict_a['country']}")
        print(vs)
        print(f"Against B: {optdict_b['name']} a {optdict_b['description']} from {optdict_b['country']}")
        answer = input('Select a or b ')

        
        # compare the results
        score = compare_answers(follower_count_a,follower_count_b,answer,score)
        if score == 0:
            end_game= True
    

    

game(end_game)