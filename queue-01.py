myqueue=[]

def enqueue():
    myqueue.append(int(input("Enter a number:")))
def dequeue():
    myqueue.pop(0)
def display_queue():
    print(myqueue)

while True:
    print("1. Add to the queue")
    print("2. Remove from the queue")
    print("3. Display the queue")
    print("4. Exit")
    choice = input("Enter your choice:")
    if choice <"1" or choice>"4":
        print("Enter a valid number")
    if choice == "4":
        break
    if choice == "1":
        enqueue()
    elif choice == "2":
        dequeue()
    elif choice == "3":
        display_queue()
