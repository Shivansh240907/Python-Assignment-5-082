
file = open("students.txt", "w")

for i in range(5):
    name = input("Enter student name: ")
    file.write(name + "\n")

file.close()

print("Five student names saved successfully.")
