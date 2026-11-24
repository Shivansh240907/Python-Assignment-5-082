with open("test.txt", "r") as f:
    f.seek(6)
    print("From index 6:", f.read())

    f.seek(0)
    print("Back to start:", f.read(5))

    print("Current position:", f.tell())