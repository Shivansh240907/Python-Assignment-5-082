filename = "zenai.txt.txt"

with open(filename, "w") as file:
    file.write("Welcome to Python File Handling!\n")
    file.write("This file is opened in read mode ('r').\n")

with open(filename, "r") as file:
     print("\nFinal File Contents:")
     print("-" * 20)
     print(file.read())