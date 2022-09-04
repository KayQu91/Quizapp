from questions import QUESTIONS
import random

score = 0
questions_asked = 0

def ask_questions():
    global score, questions_asked
    for questions, answers in QUESTIONS.items():
        correct_answer = answers[0]
        sorted_answers = sorted(answers)
        print(questions, "\n")
        questions_asked += 1

        for label, answer in enumerate(sorted_answers):
            print(f"{label}) {answer}")
        choice = int(input("\nWhat´s your answer? \n"))
        answer = sorted_answers[choice]
        if answer == correct_answer:
            print(f"Your answer '{answer}' is correct!\n")
            score += 1
        else:
            print(f"Wrong answer! The correct answer is '{correct_answer}' and not '{answer}'!\n")

ask_questions()
print(f"You aswered {score} out of {questions_asked} correct!")