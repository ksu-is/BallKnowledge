#Quiz Application
quiz = [{"questions":"What teams played in the 2019 UEFA UCL final?","options":"A) PSG vs. FCB\nB) RMA vs. FCB\nC) LIV vs. TOT\nD) SEV vs. MAN","answer":"C"},
        {"questions":"What city hosted the 2019 UEFA UCL final?","options":"A) Kennesaw\nB) Lisbon\nC) Amsterdam\nD) Madrid","answer":"D"},
        {"questions":"What was the final score of the 2019 UEFA UCL final?","options":"A) LIV 2 - TOT 0\nB) LIV 5 - TOT 10\nC) LIV 1 - TOT 2\nD) LIV 2 - TOT 3","answer":"A"}]
score = 0
for q in quiz:
    print("Question:" , q["questions"])
    print("\nOptions:\n",q["options"])
    user_answer = input("\n Enter your Answer:").upper()
    if user_answer == q["answer"]:
        print("Correct!")
        score +=1
    else:
        print("Incorrect! The correct answer is:", q["answer"])
print("\n Your final score is:",score)
print("Thank you for playing the quiz!")
# End of Quiz Application
