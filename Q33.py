digit_count = 0
special_count = 0

with open("India.txt", "r") as f:
    text = f.read()
    for char in text:
        if char.isdigit():
            digit_count += 1
        elif not char.isalpha() and not char.isspace():
            special_count += 1

print("Digits:", digit_count)
print("Special characters:", special_count)