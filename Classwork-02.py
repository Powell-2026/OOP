List01= [2,4,6,8,10]

print(List01)

while (1):
    print("1: Add an element")
    print("2: Remove an element")
    print("3: Replace an element")
    print("4: Sort the elements")
    print("5: Print the list")
    print("6: Exit")

    choice = input("Enter your choice: ")
    if choice == "6":
        break
    elif choice < "0" or choice > "6":
        print("Please enter a valid choice")
    elif choice == "1":
        a=int(input("Enter the desired number: "))
        List01.append(a)
    elif choice == "2":
        b=int(input("Enter the desired number: "))
        for i in List01:
            if i == b:
                List01.remove(b)
            else:
                print("Please enter a number from the current list")
                break
    elif choice == "3":
        old_element=int(input("Enter the number you want to replace: "))
        new_element=int(input("Enter the new number: "))
        index = List01.index(old_element)
        List01[index] = new_element
    elif choice == "4":
        List01.sort()
    elif choice == "5":
        print(List01)
