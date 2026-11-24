import os

filename = "lifecycle_demo.txt"

f = open(filename, "w")
f.write("Hello World!\nThis file goes through a full lifecycle.")
f.close()
print(f"1. Created and wrote to '{filename}'.")

f = open(filename, "r")
print("\n2. File Contents:")
print("-" * 20)
print(f.read())
print("-" * 20)
f.close()
print("3. File closed status:", f.closed)

if os.path.exists(filename):
    os.remove(filename)
    print(f"4. File '{filename}' has been deleted.")
