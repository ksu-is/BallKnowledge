#Test Run
quiz = [
    {"questions":"What teams played in the 2019 UEFA UCL final?",
     "options":"A) PSG vs. FCB\nB) RMA vs. FCB\nC) LIV vs. TOT\nD) SEV vs. MAN",
     "answer":"C"},

    {"questions":"What city hosted the 2019 UEFA UCL final?",
     "options":"A) Kennesaw\nB) Lisbon\nC) Amsterdam\nD) Madrid",
     "answer":"D"},

    {"questions":"What was the final score of the 2019 UEFA UCL final?",
     "options":"A) LIV 2 - TOT 0\nB) LIV 5 - TOT 10\nC) LIV 1 - TOT 2\nD) LIV 2 - TOT 3",
     "answer":"A"}
]

score = 0

for q in quiz:
    print("Question:", q["questions"])
    print("\nOptions:\n", q["options"])

    user_answer = input("\nEnter your Answer: ").upper()

    # Split options into lines
    options_list = q["options"].split("\n")

    # Find the full correct answer text
    correct_text = ""
    for option in options_list:
        if option.startswith(q["answer"]):
            correct_text = option
            break

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("The correct answer is:", correct_text)

print("\nYour final score is:", score)
print("Thank you for playing the quiz!")

#This change in code is so that the correct answers are displayed if the user picked the wrong one
