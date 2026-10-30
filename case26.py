rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

reserved = int(input("Enter number of reserved seats: "))

reserved_seats = set()

for i in range(reserved):
    r, c = map(int, input("Enter reserved row and column: ").split())

    if 1 <= r <= rows and 1 <= c <= cols:
        reserved_seats.add((r, c))
    else:
        print("Invalid seat position")

print("\nExamination Seating Arrangement\n")

for r in range(1, rows + 1):
    for c in range(1, cols + 1):

        if (r, c) in reserved_seats:
            print("R", end=" ")

        elif (r + c) % 2 == 0:
            print("X", end=" ")

        else:
            print("S", end=" ")

    print()
