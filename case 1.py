
balance = 5000

print("1. Deposit")
print("2. Withdraw")

choice = int(input("Enter your choice: "))
amount = int(input("Enter amount: "))

if choice == 1:
    balance = balance + amount
    print("Amount Deposited")
elif choice == 2:
    if amount <= balance:
        balance = balance - amount
        print("Amount Withdrawn")
    else:
        print("Insufficient Balance")
else:
    print("Invalid Choice")

print("Final Balance:", balance)
