password = input("Enter your password: ")

errors = []

if len(password) < 8:
    errors.append("Minimum 8 characters required")

if not any(c.isupper() for c in password):
    errors.append("At least one uppercase letter required")

if not any(c.islower() for c in password):
    errors.append("At least one lowercase letter required")

if not any(c.isdigit() for c in password):
    errors.append("At least one digit required")

if not any(not c.isalnum() for c in password):
    errors.append("At least one special character required")

if any(password[i] == password[i+1]
       for i in range(len(password)-1)):
    errors.append("Repeated consecutive characters not allowed")

prohibited = ["password", "123456", "admin"]

if any(word in password.lower() for word in prohibited):
    errors.append("Contains prohibited substring")

if errors:
    print("\nInvalid Password")
    for error in errors:
        print("-", error)
else:
    print("\nValid Password")
