vowels = "aeiouAEIOU"
count = 0

with open("test.txt", "r") as f:
    text = f.read()
    for char in text:
        if char in vowels:
            count += 1

print("Total number of vowels:", count)