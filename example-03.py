Number1 = int(input("Enter number1:"))
Operator= input("Enter operator:")
Number2 = int(input("Enter number2:"))

if Operator== "+":
    c=Number1+Number2
    print("The total is:", c)
elif Operator== "-":
    c=Number1-Number2
    print("The total is:", c)
elif Operator== "*":
    c=Number1*Number2
    print("The total is:", c)
elif Operator== "/":
    if Number2 == 0:
        print("Invalid Operation, please enter a number different from 0")
    else:
        print("The total is:", Number1/Number2)
else:
    print("Invalid operator")