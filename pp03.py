students={}
i=1
while (1)
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Edit Student")
    print("4. Print Student")
    print("5. Exit")
    choice=input("Enter your choice: ")
    if choice<1 or choice>5:
        print("Please enter a valid choice")
    elif choice=="1":
        name=input("Enter student name: ")
        major=input("Enter student major: ")
        year=input("Enter student year: ")
        gpa=input("Enter student GPA: ")
        students.update({"s"+str(i):{"stu_name"+str(i):name,"stu_major"+str(i):major,"stu_year"+str(i):year,"stu_gpa"+str(i):gpa}})
        i=i+1
    elif choice=="2":
        stu_num=input("Enter student number (formatted as's1': ")
        del students[stu_num]
    elif choice=="3":
        stu_num=input("Enter student number you would like to edit (formatted as's1': ")
        if stu_num not in students:
           print("Please enter a valid student number")
        else:
            print("1. Name")
            print("2. Major")
            print("3. Year")
            print("4. GPA")
            option = input("Enter which field you would like to edit: ")
            if option=="1":
                stu_name=input("")


