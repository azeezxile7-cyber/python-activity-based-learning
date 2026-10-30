

n = int(input("Enter number of students: "))

branches = ["CSE", "ECE", "EEE", "MECH", "CIVIL"]

valid_ids = []
invalid_ids = []
classification = {}

for i in range(n):

    reg_id = input("\nEnter registration ID: ").upper()

    if len(reg_id) != 11:
        invalid_ids.append(reg_id)
        continue


    year = reg_id[:4]
    branch = reg_id[4:7]
    number = reg_id[7:]


    if (year.isdigit() and
        2020 <= int(year) <= 2030 and
        branch in branches and
        number.isdigit() and
        int(number) > 0):

        valid_ids.append(reg_id)

        key = (year, branch)

        if key not in classification:
            classification[key] = []

        classification[key].append(number)

    else:
        invalid_ids.append(reg_id)


print("\nVALID REGISTRATION IDs")

for reg_id in valid_ids:
    print(reg_id)


print("\nINVALID REGISTRATION IDs")

for reg_id in invalid_ids:
    print(reg_id)

print("\nSTUDENT CLASSIFICATION REPORT")

for key, students in sorted(classification.items()):

    year, branch = key

    print("\nAdmission Year:", year)
    print("Branch:", branch)
    print("Number of Students:", len(students))
    print("Student Numbers:", ", ".join(students))
