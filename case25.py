n = int(input("Enter number of households: "))

fixed_fee = 50
excessive_users = []

for i in range(1, n + 1):
    units = float(input(f"Enter units for household {i}: "))

    if units < 0:
        print("Invalid consumption")
        continue

    if units <= 30:
        bill = units * 2
    elif units <= 60:
        bill = 30 * 2 + (units - 30) * 3
    elif units <= 100:
        bill = 30 * 2 + 30 * 3 + (units - 60) * 5
    else:
        bill = 30 * 2 + 30 * 3 + 40 * 5
        bill += (units - 100) * 8

    bill += fixed_fee

    if units > 100:
        bill += 100
        excessive_users.append(i)

    print("Household", i, "Bill: Rs.", round(bill, 2))

print("\nExcessive consumption households:")

if excessive_users:
    print(excessive_users)
else:
    print("None")
