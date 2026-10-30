key = input("Enter answer key: ").upper().split(",")

answers = input("Enter student answers: ").upper().split(",")

if len(key) != len(answers):
    print("Error: Number of answers must match answer key")

else:
    correct = 0
    incorrect = 0
    unanswered = 0

    positive_mark = 4
    negative_mark = 1

    for i in range(len(key)):

        if answers[i] == "":
            unanswered += 1

        elif answers[i] == key[i]:
            correct += 1

        else:
            incorrect += 1

    score = (correct * positive_mark) - (incorrect * negative_mark)

    print("\nExamination Results")
    print("Correct Answers:", correct)
    print("Incorrect Answers:", incorrect)
    print("Unanswered Questions:", unanswered)
    print("Final Score:", score)
