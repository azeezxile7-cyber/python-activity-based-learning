
text = input("Enter a string: ")

result = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count = count + 1
    else:
        result = result + text[i - 1] + str(count)
        count = 1

if len(text) > 0:
    result = result + text[-1] + str(count)

print("Compressed String:", result)
