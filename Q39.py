with open("source.txt", "r") as src, open("destination.txt", "w") as dest:
    content = src.read()
    dest.write(content[::-1])

with open("destination.txt", "r") as dest:
    print("Contents of destination.txt:")
    print("-" * 28)
    print(dest.read())