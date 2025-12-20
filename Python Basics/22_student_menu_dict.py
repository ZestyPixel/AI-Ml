students = {}

while True:
    print("\nMenu:")
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students and marks")
    print("E - Exit")

    choice = input("Enter your choice (A/B/C/D/E): ").upper()

    match choice:
        case 'A':
            name = input("Enter student name: ")
            marks = int(input("Enter marks: "))
            students[name] = marks
            print("Student added successfully.")

        case 'B':
            name = input("Enter student name to update marks: ")
            if name in students:
                marks = int(input("Enter new marks: "))
                students[name] = marks
                print("Marks updated successfully.")
            else:
                print("Student not found.")

        case 'C':
            name = input("Enter student name to search: ")
            if name in students:
                print(f"{name}'s marks: {students[name]}")
            else:
                print("Student not found.")

        case 'D':
            if not students:
                print("No records to display.")
            else:
                print("\nStudent Records:")
                for name, marks in students.items():
                    print(f"{name}: {marks}")

        case 'E':
            print("Exiting program.")
            break

        case _:
            print("Invalid choice. Please try again.")
