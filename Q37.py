char = input("Enter the starting character: ")

print(f"\nLines starting with '{char}':")
with open("India.txt", "r") as f:
    for line in f:
        if line.startswith(char):
            print(line.strip())