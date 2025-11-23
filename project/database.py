from student import Student

# In a real application, this would be a database connection.
# For simplicity, we use a global list to store Student objects.
_student_data = []

def add_student(student):
    """Adds a new Student object to the data store."""
    if not isinstance(student, Student):
        raise TypeError("Input must be a Student object.")
    _student_data.append(student)

def get_all_students():
    """Returns a copy of all stored Student objects."""
    return list(_student_data)

def find_student_by_id(student_id):
    """Searches for a student by their ID."""
    for student in _student_data:
        if student.student_id == student_id:
            return student
    return None

def initialize_data():
    """Adds initial sample data."""
    if not _student_data:
        add_student(Student(101, "Alice Smith", "Computer Science", 3.9))
        add_student(Student(102, "Bob Johnson", "Electrical Engineering", 3.5))
        add_student(Student(103, "Charlie Brown", "Business", 3.2))