# Student Management System

students = {}  

def add_student():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_age = input("Enter student age: ")
    student_major = input("Enter student major: ")

    if type(student_id) !=int:
        print("ID must be an integer. Please enter a valid ID.")
        return
    elif student_age < 0:
        print("Age cannot be negative. Please enter a valid age.")
        return
    elif student_age > 120:
        print("Age seems unrealistic. Please enter a valid age.")
        return
    elif type(student_major) != str:
        print("Major must be a string. Please enter a valid major.")
        return
    elif type(student_name) != str:
        print("Name must be a string. Please enter a valid name.")
        return



    students[student_id] = {
        "name": student_name,
        "age": student_age,
        "major": student_major
    }
    print(f"Student record \n{students}\n added successfully!")

def view_students():
    print("\n--- List of Students ---")
    for student_id, details in students.items():
        print(f"ID: {student_id}")
        print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print(f"Major: {details['major']}\n")


def save_students_to_file(filename):
    import json as js
    with open(filename, 'w') as file:
        js.dump(students, file)
        print(f"Student records saved to {filename} successfully!")


def load_students_from_file(filename):
    import json as js
    try:
        with open(filename, 'r') as file:
            global students
            students = js.load(file)
            print(f"Student records loaded from {filename} successfully!")
    except FileNotFoundError:
        print(f"File {filename} not found. Please save students first.")

while True:
    print("\nMenu:")
    print("1) Add a student")
    print("2) View all students")
    print("3) Save students to a file")
    print("4) Load students from a file")
    print("5) Exit")

    choice = input("Select an option (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        save_students_to_file("students.json")
    elif choice == "4":
        load_students_from_file("students.json")
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid option! Try again.")