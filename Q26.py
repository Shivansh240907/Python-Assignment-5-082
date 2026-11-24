
with open("test.txt", "w") as f:
    f.write("Hello World\n")

with open("test.txt", "a+") as f:
    f.write("Appended Line") 
    f.seek(0)                  
    print("Content:\n" + f.read())
