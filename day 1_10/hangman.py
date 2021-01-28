#Step 2

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lives = 6
end_of_game = False






#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = ['_' for letter in chosen_word]
print(display)

guess_count = 1

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    inword = False
       
    letter_index = 0
    for letter in chosen_word:
        if letter == guess:
            display[letter_index] = letter
            letter_index +=1
            inword = True
            
    lives -=1
    print(display)
    print(stages[lives])
 
    

if not '_' in display:
    print()
    print ('You win!')
else:
    print()
    print('You loose')
        
