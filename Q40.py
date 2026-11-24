
with open("file1.txt", "w") as f1:
    f1.write("This is the content of File 1.\n")

with open("file2.txt", "w") as f2:
    f2.write("This is the content of File 2.\n")

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("merged.txt", "w") as out:
    out.write(f1.read())
    out.write(f2.read())

with open("merged.txt", "r") as out:
    print("Merged File Contents:")
    print("-" * 22)
    print(out.read())
