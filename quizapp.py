from questions import QUESTIONS

for questions, answers in QUESTIONS.items():
    correct_answer = answers[0]
    print(questions)  
    for answer in answers:
        print(f"- {answer}")
    choice = input("What´s your answer? \n")
    if choice == correct_answer:
        print("Your answer is correct!")
    else:
        print(f"Wrong answer! The correct answer is {correct_answer}!")