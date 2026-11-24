
with open("source.txt", "w") as f:
    f.write("Hello World! Welcome to Python file handling.\n")
    f.write("All lowercase letters will become uppercase.")

with open("source.txt", "r") as src, open("destination.txt", "w") as dest:
    content = src.read()
    dest.write(content.upper())

with open("destination.txt", "r") as dest:
    print("Contents of destination.txt:")
    print("-" * 28)
    print(dest.read())
