myEmployees={}
i=1
def addEmployee():
    employeeName=input("Enter employee name: ")
    employeepay=int(input("Enter employee basic pay: "))
    employeeallowance=int(input("Enter employee allowance: "))
    employeedeductions=int(input("Enter employee deductions: "))
    employeetax=int(input("Enter tax percentage: "))
    if employeetax > 100 or employeetax <= 0:
        print("Invalid tax percentage")
        return
    grosspay=employeepay+employeeallowance
    netpay=(grosspay-employeedeductions)-(grosspay*(employeetax*.01))
    myEmployees.update({"e"+str(i):
                           {"employeename":employeeName,
                            "employeepay":employeepay,
                            "employeeallowance":employeeallowance,
                            "employeedeductions":employeedeductions,
                            "employeetax":employeetax,
                            "grosspay":grosspay,
                            "netpay":netpay,}
                        })

def deleteEmployee():
    del myEmployees[input("Enter employee ID you want deleted (formatted as 'e1': ")]

def modifyEmployee():
    employeeID=input("Enter employee ID (formatted as 'e1'): ")
    if employeeID in myEmployees:
        print("1. Change name")
        print("2. Change basic pay")
        print("3. Change allowance")
        print("4. Change deductions")

        choice=input("Enter your choice: ")
        if choice=="1":
            myEmployees[employeeID]["employeeName"]=input("Enter new name: ")
        elif choice=="2":
            myEmployees[employeeID]["employeepay"]=int(input("Enter new pay: "))
        elif choice=="3":
            myEmployees[employeeID]["employeeallowance"]=int(input("Enter new allowance: "))
        elif choice=="4":
            myEmployees[employeeID]["employeedeductions"]=int(input("Enter new deductions: "))
        else:
            print("Invalid choice")
    else:
        print("Enter a valid employee ID")

def displayEmployees():
    print(myEmployees)

while True:
    print("1. Add employee")
    print("2. Delete employee")
    print("3. Modify employee")
    print("4. Display employees")
    print("5. Exit")
    choice=input("Enter your choice: ")
    if choice== "5":
        break
    elif choice=="1":
        addEmployee()
        i=i+1
    elif choice=="2":
        deleteEmployee()
    elif choice=="3":
        modifyEmployee()
    elif choice=="4":
        displayEmployees()
    else:
        print("Invalid choice")

