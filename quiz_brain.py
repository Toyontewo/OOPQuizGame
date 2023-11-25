class QuizBrain:

    def __init__(self, q_list):
        self.q_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.q_number < len(self.question_list)

    def new_question(self):
        current_question = self.question_list[self.q_number]
        self.q_number += 1
        user_ans = input(f"{self.q_number}) {current_question.text} (True/False): ")
        self.check_answer(user_ans, current_question.answer)

    def check_answer(self, user_ans, correct_answer):
        if user_ans.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Wrong!")
            print(f"Correct answer is: {correct_answer}")
        print(f"Your current score is {self.score}/{self.q_number}")
        print("\n")
