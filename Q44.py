import os

filename = "delete_me.txt"
with open(filename, "w") as f:
    f.write("Temporary file.")

if os.path.exists(filename):
    os.remove(filename)
    print(f"File '{filename}' has been deleted.")
else:
    print(f"Error: '{filename}' does not exist.")
