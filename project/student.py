class Student:
    def __init__(self, student_id, name, major, gpa):
        self.student_id = student_id
        self.name = name
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return (f"ID: {self.student_id}, Name: {self.name}, "
                f"Major: {self.major}, GPA: {self.gpa:.2f}")

    def __repr__(self):
        return f"Student({self.student_id}, '{self.name}', '{self.major}', {self.gpa})"