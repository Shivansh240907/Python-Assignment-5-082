filename = "studenttttt.txt"

num_students = int(input("Enter the number of students: "))

with open(filename, "a") as file:
    for i in range(num_students):
        print(f"\nEnter details for Student {i + 1}:")
        name = input("Name: ")
        roll_no = input("Roll Number: ")
        marks = input("Marks: ")
        
        file.write(f"Name: {name}, Roll No: {roll_no}, Marks: {marks}\n")

print(f"\nStudent details successfully saved to '{filename}'.")
