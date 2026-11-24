filename = "zenai.txt.txt"

with open(filename, "w") as file:
    file.write("Line 1: Initial content.\n")

with open(filename, "w") as file:
    file.write("Line 1: Overwritten content.\n")

with open(filename, "a") as file:
    file.write("Line 2: Appended content.\n")

with open(filename, "r") as file:
    print("Final File Content:")
    print(file.read())
