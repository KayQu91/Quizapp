from questions import QUESTIONS

for questions, answers in QUESTIONS.items():
    correct_answer = answers[0]
    sorted_answers = sorted(answers)
    print(questions, "\n")

    for label, answer in enumerate(sorted_answers):
        print(f"{label}) {answer}")
    choice = int(input("\nWhat´s your answer? \n"))
    answer = sorted_answers[choice]
    if answer == correct_answer:
        print(f"Your answer '{answer}' is correct!\n")
    else:
        print(f"Wrong answer! The correct answer is '{correct_answer}' and not '{answer}'!\n")