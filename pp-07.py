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

    def add():
        c=A+B
        print(A,"+",B,"=",c)
    def subtract():
        c=A-B
        print(A,"-",B,"=",c)
    def multiply():
        c=A*B
        print(A,"*",B,"=",c)
    def divide():
        c=A/B
        print(A,"/",B,"=",c)

    if choice == "1":
        add()
    elif choice == "2":
        subtract()
    elif choice == "3":
        multiply()
    elif choice == "4":
        divide()