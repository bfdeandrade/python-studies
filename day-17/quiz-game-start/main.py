import imp
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = list()
for i in question_data:
    current_text = i['text']
    current_answer = i['answer']
    question_bank.append(Question(current_text, current_answer))
    


quiz = QuizBrain(question_bank)


quiz.next_question()

quiz.print_score()