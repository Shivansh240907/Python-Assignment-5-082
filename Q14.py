
file = open("user_text.txt", "w")

text = input("Enter the text you want to save: ")

file.write(text + "\n")

file.close()

print("Text saved successfully!")
