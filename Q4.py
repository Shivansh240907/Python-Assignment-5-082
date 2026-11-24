
file = open("India.txt", "r")

line = file.readline()

while line != "":
    print(line, end="")
    line = file.readline()

# Close the file
file.close()
