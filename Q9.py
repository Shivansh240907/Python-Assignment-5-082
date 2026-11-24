
file = open("India.txt", "r")

search_word = "India"

for line in file:
    if search_word in line:
        print(line, end="")

file.close()
