class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        q = self.q_list[self.q_number]
        self.q_number += 1
        choice = input(f"Q.{self.q_number} {q.text} (True/False)? :")
        self.check_answer(choice, q.answer)

    def check_answer(self, choice, correct_answer):
        if choice.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score}/{self.q_number}")
        print("\n")

    def still_has_questions(self):
        return len(self.q_list) > self.q_number