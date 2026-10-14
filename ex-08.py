import pickle
class Student(object):
    def __init__(self):
        self.id=""
        self.name = ""
        self.major=""
        self.advisor=""

    def create_student(self):
        self.id=input("Enter Student ID: ")
        self.name=input("Enter Student Name: ")
        self.major=input("Enter Student major: ")
        self.advisor=input("Enter Student Advisor: ")

    def display_student(self):
        print("Student ID:",self.id)
        print("Student Name:",self.name)
        print("Student Major:",self.major)
        print("Student Advisor:",self.advisor)

#main
s1=Student()
s1.create_student()
s1.display_student()

file1=open("myStudents.dat", "ab")
pickle.dump(s1, file1)
file1.close()

file2=open("myStudents.dat", "rb")

while True:
    try:
        data=pickle.load(file2)
        print(data.id)
        print(data.name)
        print(data.major)
        print(data.advisor)
    except(EOFError):
        break
file2.close()