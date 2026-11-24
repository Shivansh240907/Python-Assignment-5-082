import os

path = input("Enter a file or directory path: ")

if os.path.isfile(path):
    print(f"'{path}' is a FILE.")
elif os.path.isdir(path):
    print(f"'{path}' is a DIRECTORY.")
else:
    print(f"'{path}' does not exist.")
