filename = "append_demo.txt"

with open(filename, "w") as file:
    file.write("Line 1: Initial entry.\n")

with open(filename, "a") as file:
    file.write("Line 2: Added using append mode.\n")
    file.write("Line 3: Existing data remains safe.\n")

with open(filename, "r") as file:
    print("Final File Contents:")
    print("-" * 20)
    print(file.read())
