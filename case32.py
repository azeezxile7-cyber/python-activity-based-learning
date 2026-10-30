
prepared = int(input("Enter meals prepared: "))
served = int(input("Enter meals served: "))

waste = prepared - served
percentage = (waste / prepared) * 100

print("Food Wasted:", waste)
print("Waste Percentage:", percentage, "%")

if percentage > 20:
    print("High Food Wastage")
else:
    print("Food Wastage is Normal")
