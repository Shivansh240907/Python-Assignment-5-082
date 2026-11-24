import os
import time

f = open("sample.txt", "r")
print("--- File Object Info ---")
print("File Name:", f.name)
print("File Mode:", f.mode)
print("Is Closed?:", f.closed)
f.close()

print("\n--- System Metadata ---")
print("Absolute Path:", os.path.abspath("sample.txt"))
print("File Size (bytes):", os.path.getsize("sample.txt"))

mod_time = os.path.getmtime("sample.txt")
print("Last Modified:", time.ctime(mod_time))
