import pandas as pd
import csv

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

csv_path = r"C:\Users\pfiel\Documents\Python\100doc\day 22_30\Day 26 list dictionary and dataframe comprehensions\Nata Alphabet Challenge\nato_phonetic_alphabet.csv"
data = pd.read_csv(csv_path)

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
dict = {row['letter']:row['code'] for (index,row) in data.iterrows()}

########### Alternaivly ################
# Create a pandas DF and convert that to a dictionary
# dict = pd.read_csv(csv_path, index_col=0, squeeze=True).to_dict()

word = input('Enter a word: ').upper()

# get the value (code word) for the given key (letter) in the dictionary (dict)
nato_list = [dict.get(letter) for letter in word]

print(nato_list)