import os

# Create a sample file first so it exists
with open("old_name.txt", "w") as f:
    f.write("This file will be renamed.")

old_name = "old_name.txt"
new_name = "new_name.txt"

# Check if the file exists before renaming
if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"File successfully renamed from '{old_name}' to '{new_name}'.")
else:
    print(f"Error: '{old_name}' does not exist.")
