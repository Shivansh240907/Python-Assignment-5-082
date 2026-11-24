
file = open("example.txt", "r")

content = file.read()

words = content.split()

word_count = len(words)

print("Total words:", word_count)

file.close()
