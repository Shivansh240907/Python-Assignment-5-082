
file = open("lines.txt", "w")

lines = [
    "First line of text.\n",
    "Second line of text.\n",
    "Third line of text.\n"
]

file.writelines(lines)

file.close()

print("Lines written successfully.")
