with open("test.txt", "r") as f:
    print("Initial position:", f.tell())      

    print("First 5 chars:", f.read(5))     
    print("Position after reading 5 chars:", f.tell())

    print("Remaining text:", f.read())         
    print("Final position:", f.tell())