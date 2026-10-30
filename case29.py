
key = ["A", "B", "C", "D", "A"]
score = 0

for i in range(5):
    answer = input("Enter answer: ")

    if answer.upper() == key[i]:
        score = score + 1

print("Total Correct Answers:", score)
print("Total Marks:", score * 2)
