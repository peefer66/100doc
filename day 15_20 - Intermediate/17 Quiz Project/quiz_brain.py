class QuizBrain:

    def __init__(self,q_list):
        self.q_number = 0
        self.q_score = 0
        self.q_list = q_list

    def check_answer(self, user_answer, correct_answer):
        '''Compares the users answer with the ccorrect answer '''
        if user_answer.lower() == correct_answer.lower():
            self.q_score += 1
            print('Correct')
        else:
            print('Incorrect')
            print(f'The correct answer was {correct_answer}') 
        print(f'Your current score is : {self.q_score}/{self.q_number}')      

#TODO Ask the question
    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f'Q.{self.q_number} True or False. {current_question.text}')
        self.check_answer(user_answer,current_question.answer)
        

   
#TODO Check if we are at the end of the list
    def still_has_questions(self):
        return self.q_number < len(self.q_list)
            
