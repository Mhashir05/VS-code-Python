class Student:
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number
        self.enrolled_courses = {}
        self.grades = {}

    def enroll_course(self, course_name):
        if course_name not in self.enrolled_courses:
            self.enrolled_courses[course_name] = True
            print(f"{self.name} enrolled in the course: {course_name}")
        else:
            print(f"{self.name} is already enrolled in the course: {course_name}")

    def record_grade(self, course_name, grade):
        if course_name in self.enrolled_courses:
            self.grades[course_name] = grade
            print(f"Grade recorded for {self.name} in course {course_name}: {grade}")
        else:
            print(f"{self.name} is not enrolled in the course: {course_name}")

    def view_enrolled_courses(self):
        if self.enrolled_courses:
            print(f"{self.name}'s enrolled courses:")
            for course in self.enrolled_courses:
                print(course)
        else:
            print(f"{self.name} has not enrolled in any courses yet.")

    def view_grades(self):
        if self.grades:
            print(f"{self.name}'s grades:")
            for course, grade in self.grades.items():
                print(f"Course: {course}, Grade: {grade}")
        else:
            print(f"{self.name} has no recorded grades yet.")


# Example usage with user input:
if __name__ == "__main__":
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    roll_number = input("Enter student's roll number: ")

    student = Student(name, age, roll_number)

    while True:
        print("\n1. Enroll in a course")
        print("2. Record grade for a course")
        print("3. View enrolled courses")
        print("4. View grades")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            course_name = input("Enter course name to enroll: ")
            student.enroll_course(course_name)
        elif choice == '2':
            course_name = input("Enter course name to record grade: ")
            grade = input("Enter grade: ")
            student.record_grade(course_name, grade)
        elif choice == '3':
            student.view_enrolled_courses()
        elif choice == '4':
            student.view_grades()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-5).")
