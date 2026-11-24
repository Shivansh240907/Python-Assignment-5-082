import os

dir_path = input("Enter directory path (or press Enter for current folder): ") or "."

if os.path.isdir(dir_path):
    print(f"\nFiles in '{dir_path}':")
    for item in os.listdir(dir_path):
        full_path = os.path.join(dir_path, item)
        if os.path.isfile(full_path):
            print(item)
else:
    print(f"Error: Directory '{dir_path}' does not exist.")
