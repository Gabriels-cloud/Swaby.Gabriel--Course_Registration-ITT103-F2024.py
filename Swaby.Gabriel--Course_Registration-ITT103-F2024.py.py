# Class representing a course
class Course:
    def __init__(self, c_id, c_name, c_fee):
        self.c_id = c_id
        self.c_name = c_name
        self.c_fee = c_fee

    # Class reprsenting a student

class Student:
    def __init__(self, stu_id, stu_name, stu_email):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_email = stu_email
        self.courses = []
        self.balance = 0.0



    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            self.balance += course.c_fee
            print(f"Successfully enrolled in course: {course.c_name}. Fee added to balance.")
        else:
            print(f"Already enrolled in course: {course.c_name}.")


         # Class representing the course registration system
class RegistrationSystem:
    def __init__(self):

     #list to store abvaliable courses

        self.courses = []
# dictionary  to store stdent id number


        self.students = {}  

    def add_course(self):
        course_id = input("Enter Course ID: ")
        name = input("Enter Course Name: ")
        try:
            fee = float(input("Enter Course Fee: "))
            if any(course.c_id == course_id for course in self.courses):
                print("Error: Course ID already exists.")
                return
            self.courses.append(Course(course_id, name, fee))
            print(f"Course '{name}' added successfully.")
        except ValueError:
            print("Error: Fee must be a valid number.")

    def register_student(self):
        
        stu_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        email = input("Enter Student Email: ")
        if stu_id in self.students:
            print("Error: Student ID already exists.")
            return
        self.students[stu_id] = Student(stu_id, name, email)
        print(f"Student '{name}' registered successfully.")

    def enroll_in_course(self):
        stu_id = input("Enter Student ID: ")
        course_id = input("Enter Course ID: ")
        student = self.students.get(stu_id)
        if not student:
            print("Error: Student not found.")
            return
        course = next((c for c in self.courses if c.c_id == course_id), None)
        if not course:
            print("Error: Course not found.")
            return
        student.enroll(course)

    def calculate_payment(self):
        stu_id = input("Enter Student ID: ")
        try:
            amount = float(input("Enter Payment Amount: "))
            student = self.students.get(stu_id)
            if not student:
                print("Error: Student not found.")
                return
            if amount < 0.4 * student.balance:
                print("Error: Minimum payment of 40% of balance required.")
                return
            student.balance -= amount
            print(f"Payment successful! Remaining balance: {student.balance}")
        except ValueError:
            print("Error: Amount must be a valid number.")

    def show_courses(self):
        if not self.courses:
            print("No courses available.")
        else:
            print("\nAvailable Courses:")
            for course in self.courses:
                print(f"ID: {course.c_id}, Name: {course.c_name}, Fee: {course.c_fee}")

    def show_registered_students(self):
        if not self.students:
            print("No students registered.")
        else:
            print("Registered Students:")
            for student in self.students.values():
                print(f"ID: {student.stu_id}, Name: {student.stu_name}, Email: {student.stu_email}")

    def check_student_balance(self):
        stu_id = input("Enter Student ID: ")
        student = self.students.get(stu_id)
        if student:
            print(f"Balance for {student.stu_name}: {student.balance}")
        else:
            print("Error: Student not found.")


# Main menu function


def main():
    system = RegistrationSystem()

    while True:
        print("\nCourse Registration System")
        print("1. Add Course")
        print("2. Register Student")
        print("3. Enroll in Course")
        print("4. Make Payment")
        print("5. Show Courses")
        print("6. Show Students")
        print("7. Check Balance")
        print("8. Exit")





        choice = input("Enter your choice: ")
        if choice == '1':
            system.add_course()
        elif choice == '2':
            system.register_student()
        elif choice == '3':
            system.enroll_in_course()
        elif choice == '4':
            system.calculate_payment()
        elif choice == '5':
            system.show_courses()
        elif choice == '6':
            system.show_registered_students()
        elif choice == '7':
            system.check_student_balance()
        elif choice == '8':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
