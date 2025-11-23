import database
import view
from student import Student

def add_new_student_action():
    """Logic to get student data, create the object, and save it."""
    try:
        student_id, name, major, gpa = view.get_student_data()

        # Check for ID conflict (basic validation)
        if database.find_student_by_id(student_id):
            view.display_message(f"Error: Student with ID {student_id} already exists.")
            return

        new_student = Student(student_id, name, major, gpa)
        database.add_student(new_student)
        view.display_message(f"Successfully added student: {name} (ID: {student_id})")

    except Exception as e:
        view.display_message(f"An unexpected error occurred: {e}")

def view_all_students_action():
    """Logic to fetch all students and display them."""
    students = database.get_all_students()
    view.display_all_students(students)

def find_student_action():
    """Logic to get an ID and find the corresponding student."""
    student_id = view.get_student_id_for_search()
    student = database.find_student_by_id(student_id)
    view.display_student(student)

def run_application():
    """The main loop of the application."""
    database.initialize_data() # Load initial data

    while True:
        view.display_menu()
        choice = view.get_menu_choice()

        if choice == '1':
            add_new_student_action()
        elif choice == '2':
            view_all_students_action()
        elif choice == '3':
            find_student_action()
        elif choice == '4':
            view.display_message("Exiting application. Goodbye!")
            break