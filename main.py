# Class to represent a Student
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}  # Dictionary to store courses and grades

    # Method to enroll in a course
    def enroll_course(self, course_name):
        self.courses[course_name] = None  # Initialize with no grade

    # Method to assign a grade to a course
    def assign_grade(self, course_name, grade):
        if course_name in self.courses:
            self.courses[course_name] = grade
        else:
            print(f"{self.name} is not enrolled in {course_name}.")

    # Method to view student details
    def view_details(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print("Courses and Grades:")
        for course, grade in self.courses.items():
            print(f"  - {course}: {grade if grade is not None else 'Not Assigned'}")
        print("\n")


# Class to represent a Teacher
class Teacher:
    def __init__(self, teacher_id, name):
        self.teacher_id = teacher_id
        self.name = name
        self.courses = []  # List to store courses taught

    # Method to assign a course to the teacher
    def assign_course(self, course_name):
        self.courses.append(course_name)

    # Method to view teacher details
    def view_details(self):
        print(f"Teacher ID: {self.teacher_id}")
        print(f"Name: {self.name}")
        print("Courses Taught:")
        for course in self.courses:
            print(f"  - {course}")
        print("\n")


# Class to represent a Course
class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []  # List to store enrolled students

    # Method to enroll a student in the course
    def enroll_student(self, student):
        self.students.append(student)
        student.enroll_course(self.course_name)

    # Method to view course details
    def view_details(self):
        print(f"Course Name: {self.course_name}")
        print("Enrolled Students:")
        for student in self.students:
            print(f"  - {student.name}")
        print("\n")


# School Management System class
class SchoolManagementSystem:
    def __init__(self):
        self.students = {}  # Dictionary to store students
        self.teachers = {}  # Dictionary to store teachers
        self.courses = {}  # Dictionary to store courses

    # Method to add a new student
    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        student = Student(student_id, name)
        self.students[student_id] = student
        print(f"Student {name} added successfully!\n")

    # Method to add a new teacher
    def add_teacher(self):
        teacher_id = input("Enter Teacher ID: ")
        name = input("Enter Teacher Name: ")
        teacher = Teacher(teacher_id, name)
        self.teachers[teacher_id] = teacher
        print(f"Teacher {name} added successfully!\n")

    # Method to add a new course
    def add_course(self):
        course_name = input("Enter Course Name: ")
        course = Course(course_name)
        self.courses[course_name] = course
        print(f"Course {course_name} added successfully!\n")

    # Method to enroll a student in a course
    def enroll_student_in_course(self):
        student_id = input("Enter Student ID: ")
        course_name = input("Enter Course Name: ")

        if student_id in self.students and course_name in self.courses:
            self.courses[course_name].enroll_student(self.students[student_id])
            print(f"Student {self.students[student_id].name} enrolled in {course_name} successfully!\n")
        else:
            print("Invalid Student ID or Course Name!\n")

    # Method to assign a grade to a student for a course
    def assign_grade(self):
        student_id = input("Enter Student ID: ")
        course_name = input("Enter Course Name: ")
        grade = input("Enter Grade: ")

        if student_id in self.students:
            self.students[student_id].assign_grade(course_name, grade)
            print(f"Grade {grade} assigned to {self.students[student_id].name} for {course_name}.\n")
        else:
            print("Invalid Student ID!\n")

    # Method to view student details
    def view_student(self):
        student_id = input("Enter Student ID: ")
        if student_id in self.students:
            self.students[student_id].view_details()
        else:
            print("Invalid Student ID!\n")

    # Method to view teacher details
    def view_teacher(self):
        teacher_id = input("Enter Teacher ID: ")
        if teacher_id in self.teachers:
            self.teachers[teacher_id].view_details()
        else:
            print("Invalid Teacher ID!\n")

    # Method to view course details
    def view_course(self):
        course_name = input("Enter Course Name: ")
        if course_name in self.courses:
            self.courses[course_name].view_details()
        else:
            print("Invalid Course Name!\n")

    # Main menu for the system
    def menu(self):
        while True:
            print("School Management System")
            print("1. Add Student")
            print("2. Add Teacher")
            print("3. Add Course")
            print("4. Enroll Student in Course")
            print("5. Assign Grade")
            print("6. View Student Details")
            print("7. View Teacher Details")
            print("8. View Course Details")
            print("9. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.add_teacher()
            elif choice == '3':
                self.add_course()
            elif choice == '4':
                self.enroll_student_in_course()
            elif choice == '5':
                self.assign_grade()
            elif choice == '6':
                self.view_student()
            elif choice == '7':
                self.view_teacher()
            elif choice == '8':
                self.view_course()
            elif choice == '9':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice! Please try again.\n")


# Main function to run the school management system
if __name__ == "__main__":
    sms = SchoolManagementSystem()
    sms.menu()
