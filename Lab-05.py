import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lab05"
)
cursor=db.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Student (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    Major VARCHAR(50),
    Courses VARCHAR(50),
    GPA VARCHAR(50)
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Faculty (
    FacultyID INT PRIMARY KEY,
    Name VARCHAR(50),
    Department VARCHAR(50),
    Courses VARCHAR(50)
    )
""")
class Student_Master(object):
    def __init__(self):
        self.stu_id=""
        self.stu_name=""
        self.stu_major=""
        self.stu_courses=""
        self.stu_cgpa=""
    def add_student(self):
        self.stu_id=int(input("Enter Student ID: "))
        self.stu_name=input("Enter Student Name: ")
        self.stu_major=input("Enter Student Major: ")
        self.stu_courses=input("Enter Student Courses: ")
        self.stu_cgpa=input("Enter Student GPA: ")
        sql="INSERT INTO Student VALUES (%s,%s,%s,%s,%s)"
        values=(self.stu_id,self.stu_name,self.stu_major,self.stu_courses,self.stu_cgpa)
        db.commit()
    def display_student(self):
        cursor.execute("SELECT * FROM Student")
        for row in cursor.fetchall():
            print(row)
class Faculty_Master(object):
    def __init__(self):
        self.fac_id=""
        self.fac_name=""
        self.fac_department=""
        self.fac_teaches_courses=""
    def add_faculty(self):
        self.fac_id=int(input("Enter Faculty ID: "))
        self.fac_name=input("Enter Faculty Name: ")
        self.fac_department=input("Enter Faculty Department: ")
        self.fac_teaches_courses=input("Enter Courses Taught by Faculty: ")
        sql = "INSERT INTO Faculty VALUES (%s,%s,%s,%s)"
        values=(self.fac_id,self.fac_name,self.fac_department,self.fac_teaches_courses)
        db.commit()
    def display_faculty(self):
        cursor.execute("SELECT * FROM Faculty")
        for row in cursor.fetchall():
            print(row)
while True:
    print("1. Add Student")
    print("2. Display Student")
    print("3. Update Student")
    print("4. Add Faculty")
    print("5. Display Faculty")
    print("6. Update Faculty")
    print("7. Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
        Student_Master().add_student()
    elif choice=="2":
        Faculty_Master().display_faculty()
    elif choice=="3":
        print("inprogress")
    elif choice=="4":
        Faculty_Master().add_faculty()
    elif choice=="5":
        Faculty_Master().display_faculty()
    elif choice=="6":
        print("inprogress")
    elif choice=="7":
        cursor.close()
        db.close()
        break
    else:
        print("Invalid Choice")