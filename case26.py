
marks = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    m = int(input("Enter marks: "))
    marks.append(m)

total = sum(marks)
average = total / n

print("Total Marks:", total)
print("Average Marks:", average)

if average >= 90:
    print("Excellent")
elif average >= 75:
    print("Good")
elif average >= 50:
    print("Average")
else:
    print("Poor")
