import os

old_name = "original.txt"
new_name = "renamed.txt"

with open(old_name, "w") as f:
    f.write("Hello World!\nThis file was renamed and then read.")

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"Renamed '{old_name}' to '{new_name}'.\n")

    with open(new_name, "r") as f:
        print("File Contents:")
        print("-" * 20)
        print(f.read())
else:
    print(f"Error: '{old_name}' does not exist.")
