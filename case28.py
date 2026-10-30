n = int(input("Enter number of transactions: "))

transactions = []

for i in range(n):
    tid = input("Enter transaction ID: ")
    amount = float(input("Enter amount: "))

    transactions.append((tid, amount))

threshold = float(input("Enter suspicious amount threshold: "))

id_count = {}

for tid, amount in transactions:
    id_count[tid] = id_count.get(tid, 0) + 1

print("\nSuspicious Transactions:")

found = False

for tid, amount in transactions:

    reasons = []

    if id_count[tid] > 1:
        reasons.append("Duplicate ID")

    if amount > threshold:
        reasons.append("High Amount")

    if reasons:
        print(tid, amount, "-", ", ".join(reasons))
        found = True

if not found:
    print("No suspicious transactions found")
