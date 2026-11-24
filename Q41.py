import os

filename = input("Enter the file name to check: ")

if os.path.isfile(filename):
    print(f"Yes, the file '{filename}' exists.")
else:
    print(f"No, the file '{filename}' does not exist.")
