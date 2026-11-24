
with open("test.txt", "w") as f:
    f.write("Hello World")

with open("test.txt", "r+") as f:
    print("Before:", f.read())   
    f.write(" - Updated!")      


with open("test.txt", "r") as f:
    print("After:", f.read())
