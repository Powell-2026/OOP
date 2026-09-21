mystack=[]

def pushbook():
    mystack.append(input("Enter book: "))
def popbook():
    m
while True:
    print("1. Add to stack")
    print("2. Remove from stack")
    print("3. Display queue")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice <"1" or choice >"4":
        print("Enter a valid choice")
    if choice =="4":
        break
    elif choice =="1":
        pushbook()