
m1 = int(input("Enter subject 1 marks: "))
m2 = int(input("Enter subject 2 marks: "))
m3 = int(input("Enter subject 3 marks: "))

total = m1 + m2 + m3
average = total / 3

print("Total Marks:", total)
print("Average:", average)

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
