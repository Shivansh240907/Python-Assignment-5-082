pos = int(input("Enter the starting position (index): "))

with open("test.txt", "r") as f:
    f.seek(pos)
    print("Content from position", pos, ":", f.read())