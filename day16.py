students = {}
# Add Student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    students[roll] = {
        "Name": name,
        "Marks": marks
    }
    print("Student Added Successfully!\n")


# Display 1
def display_students():
    if not students:
        print("No Student Records Found.\n")
    else:
        print("\nStudent Records:")
        for roll, details in students.items():
            print("Roll No:", roll)
            print("Name:", details["Name"])
            print("Marks:", details["Marks"])
            print("----------------------")


# Search Student
def search_student():
    roll = input("Enter Roll Number to Search: ")
    if roll in students:
        print("Student Found:")
        print("Name:", students[roll]["Name"])
        print("Marks:", students[roll]["Marks"])
    else:
        print("Student Not Found.")
    print()


# Delete Student
def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    if roll in students:
        del students[roll]
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found.")
    print()



while True:
    print("===== Student Record System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice! Try Again.\n")