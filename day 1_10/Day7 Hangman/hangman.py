#Step 2

import random
from hangman_art import stages, logo
from hangman_words import word_list


chosen_word = random.choice(word_list)
lives = 6
end_of_game = False

print(logo) 
print(f'Pssst, the solution is {chosen_word}.')

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
        else:
          letter_index += 1
    
    if '_' not in display:
      end_of_game = True
      print('You win. Well Done!')
    else:
      print(display)
      if inword == False:
        lives -= 1
        print(stages[lives])
      if lives == 0:
        end_of_game=True


            
    
        
