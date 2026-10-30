weight = float(input("Enter parcel weight in kg: "))
length = float(input("Enter length in cm: "))
width = float(input("Enter width in cm: "))
height = float(input("Enter height in cm: "))
zone = int(input("Enter distance zone (1, 2, 3): "))
urgent = input("Urgent delivery? (yes/no): ").lower()
restricted = input("Contains restricted items? (yes/no): ").lower()
if weight <= 0 or min(length, width, height) <= 0:
    print("Invalid parcel dimensions or weight")
elif zone not in [1, 2, 3]:
    print("Invalid distance zone")

elif restricted == "yes":
    print("Parcel rejected due to restrictions")

else:
    volume_weight = (length * width * height) / 5000
    charge_weight = max(weight, volume_weight)

    zone_rate = {1: 40, 2: 60, 3: 80}
    base = zone_rate[zone]

    services = {
        "Standard": base + charge_weight * 20,
        "Express": base + charge_weight * 35
    }

    if urgent == "yes":
        services.pop("Standard")

    print("\nEligible Services:")

    for service, charge in services.items():
        print(service, ":", round(charge, 2))

    if services:
        best = min(services, key=services.get)
        print("Cheapest service:", best)
        print("Courier charge:", round(services[best], 2))
