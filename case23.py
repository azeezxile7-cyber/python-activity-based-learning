

def to_minutes(time_str):
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes

courses = []
conflicts = []

n = int(input("Enter number of courses: "))

unavailable_rooms = input("Enter unavailable rooms (comma separated): ").split(",")
unavailable_rooms = [room.strip() for room in unavailable_rooms]

for i in range(n):
    print(f"\nEnter details for Course {i+1}")
    name = input("Course Name: ")
    day = input("Day: ")
    start = input("Start Time (HH:MM): ")
    end = input("End Time (HH:MM): ")
    room = input("Room: ")

    courses.append((name, day, start, end, room))


for i in range(len(courses)):
    for j in range(i + 1, len(courses)):
        c1 = courses[i]
        c2 = courses[j]

        if c1[1] == c2[1]:  
            s1 = to_minutes(c1[2])
            e1 = to_minutes(c1[3])
            s2 = to_minutes(c2[2])
            e2 = to_minutes(c2[3])

            if s1 < e2 and s2 < e1:
                conflicts.append(
                    f"{c1[0]} overlaps with {c2[0]} on {c1[1]}"
                )


room_conflicts = []

for course in courses:
    if course[4] in unavailable_rooms:
        room_conflicts.append(
            f"{course[0]} uses unavailable room {course[4]}"
        )


print("\n===== TIMETABLE VALIDATION =====")

if conflicts:
    print("\nTime Conflicts:")
    for c in conflicts:
        print("-", c)
else:
    print("\nNo time conflicts found.")

if room_conflicts:
    print("\nUnavailable Room Conflicts:")
    for r in room_conflicts:
        print("-", r)
else:
    print("\nNo unavailable room conflicts found.")

if not conflicts and not room_conflicts:
    print("\nTimetable Status: VALID")
else:
    print("\nTimetable Status: INVALID")

print("\n===== PROCESS COMPLETED =====")
