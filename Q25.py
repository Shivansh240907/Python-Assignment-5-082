
with open("test.txt", "w+") as f:
    f.write("Hello World!")   
    f.seek(0)                 
    print("Content:", f.read())
