
attendance = int(input("Enter attendance percentage: "))
lab = input("Lab completed? (yes/no): ")
marks = int(input("Enter internal marks: "))
fees = input("Fees paid? (yes/no): ")

if attendance >= 75 and lab == "yes" and marks >= 40 and fees == "yes":
    print("Eligible for Examination")
else:
    print("Not Eligible for Examination")
