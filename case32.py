n = int(input("Enter number of invoice records: "))

valid_records = []
invalid_records = []

for i in range(n):

    record = input("Enter invoice record: ")

    parts = record.split("|")

    if len(parts) != 3:
        invalid_records.append(record)
        continue

    code = parts[0].strip()

    try:
        quantity = int(parts[1])
        amount = float(parts[2])

        if (not code or
            quantity <= 0 or
            amount < 0):
            invalid_records.append(record)

        else:
            valid_records.append((code, quantity, amount))

    except ValueError:
        invalid_records.append(record)

print("\nValid Invoice Records:")

for code, quantity, amount in valid_records:
    print("Product Code:", code)
    print("Quantity:", quantity)
    print("Amount: Rs.", round(amount, 2))
    print()

print("Malformed Invoice Records:")

if invalid_records:
    for record in invalid_records:
        print(record)
else:
    print("None")
