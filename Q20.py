filename = "natural_numbers.txt"

with open(filename, "w") as file:
    for number in range(1, 101):
        file.write(f"{number}\n")

print(f"First 100 natural numbers have been written to '{filename}'.")
