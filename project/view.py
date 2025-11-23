def display_menu():
    """Displays the main menu options."""
    print("\n--- Student Management System ---")
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Find Student by ID")
    print("4. Exit")

def get_menu_choice():
    """Gets a valid menu choice from the user."""
    while True:
        try:
            choice = input("Enter your choice (1-4): ")
            if choice in ('1', '2', '3', '4'):
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except EOFError:
            return '4' # Exit on end-of-file

def get_student_data():
    """Collects necessary data from the user to create a new student."""
    print("\n--- Enter New Student Data ---")
    while True:
        try:
            student_id = int(input("Student ID (e.g., 104): "))
            break
        except ValueError:
            print("Invalid input. Student ID must be an integer.")

    name = input("Name: ")
    major = input("Major: ")

    while True:
        try:
            gpa = float(input("GPA (e.g., 3.75): "))
            if 0.0 <= gpa <= 4.0:
                break
            else:
                print("GPA must be between 0.0 and 4.0.")
        except ValueError:
            print("Invalid input. GPA must be a number.")

    return student_id, name, major, gpa

def get_student_id_for_search():
    """Prompts the user for a student ID to search."""
    while True:
        try:
            return int(input("Enter Student ID to search: "))
        except ValueError:
            print("Invalid input. Student ID must be an integer.")

def display_student(student):
    """Displays a single student's details."""
    if student:
        print("\nStudent Found:")
        print(student)
    else:
        print("\nError: Student not found.")

def display_all_students(students):
    """Displays a list of all students."""
    if students:
        print("\n--- All Students in System ---")
        for student in students:
            print(student)
        print("-------------------------------")
    else:
        print("\nNo students currently in the system.")

def display_message(message):
    """Displays a general message to the user."""
    print(f"\n[SYSTEM] {message}")