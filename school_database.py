'''Create a program to manage the school base. It is possible to create three types of users (student, teacher, educator) and also manage them.

After starting the program, you can enter one of the following commands: create, manage, end.

The command "create" - Goes to the process of creating users.
Command "manage" - Goes to the process of managing users.
The command "end" - Ends the operation of the application.

The process of creating users:

Enter the option you want to select: student, teacher, educator, end. After each option (except "end") is done, it displays this menu again.
The command "student" - Fetch the name of the student (as one variable, it can be fetched as two variables if handled correctly) and the name of the class (e.g. "3C")
Command "teacher" - Fetch the name of the teacher (as one variable, labo two, if handled correctly), the name of the subject taught, and then on new lines the names of the classes that the teacher teaches, until you get a blank line.
The command "educator" - Fetch the name of the educator (as one variable, or two, if handled correctly), as well as the name of the class taught.
The command "end" - Returns to the first menu.

User management process:

Enter the option you want to select: class, student, teacher, educator, end. After each option (except "end") is executed, it displays this menu again.
'''

class Student:
    def __init__(self, name, surname, schoolclass):
        self.name = name
        self.surname = surname
        self.schoolclass = schoolclass

    def __repr__(self):
        return f"Student {self.name} {self.surname}, class {self.schoolclass}"


class Teacher:
    def __init__(self, name, surname, subject, schoolclasses):
        self.name = name
        self.surname = surname
        self.subject = subject
        self.schoolclasses = schoolclasses

    def __repr__(self):
        return (f"Teacher {self.name} {self.surname}, subject {self.subject}, "
                f"classes: {', '.join(self.schoolclasses)}")


class Tutor:
    def __init__(self, name, surname, schoolclass):
        self.name = name
        self.surname = surname
        self.schoolclass = schoolclass

    def __repr__(self):
        return f"Tutor {self.name} {self.surname}, class {self.schoolclass}"

students = [Student("Mark", "Lee", "1"),
            Student("Amanda", "Seyfried", "3")]
teachers = [Teacher("Severus", "Snape", "P.E.", "3")]
tutors = [Tutor("Javier", "Bardem", "3")]

def create_student():
    name = input("Enter student's name: ")
    surname = input("Enter student's surname: ")
    schoolclass = input("Enter student's class: ")
    students.append(Student(name, surname, schoolclass))

def create_teacher():
    name = input("Enter teacher's name: ")
    surname = input("Enter teacher's surname: ")
    subject = input("Enter subject taught by the teacher: ")
    schoolclasses = []
    print("Enter classes taught by the teacher (one per line). "
          "Leave blank line to finish:")
    while True:
        schoolclass = input()
        if schoolclass:
            schoolclasses.append(schoolclass)
        else:
            break
    teachers.append(Teacher(name, surname, subject, schoolclasses))

def create_tutor():
    name = input("Enter tutor's name: ")
    surname = input("Enter tutor's surname: ")
    schoolclass = input("Enter class tutored by the tutor: ")
    tutors.append(Tutor(name, surname, schoolclass))

def create_user():
    while True:
        print("\nSelect user type to create:")
        print("1. Student")
        print("2. Teacher")
        print("3. Tutor")
        print("4. Go back")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_student()
        elif choice == "2":
            create_teacher()
        elif choice == "3":
            create_tutor()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


def manage_class():
    class_name = input("Enter the name of the class you want to manage: ")
    print(f"Students in class {class_name}:")
    for student in students:
        if student.schoolclass == class_name:
            print(student)
    print(f"Tutor of the class {class_name}:")
    for tutor in tutors:
        if tutor.schoolclass == class_name:
            print(tutor)

def manage_student():
    student_name = input("Enter the name and surname of the student whose "
                         "subjects you want to display: ")
    for student in students:
        if f"{student.name} {student.surname}" == student_name:
            print(f"Subjects of student {student_name}:")
            for teacher in teachers:
                if student.schoolclass in teacher.schoolclasses:
                    print(f"- {teacher.subject} taught by {teacher.name} "
                          f"{teacher.surname}")

def manage_teacher():
    teacher_name = input("Enter the name and surname of the teacher whose "
                         "classes you want to display: ")
    for teacher in teachers:
        if f"{teacher.name} {teacher.surname}" == teacher_name:
            print(f"Classes taught by teacher {teacher_name}:")
            for schoolclass in teacher.schoolclasses:
                print(schoolclass)

def manage_tutor():
    tutor_name = input("Enter the name and surname of the tutor whose students "
                       "you want to display: ")
    for tutor in tutors:
        if f"{tutor.name} {tutor.surname}" == tutor_name:
            print(f"Students tutored by tutor {tutor_name}:")
            for student in students:
                if student.schoolclass == tutor.schoolclass:
                    print(student)

while True:
    option = input("Select an option:\n 1. Create\n 2. Manage\n 3. Quit\n")
    if option == "1":
        create_user()
    elif option == "2":
        while True:
            print("\nSelect user type to manage:")
            print("1. Class")
            print("2. Student")
            print("3. Teacher")
            print("4. Tutor")
            print("5. Go back")
            manage_choice = input("Enter your choice: ")
            if manage_choice == "1":
                manage_class()
            elif manage_choice == "2":
                manage_student()
            elif manage_choice == "3":
                manage_teacher()
            elif manage_choice == "4":
                manage_tutor()
            elif manage_choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")
    elif option == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")