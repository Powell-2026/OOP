while (True):
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("5 Exit")
    choice = input("Enter your choice:")

    if choice > "5" or choice < "1":
        print ("Please enter a valid choice")
        continue
    elif choice == "5":
        break

    A = int(input("Enter the first number:"))
    B = int(input("Enter the second number:"))

    if choice == "1":
        c=A+B
        print(A,"+",B,"=",c)
    elif choice == "2":
        c=A-B
        print(A,"-",B,"=",c)
    elif choice == "3":
        c=A*B
        print(A,"*",B,"=",c)
    elif choice == "4":
        c=A/B
        print(A,"/",B,"=",c)