import random
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

# Create a list of Question objects
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


#TODO While not at the end of the list
while quiz.still_has_questions():
    quiz.next_question()






