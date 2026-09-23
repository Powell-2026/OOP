mystudents={}
i=1
def add_student():
    stu_name=input("Enter a student name: ")
    lab1=int(input("Enter grade for Lab 1: "))
    if lab1 <0 or lab1>10:
        print("Please enter a grade between 0 and 10")
    lab2=int(input("Enter grade for Lab 2: "))
    if lab2 < 0 or lab2 > 10:
        print("Please enter a grade between 0 and 10")
    lab3=int(input("Enter grade for Lab 3: "))
    if lab3 < 0 or lab3 > 10:
        print("Please enter a grade between 0 and 10")
    lab4=int(input("Enter grade for Lab 4: "))
    if lab4 < 0 or lab4 > 10:
        print("Please enter a grade between 0 and 10")
    lab5=int(input("Enter grade for Lab 5: "))
    if lab5 < 0 or lab5 > 10:
        print("Please enter a grade between 0 and 10")
    total=lab1+lab2+lab3+lab4+lab5
    percent=(total/50)*100
    average=total/5
    mystudents.update({"s"+str(i):
                           {"student"+str(i):stu_name,
                            "Lab 01"+str(i):lab1,
                            "Lab 02"+str(i):lab2,
                            "Lab 03"+str(i):lab3,
                            "Lab 04"+str(i):lab4,
                            "Lab 05"+str(i):lab5,
                            "Total"+str(i):total,
                            "percent"+str(i):percent,
                            "average"+str(i):average,
                            }
    })

def delete_student():
    del mystudents[input("Enter student number to delete (formatted as 's1': ")]

def display_students():
    print(mystudents)

while True:
    print("1. Add a student")
    print("2. Remove a student")
    print("3. Display Students")
    print("4. Exit")
    choice=input("Enter your choice: ")
    if choice <"1" or choice >"4":
        print("Please enter a valid choice")
    elif choice=="4":
        break
    elif choice=="1":
        add_student()
    elif choice=="2":
        delete_student()
    elif choice=="3":
        display_students()