'''
Dictionary Comprehension 1
Instructions
You are going to use Dictionary Comprehension to create a dictionary called
result that takes each word in the given sentence and calculates the number of letters in each word.

Try Googling to find out how to convert a sentence into a list of words.

Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

Example Output
{
'What': 4, 
'is': 2, 
'the': 3, 
'Airspeed': 8, 
'Velocity': 8, 
'of': 2, 
'an': 2, 
'Unladen': 7, 
'Swallow?': 8
}
Hint
Use the keyword method for starting the Dictionary comprehension and fill in the relevant parts.

You can get a list of the words in a string by using the .split() method: https://www.w3schools.com/python/ref_string_split.asp

Test Your Code
Before checking the solution, try copy-pasting your code into this repl:

https://repl.it/@appbrewery/day-26-4-test-your-code

This repl includes my testing code that will check if your code meets this assignment's objectives.
'''


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# words_in_sentence = sentence.split() ==> convert to list of words

result = {word:len(word) for word in sentence.split() }
print(result)