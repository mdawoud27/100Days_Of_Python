from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for que in question_data:
    new_q = Question(que["question"], que["correct_answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.get_score()}/{len(question_bank)}")
