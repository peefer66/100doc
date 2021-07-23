# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

from os import truncate
import pandas

alphabet = False

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# Create a function that generates the NATO phonetics
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print('Name must be letters only')
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()



