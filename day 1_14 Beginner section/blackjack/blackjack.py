from blackjack_art import logo
import random


deal_again = True
another_game = True

def deal_card():
    '''Deal card to the dealer and player '''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)

    return card

def calculate_score(user):
    score = sum(user)
    if len(user)== 2 and  score == 21:
        return 0
    else:
        return score


#############################################################################

player = []
dealer = []
player_score = 0
dealer_score = 0

play_game = input('Do you want to play a game of Blackjack?. (y/n): ').lower()

if play_game == 'y':
    print(logo)

    for c in range(2):
        player.append(deal_card())
        dealer.append(deal_card())
    
    player_score = calculate_score(player)
    dealer_score = calculate_score(dealer)

    if player_score == 0:
        deal_again = False
        print()
        print(f'Your cards are {player} .. BlackJack.. You win!! ')
        print(f' Computers first card {dealer[0]}')

    elif dealer_score == 0:
            deal_again = False
            print()
            print(f'Your cards are {player}')
            print(f'Dealer cards are {dealer} .. BlackJack.. dealer win!! ')
    else:
        print()
        print(f'Your cards are {player} current score is {player_score}')
        print(f'Computers first card is {dealer[0]}')
else:
    deal_again = False
############## Player ####################
while deal_again:
    another_card = input('Type y for another card or n to pass ')
    if another_card == 'y':
        player.append(deal_card())
        player_score = calculate_score(player)
        print()
        print(f'Your cards {player} current score {player_score}')
        print(f'Computers first card {dealer[0]}')
        
        if player_score > 21:
            if 11 in player:
                player[player.index(11)] = 1
                player_score = calculate_score(player)
                print()
                print(f'Your cards {player} current score {player_score}')
            else:
                deal_again = False
                print('You lose')
    else:
        ################## The dealer #################
        deal_again=False
        if dealer_score < 17:
            while dealer_score < 17 and dealer_score < player_score:
                dealer.append(deal_card())
                dealer_score = calculate_score(dealer)
            
        if dealer_score > 21:
            if 11 in dealer:
                dealer[dealer.index(11)] = 1
                dealer_score = calculate_score(dealer)
                if dealer_score < 17:
                    while dealer_score < 17:
                        dealer.append(deal_card())
                        dealer_score = calculate_score(dealer)

            else:
                print()
                print(f'Your cards {player} current score {player_score}')
                print(f'Computers cards {dealer} score = {dealer_score}')
                print('You win')
        else:
            print()
            print(f'Your cards {player} current score {player_score}')
            print(f'Computers  cards {dealer} score = {dealer_score}')

            if dealer_score >= player_score:
                print()
                print('Dealer wins !')
            else:
                while dealer_score < player_score:
                    dealer.append(deal_card())
                    dealer_score = calculate_score(dealer)
                if dealer_score > 21:
                    if 11 in dealer:
                        dealer[dealer.index(11)] = 1
                        dealer_score = calculate_score(dealer)
                print()
                print(f'Your cards {player} current score {player_score}')
                print(f'Computers cards {dealer} score = {dealer_score}')


                    
                
       
            
                    



               
        

    