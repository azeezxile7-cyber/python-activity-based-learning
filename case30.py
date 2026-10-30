email = input("Enter student email: ")
reg_id = input("Enter registration ID: ")


email_valid = False

if email.count("@") == 1:
    username, domain = email.split("@")

    if (username and domain and
        "." in domain and
        not domain.startswith(".") and
        not domain.endswith(".") and
        all(c.isalnum() or c in "._-" for c in username) and
        all(c.isalnum() or c in ".-" for c in domain)):
        email_valid = True


id_valid = (
    reg_id.startswith("STU") and
    len(reg_id) == 7 and
    reg_id[3:].isdigit()
)

print("\nValidation Results:")

if email_valid:
    print("Email: Valid")
else:
    print("Email: Invalid")

if id_valid:
    print("Registration ID: Valid")
else:
    print("Registration ID: Invalid")
