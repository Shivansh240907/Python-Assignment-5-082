f = open("test.txt", "r")

print("Before close() - Is file closed?:", f.closed)

f.close()

print("After close()  - Is file closed?:", f.closed)