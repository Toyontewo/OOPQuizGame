from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

game = True
print("Welcome to My Quiz Game of 22 Randomly selected questions \nGood Luck ")


while game:
    begin = input("Press 'B' to begin and 'Q' to Quit: ").lower()

    if begin == "b":

        question_bank = []
        for question in question_data:
            question_text = question["text"]
            question_answer = question["answer"]
            new_question = Question(question_text, question_answer)
            question_bank.append(new_question)

        quiz = QuizBrain(question_bank)

        while quiz.still_has_questions():
            quiz.new_question()

        print("You've Completed the Quiz")
        print(f"Final Score: {quiz.score}/{quiz.q_number}")

    else:
        print("Quiz Ended...")
        game = False
