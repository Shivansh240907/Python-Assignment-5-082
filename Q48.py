import os
filename = "sample.txt"
if os.path.exists(filename):
    size = os.path.getsize(filename)
    print(f"File '{filename}' exists.")
    print(f"File size: {size} bytes")
else:
    print(f"File '{filename}' does not exist.")