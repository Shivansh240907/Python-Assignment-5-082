
file = open("India.txt", "r")

content = file.read()

char_count = len(content)

print("Total characters:", char_count)

file.close()
