import random
from blackjack_art import logo
from os import system

user_score = 0
computer_score = 0


def clear_output():
    system('cls')

def deal_cards():
    cards =[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_cards(cards):
    if sum(cards) == 21 and len(cards)==2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_scores(user, computer):
    ''' Compare the user score with the computer'''
    if user > 21 and computer <= 21:
        return 'You lose '
    elif user > 21 and computer > 21:
        return 'No winner'
    elif user <=21 and computer > 21:
        return 'You win'
    elif user == computer:
        return 'Draw'
    elif user > computer:
        return 'You Win!'
    elif user < computer:
        return 'You Lose'

def play_the_game():
    ''' Main game play'''
    user_cards = []
    computer_cards = []
    
    is_game_over = False

    clear_output()
    print(logo)

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    user_score = calculate_cards(user_cards)
    computer_score = calculate_cards(computer_cards)

    
    print(f' Your cards: {user_cards} score: {user_score}')
    print(f' Computer first card {computer_cards[0]}')

    if user_score == 0 and computer_score !=0:
        print('Blackjack.. You win')
        is_game_over = True
    elif user_score != 0 and computer_score == 0:
        print('Blackjack.. Computer wins')
        is_game_over = True
    elif user_score == 0 and computer_score == 0:
        print('Blackjack.. Draw')
        is_game_over = True

    while  is_game_over == False and user_score <21:
        another_deal = input('Another card? (y/n): ').lower()
        if another_deal == 'y':
            user_cards.append(deal_cards())
            user_score=calculate_cards(user_cards)
            print(f' Your cards: {user_cards} score: {user_score}')
            print(f' Computer first card {computer_cards[0]}')
        else:
            is_game_over = True

    while computer_score < 17 and computer_score <21:
        computer_cards.append(deal_cards())
        computer_score = calculate_cards(computer_cards)

    print(f' Your cards: {user_cards} score: {user_score}')
    print(f' Computer first card {computer_cards} score: {computer_score}')


    print(compare_scores(user_score, computer_score))

while input('Do you want to playa game of Blackjack?: ').lower() == 'y':
    clear_output()
    play_the_game()





