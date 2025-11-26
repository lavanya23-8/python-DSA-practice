# ---------------------------------------------
# STUDENT MANAGEMENT SYSTEM (LONG PROGRAM)
# ---------------------------------------------

students = []   # List to store student records


def add_student():
    print("\n--- Add Student ---")
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    student = {"roll": roll, "name": name, "marks": marks}
    students.append(student)

    print("Student Added Successfully!")


def view_students():
    print("\n--- Student List ---")
    if not students:
        print("No records found.")
        return

    for s in students:
        print(f"Roll: {s['roll']}  Name: {s['name']}  Marks: {s['marks']}")


def search_student():
    print("\n--- Search Student ---")
    roll = input("Enter Roll Number to search: ")

    for s in students:
        if s["roll"] == roll:
            print("Record Found:")
            print(f"Roll: {s['roll']}  Name: {s['name']}  Marks: {s['marks']}")
            return
    print("Student not found.")


def update_student():
    print("\n--- Update Student ---")
    roll = input("Enter Roll Number to update: ")

    for s in students:
        if s["roll"] == roll:
            print("Old Name:", s['name'])
            print("Old Marks:", s['marks'])

            s['name'] = input("Enter New Name: ")
            s['marks'] = float(input("Enter New Marks: "))

            print("Record Updated Successfully!")
            return

    print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")
    roll = input("Enter Roll Number to delete: ")

    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Record Deleted Successfully!")
           return

    print("Student not found.")


# ---------- MAIN MENU ----------
while True:
    print("\n===============================")
    print("   STUDENT MANAGEMENT SYSTEM   ")
    print("===============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting Program...")
        break
    else:
        print("Invalid choice. Try again!")
