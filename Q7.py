
file = open("India.txt", "r")

lines = file.readlines()

line_count = len(lines)

print("Total lines:", line_count)

file.close()
