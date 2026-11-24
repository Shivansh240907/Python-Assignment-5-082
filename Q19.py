filename = "multiplication_table.txt"

num = int(input("Enter a number to generate its multiplication table: "))

with open(filename, "w") as file:
    file.write(f"Multiplication Table of {num}:\n")
    file.write("-" * 28 + "\n")
    for i in range(1, 11):
        file.write(f"{num} x {i} = {num * i}\n")

print(f"Multiplication table of {num} has been saved to '{filename}'.")
