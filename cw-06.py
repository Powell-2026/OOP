class Student(object):
    def __init__(self):
        self.id=""
        self.name = ""
        self.major=""
        self.advisor=""

    def create_new_student(self):
        self.id=input("Enter Student ID: ")
        self.name=input("Enter Student Name: ")
        self.major=input("Enter Student major: ")
        self.advisor=input("Enter Student Advisor: ")

    def display_student(self):
        print("Student ID:",self.id)
        print("Student Name:",self.name)
        print("Student Major:",self.major)
        print("Student Advisor:",self.advisor)

    def assign_advisor(self):
        facultyid=input("Enter Faculty ID: ")
        for i in myFaculty:
            if i.id==facultyid:
                stu.assign_advisor(i)

myStudents=[]
stu=Student()

stu.create_new_student()
stu.display_student()
stu.assign_advisor()

myStudents.append(stu)
print(myStudents)

class Faculty(object):
    def __init__(self):
        self.id=""
        self.name=""
        self.department=""
        self.degree=""
        self.students=[]

    def create_new_faculty(self):
        self.id=input("Enter Faculty ID: ")
        self.name=input("Enter Faculty Name: ")
        self.department=input("Enter Faculty Department: ")
        self.degree=input("Enter Faculty Degree: ")
        self.students=input("Enter Faculty Students: ")

    def display_faculty(self):
        print("Faculty ID:",self.id)
        print("Faculty Name:",self.name)
        print("Faculty Department:",self.department)
        print("Faculty Degree:",self.degree)
        print("Faculty Students:",self.students)

    def enroll_students(self):
        studentid=input("Enter Student ID: ")
        for i in myStudents:
            if i.id==studentid:
                fac.enroll_students(i)

myFaculty=[]
fac=Faculty()

fac.create_new_faculty()
fac.display_faculty()
fac.enroll_students()

myFaculty.append(fac)
print(myFaculty)

class Course(object):
    def __init__(self):
        self.id=""
        self.title=""
        self.faculty=""
        self.credits=""
        self.department=""
        self.students=[]

    def create_new_course(self):
        self.id=input("Enter Course ID: ")
        self.title=input("Enter Course Title: ")
        self.faculty=input("Enter Course Faculty: ")
        self.credits=input("Enter Course Credits: ")
        self.department=input("Enter Course Department: ")
        self.students=input("Enter Course Students: ")

    def display_course(self):
        print("Course ID:",self.id)
        print("Course Title:",self.title)
        print("Faculty:",self.faculty)
        print("Credits:",self.credits)
        print("Department:",self.department)
        print("Students:",self.students)

    def assign_faculty(self):
        facultyid=input("Enter Faculty ID: ")
        for i in myFaculty:
            if i.id==facultyid:
                facultyid=self.faculty

    def register_students(self):
        studentid=input("Enter Student ID: ")
        for i in myStudents:
            if i.id==studentid:
                studentid=self.students

myCourses=[]
cour=Course()

cour.create_new_course()
cour.display_course()
cour.assign_faculty()
cour.register_students()

myCourses.append(cour)
print(myCourses)

#Main Program
