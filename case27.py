n = int(input("Enter diamond size: "))

if n <= 0:
    print("Invalid dimension")

else:
    print("\nHollow Diamond Pattern\n")

    
    for i in range(n):
        print(" " * (n - i - 1), end="")

        if i == 0:
            print("*")
        else:
            print("*" + " " * (2 * i - 1) + "*")

    
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1), end="")

        if i == 0:
            print("*")
        else:
            print("*" + " " * (2 * i - 1) + "*")
