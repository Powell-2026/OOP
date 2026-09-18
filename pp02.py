mycourses={}
while (1):
    print("1. Enter a course")
    print("2. Remove a course")
    print("3. Replace a course")
    print("4. Print Courses")
    print("5. Exit")

    choice=int(input("Enter your choice: "))
    if choice <1 or choice >5:
        print("Please enter a valid choice")
        break
    elif choice==5:
        break
    elif choice==1:
        course_name=input("Enter the course you want to add: ")
        mycourses.update({"course_name1":course_name})
    elif choice==2:
        course_number=input("Enter the course number you want to remove: ")
        if course_number not in mycourses:
            print("Please enter a valid course number")
        else:
            del mycourses[course_number]
    elif choice==3:
        course_name=input("Enter the course number you want to replace: ")
        mycourses[course_name]=input("Enter the new course name: ")
    elif choice==4:
        print(mycourses)
